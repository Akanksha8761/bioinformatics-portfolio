# Day 10: Dictionaries - Concepts

## 📌 Core Concepts Covered

Dictionaries are Python's key-value mapping data structure. While lists use numeric indices, dictionaries use **keys** to access values. This makes them perfect for storing related data, lookups, and representing real-world relationships.

---

## 1. What is a Dictionary?

A **dictionary** is an unordered collection of key-value pairs.

### **Characteristics:**
- **Key-Value Pairs**: Each item has a key and a value
- **Unordered**: Items don't have a fixed position (Python 3.7+ maintains insertion order)
- **Mutable**: Can be changed after creation
- **Keys are Unique**: Each key appears only once
- **Fast Lookups**: Access by key is very efficient (O(1) time)

### **Creating Dictionaries:**

**Empty dictionary:**
```python
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>
```

**With initial data:**
```python
gene_expression = {
    'TP53': 150.5,
    'BRCA1': 85.2,
    'MYC': 210.0
}
```

**Mixed value types:**
```python
sample_info = {
    'sample_id': 'patient1',
    'age': 30,
    'gender': 'female',
    'is_treated': True,
    'files': ['file1.csv', 'file2.csv']
}
```

**Using dict() constructor:**
```python
another_dict = dict(gene="TP53", count=10, active=True)
# Result: {'gene': 'TP53', 'count': 10, 'active': True}
```

---

## 2. Accessing Values

### **Square Brackets [] - Direct Access:**
```python
gene_expression = {'TP53': 150.5, 'BRCA1': 85.2}
value = gene_expression['TP53']  # 150.5
```

**Problem:** Raises `KeyError` if key doesn't exist:
```python
value = gene_expression['EGFR']  # KeyError!
```

### **.get() Method - Safe Access:**
```python
# Returns None if key doesn't exist
value = gene_expression.get('EGFR')  # None

# Provide a default value
value = gene_expression.get('EGFR', 0.0)  # 0.0
```

**When to use which:**
- Use `[]` when you're **certain** the key exists
- Use `.get()` when the key **might not exist**

---

## 3. Adding and Modifying Items

### **Adding a New Key-Value Pair:**
```python
gene_expression = {'TP53': 150.5}
gene_expression['BRCA1'] = 85.2
# Result: {'TP53': 150.5, 'BRCA1': 85.2}
```

### **Modifying an Existing Value:**
```python
gene_expression['TP53'] = 200.0  # Updates value
# Result: {'TP53': 200.0, 'BRCA1': 85.2}
```

**Key insight:** Same syntax for adding and modifying!
- If key exists → modifies value
- If key doesn't exist → adds new pair

### **update() - Add Multiple Items:**
```python
gene_expression = {'TP53': 150.5}

# Add from another dictionary
more_genes = {'BRCA1': 85.2, 'MYC': 210.0}
gene_expression.update(more_genes)

# Add with keyword arguments
gene_expression.update(KRAS=60.0, PTEN=75.0)
```

---

## 4. Removing Items

### **del - Delete by Key:**
```python
sample_info = {'age': 30, 'gender': 'female'}
del sample_info['age']
# Result: {'gender': 'female'}
```

**Raises KeyError if key doesn't exist!**

### **pop() - Remove and Return Value:**
```python
sample_info = {'age': 30, 'gender': 'female'}

# Remove and get value
age = sample_info.pop('age')  # Returns 30
# sample_info is now: {'gender': 'female'}

# With default (if key might not exist)
city = sample_info.pop('city', 'Unknown')  # Returns 'Unknown'
```

### **popitem() - Remove Last Item:**
```python
gene_counts = {"A": 5, "B": 10, "C": 3}
item = gene_counts.popitem()  # Returns ('C', 3)
# gene_counts is now: {"A": 5, "B": 10}
```

In Python 3.7+, removes the **last** inserted item.

### **clear() - Remove All Items:**
```python
gene_expression.clear()
# Result: {}
```

---

## 5. Dictionary Views

### **keys() - Get All Keys:**
```python
sample_info = {'age': 30, 'gender': 'female'}
keys = sample_info.keys()
# dict_keys(['age', 'gender'])

# Convert to list
keys_list = list(keys)  # ['age', 'gender']
```

### **values() - Get All Values:**
```python
values = sample_info.values()
# dict_values([30, 'female'])

values_list = list(values)  # [30, 'female']
```

### **items() - Get Key-Value Pairs:**
```python
items = sample_info.items()
# dict_items([('age', 30), ('gender', 'female')])

items_list = list(items)
# [('age', 30), ('gender', 'female')]
```

### **Views are Dynamic:**
```python
gene_counts = {"GeneA": 5, "GeneB": 10}
keys_view = gene_counts.keys()
print(keys_view)  # dict_keys(['GeneA', 'GeneB'])

gene_counts['GeneC'] = 15
print(keys_view)  # dict_keys(['GeneA', 'GeneB', 'GeneC'])
# View updates automatically!
```

---

## 6. Membership Testing

### **in Operator - Check if Key Exists:**
```python
gene_expression = {'TP53': 150.5, 'BRCA1': 85.2}

if 'TP53' in gene_expression:
    print("Found!")  # Prints

if 'EGFR' not in gene_expression:
    print("Not found!")  # Prints
```

**Important:** `in` checks **keys**, not values!

### **Safe Access Pattern:**
```python
gene = "TP53"
if gene in gene_expression:
    level = gene_expression[gene]
    print(f"Level: {level}")
else:
    print("Gene not found")
```

---

## 7. Iterating Through Dictionaries

### **Iterate Through Keys (Default):**
```python
gene_expression = {'TP53': 150.5, 'BRCA1': 85.2}

for gene in gene_expression:  # Same as .keys()
    level = gene_expression[gene]
    print(f"{gene}: {level}")
```

### **Iterate Through Values:**
```python
for level in gene_expression.values():
    print(f"Level: {level}")
```

### **Iterate Through Items (Most Common!):**
```python
for gene, level in gene_expression.items():
    print(f"{gene}: {level}")
```

**This is the most Pythonic way!**

### **Filtering While Iterating:**
```python
threshold = 100

for gene, level in gene_expression.items():
    if level > threshold:
        print(f"{gene}: {level}")
```

---

## 8. Common Patterns

### **Pattern 1: Building a Dictionary:**
```python
# From lists
genes = ['TP53', 'BRCA1', 'MYC']
levels = [150.5, 85.2, 210.0]

gene_dict = {}
for i in range(len(genes)):
    gene_dict[genes[i]] = levels[i]

# Or use zip() (more Pythonic)
gene_dict = dict(zip(genes, levels))
```

### **Pattern 2: Counting Occurrences:**
```python
bases = ['A', 'T', 'G', 'C', 'A', 'T', 'A']
counts = {}

for base in bases:
    if base in counts:
        counts[base] += 1
    else:
        counts[base] = 1
# Result: {'A': 3, 'T': 2, 'G': 1, 'C': 1}

# Or use .get() (cleaner)
counts = {}
for base in bases:
    counts[base] = counts.get(base, 0) + 1
```

### **Pattern 3: Filtering:**
```python
# Filter dictionary based on condition
high_expression = {}
for gene, level in gene_expression.items():
    if level > 100:
        high_expression[gene] = level
```

### **Pattern 4: Swapping Keys and Values:**
```python
original = {'TP53': 'Gene1', 'BRCA1': 'Gene2'}
swapped = {v: k for k, v in original.items()}
# Result: {'Gene1': 'TP53', 'Gene2': 'BRCA1'}
```

---

## 9. Dictionaries vs Lists

| Feature | Lists | Dictionaries |
|---------|-------|--------------|
| Access | By index (number) | By key (any immutable) |
| Order | Ordered | Insertion order (3.7+) |
| Syntax | `my_list[0]` | `my_dict['key']` |
| Use case | Sequences | Mappings/Lookups |
| Speed | O(n) search | O(1) lookup |

**When to use lists:**
- Ordered collection of items
- Access by position
- Duplicate values matter

**When to use dictionaries:**
- Key-value relationships
- Fast lookups
- Named data fields

---

## 10. Valid Keys and Values

### **Keys Must Be Immutable:**
Valid keys:
```python
valid_dict = {
    'string_key': 1,     # Strings ✓
    42: 'value',         # Numbers ✓
    (1, 2): 'tuple',     # Tuples ✓
    True: 'boolean'      # Booleans ✓
}
```

Invalid keys:
```python
# Lists are mutable - cannot be keys
# invalid = {[1, 2]: 'value'}  # TypeError!

# Dictionaries are mutable - cannot be keys
# invalid = {{}: 'value'}  # TypeError!
```

### **Values Can Be Anything:**
```python
flexible_dict = {
    'list': [1, 2, 3],
    'dict': {'nested': 'dict'},
    'function': print,
    'number': 42
}
```

---

## 11. Bioinformatics Applications

### **Gene Expression Data:**
```python
gene_expression = {
    'TP53': 150.5,
    'BRCA1': 85.2,
    'MYC': 210.0
}

# Find high expression
for gene, level in gene_expression.items():
    if level > 100:
        print(f"{gene} is highly expressed")
```

### **Patient Metadata:**
```python
patient = {
    'id': 'PAT001',
    'age': 45,
    'diagnosis': 'breast_cancer',
    'stage': 2,
    'treated': True
}

# Access specific field
if patient['treated']:
    print(f"Patient {patient['id']} is under treatment")
```

### **Methylation Analysis:**
```python
methylation_data = [
    ("site_A", 0.8),
    ("site_B", 0.3),
    ("site_C", 0.9)
]

# Build dictionary of hypermethylated sites
threshold = 0.75
hyper_sites = {}

for site, level in methylation_data:
    if level > threshold:
        hyper_sites[site] = level

print(f"Found {len(hyper_sites)} hypermethylated sites")
```

---

## 💡 Key Takeaways

1. **Dictionaries map keys to values** - fast lookups!
2. **Keys must be unique and immutable**
3. **Use [] for access when key exists, .get() when uncertain**
4. **Same syntax for adding and modifying** - dict[key] = value
5. **pop() removes and returns, del just deletes**
6. **.items() iteration is most common** - for k, v in dict.items()
7. **Use in to check if key exists**
8. **Views (.keys(), .values(), .items()) are dynamic**
9. **Dictionaries are mutable** - can be changed after creation
10. **Perfect for structured data** - patient info, gene expression, etc.

---

## 📚 Method Quick Reference

| Method | Purpose | Returns |
|--------|---------|---------|
| `get(key, default)` | Safe access | Value or default |
| `update(dict)` | Add multiple items | None |
| `pop(key, default)` | Remove and return | Value or default |
| `popitem()` | Remove last item | (key, value) tuple |
| `clear()` | Remove all | None |
| `keys()` | Get all keys | View object |
| `values()` | Get all values | View object |
| `items()` | Get all pairs | View object |

---

*Dictionaries are fundamental to data organization in Python. They're everywhere in real programming - from configs to APIs to databases!*
