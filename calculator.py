#Task 1:Command Line Calculator
#Name:KAVYA
#Internship:Elevate Labs-python Developer Inetrnship
#Description:A Simple Command-line calculator using functions and loops


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def percentage(a, b):
    return (a * b) / 100

print("Simple Calculator")
print("------------------")

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 6:
        print("Exiting... Thank you! 💙")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", subtract(num1, num2))
    elif choice == 3:
        print("Result:", multiply(num1, num2))
    elif choice == 4:
        print("Result:", divide(num1, num2))
    elif choice == 5:
        print("Result:", percentage(num1, num2))
    else:
        print("Invalid choice! Try again.")
