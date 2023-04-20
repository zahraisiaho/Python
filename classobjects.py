class Student:
    firstname = "eMobilis"
    lastname = "Technology"

    def course(self):
        print("I study python")
stu = Student()
stu.course()
name = stu.firstname
print(name)

class Employee:
    empname = "Zahra Isiaho"
    empid = 456

    def info(self):
        print("I started in February")

    def employee(self):
        print("I work at eMobilis")
emp = Employee()
name = emp.empname
id = emp.empid
print(name, id)
emp.employee()
emp.info()