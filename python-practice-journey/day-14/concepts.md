# Day 14: Week 3 Revision - Concepts Summary

## 📌 Week 3 Overview

Week 3 focused on **Data Structures & Comprehensions** - the foundation of data organization and manipulation in Python. This revision consolidates all concepts from Days 9-13.

---

## 🗂️ The Four Core Data Structures

### **1. Lists (Day 9) - Mutable Sequences**

**Characteristics:**
- Ordered, mutable, allow duplicates
- Syntax: `[]`
- Indexed by position (0-based)

**Key Operations:**
```python
# Creation
my_list = [1, 2, 3, 4, 5]

# Access
first = my_list[0]
last = my_list[-1]
middle = my_list[1:4]

# Modification
my_list[0] = 10  # Change element
my_list.append(6)  # Add to end
my_list.insert(0, 0)  # Insert at position
my_list.remove(3)  # Remove by value
my_list.pop(2)  # Remove by index
```

**When to Use:**
- Ordered collections that need to change
- Sequential data processing
- When order and duplicates matter

---

### **2. Dictionaries (Day 10) - Key-Value Mapping**

**Characteristics:**
- Ordered (Python 3.7+), mutable
- Syntax: `{key: value}`
- Fast O(1) lookups by key

**Key Operations:**
```python
# Creation
my_dict = {"name": "John", "age": 30}

# Access
value = my_dict["name"]  # Direct (raises KeyError if missing)
value = my_dict.get("name", "default")  # Safe with default

# Modification
my_dict["age"] = 31  # Update
my_dict["city"] = "NYC"  # Add new
del my_dict["age"]  # Delete
removed = my_dict.pop("city")  # Remove and return

# Iteration
for key in my_dict:  # Keys
for value in my_dict.values():  # Values
for key, value in my_dict.items():  # Both (most common)
```

**When to Use:**
- Key-value relationships
- Fast lookups by identifier
- Structured data (JSON-like)
- Configurations, metadata

---

### **3. Tuples (Day 11) - Immutable Sequences**

**Characteristics:**
- Ordered, immutable, allow duplicates
- Syntax: `()`
- Faster than lists, less memory

**Key Operations:**
```python
# Creation
my_tuple = (1, 2, 3)
single = (1,)  # Trailing comma required!
packed = 1, 2, 3  # Parentheses optional

# Access (same as lists)
first = my_tuple[0]
subset = my_tuple[1:3]

# Unpacking
x, y, z = my_tuple

# Methods (only 2!)
count = my_tuple.count(2)
index = my_tuple.index(3)
```

**When to Use:**
- Data that shouldn't change
- Dictionary keys (must be immutable)
- Function return values (multiple)
- Coordinates, configurations

---

### **4. Sets (Day 12) - Unique Elements**

**Characteristics:**
- Unordered, mutable, NO duplicates
- Syntax: `{}`
- Fast O(1) membership testing

**Key Operations:**
```python
# Creation
my_set = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3])  # Removes duplicates
empty = set()  # NOT {}, which is dict!

# Modification
my_set.add(6)
my_set.update([7, 8, 9])
my_set.remove(1)  # Raises KeyError if not found
my_set.discard(10)  # No error if not found

# Set Operations
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

union = setA | setB  # {1, 2, 3, 4, 5, 6}
intersection = setA & setB  # {3, 4}
difference = setA - setB  # {1, 2}
symmetric_diff = setA ^ setB  # {1, 2, 5, 6}
```

**When to Use:**
- Remove duplicates
- Fast membership testing
- Mathematical set operations
- Finding common/unique elements

---

## 📝 List Comprehensions (Day 13) - Elegant List Creation

**Purpose:** Create lists in a single, readable line instead of loops.

### **Basic Syntax:**
```python
[expression for item in iterable]
```

### **Common Patterns:**

**1. Simple Transformation:**
```python
# Traditional
squares = []
for x in range(10):
    squares.append(x**2)

# Comprehension
squares = [x**2 for x in range(10)]
```

**2. Filtering:**
```python
# Traditional
evens = []
for x in range(20):
    if x % 2 == 0:
        evens.append(x)

# Comprehension
evens = [x for x in range(20) if x % 2 == 0]
```

**3. Conditional Expression (if/else):**
```python
# Traditional
labels = []
for x in range(10):
    if x % 2 == 0:
        labels.append("Even")
    else:
        labels.append("Odd")

# Comprehension
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
```

**4. Transform + Filter:**
```python
# Squares of even numbers only
squares_evens = [x**2 for x in range(20) if x % 2 == 0]
```

**5. Nested Comprehensions:**
```python
# Traditional
coords = []
for i in range(10):
    for j in range(5):
        coords.append((i, j))

# Comprehension
coords = [(i, j) for i in range(10) for j in range(5)]
```

**6. Flattening:**
```python
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in list_of_lists for num in sublist]
# Result: [1, 2, 3, 4, 5, 6]
```

### **Dictionary Comprehensions:**
```python
{key_expr: value_expr for item in iterable}

# Example
genes = ["GeneA", "GeneB", "GeneC"]
counts = [150, 80, 220]
gene_dict = {gene: count for gene, count in zip(genes, counts)}
```

### **Set Comprehensions:**
```python
{expression for item in iterable}

# Example
unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 4]}
# Result: {1, 4, 9, 16}
```

---

## 🔄 Comparison Table

| Feature | List | Dict | Tuple | Set |
|---------|------|------|-------|-----|
| **Ordered** | ✓ | ✓ (3.7+) | ✓ | ✗ |
| **Mutable** | ✓ | ✓ | ✗ | ✓ |
| **Duplicates** | ✓ | Values: ✓ | ✓ | ✗ |
| **Indexing** | By position | By key | By position | None |
| **Syntax** | `[]` | `{k:v}` | `()` | `{}` |
| **Speed** | O(n) lookup | O(1) lookup | O(n) lookup | O(1) lookup |
| **Use Case** | Sequences | Mapping | Fixed data | Unique items |

---

## 🧬 Bioinformatics Applications

### **Lists:**
```python
expression_values = [120.5, 88.3, 210.1, 55.7, 15.9]
gene_names = ["TP53", "BRCA1", "MYC", "KRAS"]
```

### **Dictionaries:**
```python
patient_info = {
    "patient_id": "PAT001",
    "age": 45,
    "diagnosis": "breast_cancer",
    "is_treated": True
}

gene_expression = {
    "TP53": 150.5,
    "BRCA1": 85.2,
    "MYC": 220.1
}
```

### **Tuples:**
```python
genomic_coordinate = ("chr17", 76735400, 76760000)
chromosome, start, end = genomic_coordinate

# List of tuples
regions = [
    ("chr1", 100, 200),
    ("chr2", 300, 400),
    ("chr3", 500, 600)
]
```

### **Sets:**
```python
genes_pathway1 = {"TP53", "MYC", "KRAS", "PTEN"}
genes_pathway2 = {"MYC", "EGFR", "BRAF", "PTEN"}

# Common genes
common = genes_pathway1 & genes_pathway2

# Unique to pathway1
unique = genes_pathway1 - genes_pathway2
```

### **List Comprehensions:**
```python
# Filter high expression
high_expr = [val for val in expression_values if val > 100]

# Categorize levels
categories = ["High" if val > 100 else "Low" for val in expression_values]

# Process gene names
uppercase_genes = [gene.upper() for gene in gene_names]
processed = [gene + "_processed" for gene in gene_names]
```

---

## 💡 Key Decision Guide

**When choosing a data structure, ask:**

1. **Do I need order?**
   - Yes → List or Tuple
   - No → Set or Dict

2. **Will it change?**
   - Yes → List, Dict, or Set
   - No → Tuple

3. **Do I need fast lookups?**
   - By key → Dict
   - By value → Set
   - By position → List or Tuple

4. **Do I need unique values only?**
   - Yes → Set
   - No → List, Tuple, or Dict (values)

5. **Do I need key-value pairs?**
   - Yes → Dict
   - No → List, Tuple, or Set

---

## 🎯 Best Practices

**Lists:**
- Use for ordered collections that change
- Prefer list comprehensions over loops
- Use methods like `.append()`, `.extend()`, `.pop()`

**Dictionaries:**
- Use `.get()` for safe access
- Use `.items()` for iteration
- Use for fast O(1) lookups

**Tuples:**
- Use for data that shouldn't change
- Use for multiple return values
- Use as dict keys when needed

**Sets:**
- Use to remove duplicates: `unique = list(set(my_list))`
- Use for membership testing: `if item in my_set:`
- Use for set operations: union, intersection, difference

**List Comprehensions:**
- Keep them simple and readable
- Use for transformation and filtering
- Avoid overly complex nested comprehensions

---

## 📚 Quick Reference

### **Creation:**
```python
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2}
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
```

### **Access:**
```python
my_list[0]  # By index
my_dict["a"]  # By key
my_tuple[0]  # By index
# Sets: no indexing (unordered)
```

### **Modification:**
```python
my_list[0] = 10  # Change
my_dict["a"] = 10  # Change
# my_tuple[0] = 10  # Error! Immutable
my_set.add(4)  # Add
```

### **Comprehensions:**
```python
[x*2 for x in range(10)]  # List
{x*2 for x in range(10)}  # Set
{x: x*2 for x in range(10)}  # Dict
```

---

*Week 3 complete! You now have mastery over Python's core data structures and elegant ways to work with them!*
