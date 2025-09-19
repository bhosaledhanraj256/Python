class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class constructor
        # It returns a temporary object of the parent class
        
        self.breed = breed

    def speak(self):
        super().speak()         # Call parent class method
        print(f"{self.name} barks")

# Test
d = Dog("Tommy", "Bulldog")
d.speak()
