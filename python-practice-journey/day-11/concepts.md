# Day 11: Tuples - Concepts

## 📌 Core Concepts Covered

Tuples are Python's **immutable** sequence type. Like lists, they store multiple items in order, but unlike lists, they **cannot be changed** after creation. This immutability makes them perfect for data that shouldn't be modified and enables them to be used as dictionary keys.

---

## 1. What is a Tuple?

A **tuple** is an ordered, immutable collection of items.

### **Characteristics:**
- **Ordered**: Items maintain their position
- **Immutable**: Cannot be changed after creation
- **Allow duplicates**: Same value can appear multiple times
- **Mixed types**: Can contain different data types
- **Indexed**: Access items by position (starting at 0)
- **Hashable**: Can be used as dictionary keys (if all elements are hashable)

### **Creating Tuples:**

**With parentheses:**
```python
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))  # <class 'tuple'>
```

**Tuple packing (without parentheses):**
```python
my_tuple = 1, 2, 3, 4, 5  # Parentheses optional!
print(type(my_tuple))  # <class 'tuple'>
```

**Single element tuple (trailing comma required!):**
```python
# WRONG - This is an int, not a tuple!
not_a_tuple = (1)
print(type(not_a_tuple))  # <class 'int'>

# CORRECT - Trailing comma makes it a tuple
my_tuple = (1,)
print(type(my_tuple))  # <class 'tuple'>
```

**Empty tuple:**
```python
empty_tuple = ()
print(type(empty_tuple))  # <class 'tuple'>
```

**Mixed types:**
```python
data_tuple = ("Chromosome1", 150000, 150500, True)
```

---

## 2. Accessing Tuple Elements

Tuples use the same indexing and slicing as lists and strings!

### **Positive Indexing:**
```python
my_tuple = ("A", "B", "C", "D", "E")

first = my_tuple[0]    # "A"
second = my_tuple[1]   # "B"
last = my_tuple[4]     # "E"
```

### **Negative Indexing:**
```python
last = my_tuple[-1]        # "E"
second_last = my_tuple[-2] # "D"
```

### **Slicing:**
```python
my_tuple = ("Chromosome1", 150000, 150500, "Gene1", "Gene2")

# Get elements from index 1 to 3 (exclusive)
subset = my_tuple[1:3]  # (150000, 150500)

# Get first 3 elements
first_three = my_tuple[:3]

# Get last 2 elements
last_two = my_tuple[-2:]

# Reverse the tuple
reversed_tuple = my_tuple[::-1]

# Copy the entire tuple
copy = my_tuple[:]
```

---

## 3. Tuple Immutability

**Tuples CANNOT be changed** after creation - this is their defining feature!

### **What You CANNOT Do:**

```python
my_tuple = (1, 2, 3, 4, 5)

# These all raise AttributeError or TypeError:
# my_tuple[0] = 10           # TypeError!
# my_tuple.append(6)         # AttributeError!
# my_tuple.insert(2, 10)     # AttributeError!
# my_tuple.remove(3)         # AttributeError!
# my_tuple.pop()             # AttributeError!
# del my_tuple[0]            # TypeError!
```

### **What You CAN Do:**

**Create new tuples from existing ones:**
```python
tuple1 = (1, 2)
tuple2 = (3, 4)

# Concatenation creates a NEW tuple
combined = tuple1 + tuple2  # (1, 2, 3, 4)

# Original tuples unchanged
print(tuple1)  # (1, 2)
print(tuple2)  # (3, 4)
```

**Repetition:**
```python
my_tuple = (1, 2)
repeated = my_tuple * 3  # (1, 2, 1, 2, 1, 2)
```

**Delete the entire tuple:**
```python
my_tuple = (1, 2, 3)
del my_tuple  # my_tuple no longer exists
```

---

## 4. Tuple Unpacking

Extract tuple elements into separate variables!

### **Basic Unpacking:**
```python
coordinates = (10, 20)
x, y = coordinates

print(x)  # 10
print(y)  # 20
```

### **With Different Types:**
```python
data = (10, 'Patient1', 2.5, True)
id_num, name, score, active = data

print(id_num)  # 10
print(name)    # 'Patient1'
print(score)   # 2.5
print(active)  # True
```

### **Unpacking Errors:**
```python
data = (1, 2, 3, 4)

# Too few variables
# x, y = data  # ValueError: too many values to unpack (expected 2)

# Too many variables
# a, b, c, d, e = data  # ValueError: not enough values to unpack (expected 5, got 4)
```

### **Extended Unpacking (Python 3+):**
```python
numbers = (1, 2, 3, 4, 5)

# Capture remaining elements
first, *rest = numbers
# first = 1
# rest = [2, 3, 4, 5]  # Note: rest is a LIST!

*beginning, last = numbers
# beginning = [1, 2, 3, 4]
# last = 5

first, *middle, last = numbers
# first = 1
# middle = [2, 3, 4]
# last = 5
```

---

## 5. Tuple Methods

Tuples have only **2 methods** (because they're immutable):

### **count() - Count Occurrences:**
```python
sample_ids = ("Patient1", "Patient2", "Patient3", "Patient1", "Patient4")

count = sample_ids.count("Patient1")  # 2
count_missing = sample_ids.count("Patient5")  # 0
```

### **index() - Find Position:**
```python
sample_ids = ("Patient1", "Patient2", "Patient3")

# Find first occurrence
index = sample_ids.index("Patient2")  # 1

# Raises ValueError if not found
# index = sample_ids.index("Patient5")  # ValueError!
```

**Safe pattern with try/except:**
```python
try:
    index = sample_ids.index("Patient5")
    print(f"Found at index: {index}")
except ValueError:
    print("Item not found")
```

---

## 6. Tuple vs List vs Dictionary

| Feature | Tuple | List | Dictionary |
|---------|-------|------|------------|
| Mutability | Immutable | Mutable | Mutable |
| Syntax | `()` | `[]` | `{}` |
| Ordered | Yes | Yes | Yes (3.7+) |
| Duplicates | Allowed | Allowed | Keys: No, Values: Yes |
| Indexing | By position | By position | By key |
| Use case | Fixed data | Changeable sequences | Key-value mapping |
| Speed | Faster | Slower | Fast lookups |
| Memory | Less | More | More |

---

## 7. When to Use Tuples

### **Use Tuples When:**

1. **Data shouldn't change:**
```python
coordinates = (40.7128, -74.0060)  # NYC latitude, longitude
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
```

2. **Returning multiple values from functions:**
```python
def get_stats(data):
    return (min(data), max(data), sum(data)/len(data))

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])
```

3. **As dictionary keys:**
```python
# Tuples can be dict keys (lists cannot!)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}
```

4. **Ensuring data integrity:**
```python
# Patient ID shouldn't change
patient_record = ("PAT001", "John Doe", 45)
```

5. **Slight performance benefit:**
Tuples are faster than lists for iteration and creation.

---

## 8. Common Operations

### **Membership Testing:**
```python
my_tuple = (1, 2, 3, 4, 5)

if 3 in my_tuple:
    print("Found!")  # Prints

if 10 not in my_tuple:
    print("Not found!")  # Prints
```

### **Length:**
```python
my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)  # 5
```

### **Iteration:**
```python
sample_ids = ("Patient1", "Patient2", "Patient3")

for patient_id in sample_ids:
    print(f"Processing {patient_id}")
```

### **Min/Max/Sum:**
```python
numbers = (5, 2, 8, 1, 9)

minimum = min(numbers)  # 1
maximum = max(numbers)  # 9
total = sum(numbers)    # 25
```

### **Sorting (creates a list!):**
```python
my_tuple = (5, 2, 8, 1, 9)
sorted_list = sorted(my_tuple)  # Returns a LIST: [1, 2, 5, 8, 9]

# To get a sorted tuple:
sorted_tuple = tuple(sorted(my_tuple))  # (1, 2, 5, 8, 9)
```

---

## 9. Converting Between Types

### **List to Tuple:**
```python
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3, 4, 5)
```

### **Tuple to List:**
```python
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)  # [1, 2, 3, 4, 5]
```

### **String to Tuple:**
```python
text = "hello"
char_tuple = tuple(text)
print(char_tuple)  # ('h', 'e', 'l', 'l', 'o')
```

---

## 10. Common Patterns

### **Pattern 1: Returning Multiple Values**
```python
def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

# Unpacking
min_val, max_val, avg = calculate_stats([1, 2, 3, 4, 5])
```

### **Pattern 2: Swapping Variables**
```python
# Without tuple:
temp = a
a = b
b = temp

# With tuple (elegant!):
a, b = b, a
```

### **Pattern 3: Coordinate Pairs**
```python
coordinates = [
    (0, 0),
    (1, 2),
    (3, 4)
]

for x, y in coordinates:
    print(f"Point: ({x}, {y})")
```

### **Pattern 4: Named Tuples (Advanced)**
```python
from collections import namedtuple

Patient = namedtuple('Patient', ['id', 'name', 'age'])
patient = Patient('P001', 'John', 45)

print(patient.name)  # Access by name!
print(patient[1])    # Also by index
```

---

## 11. Bioinformatics Applications

### **Genomic Coordinates:**
```python
# (chromosome, start, end)
gene_location = ("chr1", 150000, 150500)
chromosome, start, end = gene_location
```

### **Read-only Configuration:**
```python
# DNA bases that shouldn't change
DNA_BASES = ('A', 'T', 'G', 'C')

for base in DNA_BASES:
    count = sequence.count(base)
```

### **Patient Sample Records:**
```python
sample_ids = ("Patient1", "Patient2", "Patient3", "Patient1")

# Count how many times each patient appears
for patient in set(sample_ids):
    count = sample_ids.count(patient)
    print(f"{patient}: {count} samples")
```

### **Coordinate Systems:**
```python
# Store coordinates that shouldn't be modified
positions = [
    (1, 100, 200),  # chr1, start, end
    (2, 300, 400),
    (3, 500, 600)
]

for chr_num, start, end in positions:
    print(f"Chr{chr_num}: {start}-{end}")
```

---

## 💡 Key Takeaways

1. **Tuples are immutable** - cannot be changed after creation
2. **Use () to create**, but parentheses are optional for packing
3. **Single element tuple** requires trailing comma: `(1,)`
4. **Same indexing and slicing** as lists and strings
5. **Only 2 methods:** `count()` and `index()`
6. **Unpacking** extracts elements into variables
7. **Faster and use less memory** than lists
8. **Can be dictionary keys** (lists cannot!)
9. **Perfect for data that shouldn't change**
10. **Common for returning multiple values** from functions

---

## 📚 Quick Reference

| Operation | Syntax | Result |
|-----------|--------|--------|
| Create | `(1, 2, 3)` | Tuple |
| Single element | `(1,)` | Tuple (comma required!) |
| Packing | `1, 2, 3` | Tuple |
| Access | `my_tuple[0]` | First element |
| Slice | `my_tuple[1:3]` | Subset |
| Unpack | `x, y = (1, 2)` | x=1, y=2 |
| Concatenate | `t1 + t2` | New tuple |
| Repeat | `t * 3` | New tuple |
| Length | `len(my_tuple)` | Integer |
| Count | `my_tuple.count(x)` | Integer |
| Index | `my_tuple.index(x)` | Integer |

---

*Tuples provide data integrity through immutability. Use them when your data should stay constant!*
