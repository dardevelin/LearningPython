## Dictionary 
# 

dict = {1:"one", 2:"two", 3:"four", 4:"five"}

dict['3'] = "three"

del dict[4]

if(dict.__contains__(4)):
    print("dict contains 4")
else:
    print("dict doesn't contain 4")
