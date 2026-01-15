# Day 3: Arithmetic Operators - Concepts

## 📌 Core Concepts Covered

Python provides a comprehensive set of arithmetic operators for performing mathematical calculations. Today we explore all the fundamental operators and their behaviors.

---

## 1. Basic Arithmetic Operators

### **Addition (+)**
Adds two numbers together.

```python
a = 10
b = 48
c = a + b  # 58
print(f"The value addition of A and B is {c}")
```

**Use Cases:**
- Summing numbers
- Incrementing counters
- Combining values

---

### **Subtraction (-)**
Subtracts the second number from the first.

```python
a = 10
b = 48
d = a - b  # -38
print(f"The value subtraction of A and B is {d}")
```

**Use Cases:**
- Finding differences
- Decrementing counters
- Calculating changes

---

### **Multiplication (*)**
Multiplies two numbers.

```python
a = 10
b = 48
e = a * b  # 480
print(f"The value multiplication of A and B is {e}")
```

**Use Cases:**
- Calculating areas
- Scaling values
- Repeating operations

---

### **Division (/)**
Divides the first number by the second. **Always returns a float.**

```python
a = 10
b = 48
f = a / b  # 0.20833333333333334
print(f"The value division of A and B is {f}")
```

**Important:** Division by zero raises a `ZeroDivisionError`.

```python
# This will cause an error:
# result = 10 / 0  # ZeroDivisionError
```

---

## 2. Advanced Arithmetic Operators

### **Floor Division (//)**
Divides and rounds down to the nearest whole number (integer). Returns the quotient without the remainder.

```python
a = 10
b = 3
g = a // b  # 3 (not 3.333...)
print(f"The floor division of A and B is {g}")
```

**How it works:**
- `10 // 3` = 3 (rounds down from 3.333...)
- `20 // 5` = 4 (exact division, no rounding needed)
- `20 // 6` = 3 (rounds down from 3.333...)

**With Negative Numbers:**
```python
-7 // 2  # -4 (rounds down, not towards zero!)
7 // -2  # -4
-7 // -2 # 3
```

**Key Difference from Regular Division:**
```python
# Regular division (/) - always returns float
20 / 5  # 4.0 (float)

# Floor division (//) - returns integer
20 // 5  # 4 (int)
```

---

### **Modulus (%)**
Returns the **remainder** after division.

```python
a = 10
b = 3
h = a % b  # 1 (10 ÷ 3 = 3 remainder 1)
print(f"The modulus of A and B is {h}")
```

**Common Use Cases:**

**1. Check if a number is even or odd:**
```python
number = 10
if number % 2 == 0:
    print("Even")  # Remainder is 0
else:
    print("Odd")   # Remainder is 1
```

**2. Check divisibility:**
```python
# Is 15 divisible by 5?
15 % 5 == 0  # True (no remainder)

# Is 15 divisible by 4?
15 % 4 == 0  # False (remainder is 3)
```

**3. Cycling through ranges:**
```python
# Get day of week (0-6)
day_number = 25
day_of_week = day_number % 7  # 4 (cycles through 0-6)
```

---

### **Exponentiation (**)**
Raises a number to a power.

```python
a = 10
b = 2
i = a ** b  # 100 (10²)
print(f"The exponentiation of A and B is {i}")
```

**Special Uses:**

**Square root (power of 0.5):**
```python
k = 9
j = k ** 0.5  # 3.0 (square root of 9)
```

**Cube root (power of 1/3):**
```python
number = 27
cube_root = number ** (1/3)  # 3.0
```

**Squares and cubes:**
```python
5 ** 2   # 25 (5 squared)
5 ** 3   # 125 (5 cubed)
2 ** 10  # 1024 (2 to the power of 10)
```

---

## 3. Operator Precedence (BODMAS/PEMDAS)

Python follows standard mathematical order of operations:

**Order (highest to lowest priority):**
1. **P**arentheses `()`
2. **E**xponentiation `**`
3. **M**ultiplication `*`, **D**ivision `/`, Floor Division `//`, **M**odulus `%` (left to right)
4. **A**ddition `+`, **S**ubtraction `-` (left to right)

### Examples:

```python
result1 = 10 + 3 * 2
# 3 * 2 = 6 first (multiplication before addition)
# 10 + 6 = 16
print(result1)  # 16

result2 = (10 + 3) * 2
# (10 + 3) = 13 first (parentheses first)
# 13 * 2 = 26
print(result2)  # 26

result3 = 100 / 10 * 2
# Left to right: 100 / 10 = 10, then 10 * 2 = 20
print(result3)  # 20.0

result4 = 100 / (10 * 2)
# Parentheses first: 10 * 2 = 20, then 100 / 20 = 5
print(result4)  # 5.0

result5 = 2 ** 3 ** 2
# Exponentiation is right-to-left!
# 3 ** 2 = 9 first, then 2 ** 9 = 512
print(result5)  # 512
```

**Important:** Exponentiation associates **right-to-left**:
```python
2 ** 3 ** 2  # Same as 2 ** (3 ** 2) = 2 ** 9 = 512
# NOT (2 ** 3) ** 2 = 8 ** 2 = 64
```

---

## 4. Division: Float vs Floor Division

Understanding the difference between `/` and `//` is crucial:

| Operation | Operator | Result Type | Example |
|-----------|----------|-------------|---------|
| Regular Division | `/` | Always float | `10 / 3 = 3.333...` |
| Floor Division | `//` | Integer (rounds down) | `10 // 3 = 3` |

```python
num_a = 20
num_b = 5

# Regular division - ALWAYS returns float
div_float = num_a / num_b  
# Result: 4.0 (float), even though it's a whole number

# Floor division - returns integer
div_int = num_a // num_b   
# Result: 4 (int)

# When there's a remainder:
num_b = 6
div_float = num_a / num_b   # 3.3333... (float)
div_int = num_a // num_b    # 3 (int, rounded down)
```

---

## 5. Type Conversion in Arithmetic

Python automatically handles some type conversions:

**Integer + Integer = Integer**
```python
5 + 3  # 8 (int)
```

**Integer + Float = Float**
```python
5 + 3.0  # 8.0 (float)
```

**Integer / Integer = Float**
```python
10 / 2  # 5.0 (float, even though result is whole)
```

**Integer // Integer = Integer**
```python
10 // 2  # 5 (int)
```

---

## 6. Practical Applications

### **Even/Odd Checker**
```python
number = int(input("Enter a whole number: "))
remainder = number % 2

if remainder == 0:
    print("This number is even.")
else:
    print("This number is odd.")
```

### **Power Calculator**
```python
base = float(input("Enter base number: "))
exponent = float(input("Enter exponent: "))
result = base ** exponent
print(f"{base} to the power of {exponent} is {result}")
```

### **Rectangle Calculator**
```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
```

### **Simple Interest Calculator**
```python
# Formula: Interest = (P * R * T) / 100
principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

interest = (principal * rate * time) / 100
total = principal + interest

print(f"Simple Interest: {interest}")
print(f"Total Amount: {total}")
```

### **Tip Calculator**
```python
bill = float(input("Enter bill amount: "))
tip_percent = float(input("Enter tip percentage: "))

tip_amount = bill * (tip_percent / 100)
total_pay = bill + tip_amount

print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total to Pay: ${total_pay:.2f}")
```

---

## 💡 Key Takeaways

1. **Division (/)** always returns a float
2. **Floor Division (//)** returns an integer (rounds down)
3. **Modulus (%)** returns the remainder
4. **Exponentiation (**)** raises to a power
5. **Use parentheses** to control order of operations
6. **BODMAS/PEMDAS** determines operator precedence
7. **Exponentiation** associates right-to-left
8. **Type conversion** happens automatically in mixed operations

---

## 🔍 Quick Reference Table

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 3` | `1.6666...` |
| `//` | Floor Division | `5 // 3` | `1` |
| `%` | Modulus | `5 % 3` | `2` |
| `**` | Exponentiation | `5 ** 3` | `125` |

---

## 🎯 Common Patterns

**Check if even:**
```python
number % 2 == 0
```

**Check if divisible by x:**
```python
number % x == 0
```

**Get last digit:**
```python
number % 10
```

**Calculate square root:**
```python
number ** 0.5
```

**Round down:**
```python
number // 1
```

---

## 📚 Further Reading

- [Python Operators Documentation](https://docs.python.org/3/library/operator.html)
- [Operator Precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
