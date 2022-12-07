#prevents a user from creating an object of that class
# * compels a user to override the abstraa methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method which is declared, but contains no implementation

class Vehicle:
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("I drive a car")

class MoterCyvle(Vehicle):
    def go(self):
        print("I drive a motorcycle")


car = Car()
car.go()
vehicle = Vehicle()
vehicle.go()