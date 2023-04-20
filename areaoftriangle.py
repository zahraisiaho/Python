#Hero's formula
a = float(input("Enter first side:"))
b = float(input("Enter second side:"))
c = float(input("Enter third side:"))

p = (a+b+c)
s = p/2

area = (s*(s-a)*(s-b)*(s-c))**0.5
print(area)

#a half, base, height
d = float(input("Enter base:"))
e = float(input("Enter height:"))

z = (d*e*0.5)
print(z)

#OR
class area:
    def area(self, a, b):
        return 0.5*a*b

a = area()
print(a.area(9, 20))
