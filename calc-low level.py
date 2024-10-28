
def myproject(x, y, z):
    if z == "+":
        return x + y
    elif z == "-":
        return x - y
    elif z == "*":
        return x * y
    elif z == "/":
        return x / y
    else:
        print("Wrong input")
        return 0


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = input("Enter the act: ")

re = myproject(x, y, z)
print(re)
