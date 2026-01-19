# Day 5: The "Smart Inventory Manager" Challenge

## 🎯 Challenge Description

### The Scenario
You have a list of product names and a list of their current stock levels.

```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [10, 0, 15, 5]
```

### The Task
1. Create a dictionary called `inventory` where the **Product** is the key and the **Stock** is the value
2. **Filter**: Only include products that are actually in stock (stock > 0)
3. **Transformation**: If a product is "Laptop", change its name to "Apple Laptop" in the dictionary

### The Constraint
Use `zip()` to combine the lists and a **Dictionary Comprehension** to create the final result in **one line**.

## 📚 Concepts Covered

- **zip() Function**: Combining multiple iterables
- **Dictionary Comprehensions**: Creating dictionaries concisely
- **Dictionary Methods**: `.update()`, `.items()`, `.keys()`, `.values()`
- **Filtering in Comprehensions**: Conditional logic
- **String Transformations**: Modifying values during creation
- **Ternary Operators**: Inline if-else expressions

## 💡 Solution Approaches

### Approach 1: One-Line Dictionary Comprehension (Meeting All Requirements)
```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [10, 0, 15, 5]

# One-liner with all requirements
inventory = {
    ("Apple Laptop" if prod == "Laptop" else prod): qty 
    for prod, qty in zip(products, stock) 
    if qty > 0
}

print(inventory)
```

**Output:**
```python
{'Apple Laptop': 10, 'Keyboard': 15, 'Monitor': 5}
```

### Approach 2: Breaking Down the One-Liner (For Understanding)
```python
# Step 1: zip() combines the two lists
combined = zip(products, stock)
# Result: [('Laptop', 10), ('Mouse', 0), ('Keyboard', 15), ('Monitor', 5)]

# Step 2: Dictionary comprehension with filter
inventory = {prod: qty for prod, qty in combined if qty > 0}
# Result: {'Laptop': 10, 'Keyboard': 15, 'Monitor': 5}

# Step 3: Add transformation for "Laptop"
inventory = {
    ("Apple Laptop" if prod == "Laptop" else prod): qty 
    for prod, qty in zip(products, stock) 
    if qty > 0
}
```

### Approach 3: Using Traditional Loop (Your Approach - Improved)
```python
inventory = {}
for product, quantity in zip(products, stock):
    if quantity > 0:  # Filter: only in-stock items
        # Transform: change "Laptop" to "Apple Laptop"
        key = "Apple Laptop" if product == "Laptop" else product
        inventory[key] = quantity

print(inventory)
```

### Approach 4: Using dict() with zip()
```python
# First create full inventory, then filter and transform
full_inventory = dict(zip(products, stock))
inventory = {
    ("Apple Laptop" if k == "Laptop" else k): v 
    for k, v in full_inventory.items() 
    if v > 0
}
```

### Approach 5: Using map() and filter() (Functional Approach)
```python
# Transform products first
transformed_products = [
    "Apple Laptop" if p == "Laptop" else p 
    for p in products
]

# Filter out zero stock items
inventory = {
    prod: qty 
    for prod, qty in zip(transformed_products, stock) 
    if qty > 0
}
```

## 🔍 Code Breakdown

### Understanding zip():
```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [10, 0, 15, 5]

# zip() pairs elements from both lists
pairs = list(zip(products, stock))
print(pairs)
# [('Laptop', 10), ('Mouse', 0), ('Keyboard', 15), ('Monitor', 5)]

# You can unpack in a loop
for product, quantity in zip(products, stock):
    print(f"{product}: {quantity}")
# Laptop: 10
# Mouse: 0
# Keyboard: 15
# Monitor: 5
```

### Understanding Dictionary Comprehension Syntax:
```python
# Basic syntax
{key_expression: value_expression for item in iterable}

# With condition (filter)
{key: value for item in iterable if condition}

# With transformation (ternary operator)
{(new_key if condition else key): value for key, value in iterable}

# Complete example
{
    ("Apple Laptop" if prod == "Laptop" else prod): qty
    #  └─ key transformation ─┘                      └─ value
    for prod, qty in zip(products, stock)
    #   └─ unpacking zip ────┘
    if qty > 0
    #  └─ filter condition
}
```

### Your Original Code Analysis:
```python
# Your Approach 1: Using .update() inside loop
inventory = {}
for i, j in zip(products, stock):
    inventory.update(zip(products, stock))  # ❌ Issue: updates with ALL pairs every iteration
print(inventory)
# Result: {'Laptop': 10, 'Mouse': 0, 'Keyboard': 15, 'Monitor': 5}
# Problem: No filtering, no transformation, inefficient

# Your Approach 2: Dictionary Comprehension
inventory = {i: j for i, j in zip(products, stock)}
print(inventory)
# Result: {'Laptop': 10, 'Mouse': 0, 'Keyboard': 15, 'Monitor': 5}
# Better! But missing: filter (qty > 0) and transformation (Laptop -> Apple Laptop)
```

### Issues to Fix:
```python
# ❌ Wrong: .update() with zip inside loop
for i, j in zip(products, stock):
    inventory.update(zip(products, stock))  # This adds ALL items every iteration!

# ✅ Correct: Add items individually
for product, quantity in zip(products, stock):
    inventory[product] = quantity

# ✅ Better: Use dict comprehension
inventory = {p: q for p, q in zip(products, stock)}
```

## 🎓 Key Takeaways

1. **`zip()` combines iterables** element by element
2. **Dictionary comprehensions** are powerful and concise
3. **Ternary operators** allow inline if-else: `value_if_true if condition else value_if_false`
4. **Filtering in comprehensions** uses `if` at the end
5. **Transformation** happens in the key/value expressions
6. **Unpacking** makes code more readable: `for k, v in ...`

## 🚀 Variations to Try

### Challenge Yourself:

1. **Add low-stock warnings** (stock < 5)
2. **Calculate total inventory value** with prices
3. **Group products by stock level** (low, medium, high)
4. **Sort by stock quantity**
5. **Handle multiple transformations** for different products

### Example Solutions:

**Add Low-Stock Warnings:**
```python
inventory = {
    ("Apple Laptop" if prod == "Laptop" else prod): 
    f"{qty} ⚠️ LOW STOCK" if 0 < qty < 5 else qty
    for prod, qty in zip(products, stock) 
    if qty > 0
}
# {'Apple Laptop': 10, 'Keyboard': 15, 'Monitor': '5 ⚠️ LOW STOCK'}
```

**Calculate Total Value:**
```python
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [10, 0, 15, 5]
prices = [999.99, 29.99, 79.99, 299.99]

inventory = {
    ("Apple Laptop" if p == "Laptop" else p): {
        'quantity': q,
        'price': pr,
        'total_value': q * pr
    }
    for p, q, pr in zip(products, stock, prices) 
    if q > 0
}
```

**Group by Stock Level:**
```python
def stock_level(qty):
    if qty == 0: return "out_of_stock"
    if qty < 5: return "low"
    if qty < 10: return "medium"
    return "high"

grouped = {}
for prod, qty in zip(products, stock):
    level = stock_level(qty)
    if level not in grouped:
        grouped[level] = {}
    if level != "out_of_stock":
        grouped[level][prod] = qty
```

**Sort by Stock Quantity:**
```python
# Create inventory
inventory = {p: q for p, q in zip(products, stock) if q > 0}

# Sort by value (stock quantity) descending
sorted_inventory = dict(sorted(inventory.items(), key=lambda x: x[1], reverse=True))
# {'Keyboard': 15, 'Laptop': 10, 'Monitor': 5}
```

**Multiple Transformations:**
```python
transformations = {
    "Laptop": "Apple Laptop",
    "Monitor": "Dell Monitor",
    "Keyboard": "Mechanical Keyboard"
}

inventory = {
    transformations.get(prod, prod): qty  # Use .get() with default
    for prod, qty in zip(products, stock) 
    if qty > 0
}
```

## 📊 Performance Comparison

| Approach | Lines | Readability | Performance | Memory |
|----------|-------|-------------|-------------|--------|
| Dict Comprehension | 1-3 | Excellent | O(n) | O(n) |
| Traditional Loop | 5-7 | Good | O(n) | O(n) |
| dict() + zip() | 2 | Good | O(n) | O(n) |
| map() + filter() | 3-5 | Fair | O(n) | O(n) |

All approaches have similar performance, but dict comprehension is most Pythonic.

## 🔗 Related Topics to Explore

- `enumerate()` for index + value pairs
- `itertools.zip_longest()` for unequal length lists
- Nested dictionary comprehensions
- `collections.defaultdict` for grouped data
- `operator.itemgetter` for sorting
- Dictionary merging with `|` operator (Python 3.9+)

## 💡 Real-World Applications

- **Inventory Systems**: E-commerce stock management
- **Database Mapping**: Combining table columns
- **Data Processing**: ETL pipelines
- **Configuration Management**: Combining keys and values
- **API Responses**: Formatting paired data
- **Analytics**: Combining metrics with labels

## 🐛 Common Mistakes to Avoid

```python
# ❌ Wrong: Calling zip() repeatedly in loop
for i, j in zip(products, stock):
    inventory.update(zip(products, stock))  # Creates all pairs every iteration!

# ✅ Correct: Process pairs once
inventory = {p: s for p, s in zip(products, stock)}

# ❌ Wrong: Not filtering out-of-stock items
inventory = {p: s for p, s in zip(products, stock)}  # Includes Mouse: 0

# ✅ Correct: Add filter condition
inventory = {p: s for p, s in zip(products, stock) if s > 0}

# ❌ Wrong: Forgetting transformation requirement
inventory = {p: s for p, s in zip(products, stock) if s > 0}  # Still says "Laptop"

# ✅ Correct: Add transformation with ternary
inventory = {
    ("Apple Laptop" if p == "Laptop" else p): s 
    for p, s in zip(products, stock) if s > 0
}

# ❌ Wrong: Misunderstanding zip() with unequal lengths
products = ["A", "B", "C"]
stock = [10, 20]
result = dict(zip(products, stock))  # {'A': 10, 'B': 20} - C is lost!

# ✅ Correct: Use zip_longest if needed
from itertools import zip_longest
result = dict(zip_longest(products, stock, fillvalue=0))  # {'A': 10, 'B': 20, 'C': 0}
```

## 🧪 Testing Your Solution

```python
# Test cases
test_products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
test_stock = [10, 0, 15, 5]

expected_output = {
    'Apple Laptop': 10,
    'Keyboard': 15,
    'Monitor': 5
}

# Run your solution
inventory = {
    ("Apple Laptop" if p == "Laptop" else p): s 
    for p, s in zip(test_products, test_stock) if s > 0
}

# Test
assert inventory == expected_output, f"Test failed! Got {inventory}"
print("✅ All tests passed!")

# Edge cases
print("\nEdge Cases:")

# All out of stock
all_zero = [0, 0, 0, 0]
result = {p: s for p, s in zip(test_products, all_zero) if s > 0}
print(f"All zero stock: {result}")  # {}

# Unequal lengths
short_stock = [10, 5]
result = dict(zip(test_products, short_stock))
print(f"Unequal lengths: {result}")  # {'Laptop': 10, 'Mouse': 5}
```

## 💻 Interactive Examples

### Try These Variations:

```python
# 1. Multiple transformations
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Phone"]
stock = [10, 0, 15, 5, 8]

brand_map = {
    "Laptop": "Apple MacBook",
    "Phone": "iPhone 15",
    "Monitor": "Dell UltraSharp"
}

inventory = {
    brand_map.get(p, p): s  # Use .get() for flexible mapping
    for p, s in zip(products, stock) if s > 0
}
print(inventory)

# 2. Add stock status
inventory = {
    ("Apple Laptop" if p == "Laptop" else p): {
        'quantity': s,
        'status': 'Low' if s < 10 else 'Good'
    }
    for p, s in zip(products, stock) if s > 0
}
print(inventory)

# 3. Reverse mapping (stock as key)
reverse = {s: p for p, s in zip(products, stock) if s > 0}
# Note: Duplicate stocks will be overwritten!
print(reverse)
```

---

**Date Completed:** Day 5  
**Difficulty:** ⭐⭐⭐☆☆ (Intermediate)  
**Time Spent:** ~45 minutes  
**Skills Gained:** zip(), dictionary comprehensions, ternary operators, filtering, transformations
