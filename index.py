import os
from functions import classify_file

folder = str(input('Insert the folder path: ')); # For now, we directly ask the user for the folder path. In the future, we will convert this into a command line argument. Or we may add a proper GUI for easier use.

try:
    with os.scandir(folder) as files: # Scan the folder for files
        for file in files:
            category = classify_file(file.path) # Classify the file using the classify_file function from functions.py
            print(f'{file.name} is classified as {category}')
except FileNotFoundError: # If the folder doesn't exist, we catch the exception and print a message to the user.
    print('The folder does not exist')