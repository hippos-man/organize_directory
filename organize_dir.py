from pathlib import Path # https://docs.python.org/3.8/library/pathlib.html
from sys import argv # https://docs.python.org/3/library/sys.html 
from shutil import move # https://docs.python.org/3.8/library/shutil.html


def get_directory_name(filename):
    extension = filename.suffix[1:]
    return directories.get(extension, "Miscellaneous")

directories = {
    # Documents
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "xlsx": "Documents",
    "csv": "Documents",
    # Tableau Files
    "twb": "Tableau Files",
    "tbm": "Tableau Files",
    "twbx": "Tableau Files",
    # Images
    "jpeg": "Images",
    "png": "Images",
    "jpg": "Images",
    "git": "Images",
    # Videos
    "mp4": "Videos",
    # Music
    "mp3": "Musics",
    # Programs
    "html": "Programs",
    "css": "Programs",
    "js": "Programs",
    "java": "Programs",
    "py": "Programs"
}
# len() returns length of arguments. argv => arg[0]: script name, 
# arg[1]: 1st argument.(in this case, Path that you want to organize)
if len(argv) != 2:
    print("=" * 50)
    print("[ERROR] Invalid number of arguments were given!")
    print(f"[Usage] python {Path(__file__).name} <dir_path>")
    print("=" * 50)
    exit(1)

# Downloads Directory Path
DOWNLOADS_DIR_PATH = Path(argv[1])

for filename in DOWNLOADS_DIR_PATH.iterdir():
    absolute_path = filename.absolute()
    if absolute_path.is_file():
        destination = DOWNLOADS_DIR_PATH / get_directory_name(filename)
        if not destination.exists():
            destination.mkdir()
        
        move(str(absolute_path), str(destination))
