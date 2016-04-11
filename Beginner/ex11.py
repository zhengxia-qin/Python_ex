#Check Primality Functions
# Note: 1 is not a prime number
# Another methode: if we can find n%i == 0 when i is between 2 and n-1, then it's not a prime
def check_primality(n):
	list = []
	i = 1
	while i <= n:
		if n%i == 0:
			list.append(i)
		i += 1
	if list == [1, n]:
		print ("it's a prime number")
	else:
		print ("it's not a prime number")
		
def ask_number(prompt_text = "please give me a number: "):
	input_number = raw_input(prompt_text)
	return 	int(input_number)	

n = ask_number("input a number:")
check_primality(n)