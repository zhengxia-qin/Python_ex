#List Overlap Comprehensions, Randomly generate two lists to test this 
import random
newlist =[]
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
len1 = random.randint(1,10)
len2 = random.randint(1,10)
a = random.sample(range(20),len1)
b = random.sample(range(20),len2)
print a
print b

newlist = [i for i in a for j in b if i == j]
			
print newlist