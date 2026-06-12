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

def to_png(path: Path) -> Path:
   png_path = path.with_suffix(".png")
   image = Image.open(path)
   image.save(png_path)

   path.unlink() # rm path
   return png_path

# returns true if png, false if gif
def organise_by_suffix(img: Path, cache: Path) -> bool:
   if(img.suffix.lower() == ".png"):
      img.rename(cache / "PNGs" / img.name)
      return True
   elif(img.suffix.lower() == ".gif"):
      img.rename(cache / "GIFs" / img.name)
      return False
   else:
      raise TypeError("Only png and gif files must be organised! Cannot organise " + str(img))

for type in ("editor", "sidebar", "panel"):
   # make cache directory and parents if needed, ignore if alr exists
   cache = CACHE_DIR / type
   cache.mkdir(parents=True, exist_ok=True) 
   (cache / "GIFs").mkdir(exist_ok=True)
   (cache / "PNGs").mkdir(exist_ok=True)

   scrape(type)
   
   print("\nOrganising subfolders...")
   not_png_count = 0
   png_count = 0
   gif_count = 0
   for img in cache.iterdir():
      if not img.is_file():
         continue

      if img.suffix.lower() in (".jpg", ".jpeg", ".webp"):
         not_png_count += 1
         img = to_png(img)

      if organise_by_suffix(img, cache):
         png_count += 1
      else:
         gif_count += 1

   print(not_png_count, "images converted to png.")
   print(png_count, "PNGs moved to cache/" + type + "/PNGs")
   print(gif_count, "GIFs moved to cache/" + type + "/GIFs\n")