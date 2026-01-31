# Day 9: Lists - Concepts

## 📌 Core Concepts Covered

Lists are one of Python's most fundamental and powerful data structures. They allow you to store multiple items in a single variable, making data organization and manipulation incredibly efficient. Today marks the beginning of working with **collections** - a major step in programming capability!

---

## 1. What is a List?

A **list** is an ordered collection of items that can be of any type.

### **Characteristics:**
- **Ordered**: Items maintain their position
- **Mutable**: Can be changed after creation
- **Allow duplicates**: Same value can appear multiple times
- **Mixed types**: Can contain different data types
- **Indexed**: Access items by position (starting at 0)

### **Creating Lists:**

```python
# List of integers
my_numbers = [10, 20, 30, 40, 50]

# List of strings
my_strings = ["apple", "banana", "cherry"]

# Mixed types
my_mixed = [10, "apple", 20.5, True]

# Empty list
my_empty = []
```

### **List Type:**
```python
print(type(my_numbers))  # <class 'list'>
```

---

## 2. List Indexing

Access individual elements using their position (index).

### **Positive Indexing (from start):**
```python
my_strings = ["apple", "banana", "cherry"]

first = my_strings[0]      # "apple"
second = my_strings[1]     # "banana"
third = my_strings[2]      # "cherry"
```

**Index positions:**
```
["apple", "banana", "cherry"]
   0        1         2
```

### **Negative Indexing (from end):**
```python
last = my_strings[-1]           # "cherry"
second_last = my_strings[-2]    # "banana"
first = my_strings[-3]          # "apple"
```

**Negative index positions:**
```
["apple", "banana", "cherry"]
  -3       -2        -1
```

### **Index Errors:**
```python
# IndexError: list index out of range
item = my_strings[3]   # Only 3 items (0, 1, 2)
item = my_strings[-5]  # Only goes to -3
```

**Key Rule:** Valid indices are from `0` to `len(list)-1` or `-len(list)` to `-1`.

---

## 3. List Slicing

Extract portions of a list using slice notation: `[start:stop:step]`

### **Basic Slicing:**
```python
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# [start:stop] - items from start up to (but not including) stop
subset = my_list[1:4]  # ["banana", "cherry", "date"]
```

### **Omitting Start or Stop:**
```python
# [:stop] - from beginning to stop
first_three = my_list[:3]  # ["apple", "banana", "cherry"]

# [start:] - from start to end
last_three = my_list[2:]   # ["cherry", "date", "elderberry"]

# [:] - entire list (creates a copy!)
copy = my_list[:]
```

### **Using Step:**
```python
# [::step] - every nth item
every_second = my_list[::2]  # ["apple", "cherry", "elderberry"]

# [start:stop:step]
subset = my_list[1:4:2]  # ["banana", "date"]
```

### **Negative Step (Reverse):**
```python
# Reverse the list
reversed_list = my_list[::-1]
# ["elderberry", "date", "cherry", "banana", "apple"]
```

### **Slicing Summary:**

| Slice | Meaning |
|-------|---------|
| `[1:4]` | Items at indices 1, 2, 3 |
| `[:3]` | First 3 items (indices 0, 1, 2) |
| `[2:]` | From index 2 to end |
| `[:]` | All items (copy) |
| `[::2]` | Every 2nd item |
| `[::-1]` | Reverse order |

---

## 4. List Mutability

Unlike strings, **lists can be modified** after creation.

### **Modifying Single Elements:**
```python
gene_list = ["TP53", "BRCA1", "PTEN", "KRAS"]
gene_list[1] = "MYC"  # Change second element
# Result: ["TP53", "MYC", "PTEN", "KRAS"]
```

### **Modifying Slices:**
```python
gene_list[1:3] = ["ABC", "DEF", "GHI"]
# Replaces indices 1 and 2 with 3 new elements
# Result: ["TP53", "ABC", "DEF", "GHI", "KRAS"]
```

**Important:** Number of replacement items doesn't need to match slice size!

### **Strings vs Lists:**
```python
# Strings are IMMUTABLE
text = "hello"
# text[0] = "H"  # TypeError!

# Lists are MUTABLE
my_list = ["h", "e", "l", "l", "o"]
my_list[0] = "H"  # Works! ["H", "e", "l", "l", "o"]
```

---

## 5. Adding Elements to Lists

### **append() - Add to End:**
```python
numbers = [1, 2, 3]
numbers.append(4)
# Result: [1, 2, 3, 4]
```

**Key points:**
- Adds ONE item
- Always adds at the end
- Modifies original list (no return value)

### **insert() - Add at Specific Position:**
```python
numbers = [1, 2, 4, 5]
numbers.insert(2, 3)  # Insert 3 at index 2
# Result: [1, 2, 3, 4, 5]
```

**Syntax:** `list.insert(index, item)`

**Special case:**
```python
numbers.insert(len(numbers), 6)  # Same as append(6)
```

### **extend() - Add Multiple Items:**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
# Result: [1, 2, 3, 4, 5, 6]
```

**append() vs extend():**
```python
# append adds the list as a single element
list1 = [1, 2, 3]
list1.append([4, 5])
# Result: [1, 2, 3, [4, 5]]

# extend adds each element
list1 = [1, 2, 3]
list1.extend([4, 5])
# Result: [1, 2, 3, 4, 5]
```

---

## 6. Removing Elements from Lists

### **pop() - Remove by Index (returns removed item):**
```python
steps = ["Start", "Process", "Analyze", "Finish"]

# Remove at specific index
removed = steps.pop(2)  # "Analyze"
# steps is now: ["Start", "Process", "Finish"]

# Remove last item (no index)
removed = steps.pop()  # "Finish"
# steps is now: ["Start", "Process"]
```

### **remove() - Remove by Value:**
```python
steps = ["Start", "Process", "Analyze"]
steps.remove("Start")
# Result: ["Process", "Analyze"]
```

**Important:**
- Removes only the **first** occurrence
- Raises `ValueError` if item not found

```python
# ValueError: list.remove(x): x not in list
steps.remove("Missing")  # Error!
```

### **del - Delete by Index or Slice:**
```python
my_list = [1, 2, 3, 4, 5]

# Delete single item
del my_list[2]  # [1, 2, 4, 5]

# Delete slice
del my_list[1:3]  # [1, 5]

# Delete entire list
del my_list  # my_list no longer exists
```

### **clear() - Remove All Items:**
```python
my_list = [1, 2, 3, 4, 5]
my_list.clear()
# Result: []
```

---

## 7. List Methods and Functions

### **len() - Get List Length:**
```python
data = [5, 2, 8, 1, 9]
print(len(data))  # 5
```

### **sort() - Sort in Place:**
```python
data = [5, 2, 8, 1, 9]
data.sort()
# data is now: [1, 2, 5, 8, 9]

# Reverse order
data.sort(reverse=True)
# data is now: [9, 8, 5, 2, 1]
```

**Important:** `sort()` modifies the original list!

### **sorted() - Return Sorted Copy:**
```python
data = [5, 2, 8, 1, 9]
sorted_data = sorted(data)
# data is still: [5, 2, 8, 1, 9]
# sorted_data is: [1, 2, 5, 8, 9]
```

### **reverse() - Reverse in Place:**
```python
data = [1, 2, 3, 4, 5]
data.reverse()
# Result: [5, 4, 3, 2, 1]
```

### **count() - Count Occurrences:**
```python
data = [1, 2, 3, 2, 4, 2, 5]
print(data.count(2))  # 3
```

### **index() - Find First Position:**
```python
data = [10, 20, 30, 40]
print(data.index(30))  # 2
# Raises ValueError if not found
```

---

## 8. Membership Testing

Check if an item exists in a list using `in`:

```python
gene_status = ["Mutated", "Normal", "Amplified"]

if "Mutated" in gene_status:
    print("Found!")  # Prints

if "Deleted" in gene_status:
    print("Found!")  # Doesn't print

# Also works with not in
if "Deleted" not in gene_status:
    print("Not found!")  # Prints
```

---

## 9. Iterating Through Lists

### **Basic Iteration:**
```python
values = [0.5, 1.0, 0.22, 0.58]

for value in values:
    print(f"Value: {value}")
```

### **With Index (enumerate):**
```python
for index, value in enumerate(values):
    print(f"Index {index}: {value}")
```

### **With Conditions:**
```python
threshold = 0.6

for value in values:
    if value > threshold:
        print(f"{value} is above threshold")
```

---

## 10. List Operations

### **Concatenation (+):**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
# Result: [1, 2, 3, 4, 5, 6]
```

### **Repetition (*):**
```python
zeros = [0] * 5
# Result: [0, 0, 0, 0, 0]
```

### **Comparison:**
```python
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] == [1, 3, 2])  # False (order matters)
```

---

## 11. Common Patterns

### **Pattern 1: Build a List in a Loop:**
```python
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
# Result: [1, 4, 9, 16, 25]
```

### **Pattern 2: Filter a List:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
# Result: [2, 4, 6, 8, 10]
```

### **Pattern 3: Find Maximum/Minimum:**
```python
values = [5, 2, 9, 1, 7]
max_value = max(values)  # 9
min_value = min(values)  # 1
```

### **Pattern 4: Sum All Values:**
```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # 15
```

---

## 12. Lists vs Strings

### **Similarities:**
- Both are **sequences**
- Both support **indexing** and **slicing**
- Both can be **iterated** in loops
- Both have **len()** function

### **Differences:**

| Feature | Strings | Lists |
|---------|---------|-------|
| Mutability | Immutable | Mutable |
| Type | All characters | Any types |
| Creation | `""` or `''` | `[]` |
| Methods | `.upper()`, `.split()` | `.append()`, `.sort()` |

---

## 13. Bioinformatics Applications

### **Gene Lists:**
```python
genes = ["TP53", "BRCA1", "PTEN", "KRAS"]

# Add new gene
genes.append("MYC")

# Check if gene present
if "TP53" in genes:
    print("TP53 found!")

# Process each gene
for gene in genes:
    print(f"Analyzing {gene}...")
```

### **Methylation Data:**
```python
methylation = [0.5, 1.0, 0.22, 0.58, 0.45, 0.78]

threshold = 0.6
high_methylation = []

for value in methylation:
    if value > threshold:
        high_methylation.append(value)

print(f"High methylation: {high_methylation}")
```

### **Experiment Steps:**
```python
steps = ["Prepare", "Incubate", "Wash", "Analyze"]

# Add step
steps.insert(1, "Mix")

# Remove step
steps.remove("Wash")

# Process in order
for i, step in enumerate(steps, 1):
    print(f"Step {i}: {step}")
```

---

## 💡 Key Takeaways

1. **Lists store multiple items** in order
2. **Mutable** - can be changed after creation
3. **Indexing** starts at 0 (or -1 from end)
4. **Slicing** extracts portions: `[start:stop:step]`
5. **append()** adds to end, **insert()** adds at position
6. **pop()** removes and returns, **remove()** removes by value
7. **sort()** modifies list, **sorted()** returns sorted copy
8. **in** checks membership
9. **for loop** iterates through items
10. Lists are **fundamental** to data processing!

---

## 📚 Method Quick Reference

| Method | Purpose | Returns |
|--------|---------|---------|
| `append(x)` | Add x to end | None |
| `insert(i, x)` | Insert x at index i | None |
| `extend(list)` | Add all items from list | None |
| `pop(i)` | Remove & return item at i | Item |
| `remove(x)` | Remove first x | None |
| `clear()` | Remove all items | None |
| `sort()` | Sort in place | None |
| `reverse()` | Reverse in place | None |
| `count(x)` | Count occurrences of x | Integer |
| `index(x)` | Find position of x | Integer |

---

*Lists are the foundation of data processing in Python. Mastering lists opens the door to working with real datasets!*
