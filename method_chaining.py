#method chaining - calling multiple methods sequentially each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("The car is turned on")
        return self
    
    def drive(self):
        print("I am  driving the car")
        return self
    
    def brake(self):
        print("I am stepping on the breaks")
        return self

    def turn_off(self):
        print("The car is turned off")
        return self
#self will return car

car = Car()


car.turn_on().drive().brake().turn_off()

# car.turn_on().\
# drive().\
# brake().\
# turn_off()