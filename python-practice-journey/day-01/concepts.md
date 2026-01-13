# Day 1: Data Types and Variables - Concepts

## 📌 Core Concepts Covered

### 1. Python Data Types

Python has several built-in data types. The main ones covered today:

#### **Integer (int)**
- Whole numbers without decimal points
- Examples: `35`, `-10`, `0`, `1000`
- Use cases: Counting, indexing, discrete values

```python
my_age = 35
quantity = 1000
```

#### **Float**
- Numbers with decimal points
- Examples: `3.14`, `30.69`, `24.5`
- Use cases: Prices, measurements, scientific calculations

```python
pi_value = 3.144335
product_price = 30.69
```

#### **String (str)**
- Text data enclosed in quotes (single or double)
- Examples: `"Akanksha"`, `'Python'`, `"Hello World"`
- Use cases: Names, messages, text processing

```python
user_name = "Akanksha"
product_name = "Dabur"
```

#### **Boolean (bool)**
- Only two values: `True` or `False`
- Used for logical operations and conditions
- Use cases: Flags, conditions, status checks

```python
is_learning = True
has_admin_privileges = False
```

#### **NoneType**
- Special type representing the absence of a value
- Only one value: `None`
- Use cases: Default values, missing data

```python
database_result = None
```

---

### 2. The Print Function

The `print()` function displays output to the console.

**Basic Usage:**
```python
print(my_age)  # Prints: 35
```

**With Labels:**
```python
print("My age is:", my_age)  # Prints: My age is: 35
```

**Using F-Strings (Recommended):**
```python
print(f"My name is {user_name}, and my age is {my_age}")
# Prints: My name is Akanksha, and my age is 35
```

**Formatting Numbers:**
```python
print(f"The value of pi is {pi_value:.3f}")
# Prints: The value of pi is 3.144 (3 decimal places)
```

---

### 3. Type Checking with type()

The `type()` function returns the data type of a variable.

```python
print(type(my_age))          # <class 'int'>
print(type(pi_value))        # <class 'float'>
print(type(user_name))       # <class 'str'>
print(type(is_learning))     # <class 'bool'>
print(type(database_result)) # <class 'NoneType'>
```

---

### 4. Dynamic Typing

Python is **dynamically typed**, meaning variables can change their type during execution.

```python
item_code = 1023           # Initially an integer
print(type(item_code))     # <class 'int'>

item_code = "A101-X"       # Now a string
print(type(item_code))     # <class 'str'>
```

This flexibility is powerful but requires careful attention to avoid bugs.

---

### 5. Type Conversion (Casting)

You can explicitly convert between types using constructor functions.

**To Integer:**
```python
my_age = int(26)      # Already int, no change
my_age = int("26")    # String to int
```

**To Float:**
```python
my_age = float(26)    # Int to float: 26.0
```

**To String:**
```python
my_age = str(26.0)    # Float to string: "26.0"
```

**To Boolean:**
```python
# Most values are True except: 0, 0.0, "", None, empty collections
bool(1)        # True
bool(0)        # False
bool("")       # False
bool("Hello")  # True
```

---

### 6. User Input with input()

The `input()` function reads user input from the console.

**Important:** `input()` always returns a **string**, even if the user enters a number!

```python
visitor_name = input("Please enter your name: ")
# If user types "Alice", visitor_name = "Alice" (string)

favorite_number = input("Please enter your favorite number: ")
# If user types "42", favorite_number = "42" (string, not int!)

# Convert to integer for numerical operations
favorite_number_int = int(favorite_number)
# Now favorite_number_int = 42 (integer)
```

---

### 7. Boolean Logic

Booleans are used with logical operators:
- `and` - True if both conditions are True
- `or` - True if at least one condition is True
- `not` - Inverts the boolean value

```python
is_logged_in = True
has_admin_privileges = True

# Both must be True
if (is_logged_in and has_admin_privileges):
    print("Admin access granted")
```

---

## 💡 Key Takeaways

1. **Python has 5 basic data types**: int, float, str, bool, NoneType
2. **F-strings** are the modern, readable way to format strings
3. **type()** helps you check what type a variable is
4. **Dynamic typing** means variables can change types
5. **Type conversion** must be explicit (e.g., `int()`, `float()`)
6. **input()** always returns strings - convert when needed
7. Python is case-sensitive: `True` ≠ `true`

---

## 🎯 Practice Tips

- Always use meaningful variable names
- Use f-strings for string formatting
- Check types when debugging
- Remember to convert `input()` results when doing math
- Practice type conversion to understand how Python handles different types

---

## 📚 Further Reading

- [Python Official Docs - Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Real Python - Basic Data Types](https://realpython.com/python-data-types/)
- [PEP 498 - F-String Formatting](https://www.python.org/dev/peps/pep-0498/)
