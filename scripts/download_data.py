from pathlib import Path
import shutil
import kagglehub

# Kaggle dataset
DATASET = "yogape/logistics-operations-database"

# Project folders
RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Only the tables included in our project scope
FILES_TO_KEEP = [
    "customers.csv",
    "routes.csv",
    "loads.csv",
    "trips.csv",
    "delivery_events.csv",
]

print("Downloading dataset...")

dataset_path = Path(
    kagglehub.dataset_download(DATASET)
)

print(f"Dataset downloaded to: {dataset_path}")

# Copy only the 5 files we need into data/raw/
for filename in FILES_TO_KEEP:
    source = dataset_path / filename
    destination = RAW_DIR / filename

    if source.exists():
        shutil.copy2(source, destination)
        print(f"Copied: {filename}")
    else:
        print(f"WARNING: {filename} was not found.")

print("\nDone.")
print(f"Selected files are available in: {RAW_DIR.resolve()}")
