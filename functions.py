import os
from config import FILE_TYPE # Import dictionary from config.py
def classify_file(file_path):
    _, ext = os.path.splitext(file_path) # Get the file extension from the file_path
    ext = ext.lower()

    for category, extensions in FILE_TYPE.items(): # Search if the extension is in the dictionary
        if ext in extensions:
            return category # If it is, return the category name

    return 'Unknown' # If it isn't, return 'Unknown'