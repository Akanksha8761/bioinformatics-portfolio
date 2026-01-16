"""
Day 4: Data Types & The "Price Cleaner & Discount Calculator" Challenge
=========================================================================

Part 1: Data Types Fundamentals
Part 2: Price Cleaning Challenge
"""

import re

print("=" * 70)
print("Day 4: Data Types & Price Cleaner Challenge")
print("=" * 70)


# ============================================================================
# PART 1: DATA TYPES FUNDAMENTALS
# ============================================================================

print("\n" + "=" * 70)
print("PART 1: DATA TYPES FUNDAMENTALS")
print("=" * 70)

## DATA TYPES ##
my_age = 35  # integer
pi_value = 3.144335  # float
user_name = "Akanksha"  # String
is_learning = True  # Boolean
database_result = None  # NoneType

## PRINT FUNCTION ##
print("\n--- Basic Printing ---")
print(my_age)
print(pi_value)
print(user_name)
print(is_learning)
print(database_result)

# Printing with labels (more descriptive)
print("\n--- Printing with Labels ---")
print("My age is: ", my_age)
print("The value of pi is: ", pi_value)
print("Your user name is: ", user_name)
print("Am I learning new things: ", is_learning)
print("What is the result from database: ", database_result)

# Using f-strings (Formatted String Literals - Recommended for modern Python)
print("\n--- Using F-Strings (Recommended) ---")
print(f"My name is {user_name}, and my age is {my_age}")
print(f"The value of pi is {pi_value:.3f}")

## TYPE FUNCTION ##
print("\n--- Type Function ---")
print(f"Type of my_age: {type(my_age)}")
print(f"Type of pi_value: {type(pi_value)}")
print(f"Type of user_name: {type(user_name)}")
print(f"Type of is_learning: {type(is_learning)}")
print(f"Type of database_result: {type(database_result)}")

## Dynamic Typing in Action ##
print("\n--- Dynamic Typing ---")
print(f"{my_age} is {type(my_age)}")
print(f"{user_name} is {type(user_name)}")
print(f"{is_learning} is {type(is_learning)}")

## Type Conversion (Casting) ##
print("\n--- Type Conversion ---")
my_age = 26
my_age = int(my_age)
print(f"After int(): {my_age} ({type(my_age)})")

# Converting int to float
my_age = float(my_age)
print(f"After float(): {my_age} ({type(my_age)})")

# Converting float to string
my_age = str(my_age)
print(f"After str(): {my_age} ({type(my_age)})")

# Converting to boolean
my_age = ""  # Empty string
my_age = bool(my_age)
print(f"After bool(''): {my_age} ({type(my_age)})")


# ============================================================================
# PRACTICE TASKS
# ============================================================================

print("\n" + "=" * 70)
print("PRACTICE TASKS")
print("=" * 70)

# Task 1: Personal Details
print("\n--- Task 1: Personal Details ---")
first_name = "Akanksha"
last_name = "Sharma"
current_year = 2025
birth_year = 1998
approx_age = current_year - birth_year
print(f"My approximate age is {approx_age}")
print(f"My name is {first_name} {last_name}, and I am {approx_age} years old")

# Task 2: Product Information
print("\n--- Task 2: Product Information ---")
product_name = "Dabur"
product_price = 30.69
quantity_in_stock = 1000
print(f"Product Name: {product_name} (Type: {type(product_name).__name__})")
print(f"Product Price: ${product_price} (Type: {type(product_price).__name__})")
print(f"Quantity in Stock: {quantity_in_stock} (Type: {type(quantity_in_stock).__name__})")

# Task 3: Temperature Conversion
print("\n--- Task 3: Temperature Conversion ---")
temp_celsius = 24.5
temp_fahrenheit = ((temp_celsius * 9/5) + 32)
print(f"{temp_celsius}°C is {temp_fahrenheit}°F")

# Task 4: String Manipulation and Info
print("\n--- Task 4: Book Information ---")
favorite_book = "Atomic Habits"
published_year = 2015
is_fiction = False
print(f"My favorite book, '{favorite_book}' (published in {published_year}), "
      f"is a work of fiction: {is_fiction}")
print(f"Types: {type(favorite_book).__name__}, {type(published_year).__name__}, "
      f"{type(is_fiction).__name__}")

# Task 6: Boolean Flags
print("\n--- Task 6: Boolean Flags ---")
is_logged_in = True
has_admin_privileges = True
is_weekend = False
print(f"Logged in: {is_logged_in}")
print(f"Admin privileges: {has_admin_privileges}")
print(f"Is weekend: {is_weekend}")

if (is_logged_in and has_admin_privileges):
    print("✅ Admin access granted")
else:
    print("❌ Access denied")

# Task 7: Reassignment and Type Change
print("\n--- Task 7: Dynamic Typing Demo ---")
item_code = 1023
print(f"Item code: {item_code} (Type: {type(item_code).__name__})")

item_code = "A101-X"
print(f"Item code: {item_code} (Type: {type(item_code).__name__})")

# Task 8: Simple Quotation
print("\n--- Task 8: Quote Formatting ---")
quote = "Old is Gold"
author = "Akanksha Sharma"
print(f"'{quote}' - {author}")


# ============================================================================
# PART 2: PRICE CLEANER & DISCOUNT CHALLENGE
# ============================================================================

print("\n" + "=" * 70)
print("PART 2: PRICE CLEANER & DISCOUNT CHALLENGE")
print("=" * 70)

prices = ["$10.50", "20.25", "N/A", "$5.00", "free", "15"]
print(f"\nOriginal prices: {prices}")


# ============================================================================
# Your Original Approach
# ============================================================================
print("\n" + "=" * 70)
print("Your Original Approach")
print("=" * 70)

# Step 1: Remove dollar signs (modifies original list)
prices_copy = prices.copy()  # Work on a copy
for i in range(len(prices_copy)):
    prices_copy[i] = prices_copy[i].replace("$", "")
print(f"\nAfter removing $: {prices_copy}")

# Step 2: Filter valid prices
filter_data = []
for item in prices_copy:
    if item != "N/A" and item != "free":
        filter_data.append(float(item))
print(f"After filtering: {filter_data}")

# Step 3: Apply discount (FIXED VERSION)
print("\nApplying 10% discount to prices > $10:")
discounted_prices = []
for price in filter_data:
    if price > 10:
        discounted = price * 0.9
        discounted_prices.append(discounted)
        print(f"  ${price:.2f} -> ${discounted:.2f} (10% off)")
    else:
        discounted_prices.append(price)
        print(f"  ${price:.2f} (no discount)")

print(f"\nFinal prices: {discounted_prices}")


# ============================================================================
# Solution 1: Traditional Loop with Try-Except (Most Robust)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 1: Traditional Loop with Try-Except")
print("=" * 70)

clean_prices = []
skipped = []

for price in prices:
    try:
        # Remove dollar sign
        clean_value = price.replace("$", "")
        
        # Convert to float
        price_float = float(clean_value)
        
        # Apply 10% discount if over $10
        if price_float > 10:
            price_float = price_float * 0.9
        
        clean_prices.append(price_float)
    except ValueError:
        # Skip invalid values
        skipped.append(price)
        continue

print(f"\nClean prices: {clean_prices}")
print(f"Skipped items: {skipped}")


# ============================================================================
# Solution 2: List Comprehension with Helper Function
# ============================================================================
print("\n" + "=" * 70)
print("Solution 2: List Comprehension with Helper Function")
print("=" * 70)

def clean_price(price_str):
    """Clean and process a price string."""
    try:
        # Remove dollar sign and convert to float
        price = float(price_str.replace("$", ""))
        
        # Apply discount if over $10
        return price * 0.9 if price > 10 else price
    except ValueError:
        return None

# Process all prices, then filter out None values
results = [clean_price(p) for p in prices]
clean_prices_v2 = [r for r in results if r is not None]

print(f"\nClean prices: {clean_prices_v2}")


# ============================================================================
# Solution 3: Comprehensive Function with Statistics
# ============================================================================
print("\n" + "=" * 70)
print("Solution 3: Comprehensive Solution with Statistics")
print("=" * 70)

def clean_and_discount_prices(prices, discount_threshold=10, discount_rate=0.1):
    """
    Clean price strings and apply discount to qualifying items.
    
    Args:
        prices (list): List of price strings
        discount_threshold (float): Minimum price for discount
        discount_rate (float): Discount percentage (0.1 = 10%)
    
    Returns:
        dict: Contains clean_prices, skipped_items, and statistics
    """
    clean_prices = []
    skipped_items = []
    original_total = 0
    discounted_total = 0
    discount_applied_count = 0
    
    for price in prices:
        try:
            # Remove dollar sign and strip whitespace
            clean_value = price.replace("$", "").strip()
            
            # Convert to float
            price_float = float(clean_value)
            original_total += price_float
            
            # Apply discount if applicable
            if price_float > discount_threshold:
                price_float = price_float * (1 - discount_rate)
                discount_applied_count += 1
            
            clean_prices.append(round(price_float, 2))
            discounted_total += price_float
        except ValueError:
            skipped_items.append(price)
    
    return {
        'clean_prices': clean_prices,
        'skipped_items': skipped_items,
        'original_total': round(original_total, 2),
        'discounted_total': round(discounted_total, 2),
        'total_savings': round(original_total - discounted_total, 2),
        'discount_applied_count': discount_applied_count,
        'valid_items': len(clean_prices),
        'invalid_items': len(skipped_items)
    }

result = clean_and_discount_prices(prices)

print(f"\nClean prices: {result['clean_prices']}")
print(f"Skipped items: {result['skipped_items']}")
print(f"\nStatistics:")
print(f"  Valid items: {result['valid_items']}")
print(f"  Invalid items: {result['invalid_items']}")
print(f"  Discounts applied: {result['discount_applied_count']}")
print(f"  Original total: ${result['original_total']:.2f}")
print(f"  Final total: ${result['discounted_total']:.2f}")
print(f"  Total savings: ${result['total_savings']:.2f}")


# ============================================================================
# Bonus: Advanced Features
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Advanced Features")
print("=" * 70)

# Tiered discount system
def apply_tiered_discount(price):
    """Apply discount based on price tier."""
    if price >= 50:
        return price * 0.7, 30  # 30% off
    elif price >= 20:
        return price * 0.8, 20  # 20% off
    elif price > 10:
        return price * 0.9, 10  # 10% off
    return price, 0  # No discount

print("\n--- Tiered Discount System ---")
test_prices = [5, 15, 25, 55]
for price in test_prices:
    discounted, percent = apply_tiered_discount(price)
    if percent > 0:
        print(f"${price:.2f} -> ${discounted:.2f} ({percent}% off)")
    else:
        print(f"${price:.2f} (no discount)")


# Add tax calculation
def process_price_with_tax(price_str, discount_threshold=10, 
                           discount_rate=0.1, tax_rate=0.08):
    """Process price with discount and tax."""
    try:
        price = float(price_str.replace("$", ""))
        
        # Apply discount
        if price > discount_threshold:
            price = price * (1 - discount_rate)
        
        # Add tax
        final_price = price * (1 + tax_rate)
        
        return round(final_price, 2)
    except ValueError:
        return None

print("\n--- With Tax (8%) ---")
for price_str in prices:
    result = process_price_with_tax(price_str)
    if result:
        print(f"{price_str:>8} -> ${result:.2f} (after discount & tax)")


# Format with currency
print("\n--- Formatted with Currency ---")
formatted_prices = [f"${price:.2f}" for price in clean_prices]
print(f"Formatted: {formatted_prices}")


# ============================================================================
# Testing
# ============================================================================
print("\n" + "=" * 70)
print("Testing")
print("=" * 70)

test_cases = [
    (["$10.50"], "Should apply discount (>$10)"),
    (["$5.00"], "Should not apply discount (<$10)"),
    (["N/A"], "Should skip invalid"),
    (["20.25"], "Should work without $ sign"),
]

print("\nRunning test cases:")
for test_input, description in test_cases:
    result = clean_and_discount_prices(test_input)
    print(f"✓ {description}")
    print(f"  Input: {test_input}")
    print(f"  Output: {result['clean_prices']}")


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)

print(f"""
Part 1 - Data Types Covered:
✓ int, float, str, bool, NoneType
✓ Type conversion (casting)
✓ F-strings for formatting
✓ Dynamic typing
✓ Boolean logic

Part 2 - Challenge Completed:
✓ String cleaning (remove $)
✓ Type conversion (str to float)
✓ Error handling (try-except)
✓ Conditional logic (discount)
✓ Data validation (skip invalid)

Original prices: {prices}
Clean prices: {clean_prices}
Skipped: {skipped}

Total savings: ${result['total_savings']:.2f}
""")

print("=" * 70)
print("✅ Day 4 completed!")
print("=" * 70)
