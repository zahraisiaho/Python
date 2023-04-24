class animal:
    alive = True

    def sleep(self):
        print("It is sleeping")
    def eat(self):
        print("It is eating")

class fish(animal):
    def myfish(self):
        print("This is a fish")

fsh = fish()
fsh.sleep()
fsh.eat()
fact = fsh.alive
print(fact)
fsh.myfish()