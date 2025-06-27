print("\n")
a = int(input("Enter the operation to perform \n 1) Addition 2) Subtraction 3) Multiplication 4) Division : "))
x = int(input("Enter the first value: "))
y = int(input("Enter the second value: "))
if a == 1:
    print("", x, "+", y, " = ", x + y)
elif a == 2:
    print("", x, "-", y, " = ", x - y)
elif a == 3:
    print("", x, "*", y, " = ", x * y) 
elif a == 4:
    if y == 0:
        print("Undefined")
    else:
        print("", x, "/", y, " = ", x / y)