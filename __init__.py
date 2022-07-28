import time, random, string, os
from colorama import Fore, Back, Style, init

class color:
	

	def __init__(self):
		init()
		# Colors
		self.CYAN = Fore.LIGHTCYAN_EX
		self.BLUE = Fore.LIGHTBLUE_EX
		self.GREEN = Fore.LIGHTGREEN_EX
		self.YELLOW = Fore.LIGHTYELLOW_EX
		self.RED = Fore.LIGHTRED_EX
		self.PINK = Fore.LIGHTMAGENTA_EX
		self.RANDOMCOLOR = random.choice([self.RED, self.GREEN, self.CYAN, self.BLUE, self.YELLOW, self.PINK])
		self.RESET = Fore.RESET
	
	def success(self, text):
		print(self.GREEN + "[√] " + text + self.RESET)
	
	def fail(self, text):
		print(self.RED + "[X] " + text + self.RESET)
	
	def task(self, text):
		print(self.YELLOW + "[-] " + text + self.RESET)

class helper:
	"""
	General helper class
		randomSleep: Sleeps for a random amount of seconds between your two inputs			|	randomSleep(first: int, second: int) -> int
		randomString: Returns a random string the length of the inputs						|	randomString(a: str) -> str:
		randomBirthday: Returns a random birthday in dict form from 1980-2003 birth year.	|	randomBirthday() -> dict:
		randomPassword: Generates a random													|	randomPassword(length:int, numbers:bool=False, symbols:bool=False, upper:bool=False) -> str:
		openUrl: Opens the given URL														|	openUrl(url:str)
		title: Sets console window title to the input										|	title(text:str):
		resize: Resizes the window console with given inputs								|	resize(s1:int, s2:int):
		clear: Clears the console															|	clear()
	"""
	def randomSleep(first:int, second:int) -> int:
		number = random.randint(first, second)
		time.sleep(number)
	
	def randomString(a:str) -> str:
		letters = string.ascii_letters
		result_str = "".join(random.choice(letters) for i in range(a))
		return result_str
	
	def randomBirthday() -> dict:
		year = random.randint(1980, 2003)
		month = random.randint(1, 12)
		day = random.randint(1, 25)
	
		return {
			"day": day,
			"month": month,
			"year": year
		}
	
	def randomPassword(length:int, numbers:bool=False, symbols:bool=False, upper:bool=False) -> str:
		characters = string.ascii_lowercase
		if upper == True:
			characters = characters + string.ascii_uppercase
		if numbers == True:
			characters = characters + string.digits
		if symbols == True:
			characters = characters + "!@#$%^&*()"
		randomPassword = "".join(random.choice(characters) for x in range(length))
		return randomPassword
	
	def openUrl(url:str):
		os.system("start \"\" " + url)
	
	def title(text:str):
		os.system(f"title {text}")
	
	def resize(s1:int, s2:int):
		os.system('mode con: cols='+ str(s1) + ' lines=' + str(s2))
	
	def clear():
		os.system('cls' if os.name == 'nt' else 'clear')

class file:
	def file_exists(file:str) -> bool:
		if os.path.exists(file):
			return True
		else:
			return False
	
	def del_file(file:str):
		if os.path.exists(file):
			os.remove(file)
	
	def ensure_dir(file:str):
		if not os.path.exists(file):
			os.makedirs(file)
	
	def file_to_list(file:str) -> list:
		return [line.strip() for line in open(file).readlines()]