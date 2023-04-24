#exceptions/errors
#whether there's an error or not
try:
    x = 5
    print(x)

#if there's an error from try
except:
    print("Value is not defined")

finally:
    print("Hello world")

try:
    num1 = 10
    num2 = 2
    print(num1/num2)
except:
    print("An arithmetic error occured")
finally:
    print("It is a success")

