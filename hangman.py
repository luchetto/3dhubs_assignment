#!/usr/bin/env python

import random

secret_words = ["3dhubs", "marvin", "print", "filament", "order", "layer"]
user_guesses = ""
valid_characters="abcdefghijklmnopqrstuvwxyz1234567890"

def new_game(secret_words):
	"""
	Initialize a new game.
	secret_words: a list of words the user have to guess
	"""

	attempts=0
	word_index = random.randint(0,5)
	word_to_guess = secret_words[word_index]
	global mask
	mask = " _ " * len(secret_words[word_index])
	get_input(mask, word_to_guess, user_guesses, attempts, valid_characters, secret_words)
	return

def get_input(mask, word_to_guess, user_guesses, attempts, valid_characters, secret_words):
	"""
	Receive an imput from the command line
	mask: mask of the word_to_guess
	word_to_guess: word to be guessed
	user_guesses: list of characters already guessed
	attemtps: number of wrong attempts
	valid_characters: list of characters that can be accepted as input 
	"""

	print "\n The word to guess is: ", mask	
	print "\n # of attempts: ", attempts
	print "\n Insert a letter or a number \n"
	the_guess = raw_input()
	the_guess = the_guess.lower()
	# Check if the input is a valid character
	validity = check_validity(the_guess, valid_characters, user_guesses)
	if (validity is True):
		# CHeck if the user has guessed the letter
		if (check_if_guessed(the_guess, word_to_guess) >= 0):
			print "\n Great! your choosed the correct letter!"
			user_guesses += the_guess
			mask = calculate_mask(user_guesses, word_to_guess)
			you_won = check_if_won(user_guesses, word_to_guess, secret_words)
			if you_won is True:
				# If the user has won it stop the game
				return
		else:
			attempts = attempts + 1
			print "\n Sorry! the letter is not present in the word! you have now %d attempts" % (6 - attempts)
			you_lost = check_if_lost(attempts, secret_words)
			if you_lost is True:
				# If he user has lost it stop the game
				return
	else:
		print "\n The input is not valid! Insert a valid input"
	get_input(mask, word_to_guess, user_guesses, attempts, valid_characters, secret_words)
	return

def calculate_mask(user_guesses, word_to_guess):
	"""
	Generates the mask of the word from the given user_guesses
	"""
	global mask
	mask = ""
	for x in range(0, len(word_to_guess)):
		if (user_guesses.find(word_to_guess[x]) >= 0):
			mask += " " + word_to_guess[x] + " "
		else:
			mask += " _ "
	return mask

def check_validity(the_guess, valid_characters, user_guesses):
	"""
	CHeck if the characters inserted by the user is valid
	the_guess: The caracter inserted by the user
	"""
	validity = True
	if valid_characters.find(the_guess) < 0 or len(the_guess) != 1 or the_guess in user_guesses:
		validity = False
	return validity

def check_if_guessed(the_guess, word_to_guess):
	"""
	Check if the caracter inserted by the user is correct
	"""
	return word_to_guess.find(the_guess)


def check_if_won(user_guesses, word_to_guess,secret_words):
	"""
	Check if the user has won. If this is the case it ask to play another game
	"""
	you_won = True
	for x in range(0, len(word_to_guess)):
		if (user_guesses.find(word_to_guess[x]) < 0):
			you_won = False
			return you_won
	print "Congatulation! You won!"
	ask_if_new_game(secret_words)
	return you_won

def check_if_lost(attemtps, secret_words):
	"""
	Check if the user has won. If this is the case it ask to play another game
	"""
	you_lost = False
	if attemtps > 5:
		you_lost = True
		print "Sorry! You lost!"
		ask_if_new_game(secret_words)
	return you_lost


def ask_if_new_game(secret_words):
	"""
	Ask if the user wants to play another game. If yes it restart the game otherwise it returns and stop the game 
	"""
	print "Do you want to play another game? [y/n]"
	answer = raw_input()
	if answer not in ["y","n"]:
		print "Invalid input, press y or n!"
		ask_if_new_game(secret_words)
	if answer == "y":
		new_game(secret_words)
	else:
		return

if __name__ == "__main__":
	new_game(secret_words)


