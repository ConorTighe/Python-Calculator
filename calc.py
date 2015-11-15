
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def divide(x,y):
    return x / y

def multiply(x,y):
    return x * y

def remain(x,y):
    return x % y

pick = input(" 1.Add \n 2.Subtract \n 3.Divide \n 4.Multiply \n 5.Remainder\n ")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if pick == '1':
   print(num1," + ",num2,"=", add(num1,num2))

elif pick == '2':
   print(num1," - ",num2,"=", subtract(num1,num2))

elif pick == '3':
   print(num1," / ",num2,"=", divide(num1,num2))

elif pick == '4':
   print(num1," * ",num2,"=", multiply(num1,num2))

elif pick == '5':
   print(num1," % ",num2,"=", remain(num1,num2))

else:
   print("Invalid input")