# My first module module1.py
def greet(name):
    """Prints a greeting message to the console."""
    return f"Hello, {name}! Welcome to Palampur! This is my first module"

def calculate(num1, num2):
    """Returns multiple calculations of two numbers."""
    sum_result = num1 + num2
    sub = num1 - num2
    multi = num1 * num2
    divide = num1 / num2
    return sum_result, sub, multi, divide

# This block of code will ONLY execute if module1.py is run directly.
# It will NOT execute if module1.py is imported into another script.
if __name__ == "__main__":
    print("------- module1.py is being run directly -------")
    print("This section is for testing or demonstrating the functions in module1.py.\n")
    print(greet("John"))
    print("------ Calling calculate() from within ---------")
    add, subtract, multiply, division = calculate(30, 10)
    print(f"The addition is {add}")
    print(f"The subtract is {subtract}")
    print(f"The multiplication is {multiply}")
    print(f"The division is {division}")  # This will print a float value
    print("------ Ending module1.py ---------")
