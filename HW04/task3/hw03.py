import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

def visualize_directory_structure(directory, indent=""):
    """
    Рекурсивно виводить структуру директорії з кольоровим форматуванням.
    
    Параметри:
        directory (Path): Шлях до кореневої директорії.
        indent (str): Відступ для виводу.
    """
    for item in directory.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/")
            visualize_directory_structure(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py /шлях/до/директорії")
        sys.exit(1)
    
    path_to_directory = Path(sys.argv[1])
    
    if not path_to_directory.exists():
        print(f"{Fore.RED}Шлях {path_to_directory} не існує.")
        sys.exit(1)
    if not path_to_directory.is_dir():
        print(f"{Fore.RED}Шлях {path_to_directory} не є директорією.")
        sys.exit(1)
    
    print(f"{Fore.YELLOW}Структура директорії: {path_to_directory}\n")
    visualize_directory_structure(path_to_directory)
