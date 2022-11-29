#multi-level inheritance = inheritance of a derived class from another derived class

#this is a multi-level inheritance example, animal is the child of the class organism, dog is the child of the class animal
class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):
    def fetching(self):
        print("This dog is fetching a stick")

class Cat(Animal):
    def meow(self):
        print("This cat is meowing")

dog = Dog()
cat = Cat()

print(dog.alive)
dog.eat()
dog.fetching()