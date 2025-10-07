from pyfiglet import Figlet
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_stylish():
    # Create Figlet object
    f = Figlet(font='banner3-D')
    
    # The text to display
    text = "SAKTHI VEL"
    
    # Decorative symbols
    border = "★" * 50
    
    # Clear screen first
    clear_screen()
    
    # Print with decoration
    print(border)
    print()
    print(f.renderText(text))
    print()
    print(border)

if __name__ == "__main__":
    # You'll need to install pyfiglet first:
    # pip install pyfiglet
    print_stylish()