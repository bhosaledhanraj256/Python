class animal:
    def sound(self):
        return "all sounds of an animal"
        
class dog(animal):
    def sound(self):
       return "Bark!"
        
obj1=animal()
print(obj1.sound())
obj2=dog()
print(obj2.sound())
