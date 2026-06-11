from pathlib import Path
import subprocess

REPO_ROOT = Path(__file__).resolve().parent.parent
BG_DIR = REPO_ROOT / "backgrounds"
CACHE_DIR = REPO_ROOT / "cache"
BOARD_URL_ROOT = "https://https://in.pinterest.com/coderlisha/vscode-"

print("Repository root found at:", str(REPO_ROOT))

def scrape(type: str):
   print("\nScraping for", type, "backgrounds...")
   command = ["pinterest-dl", "scrape", "-o", str(CACHE_DIR / type), BOARD_URL_ROOT + type + "/"]
   result = subprocess.run(command, text=True)
   print("Exit code for", type, "board:", result.returncode)

for type in ("editor", "sidebar", "panel"):
   # make cache directory and parents if needed, ignore if alr exists
   folder = CACHE_DIR / type
   folder.mkdir(parents=True, exist_ok=True) 

   scrape(type)