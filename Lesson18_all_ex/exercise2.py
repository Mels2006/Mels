# cat -> color
class Animal:
    def __init__(self,age,name):
        self.age = age
        self.name = name
    def full_animal(self):
        return f"{self.name},{self.age}"
    def make_voice(self):
        return f"{self.name} is making voice"
dog = Animal("19","Shepard")
print(dog.full_animal())
class Cat(Animal):
   def __init__(self,age,name,color): 
       super().__init__(age,name)
       self.color = color
   def make_voice(self):
       return f"{self.name} is myauing"  
c = Cat("19","max","White")
print(c.color)
print(c.make_voice())