from calc_art import logo

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    choice = ""
    user_num1 = 0
    while True:
        if choice != "y":
            user_num1 = float(input("What is the first number?: "))
            
        print(", ".join([k for k in operations.keys()]))
        op = ""

        while op not in operations.keys():
            op = input("Choose a operator: ")
            
            if op not in operations.keys():
                print("Please type a valid operator!")
        
        user_num2 = float(input("What is the second number?: "))
        
        result = operations[op](user_num1, user_num2)
        
        print(str(user_num1) + " " +  op + " " + str(user_num2) + " = " + str(result))
        
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            print("You continue your calculation with the result from the previous operation!")
            user_num1 = result
        else:
            break
        
calculator() 