from colorama import Fore, Back, Style, init
import random

# Initialize colors
init()

# Colors
CYAN = Fore.LIGHTCYAN_EX
BLUE = Fore.LIGHTBLUE_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RED = Fore.LIGHTRED_EX
PINK = Fore.LIGHTMAGENTA_EX
RANDOMCOLOR = random.choice([RED, GREEN, CYAN, BLUE, YELLOW, PINK])
RESET = Fore.RESET

def success(text):
	print(GREEN + "[√] " + text + RESET)

def fail(text):
	print(RED + "[X] " + text + RESET)

def task(text):
	print(YELLOW + "[-] " + text + RESET)