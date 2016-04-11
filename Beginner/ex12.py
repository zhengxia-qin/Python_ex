#ex12

def new_list(a):
	newlist = []
	newlist.append(a[0])
	newlist.append(a[len(a)-1])
	return newlist

print new_list([1,2,3,4])
