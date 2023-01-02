#Duck typing - a concept where the class of an object is less important than the methods it defines. the class type is not checked if minimum methods/attributes are present

class Duck:
    
    def talk(self):
        print("Quack quack")
    
    def walk(self):
        print("Walks like a duck")

class Chicken:

    def talk(self):
        print("Cluck cluck")
    
    def walk(self):
        print("Walks like a chicken")

class Person:

    def catch(self, duck):
        duck.talk()
        duck.walk()
        print("I caught a duck")

duck = Duck()
chicken = Chicken()
person = Person()
#will still work, because the person class is looking for the talk and walk methods, not the class type, it doesn't matter if it's a duck or chicken
person.catch(chicken)

# class Duck:
    
#     def talk(self):
#         print("Quack quack")
    
#     def walk(self):
#         print("Walks like a duck")

# class Chicken:
    
#     def walk(self):
#         print("Walks like a chicken")

# class Person:

#     def catch(self, duck):
#         duck.talk()
#         duck.walk()
#         print("I caught a duck")

# duck = Duck()
# chicken = Chicken()
# person = Person()
# person.catch(chicken)