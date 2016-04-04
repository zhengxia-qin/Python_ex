#http://www.practicepython.org/exercises/
#Ex2

flag = True
while flag:
	num = int(raw_input("Please enter a number (if you want to stop, entre 0): "))
	if num % 2 == 0:
		if num == 0:
			flag = False
			break
		else:
			print("you entered a even number")
	else:
print("you entered an odd number")

#Ex6
#Ask the user for a string and print out whether this string
#is a palindrome or not
input_string = raw_input("Please enter a string: ")
n = len(input_string)-1
i = 0
while i <= n/2:
	if input_string[i] == input_string[n-i]:
		i = i+1
	else:
		print "this string is not a palindrome"
		break
if i == n/2 + 1:
	print "this string is a palindrome"
	
# other solutions for ex6: using string reversal
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
