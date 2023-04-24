num = float(input("Enter number:"))
num = int(num)
if num>1:
    for z in range(2,num):
        if num %z == 0:
             print("this is not prime number")
             break

    else:
         print("this is a prime number")
