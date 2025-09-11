class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s = Student("Dhanraj", 70)
s.show()
