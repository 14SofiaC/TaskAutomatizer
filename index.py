import os
import functions
import pathlib
import shutil

folder = str(input('Insert the folder path: ')) # For now, we directly ask the user for the folder path. In the future, we will convert this into a command line argument. Or we may add a proper GUI for easier use.

try:
    functions.move_files(folder)
    print('Files have been organized successfully.')
except FileNotFoundError: # If the folder doesn't exist, we catch the exception and print a message to the user.
    print('The folder does not exist.')