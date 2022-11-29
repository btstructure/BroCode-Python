class Animal:

    def eat(self):
        print("This animal is eating")

#a object will use the method from the class it is created from, if the method is not found in the class it is created from, it will look in the parent class
#this will override the method in the parent class
#to do this you must define the method in the child class with the same name as the method in the parent class 
class Dog(Animal):
    
    def eat(self):
        print("This dog is eating kibble")