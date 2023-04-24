# local variable
def car():
    x = "volvo"
    print(x)

car()

# Global variable
y = 100

def number():
    global y
    print(y)

number()
