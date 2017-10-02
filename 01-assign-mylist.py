mylist=[]
x='abac'
y=0
while y < len(x):
#	print(x[y])
	mylist.append(x[y])
	y += 1
	
# print (mylist)
y=0
while y < len(x)-1:
#	print(x[y:(y+2)])
	mylist.append(x[y:(y+2)])
	y += 1


y=0
while y < len(x)-2:
#	print(x[y:(y+3)])
	mylist.append(x[y:(y+3)])
	y += 1

mylist.append(x)
print (mylist)
print (str(mylist)[1:-1])

