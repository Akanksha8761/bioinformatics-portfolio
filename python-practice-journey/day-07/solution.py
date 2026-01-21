"""
Day 7: The "Flexible Sum Calculator" Challenge
===============================================

The Scenario:
You are building a math utility library. You need a function that can calculate 
the sum of numbers, but the user might pass in 2 numbers, 10 numbers, or even 0 numbers.

The Task:
Write a function called sum_even_numbers:
    1. It must accept any number of positional arguments (using *args).
    2. It should filter out the odd numbers and return the sum of only the even numbers.
    3. If no numbers are passed, it should return 0.
    4. If a non-integer is passed (like a string or float), the function should 
       simply ignore it and continue (don't let it crash).
"""

print("=" * 70)
print("Day 7: Flexible Sum Calculator Challenge")
print("=" * 70)


# ============================================================================
# Understanding *args
# ============================================================================
print("\n" + "=" * 70)
print("Understanding *args")
print("=" * 70)

def demo_args(*args):
    """Demonstrate how *args works."""
    print(f"Type: {type(args)}")
    print(f"Args: {args}")
    print(f"Length: {len(args)}")
    
    print("Individual arguments:")
    for i, arg in enumerate(args):
        print(f"  arg[{i}] = {arg} (type: {type(arg).__name__})")

print("\n--- Calling with multiple arguments ---")
demo_args(1, 2, 3, "four", 5.5)

print("\n--- Calling with no arguments ---")
demo_args()

print("\n--- Calling with mixed types ---")
demo_args(42, "hello", True, None, [1, 2, 3])


# ============================================================================
# Your Original Approach (with analysis)
# ============================================================================
print("\n" + "=" * 70)
print("Your Original Approach")
print("=" * 70)

def sum_even_number_original(*args):
    """Your original implementation."""
    sum = 0  # Note: This shadows built-in sum() function
    
    for i in args:
        try:
            if i % 2 == 0:
                sum = sum + i
            elif i is None:
                return 0  # Note: This returns immediately
        except (ValueError, TypeError):
            continue
    
    return sum

print("\nTesting your original function:")
print(f"sum_even_number(2, 7, 8, 9, 5) = {sum_even_number_original(2, 7, 8, 9, 5)}")
print(f"sum_even_number(0) = {sum_even_number_original(0)}")
print(f"sum_even_number() = {sum_even_number_original()}")
print(f"sum_even_number('sd') = {sum_even_number_original('sd')}")
print(f"sum_even_number(56.55) = {sum_even_number_original(56.55)}")

print("\n✅ Your approach works!")
print("⚠️  Note: Variable name 'sum' shadows built-in sum() function")
print("⚠️  Note: 'elif i is None: return 0' exits early (better to continue)")


# ============================================================================
# Your Improved Approach
# ============================================================================
print("\n" + "=" * 70)
print("Your Improved Approach (Generator Expression)")
print("=" * 70)

def sum_even_numbers(*args):
    """Sum only even integers from variable arguments."""
    return sum(i for i in args if isinstance(i, int) and i % 2 == 0)

print("\nTesting improved function:")
print(f"sum_even_numbers(2, 7, 8, 9, 5) = {sum_even_numbers(2, 7, 8, 9, 5)}")
print(f"sum_even_numbers(0) = {sum_even_numbers(0)}")
print(f"sum_even_numbers() = {sum_even_numbers()}")
print(f"sum_even_numbers('sd') = {sum_even_numbers('sd')}")
print(f"sum_even_numbers(56.55) = {sum_even_numbers(56.55)}")

print("\n✅ Perfect! Pythonic and concise!")


# ============================================================================
# Solution 2: Traditional Loop (Corrected)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 2: Traditional Loop (Best Practice)")
print("=" * 70)

def sum_even_numbers_loop(*args):
    """Sum even numbers using traditional loop."""
    total = 0  # Better variable name (doesn't shadow sum())
    
    for num in args:
        try:
            # Check if even and add to total
            if num % 2 == 0:
                total += num
        except (ValueError, TypeError):
            # Ignore non-numeric values
            continue
    
    return total

print("\nTesting loop version:")
test_cases = [
    (2, 7, 8, 9, 5),
    (0,),
    (),
    ('sd',),
    (56.55,),
    (2, 'x', 4, None, 6, 3.5)
]

for test in test_cases:
    result = sum_even_numbers_loop(*test)
    print(f"sum_even_numbers{test} = {result}")


# ============================================================================
# Solution 3: Type Checking First
# ============================================================================
print("\n" + "=" * 70)
print("Solution 3: Type Checking Before Operation")
print("=" * 70)

def sum_even_numbers_typecheck(*args):
    """Sum even numbers with explicit type checking."""
    total = 0
    
    for num in args:
        # Type check first, then logic
        if isinstance(num, int) and not isinstance(num, bool):
            if num % 2 == 0:
                total += num
    
    return total

print("\nWhy check for bool?")
print(f"isinstance(True, int) = {isinstance(True, int)}")
print(f"isinstance(False, int) = {isinstance(False, int)}")
print(f"True % 2 = {True % 2} (odd)")
print(f"False % 2 = {False % 2} (even!)")

print("\nTesting with booleans:")
print(f"sum_even_numbers_typecheck(True, False, 2, 4) = "
      f"{sum_even_numbers_typecheck(True, False, 2, 4)}")
print("✅ Booleans correctly excluded!")


# ============================================================================
# Solution 4: Using filter()
# ============================================================================
print("\n" + "=" * 70)
print("Solution 4: Using filter() Function")
print("=" * 70)

def sum_even_numbers_filter(*args):
    """Sum even numbers using filter()."""
    # Filter for integers only
    integers = filter(
        lambda x: isinstance(x, int) and not isinstance(x, bool), 
        args
    )
    
    # Filter for even numbers and sum
    return sum(num for num in integers if num % 2 == 0)

print("\nTesting filter version:")
print(f"sum_even_numbers_filter(2, 7, 8, 9, 5) = "
      f"{sum_even_numbers_filter(2, 7, 8, 9, 5)}")
print(f"sum_even_numbers_filter(2, 'x', 4, 3.5, 6) = "
      f"{sum_even_numbers_filter(2, 'x', 4, 3.5, 6)}")


# ============================================================================
# Bonus: Advanced Variations
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Advanced Variations")
print("=" * 70)

# Variation 1: With **kwargs for options
print("\n--- With Configuration Options ---")

def sum_even_numbers_config(*args, **kwargs):
    """
    Sum even numbers with configuration options.
    
    Keyword Args:
        include_zero (bool): Whether to include 0 (default: True)
        allow_floats (bool): Whether to convert floats (default: False)
    """
    include_zero = kwargs.get('include_zero', True)
    allow_floats = kwargs.get('allow_floats', False)
    
    total = 0
    for num in args:
        # Handle floats if allowed
        if allow_floats and isinstance(num, float):
            num = int(num)
        
        # Check if integer
        if isinstance(num, int) and not isinstance(num, bool):
            # Handle zero case
            if num == 0 and not include_zero:
                continue
            
            if num % 2 == 0:
                total += num
    
    return total

print(f"sum_even_numbers_config(2, 4, 6) = "
      f"{sum_even_numbers_config(2, 4, 6)}")
print(f"sum_even_numbers_config(0, 2, 4, include_zero=False) = "
      f"{sum_even_numbers_config(0, 2, 4, include_zero=False)}")
print(f"sum_even_numbers_config(2.8, 4.2, allow_floats=True) = "
      f"{sum_even_numbers_config(2.8, 4.2, allow_floats=True)}")


# Variation 2: Return statistics
print("\n--- Return Statistics ---")

def analyze_even_numbers(*args):
    """Return detailed statistics about even numbers."""
    even_nums = [
        num for num in args
        if isinstance(num, int)
        and not isinstance(num, bool)
        and num % 2 == 0
    ]
    
    if not even_nums:
        return {
            'sum': 0,
            'count': 0,
            'average': 0,
            'min': None,
            'max': None,
            'values': []
        }
    
    return {
        'sum': sum(even_nums),
        'count': len(even_nums),
        'average': sum(even_nums) / len(even_nums),
        'min': min(even_nums),
        'max': max(even_nums),
        'values': even_nums
    }

result = analyze_even_numbers(1, 2, 3, 4, 5, 6, 'x', 7.5)
print("Statistics for (1, 2, 3, 4, 5, 6, 'x', 7.5):")
for key, value in result.items():
    print(f"  {key}: {value}")


# Variation 3: With logging
print("\n--- With Verbose Logging ---")

def sum_even_numbers_verbose(*args, verbose=False):
    """Sum even numbers with optional logging."""
    total = 0
    processed = 0
    ignored = []
    
    for num in args:
        if isinstance(num, int) and not isinstance(num, bool):
            if num % 2 == 0:
                total += num
                processed += 1
                if verbose:
                    print(f"  ✓ Added: {num}, Running total: {total}")
            elif verbose:
                print(f"  ○ Skipped (odd): {num}")
        else:
            ignored.append((num, type(num).__name__))
            if verbose:
                print(f"  ✗ Ignored ({type(num).__name__}): {num}")
    
    if verbose:
        print(f"\n  Summary: {processed} even numbers, {len(ignored)} ignored")
    
    return total

print("\nProcessing with verbose=True:")
result = sum_even_numbers_verbose(2, 'x', 7, 4, 3.5, 6, verbose=True)
print(f"\nFinal result: {result}")


# Variation 4: Sum odd numbers
print("\n--- Sum Odd Numbers Variant ---")

def sum_odd_numbers(*args):
    """Sum only odd integers from variable arguments."""
    return sum(
        num for num in args
        if isinstance(num, int)
        and not isinstance(num, bool)
        and num % 2 != 0
    )

print(f"sum_odd_numbers(1, 2, 3, 4, 5) = {sum_odd_numbers(1, 2, 3, 4, 5)}")
print(f"sum_odd_numbers(2, 4, 6, 8) = {sum_odd_numbers(2, 4, 6, 8)}")


# Variation 5: Support nested iterables
print("\n--- Support Nested Iterables ---")

def sum_even_numbers_nested(*args):
    """Sum even numbers, flattening nested iterables."""
    def flatten(items):
        for item in items:
            if isinstance(item, (list, tuple, range)):
                yield from flatten(item)
            else:
                yield item
    
    return sum(
        num for num in flatten(args)
        if isinstance(num, int) 
        and not isinstance(num, bool)
        and num % 2 == 0
    )

print(f"sum_even_numbers_nested(2, [4, 6], (8, 10)) = "
      f"{sum_even_numbers_nested(2, [4, 6], (8, 10))}")
print(f"sum_even_numbers_nested(range(0, 11)) = "
      f"{sum_even_numbers_nested(range(0, 11))}")


# ============================================================================
# Common Mistakes Demonstration
# ============================================================================
print("\n" + "=" * 70)
print("Common Mistakes to Avoid")
print("=" * 70)

print("\n--- Mistake 1: Shadowing built-in sum() ---")
def bad_example1(*args):
    sum = 0  # Shadows built-in!
    # Now sum() function is not available in this scope
    return sum

print("This shadows the built-in sum() function")
print("Use 'total', 'result', or 'accumulator' instead")

print("\n--- Mistake 2: Not excluding bool ---")
def bad_example2(*args):
    return sum(i for i in args if isinstance(i, int) and i % 2 == 0)

print(f"bad_example2(False, 2, 4) = {bad_example2(False, 2, 4)}")
print("⚠️  False (0) is counted as even!")

print("\n--- Mistake 3: Early return instead of continue ---")
def bad_example3(*args):
    total = 0
    for num in args:
        if num is None:
            return 0  # Exits entire function!
        if isinstance(num, int) and num % 2 == 0:
            total += num
    return total

print(f"bad_example3(2, None, 4, 6) = {bad_example3(2, None, 4, 6)}")
print("⚠️  Returns 2 (exits early at None)")


# ============================================================================
# Comprehensive Testing
# ============================================================================
print("\n" + "=" * 70)
print("Comprehensive Testing")
print("=" * 70)

def test_sum_even_numbers():
    """Test all edge cases."""
    tests = [
        ((2, 7, 8, 9, 5), 10, "Mixed numbers"),
        ((), 0, "No arguments"),
        ((0,), 0, "Single zero"),
        (('sd',), 0, "String"),
        ((56.55,), 0, "Float"),
        ((2, 'x', 4, None, 6, 3.5), 12, "Mixed types"),
        ((1, 3, 5, 7, 9), 0, "All odd"),
        ((2, 4, 6, 8), 20, "All even"),
        ((-4, -2, 0, 2, 4), 0, "Negatives"),
        ((True, False, 2, 4), 6, "With booleans"),
    ]
    
    passed = 0
    failed = 0
    
    for args, expected, description in tests:
        result = sum_even_numbers(*args)
        if result == expected:
            print(f"✅ {description}: {result}")
            passed += 1
        else:
            print(f"❌ {description}: got {result}, expected {expected}")
            failed += 1
    
    print(f"\n{'='*70}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0:
        print("🎉 All tests passed!")
    
    return failed == 0

test_sum_even_numbers()


# ============================================================================
# Performance Comparison
# ============================================================================
print("\n" + "=" * 70)
print("Performance Comparison")
print("=" * 70)

import time

# Create large test data
large_data = list(range(100000))

print("\nTesting with 100,000 numbers...")

# Test 1: Generator expression
start = time.time()
result1 = sum_even_numbers(*large_data)
time1 = time.time() - start
print(f"1. Generator expression: {time1:.4f}s - Result: {result1}")

# Test 2: Traditional loop
start = time.time()
result2 = sum_even_numbers_loop(*large_data)
time2 = time.time() - start
print(f"2. Traditional loop: {time2:.4f}s - Result: {result2}")

# Test 3: Type check first
start = time.time()
result3 = sum_even_numbers_typecheck(*large_data)
time3 = time.time() - start
print(f"3. Type check first: {time3:.4f}s - Result: {result3}")

print("\n✅ Generator expression is typically fastest!")


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)

print("""
Challenge Requirements:
✓ Accept any number of arguments (*args)
✓ Filter out odd numbers
✓ Sum only even integers
✓ Return 0 if no arguments
✓ Ignore non-integers gracefully

Your Solutions:
1. Original (try-except): Works, with minor issues
2. Improved (generator): Perfect! Pythonic and concise

Best Practice Solution:
def sum_even_numbers(*args):
    return sum(i for i in args if isinstance(i, int) and i % 2 == 0)

Key Concepts Learned:
✓ *args for variable arguments
✓ isinstance() for type checking
✓ Generator expressions for efficiency
✓ Defensive programming
✓ Avoiding variable shadowing
✓ **kwargs for optional parameters
""")

print("=" * 70)
print("✅ Day 7 completed!")
print("=" * 70)
