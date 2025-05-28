# Calculator

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b

symbols = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}
def calculator():
    user_input1 = float(input("Enter First Number: "))
    repeat = True
    while repeat is True:
        for operation in symbols:
            print(operation)
        user_symbol = input("Enter your Operation: ")
        user_input2= float(input("Enter Second Number: "))
        ans= symbols[user_symbol](user_input1,user_input2)
        print(f"Results: {user_input1} {user_symbol} {user_input2} = {ans}")
        repeat_mode = input("Type 'y' for continue more operation with result or Type 'n' for new start.")
        if repeat_mode == 'y':
            user_input1=ans
        else:
            repeat = False
            print("\n")
            calculator()
calculator()