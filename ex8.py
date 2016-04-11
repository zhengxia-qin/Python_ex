flag = True
while flag:
	player1 = raw_input("Player 1: Give me your choice : rock, paper, scissor ? ")
	player2 = raw_input("Player 2: Give me your choice : rock, paper, scissor ? ")
	if player1 == "rock":
		if player2 == "rock":
			print("play even! If you want to continue, press c")
		elif player2 == "scissor":
			print("player 1 is the winner! If you want to continue, press c")
		elif player2 == "paper":
			print("player 2 is the winner! If you want to continue, press c")
	elif player1 == "scissor":
		if player2 == "rock":
			print("player 2 is the winner! If you want to continue, press c")
		elif player2 == "scissor":
			print("play even! If you want to continue, press c")
		elif player2 == "paper":
			print("player 1 is the winner! If you want to continue, press c")
	elif player1 == "paper":
		if player2 == "rock":
			print("player 1 is the winner! If you want to continue, press c")
		elif player2 == "scissor":
			print("player 2 is the winner! If you want to continue, press c")
		elif player2 == "paper":
			print("play even! If you want to continue, press c")	
	if raw_input() == "c": flag = True
	else: flag = False