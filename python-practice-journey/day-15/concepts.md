# Day 15: Functions - Part 1 - Concepts

## 📌 Core Concepts Covered

Functions are reusable blocks of code that perform specific tasks. They're the foundation of modular programming, allowing you to organize code, avoid repetition, and create more maintainable programs. Today we cover the fundamentals: defining functions, parameters, return values, and scope.

---

## 1. What is a Function?

A **function** is a named block of code that performs a specific task and can be reused throughout your program.

### **Why Use Functions?**
- **Reusability**: Write once, use many times
- **Organization**: Break complex problems into smaller pieces
- **Readability**: Named functions make code self-documenting
- **Maintainability**: Fix bugs in one place
- **Abstraction**: Hide implementation details

### **Function Syntax:**
```python
def function_name(parameters):
    """Docstring: describes what the function does"""
    # Function body
    # Code to execute
    return value  # Optional
```

---

## 2. Basic Functions (No Parameters, No Return)

The simplest functions just execute code when called.

### **Defining a Function:**
```python
def say_hello():
    """Print a greeting message"""
    print("Hello, world!")
```

### **Calling a Function:**
```python
say_hello()  # Output: Hello, world!
say_hello()  # Can call multiple times!
```

**Key Points:**
- Use `def` keyword to define
- Function name follows naming conventions (lowercase, underscores)
- Parentheses `()` are required, even with no parameters
- Colon `:` starts the function body
- Indent the function body (4 spaces)
- Call by using the name followed by `()`

---

## 3. Functions with Parameters

Parameters allow functions to accept input and work with different data.

### **Single Parameter:**
```python
def greet(name):
    """Greet a person by name"""
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

### **Multiple Parameters:**
```python
def area_rectangle(width, height):
    """Calculate rectangle area"""
    area = width * height
    return area

result = area_rectangle(5, 10)  # result = 50
```

**Key Points:**
- Parameters are variables defined in function definition
- Arguments are values passed when calling the function
- Must provide correct number of arguments when calling
- Parameters are separated by commas

---

## 4. Return Values

Functions can send data back to the caller using `return`.

### **Single Return Value:**
```python
def add_numbers(a, b):
    """Add two numbers and return the result"""
    sum_result = a + b
    return sum_result

result = add_numbers(5, 3)  # result = 8
```

### **Multiple Return Values:**
```python
def get_stats(numbers):
    """Return count, sum, and average"""
    count = len(numbers)
    total = sum(numbers)
    average = total / count
    return count, total, average  # Returns a tuple!

c, t, avg = get_stats([1, 2, 3, 4, 5])
```

### **No Return (Returns None):**
```python
def just_print(message):
    """Only prints, doesn't return"""
    print(message)

result = just_print("Hi")  # result = None
```

**Key Points:**
- `return` exits the function immediately
- Can return any data type
- Multiple values returned as a tuple
- Functions without `return` implicitly return `None`
- Can have multiple `return` statements (in if/else)

---

## 5. Positional vs. Keyword Arguments

### **Positional Arguments:**
Order matters!

```python
def describe_gene(name, chromosome, start):
    return f"{name} on {chromosome} at {start}"

describe_gene("TP53", "chr17", 7577)  # Order is critical
```

### **Keyword Arguments:**
Order doesn't matter!

```python
describe_gene(start=7577, name="TP53", chromosome="chr17")
# Same result, different order!
```

### **Mixing Both:**
```python
describe_gene("TP53", start=7577, chromosome="chr17")
# Positional must come BEFORE keyword arguments
```

---

## 6. Default Parameter Values

Parameters can have default values for optional arguments.

### **Basic Default:**
```python
def greet(name, greeting="Hello"):
    """Greet with custom or default greeting"""
    print(f"{greeting}, {name}!")

greet("Alice")              # Uses default: Hello, Alice!
greet("Bob", "Hi")         # Override: Hi, Bob!
greet("Carol", greeting="Hey")  # Keyword: Hey, Carol!
```

### **Multiple Defaults:**
```python
def configure_plot(title, xlabel="X-axis", ylabel="Y-axis"):
    """Configure plot with defaults"""
    return f"Title: {title}, X: {xlabel}, Y: {ylabel}"

configure_plot("My Plot")  # Uses both defaults
configure_plot("My Plot", ylabel="Values")  # Override one default
```

**Important Rules:**
- Default parameters must come AFTER non-default parameters
- `def func(a, b=10)` ✓ Correct
- `def func(a=10, b)` ✗ SyntaxError!

---

## 7. Variable Scope

Scope determines where variables can be accessed.

### **Local Scope:**
Variables defined inside functions.

```python
def my_function():
    local_var = 10  # Only exists inside function
    print(local_var)

my_function()  # Works: 10
print(local_var)  # NameError: not defined
```

### **Global Scope:**
Variables defined outside functions.

```python
global_var = 100  # Defined globally

def read_global():
    print(global_var)  # Can READ global variables

read_global()  # Works: 100
print(global_var)  # Works: 100
```

### **Modifying Global Variables:**
Need `global` keyword to modify (not recommended).

```python
count = 0

def increment():
    global count  # Declare we're using global variable
    count += 1

increment()  # count = 1
increment()  # count = 2
```

**Better Practice:**
Pass as parameter, return new value.

```python
def increment(value):
    """Better: return new value"""
    return value + 1

count = 0
count = increment(count)  # count = 1
count = increment(count)  # count = 2
```

### **Variable Shadowing:**
Local variables can have same name as global.

```python
x = 10  # Global

def func():
    x = 20  # Local (shadows global)
    print(x)  # 20

func()
print(x)  # Still 10!
```

---

## 8. Docstrings

Documentation strings describe what functions do.

### **Single Line:**
```python
def add(a, b):
    """Add two numbers and return the result."""
    return a + b
```

### **Multi-line:**
```python
def complex_function(param1, param2):
    """
    Perform complex operation.
    
    Args:
        param1: First parameter description
        param2: Second parameter description
    
    Returns:
        Result description
    """
    # Function code
    return result
```

**Access docstring:**
```python
print(add.__doc__)  # Prints the docstring
help(add)  # Shows function help
```

---

## 9. Common Patterns

### **Pattern 1: Validation Function**
```python
def is_valid_gene_name(name):
    """Check if gene name is valid"""
    if len(name) == 0:
        return False
    if not name[0].isupper():
        return False
    return True
```

### **Pattern 2: Calculation Function**
```python
def calculate_gc_content(sequence):
    """Calculate GC percentage in DNA sequence"""
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    return ((g_count + c_count) / total) * 100
```

### **Pattern 3: Processing Function**
```python
def process_values(values, threshold):
    """Filter values above threshold"""
    result = []
    for value in values:
        if value > threshold:
            result.append(value)
    return result
```

### **Pattern 4: Formatter Function**
```python
def format_gene_info(name, chromosome, position):
    """Format gene information as string"""
    return f"Gene: {name} | Chr: {chromosome} | Pos: {position}"
```

---

## 10. Best Practices

### **Naming:**
- Use descriptive names: `calculate_average` not `calc`
- Use verbs for action functions: `get_data`, `process_results`
- Use lowercase with underscores: `my_function`

### **Length:**
- Keep functions focused on ONE task
- If too long (>50 lines), consider splitting
- Short functions are easier to test and debug

### **Parameters:**
- Limit to 3-5 parameters when possible
- Use default values for optional parameters
- Consider using dictionaries for many parameters

### **Returns:**
- Be consistent with return types
- Return early for error cases
- Use meaningful return values

### **Documentation:**
- Always include docstrings
- Explain what, not how (code shows how)
- Document parameters and return values

---

## 💡 Key Takeaways

1. **Functions enable code reuse** - Write once, use many times
2. **`def` defines functions** - Followed by name and parameters
3. **Parameters accept input** - Make functions flexible
4. **`return` sends output back** - Can return any type
5. **Default parameters are optional** - Provide flexibility
6. **Keyword arguments** - Allow calling in any order
7. **Local vs Global scope** - Variables have limited visibility
8. **Avoid global keyword** - Pass parameters and return values instead
9. **Docstrings document functions** - Explain what they do
10. **Functions should be focused** - One clear purpose per function

---

## 📚 Quick Reference

| Concept | Syntax | Example |
|---------|--------|---------|
| Define | `def name():` | `def greet():` |
| Call | `name()` | `greet()` |
| Parameter | `def name(param):` | `def greet(name):` |
| Return | `return value` | `return sum` |
| Default | `def name(param=value):` | `def greet(name="World"):` |
| Keyword | `name(param=value)` | `greet(name="Alice")` |
| Global | `global var` | `global count` |
| Docstring | `"""text"""` | `"""Add two numbers"""` |

---

*Functions are the building blocks of organized, reusable code. Master them to write professional Python!*
