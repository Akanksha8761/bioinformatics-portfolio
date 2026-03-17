############ Defining and Calling Basic Functions (No Parameters, No Return) ####################

# Define a function using the 'def' keyword
def say_hello():
    """This function simply prints hello"""
    print("Hello, world!")
    print("This is my first function call")

print("---- Calling say_hello function for the first time ----")
say_hello()  # Calling say_hello() function

print("\n--- Calling say_hello() second time ---")
say_hello()  # Calling say_hello() function

# Define another simple function
def show_analysis_result():
    print("-" * 30)
    print("Starting analysis...")
    print("-" * 30)

print("\n--- Calling show_analysis_start() ---")
show_analysis_result()  # Calling show_analysis_result() function

# Write a new function called print_project_name
def print_project_name():
    print("MethylGraph-AI")

print("\n--- Calling print_project_name() ---")
print_project_name()
print_project_name()

############################## Functions with Parameters (Accepting Input) ####################

# Function with one parameter
def greet(name):
    """Greet a person using their name as argument"""
    print(f"Hello {name}! Have a great day ahead!!")

print("\n--- Calling greet() ---")
greet("Akanksha")
greet("Dr. Veerbhan")
# greet()  # TypeError: greet() missing 1 required positional argument: 'name'

# Function with multiple parameters
def area_triangle(width, height):
    area = 0.5 * width * height
    return area

print("\n--- Calling area_triangle() ---")
print(f"The area of triangle is {area_triangle(6, 8)}")

# print(f"The area of triangle is {area_triangle(6, 8, 2)}")
# TypeError: area_triangle() takes 2 positional arguments but 3 were given

########################## Functions with Return Values (Producing Output) ########################

# Function that returns a single value
def add_numbers(a, b):
    """This function is used to add two numbers and returns a single value"""
    sum_result = a + b
    return sum_result

print("\n--- Calling add_numbers() ---")
result = add_numbers(5, 10)
print(f"The result of addition of '5' and '10' is {result}")

# Use the return value directly
print(f"The addition of '20' and '50' is {add_numbers(20, 50)}")

# Function that returns multiple values (Python does this by returning a tuple)
def get_list_stats(data_list):
    """This function returns the count, sum, and average of a list of numbers"""
    count = len(data_list)
    if count == 0:
        return 0, 0, 0
    total = sum(data_list)
    average = total / count

    return count, total, average

print("\n--- Calling get_list_stats() ---")
numbers = [1, 2, 3, 4, 5]
count, total, average = get_list_stats(numbers)

print(f"Total no. of elements in list is {count}")
print(f"Sum of all elements in list is {total}")
print(f"Average of all elements in list is {average}")

# Functions that implicitly return None
def greet_simple(name):
    """This function prints a greeting message"""
    print(f"Hello, {name}")

print("\n--- Calling greet_simple() ---")
return_value = greet_simple("John")
print(f"Return value: {return_value}")  # None

# Functions that return None explicitly
def check_positive(number):
    """This function checks if the given argument is a positive number"""
    if number > 0:
        print(f"The {number} is a positive number")
        return "Is Positive"
    else:
        return None

print("\n--- Calling check_positive() ---")
print(f"The return value is: {check_positive(-2)}")
print(f"The return value is: {check_positive(2)}")

# Write a function is_even(number)
def is_even(number):
    """This function checks if the given number is even"""
    if number % 2 == 0:
        return True
    else:
        return False

print(f"\nThe number '7' is even: {is_even(7)}")
print(f"The number '8' is even: {is_even(8)}")

############################################## Arguments - Keyword and Default Values ###########

# Keyword Arguments
def gene_description(name, chromosome, start, end):
    """This function generates a description of a gene"""
    return f"Gene {name} is located on chromosome {chromosome} from position {start} to {end}"

print("\n--- Calling gene_description() with positional args ---")
print(gene_description('MYB77', 'chr13', 123456, 432567328))  # Positional - order matters!

# Order doesn't matter with keyword arguments
print(gene_description(start=541263, end=2736, chromosome='chr13', name='AP2'))

# print(gene_description(start=541263, end=2736, chromosome='chr13'))
# TypeError: gene_description() missing 1 required positional argument: 'name'

# Default Argument Values
def set_analysis_parameter(min_threshold, max_threshold=0.56):
    """Sets analysis parameters with optional max_threshold"""
    print(f"Minimum Threshold: {min_threshold}")
    print(f"Maximum Threshold: {max_threshold}")
    return f"Minimum: {min_threshold}, Maximum: {max_threshold}"

print("\n--- Calling set_analysis_parameter() ---")
print(set_analysis_parameter(10))

# You can use positional arguments for the default parameters too
print(set_analysis_parameter(10, 60))

# Call overriding defaults using keyword arguments
print(set_analysis_parameter(min_threshold=1.0, max_threshold=50))

# Incorrect default parameter definition (default before non-default)
# def bad_function_defaults(param1=10, param2): pass
# SyntaxError: non-default argument follows default argument

def bad_function_defaults(param1, param2=30):
    pass

# Write a function configure_plot
def configure_plot(title, xlabel="X-axis", ylabel="Y-axis", show_legend=True):
    """Configure plot with title, labels and legend"""
    return f"Title: {title}, X-label: {xlabel}, Y-label: {ylabel}, Legend: {show_legend}"

print("\n--- Calling configure_plot() different ways ---")
print(configure_plot(20.2))
print(configure_plot(title=20.2, ylabel=30))
print(configure_plot(20.2, ylabel=30))
print(configure_plot(20.2, ylabel=30, show_legend=False, xlabel=20))
print(configure_plot(20.2, 20, 30, False))

################################# Variable Scope (Local vs. Global) #########################################################################

# Global variable: Defined outside any function
global_message = "This message is from global scope"

def read_global():
    """This function reads the global variable"""
    print("\n----- Inside the read_global() function ------")
    print(f"{global_message}")

read_global()

def read_local():
    """This function reads the local variable"""
    print("\n----- Inside read_local() function ------")
    print("This message is from local scope")
    local_count = 30
    print(f"Local variable count: {local_count}")

read_local()

# Access local variable from global scope
# print(f"Local variable count: {local_count}")
# NameError: name 'local_count' is not defined

# Access global variable from global scope
print(f"\nGlobal message from global scope: {global_message}")

# --- Modifying Variables ---

# Attempting to modify a global variable from inside a function (common pitfall)
global_count = 10

# def increment_global_wrong():
#     """Increment global variable (WRONG - causes error)"""
#     global_count += 1
#     print(f"Inside (incorrect): {global_count}")
#
# increment_global_wrong()
# UnboundLocalError: local variable 'global_count' referenced before assignment

def increment_global():
    """Increment global variable (CORRECT - using global keyword)"""
    global global_count
    global_count += 1
    print(f"Inside: {global_count}")

print("\n--- Using global keyword ---")
increment_global()
increment_global()
increment_global()
increment_global()

# Better practice: pass variable as parameter and return new value
def increment_count(current):
    """Increment count passed as parameter"""
    new_count = current + 1
    return new_count

print("\n--- Better practice: parameter and return ---")
count = 0
print(f"The 1st new value is {increment_count(count)}")
count = increment_count(count)
print(f"The 2nd new value is {increment_count(count)}")
count = increment_count(count)
print(f"The 3rd new value is {increment_count(count)}")
count = increment_count(count)
print(f"The 4th new value is {increment_count(count)}")

# Variable shadowing example
variable = 10

def local_variable():
    """Create a local variable with the same name as the global variable"""
    variable = 20  # This creates a NEW local variable
    print(f"\nInside function: {variable}")
    return variable

print(f"Before calling function: {variable}")
result = local_variable()
print(f"After calling function, global variable: {variable}")  # Still 10!
print(f"Function returned: {result}")

# Simple calculator
def calculator(value1, value2):
    """This function serves as a simple calculator"""
    print(f"\nValue 1: {value1}")
    print(f"Value 2: {value2}")
    sum_result = value1 + value2
    sub = value1 - value2
    multi = value1 * value2
    divide = value1 / value2
    return sum_result, sub, multi, divide

print("\n--- Simple Calculator ---")
# For automated testing, using fixed values instead of input()
value1 = 10.0
value2 = 5.0
sum_result, sub, multi, divide = calculator(value1, value2)
print(f"The sum of {value1} and {value2} is {sum_result}")
print(f"The difference of {value1} and {value2} is {sub}")
print(f"The product of {value1} and {value2} is {multi}")
print(f"The quotient of {value1} and {value2} is {divide}")

# Uncomment below for interactive calculator:
# value1 = float(input("Please enter the first value: "))
# value2 = float(input("Please enter the second value: "))
# sum_result, sub, multi, divide = calculator(value1, value2)
# print(f"The sum of {value1} and {value2} is {sum_result}")
# print(f"The difference of {value1} and {value2} is {sub}")
# print(f"The product of {value1} and {value2} is {multi}")
# print(f"The quotient of {value1} and {value2} is {divide}")
