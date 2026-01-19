"""
Day 5: The "Smart Inventory Manager" Challenge
===============================================

The Scenario:
You have a list of product names and a list of their current stock levels.
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [10, 0, 15, 5]

The Task:
    1. Create a dictionary called inventory where the Product is the key 
       and the Stock is the value.
    2. Filter: Only include products that are actually in stock (stock > 0).
    3. Transformation: If a product is "Laptop", change its name to 
       "Apple Laptop" in the dictionary.

The Constraint:
Use zip() to combine the lists and a Dictionary Comprehension to create 
the final result in one line.
"""

from itertools import zip_longest

# Input data
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
stock = [10, 0, 15, 5]

print("=" * 70)
print("Day 5: Smart Inventory Manager Challenge")
print("=" * 70)
print(f"\nProducts: {products}")
print(f"Stock levels: {stock}")


# ============================================================================
# Understanding zip()
# ============================================================================
print("\n" + "=" * 70)
print("Understanding zip()")
print("=" * 70)

# zip() pairs elements from both lists
pairs = list(zip(products, stock))
print(f"\nzip(products, stock) creates pairs:")
for pair in pairs:
    print(f"  {pair}")

# Unpacking in a loop
print(f"\nUnpacking in a loop:")
for product, quantity in zip(products, stock):
    print(f"  {product}: {quantity} in stock")


# ============================================================================
# Your Original Approaches
# ============================================================================
print("\n" + "=" * 70)
print("Your Original Approaches")
print("=" * 70)

# Approach 1: Using .update() (with issue)
print("\n--- Approach 1: Using .update() ---")
inventory_v1 = {}
for i, j in zip(products, stock):
    # Note: This updates with ALL pairs every iteration (inefficient)
    inventory_v1.update(dict(zip(products, stock)))
print(f"Result: {inventory_v1}")
print("⚠️  Issue: No filtering (includes Mouse: 0), no transformation")

# Approach 2: Dictionary Comprehension (basic)
print("\n--- Approach 2: Basic Dict Comprehension ---")
inventory_v2 = {i: j for i, j in zip(products, stock)}
print(f"Result: {inventory_v2}")
print("⚠️  Issue: No filtering (includes Mouse: 0), no transformation")


# ============================================================================
# Solution 1: One-Line with All Requirements (Challenge Answer)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 1: One-Line with All Requirements ✅")
print("=" * 70)

inventory = {
    ("Apple Laptop" if prod == "Laptop" else prod): qty 
    for prod, qty in zip(products, stock) 
    if qty > 0
}

print(f"\nFinal inventory: {inventory}")
print(f"\nBreakdown:")
print("  ✓ Uses zip() to combine lists")
print("  ✓ Dictionary comprehension")
print("  ✓ Filters out-of-stock items (qty > 0)")
print("  ✓ Transforms 'Laptop' to 'Apple Laptop'")


# ============================================================================
# Solution 2: Step-by-Step Breakdown
# ============================================================================
print("\n" + "=" * 70)
print("Solution 2: Step-by-Step Breakdown")
print("=" * 70)

# Step 1: Combine lists with zip
print("\n--- Step 1: Combine with zip() ---")
combined = list(zip(products, stock))
print(f"Combined: {combined}")

# Step 2: Basic dictionary (no filter, no transform)
print("\n--- Step 2: Basic Dictionary ---")
basic_dict = {prod: qty for prod, qty in combined}
print(f"Basic: {basic_dict}")

# Step 3: Add filter (only in-stock items)
print("\n--- Step 3: Add Filter (qty > 0) ---")
filtered_dict = {prod: qty for prod, qty in combined if qty > 0}
print(f"Filtered: {filtered_dict}")

# Step 4: Add transformation (Laptop -> Apple Laptop)
print("\n--- Step 4: Add Transformation ---")
final_dict = {
    ("Apple Laptop" if prod == "Laptop" else prod): qty 
    for prod, qty in combined 
    if qty > 0
}
print(f"Final: {final_dict}")


# ============================================================================
# Solution 3: Traditional Loop (Improved from Your Code)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 3: Traditional Loop (Improved)")
print("=" * 70)

inventory_loop = {}
for product, quantity in zip(products, stock):
    # Filter: only add if in stock
    if quantity > 0:
        # Transform: change "Laptop" to "Apple Laptop"
        key = "Apple Laptop" if product == "Laptop" else product
        inventory_loop[key] = quantity

print(f"\nInventory (loop): {inventory_loop}")


# ============================================================================
# Solution 4: Using dict() with zip()
# ============================================================================
print("\n" + "=" * 70)
print("Solution 4: Using dict() with zip()")
print("=" * 70)

# First create full inventory
full_inventory = dict(zip(products, stock))
print(f"\nFull inventory: {full_inventory}")

# Then filter and transform
inventory_dict = {
    ("Apple Laptop" if k == "Laptop" else k): v 
    for k, v in full_inventory.items() 
    if v > 0
}
print(f"Filtered & transformed: {inventory_dict}")


# ============================================================================
# Bonus: Advanced Features
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Advanced Features")
print("=" * 70)

# Feature 1: Multiple transformations using a mapping dictionary
print("\n--- Multiple Transformations ---")
brand_map = {
    "Laptop": "Apple MacBook Pro",
    "Monitor": "Dell UltraSharp",
    "Keyboard": "Mechanical Gaming Keyboard"
}

inventory_multi = {
    brand_map.get(p, p): s  # Use .get() for flexible mapping
    for p, s in zip(products, stock) 
    if s > 0
}
print(f"Multi-brand inventory: {inventory_multi}")


# Feature 2: Add low-stock warnings
print("\n--- Low-Stock Warnings ---")
inventory_warnings = {
    ("Apple Laptop" if p == "Laptop" else p): 
    f"{s} ⚠️ LOW STOCK" if 0 < s < 10 else s
    for p, s in zip(products, stock) 
    if s > 0
}
print(f"With warnings: {inventory_warnings}")


# Feature 3: Nested dictionary with detailed info
print("\n--- Detailed Inventory ---")
prices = [999.99, 29.99, 79.99, 299.99]

inventory_detailed = {
    ("Apple Laptop" if p == "Laptop" else p): {
        'quantity': q,
        'price': pr,
        'total_value': q * pr,
        'status': 'Low' if q < 10 else 'Good'
    }
    for p, q, pr in zip(products, stock, prices) 
    if q > 0
}

print("Detailed inventory:")
for product, details in inventory_detailed.items():
    print(f"  {product}:")
    for key, value in details.items():
        if key == 'total_value' or key == 'price':
            print(f"    {key}: ${value:,.2f}")
        else:
            print(f"    {key}: {value}")


# Feature 4: Group by stock level
print("\n--- Grouped by Stock Level ---")
def get_stock_level(qty):
    """Categorize stock level."""
    if qty == 0: return "out_of_stock"
    if qty < 5: return "low"
    if qty < 10: return "medium"
    return "high"

grouped_inventory = {}
for prod, qty in zip(products, stock):
    level = get_stock_level(qty)
    
    if level not in grouped_inventory:
        grouped_inventory[level] = {}
    
    if level != "out_of_stock":
        grouped_inventory[level][prod] = qty

print("Grouped inventory:")
for level, items in sorted(grouped_inventory.items()):
    print(f"  {level.upper()}:")
    for prod, qty in items.items():
        print(f"    - {prod}: {qty}")


# Feature 5: Sort by stock quantity
print("\n--- Sorted by Stock Quantity ---")
sorted_inventory = dict(
    sorted(inventory.items(), key=lambda x: x[1], reverse=True)
)
print("Sorted (descending):")
for prod, qty in sorted_inventory.items():
    print(f"  {prod}: {qty}")


# ============================================================================
# Edge Cases
# ============================================================================
print("\n" + "=" * 70)
print("Edge Cases")
print("=" * 70)

# Case 1: All items out of stock
print("\n--- All Items Out of Stock ---")
all_zero_stock = [0, 0, 0, 0]
empty_inventory = {
    p: s for p, s in zip(products, all_zero_stock) if s > 0
}
print(f"Empty inventory: {empty_inventory}")

# Case 2: Unequal list lengths
print("\n--- Unequal List Lengths ---")
short_stock = [10, 5]
partial_inventory = dict(zip(products, short_stock))
print(f"Products: {products}")
print(f"Stock: {short_stock}")
print(f"Result: {partial_inventory}")
print("⚠️  Note: Extra products are ignored!")

# Using zip_longest to handle unequal lengths
print("\n--- Using zip_longest ---")
full_partial = dict(zip_longest(products, short_stock, fillvalue=0))
print(f"With fillvalue=0: {full_partial}")


# ============================================================================
# Practical Example: E-commerce Inventory System
# ============================================================================
print("\n" + "=" * 70)
print("Practical Example: E-commerce Inventory System")
print("=" * 70)

def create_inventory_report(products, stock, prices, brands=None):
    """
    Create comprehensive inventory report.
    
    Args:
        products (list): Product names
        stock (list): Stock quantities
        prices (list): Product prices
        brands (dict): Optional brand name mappings
    
    Returns:
        dict: Comprehensive inventory with statistics
    """
    brands = brands or {}
    
    # Create detailed inventory
    inventory = {
        brands.get(p, p): {
            'quantity': q,
            'price': pr,
            'value': q * pr,
            'status': 'Critical' if 0 < q < 3 
                     else 'Low' if q < 10 
                     else 'Good'
        }
        for p, q, pr in zip(products, stock, prices) 
        if q > 0
    }
    
    # Calculate statistics
    total_items = sum(item['quantity'] for item in inventory.values())
    total_value = sum(item['value'] for item in inventory.values())
    low_stock_count = sum(
        1 for item in inventory.values() 
        if item['status'] in ['Low', 'Critical']
    )
    
    return {
        'inventory': inventory,
        'statistics': {
            'total_products': len(inventory),
            'total_items': total_items,
            'total_value': total_value,
            'low_stock_items': low_stock_count
        }
    }

# Test the function
brand_mappings = {
    "Laptop": "Apple MacBook Pro",
    "Monitor": "Dell UltraSharp 27\""
}

report = create_inventory_report(products, stock, prices, brand_mappings)

print("\n📊 INVENTORY REPORT")
print("-" * 70)
print("\nProducts:")
for product, details in report['inventory'].items():
    print(f"\n  {product}:")
    print(f"    Quantity: {details['quantity']}")
    print(f"    Price: ${details['price']:,.2f}")
    print(f"    Total Value: ${details['value']:,.2f}")
    print(f"    Status: {details['status']}")

print(f"\n📈 STATISTICS")
print("-" * 70)
stats = report['statistics']
print(f"  Total Product Types: {stats['total_products']}")
print(f"  Total Items in Stock: {stats['total_items']}")
print(f"  Total Inventory Value: ${stats['total_value']:,.2f}")
print(f"  Low Stock Alerts: {stats['low_stock_items']}")


# ============================================================================
# Testing
# ============================================================================
print("\n" + "=" * 70)
print("Testing")
print("=" * 70)

def test_inventory_creation():
    """Test inventory creation with various inputs."""
    test_cases = [
        {
            'products': ["Laptop", "Mouse", "Keyboard", "Monitor"],
            'stock': [10, 0, 15, 5],
            'expected': {'Apple Laptop': 10, 'Keyboard': 15, 'Monitor': 5}
        },
        {
            'products': ["Laptop"],
            'stock': [5],
            'expected': {'Apple Laptop': 5}
        },
        {
            'products': ["Mouse"],
            'stock': [0],
            'expected': {}
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = {
            ("Apple Laptop" if p == "Laptop" else p): s 
            for p, s in zip(test['products'], test['stock']) 
            if s > 0
        }
        
        assert result == test['expected'], f"Test {i} failed!"
        print(f"✅ Test {i} passed: {result}")

test_inventory_creation()


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)

print(f"""
Challenge Requirements:
✓ Use zip() to combine lists
✓ Use dictionary comprehension
✓ Filter out-of-stock items (stock > 0)
✓ Transform "Laptop" to "Apple Laptop"

Original data:
  Products: {products}
  Stock: {stock}

Final inventory (one-liner):
  {inventory}

Key concepts learned:
✓ zip() function for pairing lists
✓ Dictionary comprehensions
✓ Ternary operators (inline if-else)
✓ Filtering in comprehensions
✓ Data transformation during creation
""")

print("=" * 70)
print("✅ Day 5 completed!")
print("=" * 70)
