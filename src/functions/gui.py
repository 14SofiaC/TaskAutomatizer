from src.functions.functions import clear, getch, move_files
from time import sleep
from pathlib import Path

def browse_folder(def_path=None): # Function to browse folders interactively. It allows the user to navigate through directories and select a folder. It starts from the user's home directory by default.
    if def_path is None:
        current = Path.home() 
    else:
        current = Path(def_path)
    while True:
        clear()
        try:
            current_folders = sorted([item for item in current.iterdir() if item.is_dir()]) # Get all the folders in the current directory and sort them alphabetically
        except PermissionError:
            print('[ERROR] Not enough permission to access this folder.')
            current = current.parent
            continue
        for i, bf_folder in enumerate(current_folders, start=1):
            print(f'[{i}] {bf_folder.name}')
        if len(current_folders) == 0:
            print('[WARNING] This folder does not have any other folders inside.') # If the current folder has no subfolders, we print a warning message to inform the user.
        print('==================================================')
        if not len(current_folders) == 0:
            print(f'[1-{len(current_folders)}] Move to another folder')
        print('[c] Choose current folder')
        print('[b] Go back')
        print('[x] Exit')
        print('==================================================')
        print(f'Current folder: {current}')
        print("\033[?25h", end="", flush=True)
        option = input('Select option: ')
        if option.lower() == 'c':
            clear()
            return str(current)
        elif option.lower() == 'x':
            clear()
            return None
        elif option.lower() == 'b':
            clear()
            current = current.parent
        elif option.isdigit():
            clear()
            index = int(option) - 1
            if 0 <= index < len(current_folders):
                current = current_folders[index]
            else:
                print('[ERROR] Out of range.')
                sleep(3)
        else:
            clear()
            print('[ERROR] Unvalid option.')
            sleep(3)

def organize(folder, simulation: bool): # Function to organize files in a given folder. It takes the folder path and a boolean indicating whether to perform a simulation or actual organization. If simulation is True, it will only log the actions without moving any files.
    try:
        if not simulation:
            move_files(folder, sim=False)
            print('[SUCCESS] Files have been organized successfully.\n* log.txt created.')
        else:
            move_files(folder, sim=True)
            print('[SUCCESS] Simulation log created successfully.\n* sim_log.txt created.')
        sleep(3)
        clear()
    except FileNotFoundError: # If the folder doesn't exist, we catch the exception and print a message to the user.
        clear()
        print('[ERROR] The folder does not exist.')
        sleep(3)
        clear()

def action_menu(simulation=False): # Function to display the action menu for organizing files. It allows the user to choose between browsing folders interactively or selecting a folder by providing its path. The simulation parameter determines whether the organization will be simulated or executed.
    clear()
    print("\033[?25l", end="", flush=True)
    try:
        while True:
            print('========== Task Automatizer ==========')
            print('1 - Browse folders (interactively)')
            print('2 - Select folder (path)')
            print('3 - Go back')
            print('======================================')

            option = getch()
            if option == '3':
                clear()
                break
            elif option == '2':
                clear()
                print("\033[?25h", end="", flush=True)
                folder = str(input('Insert the folder path: ')) # For now, we directly ask the user for the folder path. In the future, we will convert this into a command line argument. Or we may add a proper GUI for easier use.
                organize(folder, simulation)
            elif option == '1':
                clear()
                folder = browse_folder()
                if folder:
                    organize(folder, simulation)
            else:
                clear()
                print('[ERROR] You must choose an option from 1 to 3.')
                sleep(3)
    finally:
        print("\033[?25h", end="", flush=True)
            

def menu(): # Main menu function that displays the main options for the user. It allows the user to choose between organizing a folder, running a simulation, changing the language (not implemented yet), or exiting the program.
    print("\033[?25l", end="", flush=True)
    try:
        while True:
            clear()
            print('========== Task Automatizer ==========')
            print('1 - Organize folder')
            print('2 - Simulation')
            print('3 - Language')
            print('4 - Exit')
            print('======================================')

            option = getch()
            if option == '4':
                clear()
                break
            elif option == '1':
                action_menu(simulation=False)
            elif option == '2':
                action_menu(simulation=True)
            elif option == '3':
                clear()
                print('[INFO] Language selection is not implemented yet.')
                sleep(3)
            else:
                clear()
                print('[ERROR] You must choose an option from 1 to 4.')
                sleep(3)

    finally:
        print("\033[?25h", end="", flush=True)