class food:
    fruits = "Apples"
    candy = "Chocolate"

    def fd(self):
        print("I love food")

class side(food):
     pass

fd = side()
fd.fd()
mine = fd.fruits
print(mine)
yours = fd.candy
print(yours)
