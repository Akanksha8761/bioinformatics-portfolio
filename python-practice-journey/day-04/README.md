# Day 4: The "Price Cleaner & Discount Calculator" Challenge

## 🎯 Challenge Description

### The Scenario
You have a list of prices as strings. Some have dollar signs, some are missing, and some are invalid "N/A" strings. This is very common when reading data from Excel or a database.

```python
prices = ["$10.50", "20.25", "N/A", "$5.00", "free", "15"]
```

### The Task
Create a new list called `clean_prices` that:
1. Removes the `$` sign if present
2. Converts the value to a float
3. Skips any value that cannot be converted to a number (like "N/A" or "free")
4. **Bonus**: If the price is over $10, apply a 10% discount to the float value

## 📚 Concepts Covered

### Core Concepts
- **Data Types**: int, float, str, bool, NoneType
- **Type Conversion**: `int()`, `float()`, `str()`, `bool()`
- **String Methods**: `.replace()`, `.strip()`, `.isdigit()`
- **Error Handling**: `try-except` blocks
- **List Comprehensions**: Advanced filtering and transformation
- **F-strings**: Modern string formatting
- **Dynamic Typing**: Variable reassignment with different types

### Additional Topics
- Input validation
- Data cleaning and preprocessing
- Conditional logic in loops
- Exception handling for robust code

## 💡 Solution Approaches

### Approach 1: Traditional Loop with Try-Except (Most Robust)
```python
prices = ["$10.50", "20.25", "N/A", "$5.00", "free", "15"]

clean_prices = []
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
        continue

print(clean_prices)
```

**Output:**
```python
[9.45, 20.25, 4.5, 13.5]
```

### Approach 2: List Comprehension with Helper Function
```python
def clean_price(price_str):
    """Clean and process a price string."""
    try:
        # Remove dollar sign and convert to float
        price = float(price_str.replace("$", ""))
        
        # Apply discount if over $10
        return price * 0.9 if price > 10 else price
    except ValueError:
        return None

# Filter out None values
clean_prices = [clean_price(p) for p in prices if clean_price(p) is not None]
print(clean_prices)
```

### Approach 3: Generator Expression (Memory Efficient)
```python
def process_price(price_str):
    """Process a single price string."""
    try:
        price = float(price_str.replace("$", ""))
        return price * 0.9 if price > 10 else price
    except ValueError:
        return None

# Use filter to remove None values
clean_prices = list(filter(lambda x: x is not None, 
                          (process_price(p) for p in prices)))
```

### Approach 4: Using Regular Expressions (Advanced)
```python
import re

clean_prices = []
for price in prices:
    # Extract numeric values (including decimals)
    match = re.search(r'\d+\.?\d*', price)
    if match:
        price_float = float(match.group())
        # Apply discount if over $10
        final_price = price_float * 0.9 if price_float > 10 else price_float
        clean_prices.append(final_price)

print(clean_prices)
```

### Approach 5: Comprehensive Solution with Logging
```python
def clean_and_discount_prices(prices, discount_threshold=10, discount_rate=0.1):
    """
    Clean price strings and apply discount to qualifying items.
    
    Args:
        prices (list): List of price strings
        discount_threshold (float): Minimum price for discount
        discount_rate (float): Discount percentage (0.1 = 10%)
    
    Returns:
        tuple: (clean_prices, skipped_items)
    """
    clean_prices = []
    skipped_items = []
    
    for price in prices:
        try:
            # Remove dollar sign and strip whitespace
            clean_value = price.replace("$", "").strip()
            
            # Convert to float
            price_float = float(clean_value)
            
            # Apply discount if applicable
            if price_float > discount_threshold:
                price_float = price_float * (1 - discount_rate)
            
            clean_prices.append(price_float)
        except ValueError:
            skipped_items.append(price)
    
    return clean_prices, skipped_items

clean_prices, skipped = clean_and_discount_prices(prices)
print(f"Clean prices: {clean_prices}")
print(f"Skipped items: {skipped}")
```

## 🔍 Code Breakdown

### Your Solution Analysis:
```python
# Step 1: Remove dollar signs
i = []
for i in range(len(prices)):
    prices[i] = prices[i].replace("$", "")
# Result: ['10.50', '20.25', 'N/A', '5.00', 'free', '15']

# Step 2: Filter valid prices
filter_data = []
for i in prices:
    if i != "N/A" and i != "free":
        filter_data.append(float(i))
# Result: [10.5, 20.25, 5.0, 15.0]

# Step 3: Apply discount (but not storing results!)
for i in filter_data:
    if i > 10:
        i = i * 0.9  # This creates a new local variable
        print(i)     # Only prints, doesn't modify list
```

### ⚠️ Issue in Your Code:
The discount step creates a new local variable `i` but doesn't update the list. Here's the fix:

```python
# Better approach - update the list
for index, price in enumerate(filter_data):
    if price > 10:
        filter_data[index] = price * 0.9

# Or use list comprehension
filter_data = [price * 0.9 if price > 10 else price for price in filter_data]
```

## 🎓 Key Takeaways

### Data Type Concepts (from your practice)
1. **Dynamic Typing**: Variables can change types
2. **Type Conversion**: `int()`, `float()`, `str()`, `bool()`
3. **F-strings**: Modern way to format strings
4. **Input Validation**: Always validate user input
5. **Boolean Logic**: AND, OR conditions

### Challenge Concepts
1. **String Cleaning**: Remove unwanted characters
2. **Error Handling**: Use try-except for robustness
3. **List Mutations**: Modify lists properly with indexing
4. **Conditional Pricing**: Apply business logic to data
5. **Data Validation**: Skip invalid entries gracefully

## 🚀 Variations to Try

### Challenge Yourself:

1. **Add currency symbol back after processing**
2. **Track the total discount amount given**
3. **Create a discount tier system (10%, 20%, 30%)**
4. **Handle multiple currencies (€, £, ¥)**
5. **Add tax calculation**

### Example Solutions:

**Format with Currency:**
```python
formatted_prices = [f"${price:.2f}" for price in clean_prices]
# ['$9.45', '$20.25', '$4.50', '$13.50']
```

**Track Total Discount:**
```python
def calculate_discount_summary(prices):
    original_total = 0
    discounted_total = 0
    
    for price_str in prices:
        try:
            price = float(price_str.replace("$", ""))
            original_total += price
            
            if price > 10:
                discounted_total += price * 0.9
            else:
                discounted_total += price
        except ValueError:
            continue
    
    savings = original_total - discounted_total
    return {
        'original': original_total,
        'final': discounted_total,
        'savings': savings,
        'percent_saved': (savings / original_total * 100) if original_total > 0 else 0
    }
```

**Tiered Discount System:**
```python
def apply_tiered_discount(price):
    """Apply discount based on price tier."""
    if price >= 50:
        return price * 0.7  # 30% off
    elif price >= 20:
        return price * 0.8  # 20% off
    elif price > 10:
        return price * 0.9  # 10% off
    return price  # No discount
```

**Multi-Currency Support:**
```python
import re

def clean_multi_currency(price_str):
    """Handle multiple currency symbols."""
    # Remove all currency symbols
    currency_symbols = r'[$€£¥₹]'
    clean = re.sub(currency_symbols, '', price_str)
    
    try:
        return float(clean.strip())
    except ValueError:
        return None
```

**Add Tax Calculation:**
```python
def process_price_with_tax(price_str, tax_rate=0.08):
    """Process price with discount and tax."""
    try:
        price = float(price_str.replace("$", ""))
        
        # Apply discount
        if price > 10:
            price = price * 0.9
        
        # Add tax
        final_price = price * (1 + tax_rate)
        
        return round(final_price, 2)
    except ValueError:
        return None
```

## 📊 Performance Comparison

| Approach | Readability | Error Handling | Performance | Best For |
|----------|-------------|----------------|-------------|----------|
| Try-Except Loop | Excellent | Excellent | O(n) | Production code |
| List Comprehension | Good | Good | O(n) | Clean, concise code |
| Generator | Fair | Good | O(n) - Lazy | Large datasets |
| Regex | Fair | Good | O(n) | Complex patterns |

## 🔗 Related Topics to Explore

- Regular expressions for pattern matching
- Pandas for data cleaning (DataFrame operations)
- Decimal module for precise financial calculations
- CSV/Excel file reading with openpyxl or pandas
- Data validation libraries (cerberus, marshmallow)
- Error logging with the logging module

## 💡 Real-World Applications

- **E-commerce**: Processing product prices from various sources
- **Financial Systems**: Cleaning transaction data
- **Data Analysis**: Preparing messy datasets for analysis
- **Web Scraping**: Cleaning scraped price data
- **ETL Pipelines**: Extract, Transform, Load operations
- **API Integration**: Normalizing data from different APIs

## 🐛 Common Mistakes to Avoid

```python
# ❌ Wrong: Modifying loop variable doesn't update list
for price in prices:
    if price > 10:
        price = price * 0.9  # Only changes local variable

# ✅ Correct: Use enumerate to modify list
for i, price in enumerate(prices):
    if price > 10:
        prices[i] = price * 0.9

# ❌ Wrong: Not handling ValueError
price = float(price_str)  # Crashes on "N/A"

# ✅ Correct: Use try-except
try:
    price = float(price_str)
except ValueError:
    continue

# ❌ Wrong: Inefficient repeated function calls
clean_prices = [clean_price(p) for p in prices if clean_price(p) is not None]
# Calls clean_price() twice for each item!

# ✅ Correct: Store result once
results = [clean_price(p) for p in prices]
clean_prices = [r for r in results if r is not None]
```

## 🧪 Testing Your Solution

```python
# Test cases
test_cases = [
    (["$10.50"], [9.45]),  # Over $10, gets discount
    (["$5.00"], [5.0]),    # Under $10, no discount
    (["N/A"], []),         # Invalid, skipped
    (["20.25"], [18.225]), # No $, but still processed
    (["$15", "$5", "free", "$20"], [13.5, 5.0, 18.0])
]

def test_price_cleaner():
    for input_prices, expected in test_cases:
        result = clean_and_discount_prices(input_prices)[0]
        assert result == expected, f"Failed for {input_prices}"
        print(f"✅ Passed: {input_prices}")

test_price_cleaner()
```

---

**Date Completed:** Day 4  
**Difficulty:** ⭐⭐⭐☆☆ (Intermediate)  
**Time Spent:** ~60 minutes  
**Skills Gained:** Data cleaning, error handling, type conversion, string manipulation, business logic
