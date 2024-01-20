# Create a Dog class that inherits from the Animal class. Give the breed argument 
# of Dog.breed a default value of “shepard”.
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
class Dog(Animal):
    def __init__(self,age,name,breed):
        super().__init__(age,name)
        self.breed = breed
    def make_voice(self):
        return f"{self.name} is breeding"
b = Dog("19","Max","Shepard")
print(b.breed)
print(b.make_voice())