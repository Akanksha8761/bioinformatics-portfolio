# Day 5: Conditional Statements - Concepts

## 📌 Core Concepts Covered

Today marks a major milestone in programming - the ability to make **decisions**! Conditional statements allow programs to execute different code based on different conditions, making programs dynamic and intelligent.

---

## 1. Comparison Operators (Conditional Operators)

Comparison operators compare two values and return a **boolean** (`True` or `False`).

### **Equality (==)**
Checks if two values are equal.

```python
print(5 == 5)        # True
print(5 == 6)        # False
print(10 == 10.0)    # True (compares value, not type)
```

**Important:** Use `==` for comparison, not `=` (which is for assignment).

```python
# WRONG - Assignment, not comparison
if x = 5:  # SyntaxError!

# CORRECT - Comparison
if x == 5:  # This works
```

---

### **Inequality (!=)**
Checks if two values are NOT equal.

```python
print("apple" != "orange")  # True (they are different)
print(5 != 5)               # False (they are the same)
```

---

### **Greater Than (>)**
Checks if left value is greater than right value.

```python
print(5 > 6)   # False
print(10 > 5)  # True
```

---

### **Less Than (<)**
Checks if left value is less than right value.

```python
print(5 < 6)   # True
print(10 < 5)  # False
```

---

### **Greater Than or Equal To (>=)**
Checks if left value is greater than OR equal to right value.

```python
print(5 >= 6)   # False
print(5 >= 5)   # True (equal counts)
print(6 >= 5)   # True (greater counts)
```

---

### **Less Than or Equal To (<=)**
Checks if left value is less than OR equal to right value.

```python
print(5 <= 6)   # True (less counts)
print(5 <= 5)   # True (equal counts)
print(6 <= 5)   # False
```

---

## 2. Special Comparisons

### **Comparing Strings**
Strings are compared **lexicographically** (alphabetically, based on Unicode values).

```python
print("A" > "B")      # False (A comes before B)
print("apple" < "banana")  # True
print("A" < "a")      # True (uppercase < lowercase in Unicode)
```

**How it works:**
- Compares character by character
- Uses Unicode values (A=65, B=66, a=97, b=98, etc.)
- Uppercase letters come before lowercase

---

### **Comparing Booleans with Numbers**
In Python, `True` equals `1` and `False` equals `0`.

```python
print(True == 1)   # True
print(False == 0)  # True
print(True > 0)    # True
print(False < 1)   # True
```

**Why?** Booleans are a subtype of integers in Python.

---

## 3. The if Statement

The `if` statement executes code only when a condition is `True`.

### **Basic Syntax:**
```python
if condition:
    # Code to execute if condition is True
    # Note the indentation!
```

### **Example:**
```python
number = 5
if number > 0:
    print("The number is positive")
# Output: The number is positive
```

**Key Points:**
1. Condition must evaluate to `True` or `False`
2. Code inside `if` is **indented** (usually 4 spaces)
3. Indentation is **mandatory** in Python!

---

### **Indentation in Python**

Python uses indentation to define code blocks. This is different from languages like Java or C++ that use braces `{}`.

```python
# CORRECT
if number > 0:
    print("Positive")  # Indented - part of if block
    print("Good!")     # Indented - part of if block

# WRONG - IndentationError!
if number > 0:
print("Positive")  # Not indented
```

**Standard:** Use 4 spaces for each indentation level.

---

## 4. The if-else Statement

The `else` statement provides an alternative when the `if` condition is `False`.

### **Syntax:**
```python
if condition:
    # Code if condition is True
else:
    # Code if condition is False
```

### **Example: Adult or Minor**
```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

**Flow:**
- If `age >= 18` is `True` → prints "You are an adult"
- If `age >= 18` is `False` → prints "You are a minor"
- Exactly **one** of these will execute, never both

---

### **Example: Even or Odd**
```python
number = int(input("Please enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**How it works:**
- `number % 2` gives the remainder when dividing by 2
- If remainder is `0` → even number
- If remainder is not `0` (it's `1`) → odd number

---

## 5. Multiple if Statements vs if-else

### **Multiple if Statements**
Each `if` is checked independently. Multiple blocks can execute.

```python
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive")
if number == 0:
    print("The number is zero")
if number < 0:
    print("The number is negative")
```

**Problem:** All three conditions are checked, even if the first one is true. Inefficient!

---

### **Using if-else (Better)**
```python
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number == 0:
    print("The number is zero")
else:
    print("The number is negative")
```

**Better because:**
- Only checks until one condition is true
- More efficient
- Clearer logic flow

**Note:** In your code, you used separate `if` statements. We'll learn `elif` soon for better structure!

---

## 6. Practical Applications

### **Password Checker**
```python
password = input("Please enter your password: ")
correct_password = "123456"

if password == correct_password:
    print("Access granted")
else:
    print("Incorrect password! Access denied")
```

**Real-world use:**
- Login systems
- Authentication
- Security checks

---

### **Gene Expression Analysis**
```python
exp = float(input("Enter patient's gene expression level: "))

if exp == 0.0:
    print("The patient has low gene expression")
if exp > 0.0:
    print("The patient has high gene expression")
if exp < 0.0:
    print("The patient has no gene expression")
```

**Bioinformatics application:**
- Analyzing gene activity
- Diagnosing conditions
- Research analysis

**Note:** Using `elif` would be better here to avoid checking all conditions.

---

### **Grade Pass/Fail Checker**
```python
score = float(input("Please enter your score (out of 100): "))

if score >= 70:
    print("Pass")
else:
    print("Fail")
```

**Real-world use:**
- Educational systems
- Performance evaluation
- Automated grading

---

## 7. Comparison Operators Quick Reference

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 6` | `True` |
| `>` | Greater than | `5 > 6` | `False` |
| `<` | Less than | `5 < 6` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `5 <= 6` | `True` |

---

## 8. Boolean Logic Fundamentals

### **What is a Boolean?**
A boolean is a data type with only two values:
- `True`
- `False`

### **Comparison operators produce booleans:**
```python
result = 5 > 3  # result is True (boolean)
print(type(result))  # <class 'bool'>
```

### **Booleans in conditions:**
```python
is_adult = age >= 18  # Boolean variable

if is_adult:  # No need for "if is_adult == True"
    print("Adult")
```

---

## 9. Common Patterns

### **Range Check**
```python
if 0 <= score <= 100:
    print("Valid score")
```

### **Divisibility Check**
```python
if number % 5 == 0:
    print("Divisible by 5")
```

### **Empty String Check**
```python
if password == "":
    print("Password cannot be empty")
```

### **Non-zero Check**
```python
if count != 0:
    print("Count is non-zero")
```

---

## 10. Common Mistakes to Avoid

### **Mistake 1: Using = instead of ==**
```python
# WRONG
if x = 5:  # SyntaxError!

# CORRECT
if x == 5:  # Comparison
```

---

### **Mistake 2: Forgetting Indentation**
```python
# WRONG
if x > 0:
print("Positive")  # IndentationError!

# CORRECT
if x > 0:
    print("Positive")
```

---

### **Mistake 3: Comparing Strings and Numbers**
```python
age = input("Enter age: ")  # Returns string "25"

# WRONG - Comparing string to number
if age > 18:  # TypeError!

# CORRECT - Convert first
age = int(age)
if age > 18:
    print("Adult")
```

---

### **Mistake 4: Forgetting Colon**
```python
# WRONG
if x > 0  # SyntaxError! Missing colon

# CORRECT
if x > 0:
    print("Positive")
```

---

## 💡 Key Takeaways

1. **Comparison operators** return `True` or `False`
2. **if statements** execute code when condition is `True`
3. **else statements** provide alternative code when condition is `False`
4. **Indentation** is mandatory and defines code blocks
5. **Type conversion** is needed when comparing `input()` values
6. Use `==` for comparison, `=` for assignment
7. Conditions can use any comparison operator
8. String comparisons use alphabetical/Unicode order
9. `True == 1` and `False == 0` in Python

---

## 🎯 Decision-Making Flow

```
Input → Condition → True? → Execute if block
                  ↓
                False? → Execute else block
```

---

## 📚 Further Reading

- [Python if/else Documentation](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Comparison Operators](https://docs.python.org/3/reference/expressions.html#comparisons)
- [Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

---

*Conditional statements are the foundation of program logic. Mastering them unlocks the ability to build truly interactive and intelligent programs!*
