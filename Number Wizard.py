######################################################################
#                                                                    #
#                     Python - NUMBER WIZARD					     #
#		                                                             #
#																	 #
#	   This is a game created at first in C# to practice my          #
#      Unity and Game Development skills. However I rewrote		     #
#	   it in Python.                          				         #
#                                                                    #
#      For more information please visit:                            #
#      https://www.udemy.com/unitycourse/                            #
#                                                                    #
#                                                                    #
######################################################################

import os
import random
import sys

max = 1000
min = 1
guess = "undefined"

#This represents the game difficulty
maxGuessesAllowed = 5

def NextGuess():
	global guess
	
	guess = random.randint(min,max)
	
	print (" \n Is the number higher or lower than %d ?\n" %(guess))
	print (" H = Higher \n L = Lower \n E = Equal\n")

def GuessHigher():
	global min
	
	min = guess
	NextGuess()

def GuessLower():
	global max

	max = guess
	NextGuess()
	
def Victory():
	print(" __      ___      _                    \n")
	print(" \ \    / (_)    | |                   \n")
	print("  \ \  / / _  ___| |_ ___  _ __ _   _  \n")
	print("   \ \/ / | |/ __| __/ _ \| '__| | | | \n")
	print("    \  /  | | (__| || (_) | |  | |_| | \n")
	print("     \/   |_|\___|\__\___/|_|   \__, | \n")
	print("                                 __/ | \n")
	print("                                 |___/ \n")
	print("      I will beat you next time!       \n")
	print("  Press P to play again or Q to quit   \n")
	
def Defeat():
	print("   _____                         ____                  \n")
	print("  / ____|                       / __ \                 \n")
	print(" | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __  \n")
	print(" | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| \n")
	print(" | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |    \n")
	print("  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|    \n")
	print("        Better luck next time trying to beat me!       \n")
	print("           Press P to play again or Q to quit          \n")

#Game starts here
playing = 1
while playing:
	print(" \n\n")	
	print(" ### ======================== ###\n")
	print(" ### Welcome to Number Wizard ###\n")
	print(" ###      Made in Python      ###\n")
	print(" ### ======================== ###\n")

	print(" Pick a number in your head and don't tell me!\n")
	print(" The lowest number you can pick is %d and the highest is %d!\n\n" %(min, max))

	#First attempt to guess is made here
	NextGuess()
	
	#All the others attempts are made here
	attempts = maxGuessesAllowed
	while attempts > 0:
		key = input(" ").lower()
		
		if key == "h":
			#Attemps equals to 1 means it was the last chance to guess - when it comes to 0, it goes outside the loop
			if attempts == 1:
				Victory()
			else:
				GuessHigher()
		
		elif key == "l":
			#Same logic to higher guesses applies to lower guesses
			if attempts == 1:
				Victory()
			else:
				GuessLower()
		
		elif key == "e":
			Defeat()
			break
		
		else:
			attempts += 1
			print("\n Wrong key - Make it right! \n")
		
		attempts -= 1
	
	#Play again or Quit logic
	key = input(" ").lower()
	if key == "p":
		os.system('cls')
	elif key == "q":
		sys.exit()
	else:
		os.system('cls')
		

