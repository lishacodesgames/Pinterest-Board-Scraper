from pathlib import Path
from PIL import Image
import subprocess

REPO_ROOT = Path(__file__).resolve().parent.parent
BG_DIR = REPO_ROOT / "backgrounds"
CACHE_DIR = REPO_ROOT / "cache"
BOARD_URL_ROOT = "https://https://in.pinterest.com/coderlisha/vscode-"

print("Repository root found at:", str(REPO_ROOT))

def scrape(type: str) -> None:
   print("\nScraping for", type, "backgrounds...")
   command = ["pinterest-dl", "scrape", "-o", str(CACHE_DIR / type), BOARD_URL_ROOT + type + "/"]
   result = subprocess.run(command, text=True)
   print("Exit code for", type, "board:", result.returncode)

def jpg_to_png(path: Path) -> None:
   image = Image.open(path)
   image.save(path.with_suffix(".png"))

   path.unlink() # rm path

for type in ("editor", "sidebar", "panel"):
   # make cache directory and parents if needed, ignore if alr exists
   cache = CACHE_DIR / type
   cache.mkdir(parents=True, exist_ok=True) 

   scrape(type)
   
   # convert jpg to png
   for img in cache.iterdir():
      if img.suffix.lower() in (".jpg", ".jpeg"):
         jpg_to_png(img)