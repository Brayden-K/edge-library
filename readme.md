# Edge's Personal Library

## General helper class
**Import: from edge import helper**
	- randomSleep: Sleeps for a random amount of seconds between your two inputs
		`randomSleep(first: int, second: int) -> int`
	- randomString: Returns a random string the length of the inputs
		`randomString(a: str) -> str:`
	- randomBirthday: Returns a random birthday in dict form from 1980-2003 birth year
		`randomBirthday() -> dict:`
	- randomPassword: Generates a random
		`randomPassword(length:int, numbers:bool=False, symbols:bool=False, upper:bool=False) -> str:`
	- openUrl: Opens the given URL
		`openUrl(url:str)`
	- title: Sets console window title to the input
		`title(text:str):`
	- resize: Resizes the window console with given inputs
		`resize(s1:int, s2:int):`
	- clear: Clears the console
		`clear()`

## File helper class
**Import: from edge import file**
		- file_exists: Verifies that a file exists
			`file_exists(file:str) -> bool:`
		- del_file: Deletes a file
			`del_file(file:str):`
		- ensure_dir: Verifies that a folder exists and if not creates it
			`ensure_dir(file:str):	`
		- file_to_list: Reads a file and converts the lines to list
			`file_to_list(file:str) -> list:`

## Colors
**Import: from edge import color**
		- INITIALIZE: c = color()
		- success: prints a success message
			`c.success(msg:str)`
		- fail: prints a fail message
			`c.fail(msg:str)`
		- task: prints a task message
			`c.task(msg:str)`
		- To print a custom color:
			`print(f"{c.RED}hello{c.RESET}")`