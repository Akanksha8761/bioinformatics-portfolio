# Day 6: Loops - Concepts

## 📌 Core Concepts Covered

Loops are one of the most powerful programming concepts - they allow you to **repeat code** multiple times without writing it over and over. Today we explore two types of loops: `while` loops and `for` loops, along with loop control statements.

---

## 1. The while Loop

A `while` loop repeats code as long as a condition is `True`.

### **Basic Syntax:**
```python
while condition:
    # Code to repeat
    # Must eventually make condition False!
```

### **Example: Countdown**
```python
countdown = 10
print("Starting countdown...")
while countdown > 0:
    print(countdown)
    countdown -= 1  # Decrease by 1
print("Liftoff!!!")
```

**How it works:**
1. Check: Is `countdown > 0`?
2. If True → Execute loop body
3. Repeat from step 1
4. If False → Exit loop, continue with code after

**Output:**
```
Starting countdown...
10
9
8
...
1
Liftoff!!!
```

---

### **Critical: Loop Must Eventually End**

**Infinite Loop (BAD!):**
```python
countdown = 10
while countdown > 0:
    print(countdown)
    # Forgot to decrease countdown!
    # Loop runs forever!
```

**Proper Loop (GOOD):**
```python
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1  # Eventually makes condition False
```

**Rule:** Always ensure the loop condition will eventually become `False`.

---

## 2. The for Loop

A `for` loop iterates over a sequence (like a list or range).

### **Basic Syntax:**
```python
for item in sequence:
    # Code that uses item
```

### **Example: Iterating Over a List**
```python
status = ["Healthy", "Cancer", "Healthy"]
for patient_status in status:
    print(f"Processing {patient_status}")
```

**Output:**
```
Processing Healthy
Processing Cancer
Processing Healthy
```

**How it works:**
- First iteration: `patient_status = "Healthy"`
- Second iteration: `patient_status = "Cancer"`
- Third iteration: `patient_status = "Healthy"`
- After last item: Exit loop

---

### **Using range() with for Loops**

`range()` creates a sequence of numbers.

**Syntax:**
- `range(stop)` → 0, 1, 2, ..., stop-1
- `range(start, stop)` → start, start+1, ..., stop-1
- `range(start, stop, step)` → start, start+step, ..., before stop

**Examples:**
```python
# Count 0 to 4
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Count 1 to 5
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

---

### **Accessing List Items by Index**
```python
gene_list = ["BRCA1", "TP53", "PTEN"]

for i in range(len(gene_list)):
    current = gene_list[i]
    print(f"Index {i}: {current}")
```

**Output:**
```
Index 0: BRCA1
Index 1: TP53
Index 2: PTEN
```

**When to use:**
- When you need the index number
- When you need to modify the list
- When searching for something

---

## 3. Loop Control: break

`break` **immediately exits** the loop.

### **Example: Search with break**
```python
gene_list = ["BRCA1", "TP53", "PTEN", "EGFR"]
target_gene = "TP53"

print(f"Searching for {target_gene}...")
for i in range(len(gene_list)):
    current = gene_list[i]
    if current == target_gene:
        print(f"Found {target_gene} at index {i}")
        break  # Stop searching!
```

**Without break:** Loop checks all items even after finding target  
**With break:** Loop stops immediately when target is found

**Flow:**
1. Check BRCA1 → Not target, continue
2. Check TP53 → **Found!** Print message, **break** (exit loop)
3. PTEN and EGFR are never checked

---

### **while True with break Pattern**

A common pattern for continuous loops:

```python
while True:  # Infinite loop!
    action = input("Continue? (y/n): ")
    if action == "n":
        break  # Exit the loop
    print("Continuing...")
```

**Use case:** Menus, games, ATM simulations - anything that runs until user decides to quit.

---

## 4. Loop Control: continue

`continue` **skips the rest** of the current iteration and goes to the next one.

### **Example: Processing Data, Skipping Invalid**
```python
status = ["Healthy", "Cancer", "Invalid", "Cancer"]
count = 0

for patient_status in status:
    if patient_status == "Invalid":
        print("Skipping Invalid entry")
        continue  # Skip to next iteration
    
    if patient_status == "Healthy":
        print("Skipping Healthy entry")
        continue
    
    # Only "Cancer" reaches here
    print(f"Processing {patient_status}")
    count += 1

print(f"Processed {count} cancer cases")
```

**Output:**
```
Skipping Healthy entry
Processing Cancer
Skipping Invalid entry
Processing Cancer
Processed 2 cancer cases
```

**Flow:**
- "Healthy" → Hit continue → Skip to next
- "Cancer" → No continue → Process and count
- "Invalid" → Hit continue → Skip to next
- "Cancer" → No continue → Process and count

---

## 5. Practical Applications

### **Application 1: Input Validation**

Keep asking until valid input is received:

```python
valid_number = None
while valid_number is None:
    user_input = input("Enter a number between 1 and 100: ")
    try:
        num = int(user_input)
        if 0 < num <= 100:
            valid_number = num
            print("Thank you!")
        else:
            print("Number out of range. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"Processing with {valid_number}")
```

**Key features:**
- Loop continues until valid input
- Handles non-numeric input (try/except)
- Validates range
- Only exits when valid

---

### **Application 2: ATM Simulation**

```python
balance = 500

while True:
    print(f"Current balance: ${balance}")
    action = input("(d)eposit, (w)ithdraw, (q)uit: ").lower()
    
    if action == "q":
        print("Thank you!")
        break
    
    elif action == "w":
        try:
            amount = float(input("Amount to withdraw: $"))
            if amount <= balance:
                balance -= amount
                print(f"New balance: ${balance}")
            else:
                print("Insufficient funds")
        except ValueError:
            print("Invalid amount")
    
    elif action == "d":
        try:
            amount = float(input("Amount to deposit: $"))
            balance += amount
            print(f"New balance: ${balance}")
        except ValueError:
            print("Invalid amount")
    
    else:
        print("Invalid option")

print("ATM session ended.")
```

**Features:**
- Infinite loop with `while True`
- `break` to exit
- Input validation with try/except
- Balance tracking
- Multiple operations

---

### **Application 3: Gene List Search**

```python
gene_list = ["BRCA1", "TP53", "PTEN", "EGFR", "KRAS"]
target_gene = "PTEN"

found = False
for i in range(len(gene_list)):
    current = gene_list[i]
    if current == target_gene:
        print(f"Found {target_gene} at index {i}")
        found = True
        break

if not found:
    print(f"{target_gene} not found in list")
```

**Real-world use:**
- Searching genomic databases
- Finding specific genes in sequences
- Bioinformatics data processing

---

## 6. Loop Patterns Comparison

### **while vs for**

| Aspect | while Loop | for Loop |
|--------|-----------|----------|
| **Use when** | Don't know how many times | Know sequence/count |
| **Syntax** | `while condition:` | `for item in sequence:` |
| **Example** | Input validation | Processing a list |
| **Termination** | When condition is False | When sequence ends |

**while loop example:**
```python
# Don't know when user will enter valid input
while valid_number is None:
    # Keep asking...
```

**for loop example:**
```python
# Know exactly what to process
for gene in gene_list:
    # Process each gene
```

---

## 7. Common Loop Patterns

### **Pattern 1: Counting**
```python
count = 0
for item in list:
    if condition:
        count += 1
print(f"Found {count} items")
```

### **Pattern 2: Accumulating**
```python
total = 0
for number in numbers:
    total += number
average = total / len(numbers)
```

### **Pattern 3: Searching**
```python
found = False
for item in list:
    if item == target:
        found = True
        break
```

### **Pattern 4: Filtering**
```python
valid_items = []
for item in items:
    if is_valid(item):
        valid_items.append(item)
```

### **Pattern 5: Menu Loop**
```python
while True:
    choice = input("Menu: ")
    if choice == "quit":
        break
    # Process choice
```

---

## 8. try/except for Error Handling

`try/except` handles errors gracefully:

```python
try:
    # Code that might cause an error
    num = int(user_input)
except ValueError:
    # Code to run if ValueError occurs
    print("Invalid number!")
```

**Without try/except:**
```python
num = int("hello")  # Program CRASHES!
```

**With try/except:**
```python
try:
    num = int("hello")
except ValueError:
    print("Invalid input")  # Program continues
```

**Common errors:**
- `ValueError` - Invalid conversion (e.g., int("hello"))
- `ZeroDivisionError` - Division by zero
- `TypeError` - Wrong type operation

---

## 9. Increment and Decrement Operators

### **Increment (Add to variable):**
```python
count = 0
count += 1  # Same as: count = count + 1
count += 5  # Same as: count = count + 5
```

### **Decrement (Subtract from variable):**
```python
countdown = 10
countdown -= 1  # Same as: countdown = countdown - 1
countdown -= 3  # Same as: countdown = countdown - 3
```

### **Other Operations:**
```python
x *= 2   # x = x * 2
x /= 2   # x = x / 2
x %= 3   # x = x % 3
```

---

## 10. Common Mistakes

### **Mistake 1: Infinite Loop**
```python
# WRONG - Never ends
count = 0
while count < 10:
    print(count)
    # Forgot to increment!

# CORRECT
count = 0
while count < 10:
    print(count)
    count += 1
```

---

### **Mistake 2: Off-by-One Errors**
```python
# Want 1 to 10
for i in range(10):  # WRONG - gives 0 to 9
    print(i)

for i in range(1, 11):  # CORRECT - gives 1 to 10
    print(i)
```

---

### **Mistake 3: Modifying List While Iterating**
```python
# WRONG - Don't modify list while iterating
for item in my_list:
    my_list.remove(item)  # Causes problems!

# CORRECT - Use a copy or different approach
for item in my_list[:]:  # [:] creates a copy
    my_list.remove(item)
```

---

### **Mistake 4: break/continue Outside Loop**
```python
# WRONG
if condition:
    break  # SyntaxError! Not in a loop

# CORRECT
while True:
    if condition:
        break  # OK - inside loop
```

---

## 💡 Key Takeaways

1. **while loops** repeat while condition is True
2. **for loops** iterate over sequences
3. **break** exits the loop immediately
4. **continue** skips to next iteration
5. **range()** creates number sequences
6. **try/except** handles errors gracefully
7. **+=** and **-=** are shorthand operators
8. Loops must eventually end (avoid infinite loops!)
9. `while True` with `break` creates controlled infinite loops
10. Use `for` when you know the sequence, `while` when you don't

---

## 🎯 Loop Control Flow

```
while condition:
    code
    if break_condition:
        break     → Exits loop entirely
    if skip_condition:
        continue  → Skips to next iteration
    more code
```

---

## 📚 Further Reading

- [Python while Loops](https://docs.python.org/3/reference/compound_stmts.html#while)
- [Python for Loops](https://docs.python.org/3/reference/compound_stmts.html#for)
- [break and continue](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements)
- [range() Function](https://docs.python.org/3/library/stdtypes.html#range)
- [Error Handling (try/except)](https://docs.python.org/3/tutorial/errors.html)

---

*Loops are the engines of automation. With loops, you can process thousands of items with just a few lines of code!*
