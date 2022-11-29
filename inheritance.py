#classes can inherit from other classes, parent and child

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

#the class Dog inherits from the class Animal, pass the parent class as an argument, these classes can have their own methods and attributes, 
# but they all can share the same attributes and methods from the parent class
class Dog(Animal):
    def fetching(self):
        print("This dog is fetching a stick")

class Cat(Animal):
    def meow(self):
        print("This cat is meowing")

class Rabbit(Animal):
    def hop(self):
        print("This rabbit is hopping")

dog = Dog()
cat = Cat()
rabbit = Rabbit()

rabbit.eat()
rabbit.hop()
cat.meow()
dog.fetching()