## Lists : []
# Modifiable

list_1 = [1, "One", 1.0]
list_1[1] = "one" 
list_1.append("two")
del list_1[3]

for item in list_1:
    print(item," ",end="")

print("\n",len(list_1))

list_2 = [2, "two", 2.0]
print(list_1+list_2)

print(2 in list_2)

list_1.extend(list_2)
print(list_1)

l = [2,1,3,5,4]
l.sort()
print(l)