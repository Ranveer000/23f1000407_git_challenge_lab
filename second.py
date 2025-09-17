def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b if b != 0 else "Division by zero!"
    else:
        return "Invalid operation!"

print("Result:", calculator(10, 5, "mul"))
