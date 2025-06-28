#write a pogram find maximum numbers
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))

if num1>num2 and num1>num3:
    print("num1 is maximum")
elif num2>num1 and num2>num3:
    print("num2 is maximum")
else:
    print("num3 is maximum")
    