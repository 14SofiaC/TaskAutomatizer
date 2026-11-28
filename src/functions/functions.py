import os
from src.config import FILE_TYPE # Import dictionary from config.py
from pathlib import Path
import shutil
from datetime import datetime
import subprocess
import sys

def classify_file(file_path):
    _, ext = os.path.splitext(file_path) # Get the file extension from the file_path
    ext = ext.lower()

    for category, extensions in FILE_TYPE.items(): # Search if the extension is in the dictionary
        if ext in extensions:
            return category # If it is, return the category name

    return 'Others' # If it isn't, return 'Others' as the category name

def move_files(folder, sim=False):
    base_path = Path(folder) # Create a main folder to store the organized files
    main_folder = base_path / 'Organized_Files'
    if not sim:
        try:
            main_folder.mkdir(exist_ok=True) # Create the main folder if it doesn't exist
        except PermissionError: # If the user doesn't have permission to create the folder, we catch the exception and print a message to the user.
            print(f'[ERROR] Not enough permission to create folders in {main_folder}')
            return
    created_folders = set() # Create a set to store the created folders

    with os.scandir(folder) as files: # Scan the folder for files
        for file in files:
            if not file.is_file() or file.name == 'Organized_Files': # Ignore if it's the "Organized_Files" folder or a subfolder
                continue
            category = classify_file(file.path) # Classify the file using the classify_file function
            destiny = main_folder / category
            if category not in created_folders:
                if destiny.exists() and not destiny.is_dir(): # Check if the category folder wasn't already created or if there is a file with the exact same name (just in case)
                    destiny = destiny.with_name(f'{destiny.name}_folder')
                if not sim:
                    destiny.mkdir(exist_ok=True)
                created_folders.add(category)
            destiny_path = destiny / file.name # Path where we will move the file
            if destiny_path.exists(): # If the file already exists, we change the name of the new file so it doesn't overwrite the existent one
                base = destiny_path.stem
                ext = destiny_path.suffix
                num = 1
                while destiny_path.exists():
                    destiny_path = destiny / f'{base}_{num}{ext}'
                    num += 1
            if not sim:
                try:
                    shutil.move(file.path, destiny_path)
                    with open(main_folder / 'log.txt', 'a', encoding='utf-8') as log_file:
                        log_file.write(f'[{datetime.now().strftime("%H:%M:%S")}] Moved "{file.name}" from "{base_path}" to "{destiny_path}".\n') # Log the moved file and its new path
                except PermissionError:
                    print(f'[SKIPPED] File "{file.name}" already in use or not enough permission for moving it')
            else:
                with open(base_path / 'sim_log.txt', 'a', encoding='utf-8') as log_file:
                    log_file.write(f'[{datetime.now().strftime("%H:%M:%S")}] Would move "{file.name}" from "{base_path}" to "{destiny}".\n')

def clear():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def getch():
    if sys.platform == 'win32':
        import msvcrt
        return msvcrt.getch().decode('utf-8', errors='ignore')
    else:
        import termios
        import tty

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)