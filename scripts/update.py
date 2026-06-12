# This is where we will

# 1. Run the main loop
from pathlib import Path
from typing import Any
import subprocess
import requests
import random
import json

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO_ROOT / "cache"
BG_DIR = REPO_ROOT / "backgrounds"

def get_json(type: str):
   BOARD_URL_ROOT = "https://https://in.pinterest.com/coderlisha/vscode-"

   print("\nScraping for", type, "backgrounds...")
   pins_json = str(CACHE_DIR / type / "pins.json")

   # so that github workflows can run this in VM
   PINTEREST_DL =  str(REPO_ROOT / ".venv/bin/pinterest-dl")

   command = [
      PINTEREST_DL, "scrape",
      BOARD_URL_ROOT + type + "/",
      "--cache", pins_json
   ]

   result = subprocess.run(command, text=True)
   print("Pins successfully saved to", pins_json)
   print("Exit code for", type, "board:", result.returncode)

def organise(type: str):
   print("\nOrganising pins into gifs.json and images.json...")

   pins_json = CACHE_DIR / type / "pins.json"

   gifs_json = pins_json.parent / "gifs.json"
   gifs_json.touch()
   images_json = pins_json.parent / "images.json"
   images_json.touch()

   gifs: list[dict[str, Any]] = []
   images: list[dict[str, Any]] = []

   with open(pins_json, "r") as file:
      pins = json.load(file)

      for pin in pins:
         if pin["src"].lower().endswith(".gif"):
            gifs.append(pin)
         else:
            images.append(pin)
   
   with open(gifs_json, "w") as file:
      json.dump(gifs, file, indent=4)
   with open(images_json, "w") as file:
      json.dump(images, file, indent=4)

   print("Pins successfully organised!")

def choose(cache: Path) -> tuple[str, str]: # returns image link of gif, image
   gifs_json = cache / "gifs.json"
   images_json = cache / "images.json"

   gif = ""
   img = ""

   with open(gifs_json) as file:
      gifs = json.load(file)
      gif = random.choice(gifs)["src"]

   with open(images_json) as file:
      imgs = json.load(file)
      img = random.choice(imgs)["src"]
   
   return gif, img

def get_random_pins(type: str):
   print("\nChoosing a random pins...")
   gif, img = choose(CACHE_DIR / type)

   response = requests.get(gif)
   response.raise_for_status()
   with open(BG_DIR / (type + ".gif"), "wb") as file:
      file.write(response.content)

   response = requests.get(img)
   response.raise_for_status()
   with open(BG_DIR / (type + ".png"), "wb") as file:
      file.write(response.content)

   print("Pins chosen for", type + "!")

print("Repository root found at:", str(REPO_ROOT))

for type in ("editor", "sidebar", "panel"):
   (CACHE_DIR / type).mkdir(parents=True, exist_ok=True)

   # get pins.json in cache
   get_json(type)

   # separate pin objects into gifs.json and images.json
   organise(type)

   # choose 1 random gif and 1 random img
   get_random_pins(type)