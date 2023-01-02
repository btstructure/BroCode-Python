#call a function that accepts object as an argument, here it'll accept a car and color

class Car:

    color = None

#make sure arguments are lowercase
def change_color(car, color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "green")

print(car_1.color)
print(car_2.color)
print(car_3.color)