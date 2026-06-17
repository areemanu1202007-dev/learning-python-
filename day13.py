# wap that input a int in range 0-999 and then prints if the integer entered is a 1/2/3
num = int(input("enter the number:"))
if num == 0:
    print("entered number is zero")
elif num < 0:
    print("invalid entry")
elif num < 10:
    print("single digit number")
elif num < 100:
    print("two digit number")
elif num < 1000:
    print("three digit number")
else:
    print("enter in range")
