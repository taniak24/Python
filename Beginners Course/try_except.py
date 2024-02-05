
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Devided by 0")

