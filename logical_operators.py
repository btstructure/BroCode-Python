#logical operators (and, or, not) = used to check if two or more conditions are met

#this prompt is an integer data-type
temp = int(input("What is the temperature outside?: "))

#and will execute if both conditions are met
if temp >= 0 and temp <= 30:
    print("the temperature is good today")
    print("go outside")
#or will execute if one of the conditions are met
elif temp < 0 or temp > 30:
    print("the temperature isn't it")
    print("stay inside")

temp1 = int(input("What is the temperature outside?: "))

#not will flip the condition true to false/ false to true
if not(temp1 >= 0 and temp1 <= 30):
    print("the temperature is good today")
    print("go outside")
elif not(temp1 < 0 or temp1 > 30):
    print("the temperature isn't it")
    print("stay inside")