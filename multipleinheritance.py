class calculation1:
    def add(self,a,b):
        return a+b

class calculation2:
    def subtract(self,a,b):
        return a-b

class calculation3:
    def multiply(self,a,b):
        return a*b
class calculation(calculation1,calculation2,calculation3):
    def divide(self,a,b):
        return a/b

calc = calculation()
print(calc.subtract(56,8))
print(calc.divide(16,5))
print(calc.add(7,5))
print(calc.multiply(23,7))
