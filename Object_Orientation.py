#to create a object you must create a class - this is the blueprint for the object

#attributes - describe what a object is or has
#methods - describe what a object can do


class Car:
    
    #the __init__ method is called when the object is created
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    #self refers to the object used in this method, in this case it is the car
    def drive(self):
        print("This "+self.model+  " is driving")
    
    def stop(self):
        print("The " +self.model+ " has stopped")
    
