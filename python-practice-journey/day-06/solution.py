"""
Day 6: The "Employee List Flattener" Challenge
===============================================

The Scenario:
You have a list representing different departments in a company. 
Each department is a list of employee names.

The Task:
    1. Flatten this list into a single list called all_employees.
    2. Filter: Only include employees whose names have more than 4 letters.
    3. Format: Make sure all names are UPPERCASE.

The Constraint:
Do this using a single List Comprehension with a nested loop inside it.
"""

from itertools import chain

# Input data
departments = [
    ["Alice", "Bob"],
    ["Charlie", "David", "Eve"],
    ["Frank"]
]

print("=" * 70)
print("Day 6: Employee List Flattener Challenge")
print("=" * 70)
print(f"\nDepartments:")
for i, dept in enumerate(departments, 1):
    print(f"  Department {i}: {dept}")


# ============================================================================
# Your Original Approach - Step by Step
# ============================================================================
print("\n" + "=" * 70)
print("Your Original Approach - Step by Step")
print("=" * 70)

# Step 1: Flatten the list
print("\n--- Step 1: Flattening ---")
all_employees = []
for i in departments:
    for j in i:
        print(f"  Processing: {j}")
        all_employees.append(j)

print(f"\nFlattened list: {all_employees}")
print(f"Type: {type(all_employees)}")

# Step 2: Filter and transform (your original - just prints)
print("\n--- Step 2: Filter & Transform (original - prints only) ---")
for i in all_employees:
    if len(i) > 4:
        print(f"  {i} -> {i.upper()}")

print("\n⚠️  Note: This only prints, doesn't create a new list")

# Step 3: Your final solution - Perfect! ✅
print("\n--- Step 3: Your Final Solution (One-Liner) ✅ ---")
all_employees_final = [j.upper() for i in departments for j in i if len(j) > 4]
print(f"\nResult: {all_employees_final}")
print("✅ Perfect! Meets all requirements in one line!")


# ============================================================================
# Understanding Nested List Comprehensions
# ============================================================================
print("\n" + "=" * 70)
print("Understanding Nested List Comprehensions")
print("=" * 70)

# Breaking it down step by step
print("\n--- Step-by-Step Breakdown ---")

# Step 1: Just flatten (no filter, no transform)
step1 = [employee for dept in departments for employee in dept]
print(f"\nStep 1 - Flatten only:")
print(f"  {step1}")

# Step 2: Flatten + Filter
step2 = [employee for dept in departments for employee in dept if len(employee) > 4]
print(f"\nStep 2 - Flatten + Filter (len > 4):")
print(f"  {step2}")

# Step 3: Flatten + Filter + Transform
step3 = [employee.upper() for dept in departments for employee in dept if len(employee) > 4]
print(f"\nStep 3 - Flatten + Filter + Transform (UPPERCASE):")
print(f"  {step3}")


# ============================================================================
# Execution Order Visualization
# ============================================================================
print("\n" + "=" * 70)
print("Execution Order Visualization")
print("=" * 70)

print("\nHow the nested comprehension executes:")
print("-" * 70)

for dept_idx, department in enumerate(departments, 1):
    print(f"\nDepartment {dept_idx}: {department}")
    for employee in department:
        passes_filter = len(employee) > 4
        status = "✓ INCLUDE" if passes_filter else "✗ SKIP"
        result = employee.upper() if passes_filter else "N/A"
        print(f"  {employee:10} (len={len(employee)}) -> {status:10} -> {result}")


# ============================================================================
# Solution 1: Single List Comprehension (Challenge Answer)
# ============================================================================
print("\n" + "=" * 70)
print("Solution 1: Single List Comprehension ✅")
print("=" * 70)

all_employees = [
    employee.upper() 
    for department in departments 
    for employee in department 
    if len(employee) > 4
]

print(f"\nResult: {all_employees}")
print(f"Count: {len(all_employees)} employees")


# ============================================================================
# Solution 2: Traditional Nested Loops
# ============================================================================
print("\n" + "=" * 70)
print("Solution 2: Traditional Nested Loops")
print("=" * 70)

all_employees_loop = []
for department in departments:
    for employee in department:
        if len(employee) > 4:
            all_employees_loop.append(employee.upper())

print(f"\nResult: {all_employees_loop}")


# ============================================================================
# Solution 3: Using itertools.chain
# ============================================================================
print("\n" + "=" * 70)
print("Solution 3: Using itertools.chain")
print("=" * 70)

# Flatten using chain
flattened = chain.from_iterable(departments)

# Filter and transform
all_employees_chain = [
    emp.upper() 
    for emp in flattened 
    if len(emp) > 4
]

print(f"\nResult: {all_employees_chain}")
print("✅ Good for large datasets (memory efficient)")


# ============================================================================
# Solution 4: Using sum() for Flattening
# ============================================================================
print("\n" + "=" * 70)
print("Solution 4: Using sum() for Flattening")
print("=" * 70)

# Flatten using sum (clever but slow for large lists)
flattened_sum = sum(departments, [])
print(f"\nFlattened with sum(): {flattened_sum}")

# Filter and transform
all_employees_sum = [
    emp.upper() 
    for emp in flattened_sum 
    if len(emp) > 4
]

print(f"Result: {all_employees_sum}")
print("⚠️  Warning: O(n²) performance - avoid for large lists!")


# ============================================================================
# Bonus: Advanced Variations
# ============================================================================
print("\n" + "=" * 70)
print("Bonus: Advanced Variations")
print("=" * 70)

# Variation 1: Include department index
print("\n--- Include Department Number ---")
with_dept = [
    (i + 1, emp.upper()) 
    for i, dept in enumerate(departments) 
    for emp in dept 
    if len(emp) > 4
]
print("Result: (dept_num, employee)")
for dept_num, emp in with_dept:
    print(f"  Department {dept_num}: {emp}")


# Variation 2: Filter by first letter
print("\n--- Filter by First Letter (A or C) ---")
filtered_by_letter = [
    emp.upper() 
    for dept in departments 
    for emp in dept 
    if len(emp) > 4 and emp[0] in ['A', 'C']
]
print(f"Result: {filtered_by_letter}")


# Variation 3: Create department dictionary
print("\n--- Department Dictionary ---")
dept_dict = {
    f"Dept {i + 1}": [emp.upper() for emp in dept if len(emp) > 4]
    for i, dept in enumerate(departments)
}
print("Department → Employees mapping:")
for dept_name, employees in dept_dict.items():
    print(f"  {dept_name}: {employees}")


# Variation 4: Employee info with details
print("\n--- Employee Information Objects ---")
employee_info = [
    {
        'name': emp.upper(),
        'department': i + 1,
        'name_length': len(emp),
        'first_letter': emp[0]
    }
    for i, dept in enumerate(departments)
    for emp in dept
    if len(emp) > 4
]

print("Detailed employee information:")
for info in employee_info:
    print(f"  {info['name']:10} - Dept {info['department']}, "
          f"Length: {info['name_length']}, "
          f"Starts with: {info['first_letter']}")


# Variation 5: Count by department
print("\n--- Employee Count per Department ---")
dept_counts = [
    (f"Dept {i + 1}", len([e for e in dept if len(e) > 4]))
    for i, dept in enumerate(departments)
]

print("Department employee counts (names > 4 letters):")
total = 0
for dept_name, count in dept_counts:
    print(f"  {dept_name}: {count} employees")
    total += count
print(f"  Total: {total} employees")


# ============================================================================
# Handling Edge Cases
# ============================================================================
print("\n" + "=" * 70)
print("Handling Edge Cases")
print("=" * 70)

# Edge Case 1: Empty departments
print("\n--- Empty Departments ---")
departments_with_empty = [
    ["Alice", "Bob"],
    [],  # Empty department
    ["Charlie", "David"],
    ["Frank"]
]

result_with_empty = [
    emp.upper() 
    for dept in departments_with_empty 
    for emp in dept 
    if len(emp) > 4
]
print(f"Input: {departments_with_empty}")
print(f"Result: {result_with_empty}")
print("✅ Empty departments handled gracefully")

# Edge Case 2: All names too short
print("\n--- All Names Too Short ---")
short_names = [["Bob", "Eve"], ["Sam", "Joe"]]
result_short = [
    emp.upper() 
    for dept in short_names 
    for emp in dept 
    if len(emp) > 4
]
print(f"Input: {short_names}")
print(f"Result: {result_short}")

# Edge Case 3: Single department
print("\n--- Single Department ---")
single_dept = [["Alice", "Charlie", "Frank"]]
result_single = [
    emp.upper() 
    for dept in single_dept 
    for emp in dept 
    if len(emp) > 4
]
print(f"Input: {single_dept}")
print(f"Result: {result_single}")


# ============================================================================
# Performance Comparison
# ============================================================================
print("\n" + "=" * 70)
print("Performance Comparison")
print("=" * 70)

import time

# Create larger test data
large_departments = [
    [f"Employee{i}" for i in range(100)]
    for _ in range(100)
]

print("\nTesting with 100 departments, 100 employees each (10,000 total)")

# Test 1: List comprehension
start = time.time()
result1 = [emp.upper() for dept in large_departments for emp in dept if len(emp) > 4]
time1 = time.time() - start
print(f"\n1. List Comprehension: {time1:.4f}s - {len(result1)} results")

# Test 2: Traditional loops
start = time.time()
result2 = []
for dept in large_departments:
    for emp in dept:
        if len(emp) > 4:
            result2.append(emp.upper())
time2 = time.time() - start
print(f"2. Traditional Loops: {time2:.4f}s - {len(result2)} results")

# Test 3: itertools.chain
start = time.time()
result3 = [emp.upper() for emp in chain.from_iterable(large_departments) if len(emp) > 4]
time3 = time.time() - start
print(f"3. itertools.chain: {time3:.4f}s - {len(result3)} results")

print("\n✅ List comprehension is typically fastest!")


# ============================================================================
# Generator Expression (Memory Efficient)
# ============================================================================
print("\n" + "=" * 70)
print("Generator Expression (Memory Efficient)")
print("=" * 70)

# Generator doesn't create list in memory
employee_gen = (
    emp.upper() 
    for dept in departments 
    for emp in dept 
    if len(emp) > 4
)

print(f"\nGenerator object: {employee_gen}")
print("Processing one at a time:")
for i, emp in enumerate(employee_gen, 1):
    print(f"  {i}. {emp}")


# ============================================================================
# Recursive Flattening (Bonus)
# ============================================================================
print("\n" + "=" * 70)
print("Recursive Flattening (Arbitrary Depth)")
print("=" * 70)

def flatten_recursive(nested_list):
    """Flatten a list of arbitrary depth."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result

# Deep nesting
deep_nested = [
    ["Alice", ["Bob", "Charlie"]], 
    [["David"], "Eve"],
    "Frank"
]

print(f"\nDeeply nested: {deep_nested}")
flattened_deep = flatten_recursive(deep_nested)
print(f"Flattened: {flattened_deep}")

# Apply filter and transform
result_deep = [emp.upper() for emp in flattened_deep if len(emp) > 4]
print(f"Filtered & transformed: {result_deep}")


# ============================================================================
# Testing
# ============================================================================
print("\n" + "=" * 70)
print("Testing")
print("=" * 70)

test_cases = [
    {
        'input': [["Alice", "Bob"], ["Charlie", "David", "Eve"], ["Frank"]],
        'expected': ['ALICE', 'CHARLIE', 'DAVID', 'FRANK'],
        'description': 'Normal case'
    },
    {
        'input': [["Bob", "Eve"]],
        'expected': [],
        'description': 'All names <= 4 letters'
    },
    {
        'input': [[]],
        'expected': [],
        'description': 'Empty department'
    },
    {
        'input': [["Alice"], ["Frank"], ["Charlie"]],
        'expected': ['ALICE', 'FRANK', 'CHARLIE'],
        'description': 'Single employee per department'
    }
]

print("\nRunning test cases:")
for test in test_cases:
    result = [
        emp.upper() 
        for dept in test['input'] 
        for emp in dept 
        if len(emp) > 4
    ]
    
    status = "✅ PASS" if result == test['expected'] else "❌ FAIL"
    print(f"{status}: {test['description']}")
    if result != test['expected']:
        print(f"  Expected: {test['expected']}")
        print(f"  Got: {result}")


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 70)
print("Summary")
print("=" * 70)

print(f"""
Challenge Requirements:
✓ Flatten nested list
✓ Filter names with more than 4 letters
✓ Convert to UPPERCASE
✓ Use single list comprehension with nested loop

Original data:
  Departments: {departments}

Final result:
  {all_employees}

Key concepts learned:
✓ Nested list comprehensions
✓ List flattening techniques
✓ Nested loop execution order
✓ Filtering with multiple conditions
✓ String transformations
✓ Generator expressions
✓ Performance optimization

Your one-liner solution:
all_employees = [j.upper() for i in departments for j in i if len(j) > 4]
""")

print("=" * 70)
print("✅ Day 6 completed! (January 19, 2026)")
print("=" * 70)
