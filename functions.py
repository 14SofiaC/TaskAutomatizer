import os
from config import FILE_TYPE # Import dictionary from config.py
import pathlib
import shutil

def classify_file(file_path):
    _, ext = os.path.splitext(file_path) # Get the file extension from the file_path
    ext = ext.lower()

    for category, extensions in FILE_TYPE.items(): # Search if the extension is in the dictionary
        if ext in extensions:
            return category # If it is, return the category name

    return 'Others' # If it isn't, return 'Others' as the category name

def move_files(folder):
    base_path = pathlib.Path(folder) # Create a main folder to store the organized files
    main_folder = base_path / 'Organized_Files'
    # For the record, next time I'll definetely add a simulation mode, since I lost the contents of my test folder while I was trying to create "Organized_Files" as a subfolder of the current folder :(
    main_folder.mkdir(exist_ok=True) # Create the main folder if it doesn't exist
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
                destiny.mkdir(exist_ok=True)
                created_folders.add(category)
            destiny_path = destiny / file.name # Path where we will move the file

            if destiny_path.exists(): # If the file already exists, we change the name of the new file so it doesn't overwrite the existent one
                base = destiny_path.stem
                ext = destiny_path.suffix
                num = 1
                while destiny_path.exists():
                    destiny_path = f'{base}_{num}{ext}'
                    num += 1
            shutil.move(file.path, destiny_path)