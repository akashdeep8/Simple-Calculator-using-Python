def addition(a, b):
    result = a + b 
    print("Addition is:", result)
def subtraction(a, b):
    result = a - b 
    print("Subtraction is:", result)
def division(a, b):
    result = a / b 
    print("Division is", result)
def multiplication(a, b):
    result = a * b 
    print("Multiplication is", result)
print("SIMPLE CALCULATOR USING PYTHON")
while True:
    print("What Do You Want To Do")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Division")
    print("4 for Multiplication")
    print("Press Q to Quit")
    
    choice = input("Enter What You Want: ")
    if choice == 'q' or choice == 'Q':
        break
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    
    if choice == '1':
        addition(num1, num2)
    if choice == '2':
        subtraction(num1, num2)
    if choice == '3':
        division(num1, num2)
    if choice == '4':
        multiplication(num1, num2)
    else:
        print("Invalid Choice")