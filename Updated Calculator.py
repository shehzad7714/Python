x = float(input("Please enter your 1st number: "))
op = input("Please input your function: ")
y = float(input("Please input your 2nd number "))

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x/y)

else:
    print("Invalid Operator used!")

