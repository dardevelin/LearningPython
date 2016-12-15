## Python is completely object oriented, and not "statically typed". 
## You do not need to declare variables before using them, or declare 
## their type. Every variable in Python is an object.


## Numbers
# Python supports two types of numbers - integers and floating point numbers

my_int = 7
my_float = 7.0
my_float_2 = float(7.0)
boolean = True #or False

print(my_int," ",my_float," ",my_float_2," ",boolean)



## Strings
string_1 = 'it is string_1'
string_2 = "it's string_2"
print(string_1+" & "+string_2)

# %s %d %f %.<d>f %x
print("int:%d\tstring:%s" %(my_int, string_1))

words = string_1.split(sep=" ")
print(words)

# [start:stop:step]
print(string_1[0:len(string_1):2])



## Assingment
a,b = 3,4
print(a," ",b)


## Operators
# + - * / %
# ** Exponent
# // Floor Division
# in , not in
