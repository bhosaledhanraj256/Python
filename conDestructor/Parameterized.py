class Student:
    def __init__(self, name):
        self.name = name
        print(self.name, "object created")

    def __del__(self):
        print(self.name, "object destroyed")

s1 = Student("Dhanraj")
s2 = Student("Shree")
del s1
del s2
