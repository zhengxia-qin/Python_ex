# ？ how to deal with wrong input, ex "f"
import random
number = random.randint(1,9)
n = 0
while True:
	guess = raw_input("Guess the number, type exit to quit this game : ")
	n += 1
	if guess == "exit":
		break
	elif int(guess) < number:
		print ("it's too low")
	elif int(guess) > number:
		print ("it's too high")
	elif int(guess) == number:
		print("bingo! You've taken %s times to guess") %n
		break
	else:
		print ("you've input wrong content, please retry")