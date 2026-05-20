################### Basic *args Usage ###########################

print("--- Basic *args Usage ---\n")

def greet(*args):
    """This function accepts multiple positional arguments and prints them out"""
    print("-----Inside greet() ------")
    print(f"Type of args: {type(args)}")  # tuple
    print(f"Length of args: {len(args)}")
    
    if len(args) == 0:
        print("No arguments passed")
    else:
        print("Arguments received:")
        for arg in args:
            print(f"  - {arg} (type: {type(arg).__name__})")

print("--- Calling greet() ---")
# Arguments can be of any type
greet(90, 56.56, "Akanksha", True, None, {"key": "value"}, [90, 56.56, "Akanksha"])
print()

def sum_of_numbers(*args):
    """This function accepts multiple numbers and returns their sum"""
    print("-----Inside sum_of_numbers() ------")
    total = 0
    for num in args:
        print(f"  Adding: {num} (type: {type(num).__name__})")
        total += num
    return total

print("--- Calling sum_of_numbers() ---")
result = sum_of_numbers(12.345, 3, 4, 5.56, 6, 7, 8.67, 9, 10, 11.54, 12)
print(f"The sum of all numbers: {result}\n")

############ Using *args with Regular Positional Arguments ################

print("--- Using *args with Regular Arguments ---\n")

def greeting(name, age, *aliases):
    """Regular parameters BEFORE *args"""
    print("-----Inside greeting() ------")
    print(f"Name: {name}, Age: {age}")
    print(f"Type of aliases: {type(aliases)}")  # tuple
    
    if len(aliases) == 0:
        print("No aliases provided")
    else:
        print(f"Aliases: {', '.join(aliases)}")

print("--- Calling greeting() ---")
greeting("Akanksha", 30, "Radhu", "Deepu", "Ladoo")
greeting("Akanksha", 30)  # No aliases
greeting("Akanksha", 30, "Radhu")  # One alias
print()

######################## Basic **kwargs Usage #############################

print("--- Basic **kwargs Usage ---\n")

def print_all_keywords(**kwargs):
    """This function accepts multiple keyword arguments"""
    print("-----Inside print_all_keywords() ------")
    print(f"Type of kwargs: {type(kwargs)}")  # dict
    print(f"Length: {len(kwargs)}")
    
    if len(kwargs) == 0:
        print("No keyword arguments passed")
    else:
        print("Keywords received:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

print("--- Calling print_all_keywords() ---")
print_all_keywords()
print()
print_all_keywords(name="Akanksha", age=26, city="Palampur")
print()

def configure_hyperparameters(**parameters):
    """This function accepts hyperparameters with defaults"""
    print("-----Inside configure_hyperparameters() ------")
    
    # Get values with defaults
    learning_rate = parameters.get("learning_rate", 0.01)
    batch_size = parameters.get("batch_size", 32)
    epochs = parameters.get("epochs", 10)
    
    print(f"Using learning rate: {learning_rate}")
    print(f"Using batch size: {batch_size}")
    print(f"Using epochs: {epochs}")
    
    if "optimizer" in parameters:
        print(f"Using optimizer: {parameters['optimizer']}")

print("--- Calling configure_hyperparameters() ---")
configure_hyperparameters()
print()
configure_hyperparameters(learning_rate=0.001, batch_size=64, epochs=20, optimizer="adam")
print()

############### Using *args and **kwargs Together ####################

print("--- Combining *args and **kwargs ---\n")

def combined_function(param1, param2="default", *args, kwarg1, kwarg2="Palampur", **kwargs):
    """
    Order of parameters:
    1. Regular positional (param1)
    2. Regular with defaults (param2)
    3. *args (variable positional)
    4. Keyword-only (kwarg1 - REQUIRED after *args!)
    5. Keyword-only with defaults (kwarg2)
    6. **kwargs (variable keyword)
    """
    print("-----Inside combined_function() ------")
    print(f"param1: {param1}")
    print(f"param2: {param2}")
    
    if len(args) > 0:
        print(f"Extra positional args: {args}")
    
    print(f"kwarg1: {kwarg1}")
    print(f"kwarg2: {kwarg2}")
    
    if len(kwargs) > 0:
        print("Extra keyword args:")
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

print("--- Calling combined_function() ---")
combined_function("Hello", "World", kwarg1="Required!", name="Akanksha", age=26)
print()
combined_function("Hello", kwarg1="Still required!", city="Palampur", country="India")
print()

############# Basic Lambda Functions ######################

print("--- Lambda Functions (Anonymous Functions) ---\n")

# Regular function
def add(a, b):
    return a + b

print(f"Regular function: add(10, 50) = {add(10, 50)}")

# Equivalent lambda function
add_lambda = lambda a, b: a + b
print(f"Lambda function: add_lambda(10, 50) = {add_lambda(10, 50)}")
print(f"Type: {type(add_lambda)}")
print()

# Lambda to square a number
square = lambda x: x ** 2
print(f"Square lambda: square(5) = {square(5)}")

# Lambda with no arguments
greeting = lambda: "Hello Akanksha!"
print(f"No-arg lambda: greeting() = {greeting()}")

# Lambda with conditional expression
max_lambda = lambda a, b: a if a > b else b
print(f"Max lambda: max_lambda(10, 50) = {max_lambda(10, 50)}")
print()

################### Using Lambdas with Higher-Order Functions ####################

print("--- Lambdas with Higher-Order Functions ---\n")

numbers = [1, 2, 3, 4, 5, 6]
print(f"Original numbers: {numbers}")
print()

# 1. Using lambda with map() - applies function to each element
print("1. map() - Transform each element")
squares = list(map(lambda x: x ** 2, numbers))
print(f"   Squares: {squares}")
print()

# 2. Using lambda with filter() - keeps elements that match condition
print("2. filter() - Keep elements that match condition")
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"   Even numbers: {evens}")
print()

# 3. Using lambda with sorted() - custom sorting
print("3. sorted() - Custom sorting with key function")
student_scores = [("Alice", 88), ("Bob", 95), ("Charlie", 82), ("Diana", 95)]
print(f"   Original: {student_scores}")

# Sort by name (default)
sorted_by_name = sorted(student_scores)
print(f"   By name: {sorted_by_name}")

# Sort by score (second element of tuple)
sorted_by_score = sorted(student_scores, key=lambda item: item[1])
print(f"   By score (asc): {sorted_by_score}")

# Sort by score descending
sorted_by_score_desc = sorted(student_scores, key=lambda item: item[1], reverse=True)
print(f"   By score (desc): {sorted_by_score_desc}")

# Sort by score desc, then by name asc (for ties)
sorted_complex = sorted(student_scores, key=lambda item: (-item[1], item[0]))
print(f"   By score desc, name asc: {sorted_complex}")
print()

################### Practical Examples ####################

print("--- Practical Examples ---\n")

# Example 1: Flexible gene processing
def process_genes(*gene_names, organism="human", **metadata):
    """Process multiple genes with organism and optional metadata"""
    print(f"Processing {len(gene_names)} genes for {organism}")
    for gene in gene_names:
        print(f"  - {gene}")
    if metadata:
        print(f"Metadata: {metadata}")
    print()

process_genes("TP53", "BRCA1", "MYC", organism="mouse", lab="Lab A", date="2026-02-04")

# Example 2: Data analysis with lambda
methylation_values = [0.25, 0.85, 0.42, 0.91, 0.13, 0.78]
print(f"Methylation values: {methylation_values}")

# Filter high methylation (> 0.7)
high_methylation = list(filter(lambda x: x > 0.7, methylation_values))
print(f"High methylation (>0.7): {high_methylation}")

# Convert to percentages
percentages = list(map(lambda x: x * 100, methylation_values))
print(f"As percentages: {percentages}")
print()

# Example 3: Sorting genes by expression
gene_expression = [
    ("TP53", 120.5),
    ("BRCA1", 88.3),
    ("MYC", 210.1),
    ("EGFR", 55.7)
]
print(f"Gene expression data: {gene_expression}")

# Sort by expression level (descending)
sorted_genes = sorted(gene_expression, key=lambda x: x[1], reverse=True)
print(f"Sorted by expression (high to low): {sorted_genes}")
print()

print("--- Day 19 Complete! ---")
