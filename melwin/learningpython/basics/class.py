from Student import Student

s = Student("melwin",123,25)
s.display()
s.course='python'   #instance variable

# Python's garbage collector runs during program execution 
# and is triggered when an object's reference count reaches 
# zero. An object's reference count changes as the number 
# of aliases that point to it changes.

# An object's reference count increases when it is assigned 
# a new name or placed in a container (list, tuple, or 
# dictionary). The object's reference count decreases when 
# it's deleted with del, its reference is reassigned, or its 
# reference goes out of scope. When an object's reference 
# count reaches zero, Python collects it automatically.

del s