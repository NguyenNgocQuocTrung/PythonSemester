import os

folders = [
    "data/raw", 
    "data/train", 
    "data/test", 
    "data/validation",
    "models",
    "src/preprocessing",
    "src/training",
    "src/utils"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

files = [
    "src/preprocessing/resize.py",
    "src/preprocessing/augment.py",
    "src/preprocessing/normalize.py",
    "src/training/train.py",
    "src/training/evaluate.py",
    "src/training/metrics.py",
    "src/utils/logger.py",
    "src/utils/config.py",
    "src/utils/file_manager.py",
    "src/predict.py",
    "src/app.py",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

for file in files:
    with open(file, "w") as f:
        f.write("# Placeholder\n")

print("Project structure created successfully!")
