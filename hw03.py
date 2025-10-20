from pathlib import Path
from sys import argv
from colorama import Fore

# Завдання 3

def iterate_folder(path:Path, indent:str = ""):
    for item in path.iterdir():
        if item.is_dir():
            print(f"{Fore.BLUE}{indent}{item.name}/{Fore.RESET}")
            iterate_folder(item, indent + "     ")
        else:
            print(f"{Fore.YELLOW}{indent}{item.name}{Fore.RESET}")

if len(argv) > 1:
    directory_path = Path(argv[1])
    if(directory_path.exists() and directory_path.is_dir()):
        iterate_folder(directory_path)
    else:
        print("Вкажіть коректний шлях до директорії")