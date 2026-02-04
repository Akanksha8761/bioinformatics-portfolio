# Day 12: Sets - Concepts

## 📌 Core Concepts Covered

Sets are Python's implementation of mathematical sets - **unordered collections of unique elements**. They're perfect for removing duplicates, testing membership, and performing mathematical set operations like union, intersection, and difference.

---

## 1. What is a Set?

A **set** is an unordered collection of unique elements.

### **Characteristics:**
- **Unordered**: No fixed position or index
- **Unique Elements**: Automatically removes duplicates
- **Mutable**: Can add/remove elements
- **No Indexing**: Cannot access by position
- **Elements Must Be Immutable**: Only hashable types allowed
- **Fast Membership Testing**: O(1) time complexity

### **Creating Sets:**

**With curly braces:**
```python
my_set = {1, 2, 3, 4, 5}
print(type(my_set))  # <class 'set'>
```

**From a list (removes duplicates!):**
```python
my_list = ["GeneA", "GeneB", "GeneC", "GeneA"]
unique_set = set(my_list)
# Result: {'GeneA', 'GeneB', 'GeneC'}
```

**From a tuple:**
```python
my_tuple = ("GeneA", "GeneB", "GeneC", "GeneA")
unique_set = set(my_tuple)
# Result: {'GeneA', 'GeneB', 'GeneC'}
```

**Empty set:**
```python
empty_set = set()  # Correct
# empty = {}       # WRONG - this creates an empty dict!
```

---

## 2. Set Properties

### **Uniqueness - Automatic Duplicate Removal:**
```python
my_set = {1, 2, 3, 4, 5, 5, 7, 8, 9, 10}
print(my_set)  # {1, 2, 3, 4, 5, 7, 8, 9, 10}
# Duplicate 5 is automatically removed!
```

### **Unordered - No Fixed Position:**
```python
my_set = {"red", "green", "blue"}
print(my_set)  # Order may vary each time!
# Might print: {'blue', 'green', 'red'}
```

**You cannot rely on order!**

### **No Indexing or Slicing:**
```python
my_set = {"red", "green", "blue"}

# These ALL raise TypeError:
# my_set[0]       # No indexing!
# my_set[1:3]     # No slicing!
# my_set[-1]      # No negative indexing!
```

### **Elements Must Be Immutable (Hashable):**

**Valid elements:**
```python
valid_set = {
    1,              # Numbers ✓
    "string",       # Strings ✓
    (1, 2),        # Tuples ✓
    True           # Booleans ✓
}
```

**Invalid elements:**
```python
# Lists are mutable - NOT allowed!
# invalid = {1, [1, 2]}  # TypeError: unhashable type: 'list'

# Dicts are mutable - NOT allowed!
# invalid = {1, {"key": "value"}}  # TypeError: unhashable type: 'dict'
```

---

## 3. Adding Elements

### **add() - Add Single Element:**
```python
samples = {"Sample1", "Sample2", "Sample3"}
samples.add("Sample4")
# Result: {"Sample1", "Sample2", "Sample3", "Sample4"}
```

**Adding duplicate has no effect:**
```python
samples.add("Sample2")  # Already exists - no change
```

### **update() - Add Multiple Elements:**
```python
samples = {"Sample1", "Sample2"}
samples.update(["Sample3", "Sample4"])
# Result: {"Sample1", "Sample2", "Sample3", "Sample4"}

# Can also update with another set
samples.update({"Sample5", "Sample6"})
```

**Warning with strings:**
```python
samples = {"Sample1"}
samples.update("ABC")  # Adds each character!
# Result: {"Sample1", "A", "B", "C"}
```

---

## 4. Removing Elements

### **remove() - Remove Specific Element:**
```python
samples = {"Sample1", "Sample2", "Sample3"}
samples.remove("Sample2")
# Result: {"Sample1", "Sample3"}
```

**Raises KeyError if not found:**
```python
# samples.remove("Sample9")  # KeyError!
```

### **discard() - Safe Remove:**
```python
samples = {"Sample1", "Sample2", "Sample3"}
samples.discard("Sample9")  # No error even if not found!
```

**Use discard() when element might not exist!**

### **pop() - Remove Arbitrary Element:**
```python
samples = {"Sample1", "Sample2", "Sample3"}
removed = samples.pop()  # Removes and returns some element
print(removed)  # Could be any element (set is unordered)
```

### **clear() - Remove All Elements:**
```python
samples = {"Sample1", "Sample2", "Sample3"}
samples.clear()
# Result: set()
```

---

## 5. Membership Testing

Fast O(1) lookup using `in`:

```python
samples = {"Sample1", "Sample2", "Sample3"}

if "Sample1" in samples:
    print("Found!")  # Prints

if "Sample5" not in samples:
    print("Not found!")  # Prints
```

**Much faster than lists for membership testing!**

---

## 6. Set Operations (Mathematical Sets)

### **Union (|) - All Elements from Both Sets (OR):**
```python
setA = {"GeneA", "GeneB", "GeneC"}
setB = {"GeneC", "GeneD", "GeneE"}

union = setA | setB
# Result: {"GeneA", "GeneB", "GeneC", "GeneD", "GeneE"}

# Also: setA.union(setB)
```

**Union with multiple sets:**
```python
union_all = setA | setB | setC
```

### **Intersection (&) - Common Elements (AND):**
```python
setA = {"GeneA", "GeneB", "GeneC"}
setB = {"GeneC", "GeneD", "GeneE"}

intersection = setA & setB
# Result: {"GeneC"}

# Also: setA.intersection(setB)
```

### **Difference (-) - Elements in First but Not Second:**
```python
setA = {"GeneA", "GeneB", "GeneC"}
setB = {"GeneC", "GeneD", "GeneE"}

difference = setA - setB
# Result: {"GeneA", "GeneB"}

# Also: setA.difference(setB)
```

**Note:** Order matters!
```python
setA - setB  # {"GeneA", "GeneB"}
setB - setA  # {"GeneD", "GeneE"}
```

### **Symmetric Difference (^) - Elements in Either but Not Both (XOR):**
```python
setA = {"GeneA", "GeneB", "GeneC"}
setB = {"GeneC", "GeneD", "GeneE"}

sym_diff = setA ^ setB
# Result: {"GeneA", "GeneB", "GeneD", "GeneE"}

# Also: setA.symmetric_difference(setB)
```

---

## 7. Subset and Superset

### **Subset (<=) - Is Every Element of A in B?:**
```python
small = {1, 2}
large = {1, 2, 3, 4, 5}

print(small <= large)  # True (small is subset of large)
print(large <= small)  # False

# Also: small.issubset(large)
```

**Proper subset (<) - Subset but not equal:**
```python
setA = {1, 2}
setB = {1, 2, 3}
setC = {1, 2}

print(setA < setB)  # True (proper subset)
print(setA < setC)  # False (equal, not proper)
```

### **Superset (>=) - Does A Contain All Elements of B?:**
```python
small = {1, 2}
large = {1, 2, 3, 4, 5}

print(large >= small)  # True (large is superset of small)
print(small >= large)  # False

# Also: large.issuperset(small)
```

**Proper superset (>) - Superset but not equal:**
```python
print(large > small)  # True (proper superset)
```

---

## 8. Set Methods Summary

| Method | Description | Returns |
|--------|-------------|---------|
| `add(x)` | Add element x | None |
| `update(iterable)` | Add multiple elements | None |
| `remove(x)` | Remove x (error if not found) | None |
| `discard(x)` | Remove x (no error if not found) | None |
| `pop()` | Remove and return arbitrary element | Element |
| `clear()` | Remove all elements | None |
| `union(other)` or `\|` | All elements from both | New set |
| `intersection(other)` or `&` | Common elements | New set |
| `difference(other)` or `-` | Elements in first not in second | New set |
| `symmetric_difference(other)` or `^` | Elements in either not both | New set |
| `issubset(other)` or `<=` | Is subset? | Boolean |
| `issuperset(other)` or `>=` | Is superset? | Boolean |

---

## 9. Sets vs Lists vs Tuples vs Dicts

| Feature | Set | List | Tuple | Dict |
|---------|-----|------|-------|------|
| Ordered | No | Yes | Yes | Yes (3.7+) |
| Mutable | Yes | Yes | No | Yes |
| Duplicates | No | Yes | Yes | Keys: No |
| Indexing | No | Yes | Yes | By key |
| Syntax | `{}` | `[]` | `()` | `{k:v}` |
| Use case | Unique items | Sequences | Fixed data | Key-value |
| Speed | O(1) lookup | O(n) lookup | O(n) lookup | O(1) lookup |

---

## 10. Common Patterns

### **Pattern 1: Remove Duplicates:**
```python
my_list = [1, 2, 3, 2, 4, 3, 5]
unique_list = list(set(my_list))
# Result: [1, 2, 3, 4, 5] (order may vary)
```

### **Pattern 2: Find Common Elements:**
```python
list1 = ["A", "B", "C", "D"]
list2 = ["C", "D", "E", "F"]

common = set(list1) & set(list2)
# Result: {"C", "D"}
```

### **Pattern 3: Find Unique to Each:**
```python
only_in_list1 = set(list1) - set(list2)
only_in_list2 = set(list2) - set(list1)
```

### **Pattern 4: Find All Unique:**
```python
all_unique = set(list1) | set(list2)
```

### **Pattern 5: Check if Lists Share Elements:**
```python
if set(list1) & set(list2):
    print("Lists have common elements")
```

---

## 11. When to Use Sets

### **Use Sets When:**

1. **Need unique elements:**
```python
# Remove duplicates from gene list
genes = ["TP53", "BRCA1", "TP53", "MYC"]
unique_genes = set(genes)  # {"TP53", "BRCA1", "MYC"}
```

2. **Fast membership testing:**
```python
# Check if gene is in set (O(1) vs O(n) for list)
if "TP53" in gene_set:  # Very fast!
    process_gene()
```

3. **Mathematical set operations:**
```python
# Find genes in both samples
common_genes = sample1_genes & sample2_genes
```

4. **Don't need order or duplicates:**
```python
# Just need to know what's present
active_users = {"user1", "user2", "user3"}
```

---

## 12. Bioinformatics Applications

### **Unique Gene Lists:**
```python
# Remove duplicate gene names
genes = ["GeneA", "GeneB", "GeneC", "GeneA"]
unique_genes = set(genes)
# Result: {"GeneA", "GeneB", "GeneC"}
```

### **Comparing Sample Gene Lists:**
```python
sample_A_genes = {"GeneA", "GeneB", "GeneC", "GeneD"}
sample_B_genes = {"GeneC", "GeneD", "GeneE", "GeneF"}

# Genes in both samples
common = sample_A_genes & sample_B_genes

# Genes unique to Sample A
unique_to_A = sample_A_genes - sample_B_genes

# All genes across both samples
all_genes = sample_A_genes | sample_B_genes
```

### **Finding Hypermethylated Genes:**
```python
# Genes hypermethylated in at least one sample
hyper_A = {"GeneA", "GeneB", "GeneC"}
hyper_B = {"GeneC", "GeneD", "GeneE"}

# Hypermethylated in any sample
any_hyper = hyper_A | hyper_B

# Consistently hypermethylated (both samples)
consistent = hyper_A & hyper_B
```

### **Sample Comparison:**
```python
# Differentially expressed genes
sample1_de = {"GeneA", "GeneB", "GeneC"}
sample2_de = {"GeneC", "GeneD", "GeneE"}
sample3_de = {"GeneA", "GeneC", "GeneF"}

# Common to all samples
common_to_all = sample1_de & sample2_de & sample3_de

# Unique to each
unique_1 = sample1_de - sample2_de - sample3_de
```

---

## 💡 Key Takeaways

1. **Sets store unique elements only** - duplicates automatically removed
2. **Unordered** - no indexing or slicing
3. **Fast membership testing** - O(1) time complexity
4. **Elements must be immutable** - no lists or dicts as elements
5. **add()** for single element, **update()** for multiple
6. **remove()** raises error, **discard()** doesn't
7. **Set operations:** | (union), & (intersection), - (difference), ^ (symmetric difference)
8. **Perfect for** removing duplicates and comparing collections
9. **{} creates empty dict**, use **set()** for empty set
10. **Mathematical set operations** built into the language!

---

## 📚 Quick Reference

| Operation | Operator | Method |
|-----------|----------|--------|
| Union | `A \| B` | `A.union(B)` |
| Intersection | `A & B` | `A.intersection(B)` |
| Difference | `A - B` | `A.difference(B)` |
| Symmetric Diff | `A ^ B` | `A.symmetric_difference(B)` |
| Subset | `A <= B` | `A.issubset(B)` |
| Superset | `A >= B` | `A.issuperset(B)` |
| Membership | `x in A` | - |
| Add | - | `A.add(x)` |
| Remove | - | `A.remove(x)` or `A.discard(x)` |

---

*Sets bring mathematical set theory to Python - perfect for unique elements and set operations!*
