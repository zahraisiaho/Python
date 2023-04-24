class animal:
    def speak(self):
        print("Speaking")

class dog(animal):
    def speak(self):
        print("Barking")

class bee(dog):
    def speak(self):
        print("Buzzing")

b = bee()
b.speak()

d = dog()
d.speak()