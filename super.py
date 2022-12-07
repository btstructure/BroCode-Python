#super() = functions used to give access to methods of a parent class. Returns a temporary object of a parent class when used.

# class Rectangle:
#     pass

# class Square(Rectangle):
#     def __init__(self, length, width):
#         self.length   = length
#         self.width = width

# class Cube(Rectangle):
#     def __init__(self, length, width, height):
#         self.length = length #we are repeating code, when there is similaries between the 2 classes, we can use it in the rectangle class (parent)
#         self.width = width #we are repeating code, when there is similaries between the 2 classes, we can use it in the rectangle class (parent)
#         self.height = height

class Rectange:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectange):

    def __init__(self, length,width):
        super().__init__(length, width)

class Cube(Rectange):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.area() * self.height #the area method is inherited from the parent class, so we don't have to do self.length * self.width

square = (Square(3,3))
cube = (Cube(3,3,3))

print(square.area())
print(cube.volume())