# Day 19: Advanced Functions - Concepts

## 📌 Core Concepts Covered

Advanced function features make Python incredibly flexible. Today we learn *args (variable positional arguments), **kwargs (variable keyword arguments), and lambda functions (anonymous functions). These are ESSENTIAL for professional Python development!

---

## 1. Variable Arguments: *args

**`*args` allows functions to accept ANY number of positional arguments.**

### **Basic Syntax:**
```python
def function_name(*args):
    # args is a TUPLE of all positional arguments
    for arg in args:
        print(arg)
```

### **Example:**
```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_numbers(1, 2, 3)  # 6
sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 55
```

**Key Points:**
- `*args` collects arguments into a **tuple**
- Can accept 0 or more arguments
- Named `args` by convention (can be any name after `*`)
- Useful when you don't know how many arguments will be passed

---

## 2. *args with Regular Parameters

**Regular parameters must come BEFORE *args:**

```python
def greet(name, *additional_names):
    print(f"Hello {name}!")
    for other in additional_names:
        print(f"And hello {other}!")

greet("Alice")  # Just one
greet("Alice", "Bob", "Charlie")  # Multiple
```

**Order matters:**
```python
def func(a, b, *args):  # ✓ Correct
    pass

def func(*args, a, b):  # ✗ Wrong! a and b become keyword-only
    pass
```

---

## 3. Variable Keyword Arguments: **kwargs

**`**kwargs` allows functions to accept ANY number of keyword arguments.**

### **Basic Syntax:**
```python
def function_name(**kwargs):
    # kwargs is a DICTIONARY of all keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### **Example:**
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# Output:
# name: Alice
# age: 30
# city: NYC
```

**Key Points:**
- `**kwargs` collects keyword arguments into a **dictionary**
- Can accept 0 or more keyword arguments
- Named `kwargs` by convention (can be any name after `**`)
- Access with `kwargs.get(key, default)` or `kwargs[key]`

---

## 4. Combining Everything

**The COMPLETE parameter order:**

```python
def function(pos1, pos2,           # 1. Regular positional
             default1="val",        # 2. Positional with defaults
             *args,                 # 3. Variable positional
             kwonly1,               # 4. Keyword-only (required)
             kwonly2="val",         # 5. Keyword-only (with default)
             **kwargs):             # 6. Variable keyword
    pass
```

### **Example:**
```python
def analyze(sample_id, organism="human", *replicates, 
            method, threshold=0.05, **parameters):
    print(f"Sample: {sample_id}")
    print(f"Organism: {organism}")
    print(f"Replicates: {replicates}")
    print(f"Method: {method}")  # Required keyword argument!
    print(f"Threshold: {threshold}")
    print(f"Other parameters: {parameters}")

# Call it:
analyze("S001", "mouse", "R1", "R2", "R3",
        method="RNA-seq", min_reads=1000, quality=30)
```

**Key Rules:**
1. Regular positional parameters first
2. Parameters with defaults next
3. `*args` for variable positional
4. Keyword-only parameters (after `*args`)
5. `**kwargs` for variable keyword (always last!)

---

## 5. Keyword-Only Arguments

**Arguments after `*args` become keyword-only** (must be called by name):

```python
def process(data, *extras, required, optional="default"):
    # required MUST be passed as keyword argument
    # optional can be omitted (has default)
    pass

# Correct:
process([1,2,3], required="value")
process([1,2,3], "extra", required="value", optional="custom")

# Wrong:
process([1,2,3], "required_value")  # Error! required is keyword-only
```

**Force keyword-only without *args:**
```python
def function(a, b, *, c, d):
    # c and d are keyword-only
    pass

function(1, 2, c=3, d=4)  # Correct
function(1, 2, 3, 4)  # Error!
```

---

## 6. Lambda Functions

**Lambda = anonymous function (no name, single expression).**

### **Syntax:**
```python
lambda parameters: expression
```

### **vs Regular Function:**
```python
# Regular function
def add(a, b):
    return a + b

# Equivalent lambda
add = lambda a, b: a + b
```

### **Characteristics:**
- **Single expression only** - No statements, no multiple lines
- **Automatically returns** - No `return` keyword needed
- **Anonymous** - Usually not assigned to a variable
- **Inline** - Used where function is needed briefly

---

## 7. Lambda Examples

### **Basic:**
```python
square = lambda x: x ** 2
print(square(5))  # 25
```

### **Multiple Parameters:**
```python
multiply = lambda a, b: a * b
print(multiply(3, 4))  # 12
```

### **No Parameters:**
```python
greet = lambda: "Hello!"
print(greet())  # Hello!
```

### **Conditional Expression:**
```python
max_val = lambda a, b: a if a > b else b
print(max_val(10, 5))  # 10
```

**Important:** Lambda limited to **single expression** - can't have if/elif/else blocks, multiple statements, or assignments.

---

## 8. Lambda with Higher-Order Functions

**Higher-order function = function that takes/returns functions.**

### **map() - Transform Each Element:**
```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]
```

### **filter() - Keep Elements Matching Condition:**
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]
```

### **sorted() - Custom Sort Key:**
```python
students = [("Alice", 88), ("Bob", 95), ("Charlie", 82)]

# Sort by score (second element)
sorted_students = sorted(students, key=lambda x: x[1])
# [('Charlie', 82), ('Alice', 88), ('Bob', 95)]
```

---

## 9. Practical Patterns

### **Pattern 1: Flexible Logger**
```python
def log(*messages, level="INFO", **metadata):
    print(f"[{level}]", *messages)
    if metadata:
        print(f"Metadata: {metadata}")

log("Processing", "data", level="DEBUG", user="Alice")
```

### **Pattern 2: Configuration Function**
```python
def configure(**settings):
    defaults = {"host": "localhost", "port": 8080}
    defaults.update(settings)  # Override with provided settings
    return defaults

config = configure(port=3000, debug=True)
```

### **Pattern 3: Data Processing**
```python
def process_data(data, *transforms, **options):
    result = data
    for transform in transforms:
        result = transform(result)
    return result

# Use with lambdas:
data = [1, 2, 3, 4, 5]
result = process_data(data,
                     lambda x: [i*2 for i in x],
                     lambda x: [i for i in x if i > 5])
```

---

## 10. When to Use What

### **Use *args when:**
- Unknown number of similar arguments
- Wrapper functions
- Flexible input requirements

### **Use **kwargs when:**
- Configuration/options
- Optional parameters (many)
- Forward arguments to another function

### **Use lambda when:**
- Short, simple function
- Used once (inline)
- Callback/key function for map/filter/sorted
- NOT when function is complex or reused

### **DON'T use lambda when:**
- Function is complex (multiple lines)
- Function is reused many times
- Function needs documentation
- Regular function is clearer

---

## 11. Common Pitfalls

### **Pitfall 1: Wrong Parameter Order**
```python
# Wrong!
def func(**kwargs, *args):  # Error!
    pass

# Correct
def func(*args, **kwargs):
    pass
```

### **Pitfall 2: Lambda Complexity**
```python
# Bad - too complex!
process = lambda x: x * 2 if x > 0 else x / 2 if x < 0 else 0

# Good - use regular function
def process(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return x / 2
    return 0
```

### **Pitfall 3: Forgetting Keyword-Only**
```python
def func(*args, required):
    # required is keyword-only!
    pass

func(1, 2, 3)  # Error! missing required
func(1, 2, 3, required="value")  # Correct
```

---

## 💡 Key Takeaways

1. **`*args`** = tuple of positional arguments
2. **`**kwargs`** = dictionary of keyword arguments
3. **Order:** positional, defaults, *args, keyword-only, **kwargs
4. **Lambda** = anonymous single-expression function
5. **map()** transforms elements
6. **filter()** keeps matching elements
7. **sorted(key=)** custom sorting
8. **Keyword-only** arguments after `*args`
9. **Use lambdas** for simple, short, one-time functions
10. **Professional Python** uses these patterns extensively

---

## 📚 Quick Reference

| Concept | Syntax | Type |
|---------|--------|------|
| *args | `def f(*args):` | tuple |
| **kwargs | `def f(**kwargs):` | dict |
| Lambda | `lambda x: x**2` | function |
| map() | `map(func, iterable)` | iterator |
| filter() | `filter(func, iterable)` | iterator |
| sorted(key=) | `sorted(list, key=func)` | list |

---

*Master these advanced features to write flexible, professional Python code!*
