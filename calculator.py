
number1 = int(input("Write the first value: "))
number2 = int(input("Write the second value: "))
operation = input("Select an operation: ")
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    if number2 == 0:
        print("Second value can't be 0")
    else:
        print(number1 / number2)
else:
    print("Invalid operation, try again.")