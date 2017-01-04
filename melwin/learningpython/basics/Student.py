class Human():
    def __init__(self, age=10):
        self.__age = age

class Student(Human):
    no_of_students = 0  #Class variable
    def __init__(self, name, id, age):
        # needs to be explicitly called
        Human.__init__(self, age)
        self.__id = id
        self.__name = name
        Student.no_of_students+=1
    
    def display(self):
        print(self.__id,":",self.__name,":",self._Human__age)
    
    def __del__(self):
        print("Getting Destroyed")