class employee:
    def task(self):
        print("Employs")

class manager(employee):
    def role(self):
        print("Manages")
class chef(manager):
    def info(self):
        print("Works at a hotel")

c = chef()
c.task()
c.role()
c.info()



