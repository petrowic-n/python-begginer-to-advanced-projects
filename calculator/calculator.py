
def sum(first, sec):
    return first + sec

def subtraction(first, sec):
    return first - sec

def multiplication(first, sec):
    return first * sec

def division(first, sec):
    return round(first / sec, 1)

while True:
    # User Input
    first_num = int(input("Enter first number: "))
    sec_num = int(input("Enter second number: "))
    user_input = input("Choose an operation (+, -, /, *): ")

    if user_input == "+":
        print("Result: ",sum(first_num, sec_num))
        break
    elif user_input == "-":
        print("Result: ", subtraction(first_num, sec_num))
        break
    elif user_input == "*":
        print("Result: ", multiplication(first_num, sec_num))
        break
    elif user_input == "/":
        print("Result: ", division(first_num, sec_num))
        break
    else:
        print("Invalid input")

