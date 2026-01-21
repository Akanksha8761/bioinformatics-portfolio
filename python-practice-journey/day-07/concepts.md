# Day 7: Advanced Loops & Patterns - Concepts

## 📌 Core Concepts Covered

Day 7 builds on Day 6's loop foundations by exploring advanced patterns, creative uses of range(), combining loops with conditionals, and practicing real-world applications. This day solidifies loop mastery through extensive practice.

---

## 1. range() Mastery

The `range()` function is incredibly versatile. Let's explore all its capabilities.

### **Basic range(stop)**
```python
# Prints 0, 1, 2, 3, 4
for i in range(5):
    print(i)
```

### **range(start, stop)**
```python
# Count from 2 to 10
for i in range(2, 11):
    print(i)  # 2, 3, 4, 5, 6, 7, 8, 9, 10
```

### **range(start, stop, step)**

**Even numbers (step = 2):**
```python
# 0, 2, 4, 6, 8, 10
for i in range(0, 11, 2):
    print(i)
```

**Counting backwards (negative step):**
```python
# Count from 10 down to 1
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 2, 1
```

**Important:** With negative step, start must be > stop!

```python
# WRONG - produces nothing
for i in range(0, 10, -1):  
    print(i)  # Nothing prints

# CORRECT
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

---

## 2. Iterating Over Strings

Strings are sequences, so you can loop through each character.

### **Character by Character:**
```python
word = "Methylation"
for char in word:
    print(char)
```

**Output:**
```
M
e
t
h
y
l
a
t
i
o
n
```

**Use Cases:**
- DNA sequence analysis
- Text processing
- Pattern matching
- Character counting

**Bioinformatics Example:**
```python
dna = "ATGCGATCG"
count_g = 0
for base in dna:
    if base == 'G':
        count_g += 1
print(f"G count: {count_g}")
```

---

## 3. Combining Loops with Conditionals

The real power emerges when combining loops (Day 6) with conditionals (Day 5).

### **Pattern: Check Each Item**
```python
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

### **Pattern: Filter and Process**
```python
for i in range(1, 51):
    if i % 7 == 0:  # Only multiples of 7
        print(f"{i} is a multiple of 7")
```

### **Pattern: Skip Certain Items**
```python
for i in range(1, 31):
    if i % 2 == 0 and i % 3 == 0:  # Multiples of 6
        continue  # Skip these
    print(i)  # Print everything else
```

---

## 4. Logical Operators in Loops

### **AND Operator**

Both conditions must be True:

```python
for i in range(1, 31):
    if i % 2 == 0 and i % 3 == 0:
        # Only when divisible by BOTH 2 AND 3
        print(f"{i} is divisible by both 2 and 3")
```

**Results:** 6, 12, 18, 24, 30 (multiples of 6)

### **OR Operator**

At least one condition must be True:

```python
for i in range(1, 21):
    if i % 3 == 0 or i % 5 == 0:
        # Divisible by 3 OR 5 (or both)
        print(f"{i} is divisible by 3 or 5")
```

**Results:** 3, 5, 6, 9, 10, 12, 15, 18, 20

### **NOT Operator**

Inverts the condition:

```python
for i in range(1, 11):
    if not (i % 2 == 0):  # Same as: i % 2 != 0
        print(f"{i} is odd")
```

---

## 5. Common Loop Patterns

### **Pattern 1: Repetition**
Do something N times:

```python
# Print "Hello" 5 times
for i in range(5):
    print("Hello")
```

### **Pattern 2: Counting/Accumulation**
Count or sum items:

```python
# Count squares
for i in range(1, 8):
    square = i * i
    print(f"The square of {i} is {square}")
```

### **Pattern 3: Countdown/Decrement**
Decrease a value:

```python
balance = 100
while balance > 0:
    print(f"Balance: ${balance}")
    balance -= 20
```

### **Pattern 4: Search with break**
Find something and stop:

```python
for i in range(1, 11):
    if i == 5:
        print("Found 5!")
        break
```

### **Pattern 5: Filter with continue**
Skip unwanted items:

```python
for i in range(1, 21):
    if i % 3 == 0:
        continue  # Skip multiples of 3
    print(i)
```

### **Pattern 6: Input Validation Loop**
Keep asking until valid:

```python
user_input = ''
while user_input != 'quit':
    user_input = input("Enter command: ")
    print(f"You typed: {user_input}")
```

---

## 6. Advanced while Loop Patterns

### **Controlled Infinite Loop**
```python
while True:
    command = input("Enter command: ")
    if command == 'quit':
        break
    # Process command
```

**Why it works:** `while True` creates infinite loop, but `break` provides exit.

### **Condition-Based Loop**
```python
balance = 100
while balance > 0:
    balance -= 20
    print(f"Remaining: ${balance}")
```

### **Counter-Based while Loop**
```python
i = 0
while i <= 5:
    print(i)
    i += 1
```

**Note:** For counting, `for` with `range()` is usually better!

---

## 7. Practical Applications

### **Application 1: Password System (3 Attempts)**

```python
correct_password = "dna123"

for attempt in range(1, 4):  # 3 attempts
    password = input("Enter password: ")
    
    if password == correct_password:
        print("Login Successful!")
        break
    else:
        print(f"Incorrect! Attempt {attempt}/3")
    
    if attempt == 3:
        print("Account locked.")
```

**Key features:**
- Limited attempts (for loop)
- Success exits early (break)
- Tracks attempt number
- Locks after 3 failures

---

### **Application 2: Number Range Filter**

```python
# Print only numbers divisible by 5 from 50 to 20
for i in range(50, 19, -1):
    if i % 5 == 0:
        print(f"{i} is divisible by 5")
```

**Features:**
- Backward counting
- Conditional filtering
- Clear output

---

### **Application 3: Genome Scan Simulator**

```python
# Scan all 23 human chromosomes
for chromosome in range(1, 24):
    print(f"Processing DNA on Chromosome {chromosome}...")
print("Genome scan complete.")
```

**Real-world parallel:**
- Actual genomic analysis software
- Processes chromosomes sequentially
- Provides progress feedback

---

### **Application 4: User Input Validator**

```python
while True:
    user_input = input("Enter a number: ")
    
    if user_input.lower() == 'quit':
        print("Exiting.")
        break
    
    number = int(user_input)
    
    if number > 100:
        print("Too high!")
        break
    else:
        print("Nice number!")
```

**Features:**
- Continuous input
- Exit condition
- Validation
- User feedback

---

## 8. Combining Multiple Concepts

### **Squares Calculator**
```python
# Days 1-7 concepts combined
for i in range(1, 8):  # Day 6: loop
    square = i * i      # Day 3: arithmetic
    print(f"The square of {i} is {square}")  # Day 2: f-strings
```

### **Even/Odd Classifier**
```python
for i in range(1, 11):  # Day 6: loop
    if i % 2 == 0:      # Day 5: conditional, Day 3: modulus
        print(f"{i} is even")  # Day 2: f-strings
    else:
        print(f"{i} is odd")
```

---

## 9. Common Mistakes and Solutions

### **Mistake 1: Wrong range() for Countdown**
```python
# WRONG - Doesn't work
for i in range(10, 1):  # Missing negative step
    print(i)  # Prints nothing!

# CORRECT
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

---

### **Mistake 2: Off-by-One Errors**
```python
# Want 1 to 7 inclusive
for i in range(1, 7):  # WRONG - stops at 6
    print(i)

for i in range(1, 8):  # CORRECT - includes 7
    print(i)
```

---

### **Mistake 3: continue Misunderstanding**
```python
# Wants to print odd numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip evens
    else:  # else is unnecessary!
        print(i)

# BETTER
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip evens
    print(i)  # No else needed
```

---

### **Mistake 4: Infinite Loop Conditions**
```python
# WRONG
i = 0
while i <= 5:
    print(i)
    # Forgot i += 1 - infinite loop!

# CORRECT
i = 0
while i <= 5:
    print(i)
    i += 1
```

---

## 10. Loop Efficiency Tips

### **Tip 1: Choose the Right Loop**

Use `for` when:
- You know the sequence
- Iterating over a collection
- Counting a known range

Use `while` when:
- Condition-based termination
- Unknown iteration count
- User input loops

### **Tip 2: Use break When Done**
```python
# Good - stops when found
for gene in genes:
    if gene == target:
        print("Found!")
        break  # Don't check rest

# Less efficient - checks all
for gene in genes:
    if gene == target:
        print("Found!")
    # Continues checking unnecessarily
```

### **Tip 3: Use continue for Filtering**
```python
# Clean filtering
for item in items:
    if not_valid(item):
        continue
    process(item)  # Only valid items
```

---

## 💡 Key Takeaways

1. **range()** is highly versatile: range(stop), range(start, stop), range(start, stop, step)
2. **Negative step** in range() enables counting backwards
3. **Strings are iterable** - loop through each character
4. **Loops + conditionals** create powerful filtering and processing
5. **Logical operators** (and, or, not) enable complex conditions
6. **break** exits loop, **continue** skips current iteration
7. **Pattern recognition** - many programming tasks follow common loop patterns
8. **for** for known sequences, **while** for conditions
9. Always ensure **loops can terminate** (avoid infinite loops)
10. **Combining concepts** from all previous days creates sophisticated programs

---

## 🎯 Loop Pattern Reference

```python
# Repetition
for i in range(n):
    do_something()

# Iteration
for item in collection:
    process(item)

# Counting
for i in range(start, stop):
    print(i)

# Backward counting
for i in range(start, stop, -1):
    print(i)

# Filtering
for item in items:
    if condition:
        continue
    process(item)

# Searching
for item in items:
    if item == target:
        break

# Accumulation
total = 0
for num in numbers:
    total += num
```

---

## 📚 Further Reading

- [range() Documentation](https://docs.python.org/3/library/stdtypes.html#range)
- [Logical Operators](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Loop Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)
- [Common Loop Patterns](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

---

*Mastering loop patterns is like learning musical scales - practice makes perfect, and soon you'll recognize which pattern fits each problem!*
