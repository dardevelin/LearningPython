## Dictionary 
# 

dict = {1:"one", 2:"two", 3:"four", 4:"five"}

dict['3'] = "three"

del dict[4]

if(4 in dict):
    print("dict contains 4")
else:
    print("dict doesn't contain 4")

for k in dict.keys():
    print(k,":",dict[k])
    
for tuple in dict.items():
    print(tuple)