class Dog:
    number_of_dogs = 1
    def __init__(self,bread,name,color,age):
        self.bread = bread
        self.name = name
        self.color = color
        self.age = age
        Dog.number_of_dogs += 1
    def bark(self):
        return f"barking {self.name}"
    def sit(self):
        return f"sitting {self.name}"        
dog_1 = Dog(bread = "pitbull",name = "tuzik",color = "blue",age= "12")
print(Dog.number_of_dogs)
print(dog_1.bark())
print(dog_1.sit())

