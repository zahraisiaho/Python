class animal:
    age : 18

    def speak(self):
        print("Speaking")

class dog(animal):
    def eat(self):
        print("Eating")

d = dog()
d.speak()
d.eat()



print(issubclass(dog, animal))
print(isinstance(d,dog))