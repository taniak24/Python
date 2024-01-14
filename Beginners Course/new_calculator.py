
num = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num + num2)
elif op == "-":
    print(num - num2)
elif op == "/":
    print(num / num2)
elif op == "*":
    print(num * num2)
else:
    print("Invalid operator")
