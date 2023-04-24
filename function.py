def myname():
    print("My name is Zahra")

myname()

#parameters and arguments
def fullname(firstname, lastname):
    print(firstname+" "+lastname)

fullname("Zahra","Isiaho")

#tuple as an argument
def mygame(*game):
    print(game[2])

mygame("basketball","tennis","football")

#key-value arguments
def rank(position1, position2, position3):
    print("Student in first position "+position1)

rank(position1="Zahra", position2="Nicole", position3="Andrew" )