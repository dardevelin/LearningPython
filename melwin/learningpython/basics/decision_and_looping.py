var = 1

## if...else
if var == 0 :
	print("0")
else:
	print("1")
	
if var == 0:
	print("0")
elif var==1:
	print("1")
	
	
	
## while
while(var<=5):
	print(var)
	var+=1
else:
	print("var(%d) is greater than 5"%var)

## for
strings = ["one", "two", "three"]
for i in range(len(strings)):
	print(strings[i])

# continue, break, pass(just a place holder)