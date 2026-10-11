from pathlib import Path
import shutil

folder = Path.home() / "trial" 

FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Spreadsheets": [".csv", ".xls", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

def get_category(extension):
    """Return the category for a file extension."""
    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    
    return "Others"

def organize_files(folder):
    """Organize files in the given folder."""

    if not folder.exists():
        print(f"Directory does not exist: {folder}")
        return
    
    if not folder.is_dir():
        print(f"Not a directory: {folder}")
        return

    for file in folder.iterdir():

        # Ignore directories
        if not file.is_file():
            continue

        # Get extension
        category = get_category(file.suffix)

        # Create category directory
        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)

        # Destination path
        destination = destination_folder / file.name

        # Move file
        shutil.move(str(file), str(destination))

        print(f"Moved: {file.name} → {category}/")


if __name__ == "__main__":
    organize_files(folder)