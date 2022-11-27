#return statement =  functions send python values/objects back to teh caller. These values/objects are known as the functions return value

def multiply(number1, number2):
    result = number1 * number2
    return result


x = print(multiply(6,8))

print(x)