#! python3
#Roku script CLI menu
import os
import sys
import termcolor
from roku import Roku
from termcolor import colored

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
	clear_screen()
	print(colored("""
	=====================================
	|				Roku				|
    |          Roku CLI Controller      |
    |-----------------------------------|
    |  left  : Move left                |
    |  right : Move right               |
    |  up    : Move up                  |
    |  down  : Move down                |
    |  select: Select                   |
	|	back: Back	                    |
    |  volup : Volume up                |
    |  voldown: Volume down				|
	|	backspace: Backspace			|
    |  text  : Enter text mode          |
	|	aa   : Active App				|
	|	info : App Info					|
    |  exit  : Exit                     |
    =====================================
    """, 'green'))

def main():
	roku = Roku('#.#.#.#')		#The Roku device ip here

	print_menu()

	while True:
		command = input(colored("Enter command: ", 'green')).strip().lower()
		
		if command == 'left':
			roku.left()
		elif command == 'right':
			roku.right()
		elif command == 'up':
			roku.up()
		elif command == 'down':
			roku.down()
		elif command == 'select':
			roku.select()
		elif command == 'back':
			roku.back()
		elif command == 'volup':
			roku.volume_up()
		elif command == 'voldown':
			roku.volume_down()
		elif command == 'backspace':
			roku.backspace()
		elif command == 'text':
			text = input(colored("Enter text: ", 'green')).strip().lower()
			roku.literal('{text}')
		elif command == 'aa':
			print(roku.active_app)
		elif command == 'info':
			roku.info()
		elif command == 'exit':
			print(colored("Exiting...", 'green'))
			break
		else:
			print(colored('Invalid command..', 'red'))

		print_menu()

if __name__ == "__main__":
	main()