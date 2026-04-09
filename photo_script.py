import os

PHOTOS_DIR = "photos"
OUTPUT_FILE = "_data/photos.yml"

# allowed extensions
EXTENSIONS = (".jpg", ".jpeg", ".png", ".svg", ".webp")

files = sorted([
    f for f in os.listdir(PHOTOS_DIR)
    if f.lower().endswith(EXTENSIONS)
])

with open(OUTPUT_FILE, "w") as f:
    for file in files:
        f.write(f"- file: {file}\n")

print(f"Generated {OUTPUT_FILE} with {len(files)} photos.")
