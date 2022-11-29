class Car:
    #the class variable is declared in the class but before the constructor

    wheels = 4 #class variable
    
    #the __init__ method is called when the object is create, constructor
    
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
