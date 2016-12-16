class Human():
    def __init__(self, age=10):
        self.age = age

class Student(Human):
    no_of_students = 0
    def __init__(self, name, id, age):
        # needs to be explicitly called
        Human.__init__(self, age)
        self.id = id
        self.name = name
        Student.no_of_students+=1
    
    def display(self):
        print(self.id,":",self.name,":",self.age)
    
    def __del__(self):
        print("Getting Destroyed")