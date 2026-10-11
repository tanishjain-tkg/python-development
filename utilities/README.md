# File Organizer

A simple Python utility that organizes files into categorized folders based on their file extensions.

## Features

- Automatically categorizes files by extension.
- Creates destination folders when needed.
- Supports documents, images, videos, audio, spreadsheets, and archives.
- Moves unrecognized file types into an `Others` folder.
- Uses Python's `pathlib` and `shutil` modules.

## Project Structure

```text
file_organizer/
├── file_organizer.py
└── README.md
```

## Requirements

- Python 3.10 or later recommended
- No third-party packages required

## How to Run

1. Clone or download this repository.
2. Navigate to the `file_organizer` directory.
3. Update the target directory in `file_organizer.py` if necessary.
4. Run the script:

```bash
python3 file_organizer.py
```

## Supported File Categories

| Category | Examples |
|---|---|
| Documents | `.pdf`, `.docx`, `.txt`, `.pptx` |
| Images | `.jpg`, `.png`, `.gif`, `.webp` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov` |
| Audio | `.mp3`, `.wav`, `.flac` |
| Spreadsheets | `.csv`, `.xls`, `.xlsx` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Others | Unrecognized extensions |

## Technologies Used

- Python
- `pathlib`
- `shutil`

## Learning Objectives

This project demonstrates basic filesystem operations, loops, dictionaries, functions, conditional statements, and file movement in Python.

## Note

Test the utility on a sample directory before using it on important files. The script moves files, so use caution when selecting the target directory.

## License

This project is available for learning and educational purposes.