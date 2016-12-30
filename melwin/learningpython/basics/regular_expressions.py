import re


# Rule#1: simple characters match
match = re.search("ig", "come'on piiigs")
print(match.group())


# Rule#2: 
#    .    any character, except new line
#   \w    word characters :  letter, digit & _
#   \d    digit
#   \s    whitespace
#   \S    non-whitespace characters
#   +     one or more
#   *     zero or more

match = re.search("...g", "come'on piiigs")
print(match.group())

match = re.search("x...g", "come'on piiigs")
#print(match.group())    
#  won't work, all of the pattern must match 

match = re.search("\w\w:", "m!: come'on piiigs. m1: yo")
print(match.group())

match = re.search("\w\s+\d", "m1: come'on piiigs. lm 1 yo 2")
print(match.group())

match = re.search("http://\S+", "m1: come'on piiigs. http://www.abc.com lm 1 yo 2")
print(match.group())

match = re.search("[\w.]+@[\w.]+", "m1: come'on a.1@gmail.com piiigs. http://www.abc.com lm 1 yo 2")
print(match.group())

match = re.search("([\w.]+)@([\w.]+)", "m1: come'on a.1@gmail.com piiigs. http://www.abc.com lm 1 yo 2")
print("\nWhole Match: ",match.group())
print("Group#1: ",match.group(1))
print("Group#2: ",match.group(2))

match = re.findall("[\w.]+@[\w.]+", "m1: come'on a.1@gmail.com piiigs. http://www.abc.com lm 1 yo 2 b.2@yahoo.com ")
print(match)

match = re.findall("([\w.]+)@([\w.]+)", "m1: come'on a.1@gmail.com piiigs. http://www.abc.com lm 1 yo 2 b.2@yahoo.com ")
print(match)
