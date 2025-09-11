class Student:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")

s = Student()
del s
