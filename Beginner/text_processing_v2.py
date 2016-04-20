listC = []
with open('FileA.txt', 'r') as read_file_A:
	with open('FileB.txt', 'r') as read_file_B:
		listA = read_file_A.read().splitlines()  #method splitlines() returns a list with all the lines in string
		listB = read_file_B.read().splitlines()
		for i in range(len(listA)):
			listC.append(listA[i].lower() + " eat " + listB[i]) 
		print (listC)
with open('FileC.txt', 'w') as write_file_C:
    for j in listC:
    	write_file_C.write(j+'\n')
