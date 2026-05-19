########################## try-except block #################################

# WITHOUT error handling (crashes program)
# print("-------------Division without error handling------------------")
# num1 = 10
# num2 = 0
# print(f"the division of {num1} and {num2} is {num1/num2}")
# ZeroDivisionError: division by zero

print("-------------Division using error handling------------------")
try:
    num1 = 10
    num2 = 2  # Try changing to 0 to see error handling
    # num2 = 0
    print(f"The division of {num1} and {num2} is {num1/num2}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

print("Program continues after handling error!\n")

##################### Catching Specific Multiple Exceptions #################

my_list = [10, 20, 30, 40]
greeting = "Hello"

# These would crash without error handling:
# print(f"The value in index 10 is {my_list[10]}")
# IndexError: list index out of range

# greeting = int(greeting)
# ValueError: invalid literal for int() with base 10: 'Hello'

print("--- Handling Multiple Exception Types ---")
try:
    print(f"My list: {my_list}")
    print(f"Greeting is: {greeting}")
    
    # Uncomment one of these to test different errors:
    # print(f"Greeting as int: {int(greeting)}")  # ValueError
    # print(f"The value at index 10: {my_list[10]}")  # IndexError
    
except ValueError:
    print("Error: Can't convert that string to an integer")
except IndexError:
    print("Error: No element at that index")

print()

#################### The else Block in try-except ############################

print("--- Using else block (runs if NO error occurs) ---")
num3 = 30
num4 = 5  # Try changing to 0
# num4 = 0

try:
    result = num3 / num4
    print(f"Attempting division: {num3} / {num4}")
except ZeroDivisionError:
    print(f"Cannot divide by zero!")
else:
    # This runs ONLY if no exception occurred
    print(f"Success! Result: {result}")

print()

############### The finally Block in try-except-else ###########################

print("--- Using finally block (ALWAYS runs) ---")
num5 = 30
num6 = 5  # Try changing to 0 to see finally still runs
# num6 = 0

try:
    result = num5 / num6
    print(f"Division: {num5} / {num6} = {result}")
except ZeroDivisionError:
    print(f"Cannot divide by zero!")
else:
    print(f"Successful division!")
finally:
    # This ALWAYS runs, whether error occurred or not
    print(f"Finally block: Cleanup code goes here")
    print(f"This runs no matter what!\n")

############# Raising Your Own Exceptions with raise ############################

print("--- Raising Custom Exceptions ---")

def process_methylation(value):
    """Expecting a methylation value between 0 and 1"""
    if not (0 <= value <= 1):  # Fixed logic - was backwards!
        raise ValueError(f"Methylation value {value} is out of range (must be 0-1)")
    print(f"Processing valid methylation value: {value}")
    return value * 100  # Convert to percentage

try:
    print(f"Result: {process_methylation(0.7)}")  # Valid
    print(f"Result: {process_methylation(1.5)}")  # Invalid - will raise error
    print("This line won't execute")
    
except ValueError as ve:
    print(f"Caught error: {ve}")

print()

############# Introduction to Debugging #################################

print("--- Debugging Techniques ---\n")

# Technique 1: Reading Error Messages (Tracebacks)

# Syntax Error Example (commented out):
# def my_func(x)  # Missing colon!
#     print(x)
# SyntaxError: invalid syntax

print("Technique 1: Reading Tracebacks")

def calculate_average(list_num):
    """Calculate average of numbers in list"""
    total = 0
    for num in list_num:
        total += num
    average = total / len(list_num)
    return average

print(f"Average: {calculate_average([10, 20, 30])}")

# Intentional Bug 1: What if list is empty?
# print(f"Average: {calculate_average([])}")
# ZeroDivisionError: division by zero

# Better version with error handling:
def calculate_average_safe(list_num):
    """Calculate average with error handling"""
    if len(list_num) == 0:
        return 0
    return sum(list_num) / len(list_num)

print(f"Safe average of empty list: {calculate_average_safe([])}")
print()

# Technique 2: print() Debugging (The "Caveman" Debugger)

print("Technique 2: Print Debugging")

def calculate_average_debug(list_num):
    """Calculate average with debug prints"""
    print(f"DEBUG: Function called with list: {list_num}")
    
    if len(list_num) == 0:
        print(f"DEBUG: Empty list received, returning 0")
        return 0
    
    total = 0
    for num in list_num:
        print(f"DEBUG: Adding {num} to total {total}")
        total += num
    
    average = total / len(list_num)
    print(f"DEBUG: Final average: {average}")
    return average

print(f"Result: {calculate_average_debug([10, 20, 30])}")
print()
print(f"Result: {calculate_average_debug([])}")
print()

# Technique 3: Using an IDE's Debugger
print("Technique 3: IDE Debugger")
print("Use your IDE's debugger to:")
print("- Set breakpoints")
print("- Step through code line by line")
print("- Inspect variable values")
print("- Watch expressions")
print()

############# Complete Exception Handling Pattern #################

print("--- Complete Exception Handling Pattern ---")

def process_gene_expression(filename):
    """Read and process gene expression data"""
    file_obj = None
    try:
        print(f"Opening file: {filename}")
        file_obj = open(filename, 'r')
        
        data = []
        for line in file_obj:
            value = float(line.strip())
            if value < 0:
                raise ValueError(f"Negative expression value: {value}")
            data.append(value)
        
        return data
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except ValueError as ve:
        print(f"Error: {ve}")
        return []
    else:
        print(f"Successfully read {len(data)} values")
    finally:
        if file_obj:
            file_obj.close()
            print("File closed")

# Test with non-existent file
result = process_gene_expression('nonexistent.txt')
print(f"Result: {result}")
print()

############# Best Practices Summary #################

print("--- Exception Handling Best Practices ---")
print("1. Catch specific exceptions, not generic Exception")
print("2. Use try-except-else-finally pattern")
print("3. Keep try blocks small (only risky code)")
print("4. Always clean up resources in finally")
print("5. Raise meaningful error messages")
print("6. Don't silence exceptions unnecessarily")
print("7. Use exceptions for exceptional cases, not control flow")
print()

print("--- Debugging Best Practices ---")
print("1. Read error messages carefully (traceback)")
print("2. Use print() to inspect values")
print("3. Test edge cases (empty lists, zero values, etc.)")
print("4. Use debugger for complex issues")
print("5. Write defensive code (check inputs)")
print("6. Add error handling proactively")

print("\n--- Day 18 Complete! ---")
