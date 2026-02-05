# Day 13: List Comprehensions - Concepts

## 📌 Core Concepts Covered

List comprehensions are a concise and elegant way to create lists in Python. They allow you to transform and filter data in a single line, replacing traditional for loops with more readable and Pythonic code.

---

## 1. What are List Comprehensions?

A **list comprehension** is a compact syntax for creating lists by applying an expression to each item in an iterable, optionally filtering items.

### **Basic Syntax:**
```python
[expression for item in iterable]
```

### **Traditional vs List Comprehension:**

**Traditional way:**
```python
squares = []
for x in range(10):
    squares.append(x**2)
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**List comprehension:**
```python
squares = [x**2 for x in range(10)]
# Result: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Benefits:**
- More concise (1 line vs 3 lines)
- More readable once familiar
- Often faster execution
- Pythonic and idiomatic

---

## 2. Basic List Comprehensions (Transformation)

Apply a transformation to each element.

### **Syntax:**
```python
[expression for item in iterable]
```

### **Examples:**

**Squares:**
```python
squares = [x**2 for x in range(10)]
```

**Uppercase strings:**
```python
genes = ["myb77", "brca2", "tp53"]
upper_genes = [gene.upper() for gene in genes]
# Result: ['MYB77', 'BRCA2', 'TP53']
```

**Add suffix:**
```python
genes = ["gene1", "gene2", "gene3"]
processed = [gene + "_processed" for gene in genes]
# Result: ['gene1_processed', 'gene2_processed', 'gene3_processed']
```

**Mathematical operations:**
```python
temps_c = [0, 10, 20, 30, 40]
temps_f = [(temp * 9/5) + 32 for temp in temps_c]
# Result: [32.0, 50.0, 68.0, 86.0, 104.0]
```

---

## 3. List Comprehensions with Filtering

Filter items based on a condition.

### **Syntax:**
```python
[expression for item in iterable if condition]
```

The `if` clause filters which items are included.

### **Examples:**

**Even numbers only:**
```python
evens = [x for x in range(20) if x % 2 == 0]
# Result: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

**Filter by threshold:**
```python
methylation = [0.1, 0.5, 0.6, 0.9, 0.22, 1.0]
threshold = 0.75
hyper = [m for m in methylation if m > threshold]
# Result: [0.9, 1.0]
```

**Filter strings:**
```python
genes = ["myb77", "brca2", "wrky23", "bzip", "myc", "tp53"]
b_or_m_genes = [g for g in genes if g.upper().startswith('B') or g.upper().startswith('M')]
# Result: ['myb77', 'brca2', 'bzip', 'myc']
```

**Filter positive numbers:**
```python
numbers = [-5, 3, -1, 7, -2, 8]
positives = [n for n in numbers if n > 0]
# Result: [3, 7, 8]
```

---

## 4. List Comprehensions with Conditional Expression (if-else)

Apply different transformations based on a condition.

### **Syntax:**
```python
[expr_if_true if condition else expr_if_false for item in iterable]
```

**Note:** The if-else comes BEFORE the `for`!

### **Examples:**

**Label as Even/Odd:**
```python
numbers = range(10)
labels = ['Even' if n % 2 == 0 else 'Odd' for n in numbers]
# Result: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
```

**Categorize as High/Low:**
```python
values = [0.1, 0.5, 0.6, 0.9, 0.22, 1.0]
threshold = 0.75
categories = ['High' if v > threshold else 'Low' for v in values]
# Result: ['Low', 'Low', 'Low', 'High', 'Low', 'High']
```

**Cap values at maximum:**
```python
values = [50, 150, 75, 200, 30]
max_val = 100
capped = [v if v <= max_val else max_val for v in values]
# Result: [50, 100, 75, 100, 30]
```

---

## 5. Combining Filtering and Conditional Expression

You can filter AND apply conditional logic!

### **Syntax:**
```python
[expr_if_true if condition1 else expr_if_false for item in iterable if condition2]
```

- `if condition2` (at end) - filters which items are processed
- `if condition1 else` (before for) - transforms the filtered items

### **Example: Square only even numbers:**

**Traditional:**
```python
numbers = range(20)
result = []
for n in numbers:
    if n % 2 == 0:  # Filter
        result.append(n**2)  # Transform
# Result: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
```

**List comprehension:**
```python
result = [n**2 for n in range(20) if n % 2 == 0]
# Result: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
```

### **Example: Label high values, skip low:**
```python
values = [0.1, 0.5, 0.6, 0.9, 0.22, 1.0]
result = ['Very High' if v > 0.9 else 'High' for v in values if v > 0.5]
# Filter: v > 0.5 (keeps 0.6, 0.9, 1.0)
# Transform: 'Very High' if > 0.9, else 'High'
# Result: ['High', 'High', 'Very High']
```

---

## 6. Nested List Comprehensions

Create multi-dimensional structures or flatten nested lists.

### **Syntax:**
```python
[expression for item1 in iterable1 for item2 in iterable2]
```

Equivalent to nested loops - outer loop first, then inner.

### **Example 1: Coordinate Pairs:**

**Traditional:**
```python
coords = []
for x in range(3):
    for y in range(2):
        coords.append((x, y))
# Result: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

**List comprehension:**
```python
coords = [(x, y) for x in range(3) for y in range(2)]
# Result: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

### **Example 2: Flatten a List of Lists:**

**Traditional:**
```python
nested = [[1, 2], [3, 4, 5], [6, 7]]
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)
# Result: [1, 2, 3, 4, 5, 6, 7]
```

**List comprehension:**
```python
flat = [item for sublist in nested for item in sublist]
# Result: [1, 2, 3, 4, 5, 6, 7]
```

### **Example 3: Flatten with Filtering:**

**Get only even numbers from nested list:**
```python
nested = [[1, 2], [3, 4, 5], [6, 7, 8]]
evens = [n for sublist in nested for n in sublist if n % 2 == 0]
# Result: [2, 4, 6, 8]
```

---

## 7. Understanding the Order

### **For Nested Comprehensions:**
```python
[expression for item1 in iter1 for item2 in iter2 if condition]
```

Reads left to right, equivalent to:
```python
result = []
for item1 in iter1:
    for item2 in iter2:
        if condition:
            result.append(expression)
```

### **For Conditional Expression:**
```python
[value_if_true if condition else value_if_false for item in iterable]
```

The condition comes BEFORE the `for`.

### **Combining Both:**
```python
[expr_if if cond1 else expr_else for item in iter if cond2]
```

1. Filter with `if cond2` (at end)
2. For each filtered item, evaluate `cond1`
3. If `cond1` is True, use `expr_if`, else use `expr_else`

---

## 8. When to Use List Comprehensions

### **Use List Comprehensions When:**

✅ **Simple transformations:**
```python
squares = [x**2 for x in range(10)]
```

✅ **Filtering:**
```python
evens = [x for x in numbers if x % 2 == 0]
```

✅ **Simple conditional mapping:**
```python
labels = ['High' if x > 50 else 'Low' for x in values]
```

✅ **Flattening lists:**
```python
flat = [item for sublist in nested for item in sublist]
```

### **DON'T Use List Comprehensions When:**

❌ **Complex logic:**
```python
# Too complex - use traditional loop
result = [complex_function(x, y, z) if condition1 and condition2 else other_function(x) 
          for x in data if validate(x) and check(x)]
```

❌ **Multiple statements needed:**
```python
# Can't do multiple operations in comprehension
for item in data:
    x = process(item)
    y = validate(x)
    z = transform(y)
    result.append(z)
```

❌ **Side effects (printing, file I/O):**
```python
# Don't do this - comprehensions are for creating lists
[print(x) for x in items]  # Use regular loop instead
```

**Rule of thumb:** If it's hard to read, use a regular loop!

---

## 9. Common Patterns

### **Pattern 1: Transform All Items:**
```python
result = [transform(item) for item in items]
```

### **Pattern 2: Filter Items:**
```python
result = [item for item in items if condition(item)]
```

### **Pattern 3: Transform and Filter:**
```python
result = [transform(item) for item in items if condition(item)]
```

### **Pattern 4: Conditional Transform:**
```python
result = [value_a if condition else value_b for item in items]
```

### **Pattern 5: Flatten:**
```python
result = [item for sublist in nested for item in sublist]
```

### **Pattern 6: Cartesian Product:**
```python
result = [(x, y) for x in list1 for y in list2]
```

---

## 10. Bioinformatics Applications

### **Process Gene Names:**
```python
genes = ["tp53", "brca1", "myc"]
processed = [gene.upper() + "_human" for gene in genes]
# Result: ['TP53_human', 'BRCA1_human', 'MYC_human']
```

### **Filter High Expression:**
```python
expression_data = [('TP53', 150), ('BRCA1', 85), ('MYC', 210)]
threshold = 100
high_expr = [gene for gene, level in expression_data if level > threshold]
# Result: ['TP53', 'MYC']
```

### **Categorize Methylation:**
```python
methylation = [0.1, 0.5, 0.8, 0.95, 0.3]
categories = ['Hyper' if m > 0.75 else 'Normal' for m in methylation]
# Result: ['Normal', 'Normal', 'Hyper', 'Hyper', 'Normal']
```

### **Extract Coordinates:**
```python
genomic_data = [("chr1", 1000, 2000), ("chr2", 3000, 4000)]
starts = [start for chr, start, end in genomic_data]
# Result: [1000, 3000]
```

### **Calculate GC Content:**
```python
sequences = ["ATGC", "GCGC", "ATAT"]
gc_percentages = [(seq.count('G') + seq.count('C')) / len(seq) * 100 
                  for seq in sequences]
# Result: [50.0, 100.0, 0.0]
```

---

## 💡 Key Takeaways

1. **List comprehensions** create lists in a single, readable line
2. **Basic syntax:** `[expression for item in iterable]`
3. **With filtering:** `[expression for item in iterable if condition]`
4. **With if-else:** `[expr_if if cond else expr_else for item in iterable]`
5. **Order matters:** conditional expression comes BEFORE for, filter comes AFTER
6. **Nested comprehensions** flatten or create cartesian products
7. **More Pythonic** than equivalent for loops
8. **Don't overuse** - readability is key!
9. **Faster** than traditional loops for simple operations
10. **Perfect for** transforming and filtering data

---

## 📚 Quick Reference

| Pattern | Syntax | Example |
|---------|--------|---------|
| Transform | `[f(x) for x in items]` | `[x**2 for x in range(10)]` |
| Filter | `[x for x in items if cond]` | `[x for x in nums if x > 0]` |
| Transform + Filter | `[f(x) for x in items if cond]` | `[x**2 for x in nums if x > 0]` |
| Conditional | `[a if cond else b for x in items]` | `['E' if x%2==0 else 'O' for x in nums]` |
| Flatten | `[item for sub in nested for item in sub]` | `[n for list in lists for n in list]` |
| Cartesian | `[(x,y) for x in A for y in B]` | `[(a,b) for a in [1,2] for b in [3,4]]` |

---

*List comprehensions make Python code elegant and expressive - master them for truly Pythonic code!*
