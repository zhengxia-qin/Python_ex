# ex9 guessing game one


#!/usr/bin/python
import random
number = random.randint(1,9)
n = 0
while True:
	guess = raw_input("Guess the number between 1 and 9, type exit to quit this game : ")
	n += 1
	if guess == "exit":
		break
	elif not guess.isdigit():
		print ("invalid input, please retry: ")
	elif int(guess) < number:
		print ("it's too low")
	elif int(guess) > number:
		print ("it's too high")
	elif int(guess) == number:
		print("bingo! You've taken %s times to guess") %n
		break