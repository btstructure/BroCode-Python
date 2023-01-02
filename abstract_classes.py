#prevents a user from creating an object of that class
# * compels a user to override the abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method which is declared, but contains no implementation

#preventing a user from creating an object of that class, we need to import abc, which stands for abstract base class
from abc import ABC, abstractmethod

#within the class we have a go method

# class Vehicle:
#     def go(self):
#         pass

#the vehicle class is to generic, we want to force a user to create a child class of vehicle, the abstract class will inherit from ABC, now we can't create an object of the vehicle class

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

#car and motorcycle are child classes of vehicle
class Car(Vehicle):
    def go(self):
        print("I drive a car")

class MoterCycle(Vehicle):
    def go(self):
        print("I drive a motorcycle")


car = Car()
car.go()
motorcycle = MoterCycle()
motorcycle.go()