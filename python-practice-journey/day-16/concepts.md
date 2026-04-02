# Day 16: Modules - Concepts

## 📌 Core Concepts Covered

Modules are Python files containing functions, classes, and variables that can be imported and reused across multiple programs. They're essential for organizing code, promoting reusability, and building larger applications. Today we learn how to create, import, and use custom modules!

---

## 1. What is a Module?

A **module** is simply a Python file (`.py`) containing Python code that can be imported into other Python programs.

### **Why Use Modules?**
- **Code Organization**: Keep related functions together
- **Reusability**: Use the same code across multiple programs
- **Namespace Management**: Avoid naming conflicts
- **Maintainability**: Update code in one place
- **Collaboration**: Share code between team members
- **Modularity**: Break large programs into smaller pieces

### **Simple Example:**
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# main.py
import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
```

---

## 2. Creating Your First Module

Any Python file can be a module!

### **Step 1: Create the Module File**

**File: `module1.py`**
```python
# My first module

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}! Welcome to Palampur!"

def calculate(num1, num2):
    """Return sum, difference, product, quotient"""
    sum_result = num1 + num2
    sub = num1 - num2
    multi = num1 * num2
    divide = num1 / num2
    return sum_result, sub, multi, divide
```

**Key Points:**
- Module name = file name (without `.py`)
- Use descriptive names
- Include docstrings
- Group related functions together

---

## 3. Importing and Using Modules

### **Basic Import**

**File: `main_program.py`**
```python
import module1

# Use functions with module name prefix
print(module1.greet("Akanksha"))

sum_result, sub, multi, divide = module1.calculate(10, 2)
```

**Syntax:**
```python
import module_name

module_name.function_name(arguments)
```

**Key Points:**
- Must use `module_name.function_name()` syntax
- Module must be in same directory or Python path
- Import happens once (first time only)

---

## 4. The `if __name__ == "__main__":` Pattern

This special pattern allows a module to act as **both** a module AND a standalone script!

### **The Magic Variable `__name__`**

Python automatically sets `__name__`:
- When file is **run directly**: `__name__ == "__main__"`
- When file is **imported**: `__name__ == "module1"` (the module name)

### **Why Use This Pattern?**

```python
# module1.py

def greet(name):
    return f"Hello, {name}!"

# This ONLY runs when module1.py is executed directly
if __name__ == "__main__":
    print("Testing the module...")
    print(greet("Test User"))
```

**When you run `python module1.py`:**
```
Testing the module...
Hello, Test User!
```

**When you `import module1` in another file:**
```
# The if block does NOT execute!
# Only the functions are available
```

### **Benefits:**
- **Test your module** - Run it directly to test functions
- **Reuse in other programs** - Import without executing test code
- **Documentation** - Show example usage
- **Professional** - Standard Python practice

---

## 5. Different Import Styles

### **1. Standard Import**
```python
import module1

module1.greet("Alice")
```

**Pros:** Clear where function comes from  
**Cons:** Must type module name every time

### **2. Import Specific Functions**
```python
from module1 import greet

greet("Alice")  # No module prefix needed!
```

**Pros:** Shorter syntax  
**Cons:** Less clear where function is from

### **3. Import Multiple Specific Items**
```python
from module1 import greet, calculate

greet("Alice")
sum_result, sub, multi, divide = calculate(10, 5)
```

### **4. Import with Alias**
```python
import module1 as m1

m1.greet("Alice")
```

**Pros:** Short but still clear  
**Cons:** Need to remember alias

### **5. Import Everything (NOT RECOMMENDED)**
```python
from module1 import *

greet("Alice")  # Works, but...
```

**Why avoid:**
- Pollutes namespace
- Unclear where functions come from
- Can cause naming conflicts
- Hard to debug

---

## 6. Module Search Path

When you `import module_name`, Python searches in this order:

1. **Current directory** (where your script is)
2. **PYTHONPATH** environment variable directories
3. **Standard library** directories
4. **Site-packages** (installed packages)

### **Check Search Path:**
```python
import sys
print(sys.path)
```

---

## 7. Module Best Practices

### **1. Naming Conventions**
- Use lowercase names: `my_module.py` ✓
- Avoid hyphens: `my-module.py` ✗
- Avoid spaces: `my module.py` ✗
- Use underscores: `my_helper_functions.py` ✓

### **2. Module Structure**
```python
# my_module.py

"""Module docstring explaining purpose"""

# Imports at top
import math
import sys

# Constants
PI = 3.14159

# Function definitions
def function1():
    """Function docstring"""
    pass

def function2():
    """Function docstring"""
    pass

# Main execution block
if __name__ == "__main__":
    # Test code here
    pass
```

### **3. What to Put in Modules**
- **Related functions** that work together
- **Utility functions** used across projects
- **Constants** and configuration
- **Classes** (learned later)
- **Data structures** and helpers

### **4. What NOT to Put in Modules**
- **Script logic** - Put in `if __name__ == "__main__":`
- **Unrelated functions** - Keep modules focused
- **User input** - Except in main block

---

## 8. Common Module Patterns

### **Pattern 1: Utility Module**
```python
# utils.py

def is_even(num):
    """Check if number is even"""
    return num % 2 == 0

def is_odd(num):
    """Check if number is odd"""
    return num % 2 != 0

def factorial(n):
    """Calculate factorial"""
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### **Pattern 2: Calculation Module**
```python
# bio_calc.py

def gc_content(sequence):
    """Calculate GC percentage"""
    g = sequence.count('G')
    c = sequence.count('C')
    return ((g + c) / len(sequence)) * 100

def complement(sequence):
    """Return DNA complement"""
    comp = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(comp[base] for base in sequence)
```

### **Pattern 3: Data Processing Module**
```python
# data_processor.py

def clean_data(values):
    """Remove None and invalid values"""
    return [v for v in values if v is not None and v >= 0]

def normalize(values):
    """Normalize values to 0-1 range"""
    min_val = min(values)
    max_val = max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]
```

---

## 9. Module vs Script

| Aspect | Module | Script |
|--------|--------|--------|
| Purpose | Reusable code | Execute task |
| Import | Yes | No |
| `if __name__` | Has test block | Main logic |
| Functions | Many, related | Few or none |
| User Input | Only in main | Throughout |

---

## 10. Practical Example: Bioinformatics Module

### **File: `bio_tools.py`**
```python
"""Bioinformatics utility functions"""

def gc_content(sequence):
    """Calculate GC percentage in DNA sequence"""
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    return ((g_count + c_count) / total) * 100

def reverse_complement(sequence):
    """Return reverse complement of DNA sequence"""
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    sequence = sequence.upper()
    comp = ''.join(complement[base] for base in sequence)
    return comp[::-1]

def count_kmers(sequence, k=3):
    """Count all k-mers in sequence"""
    kmers = {}
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i+k]
        kmers[kmer] = kmers.get(kmer, 0) + 1
    return kmers

if __name__ == "__main__":
    # Test the module
    dna = "ATGCGATCGATCG"
    print(f"GC Content: {gc_content(dna):.2f}%")
    print(f"Reverse Complement: {reverse_complement(dna)}")
    print(f"3-mers: {count_kmers(dna, 3)}")
```

### **File: `analyze_dna.py`**
```python
import bio_tools

sequence = "ATGCGATCGATCGTAGCTAGC"

print(f"Analyzing sequence: {sequence}")
print(f"GC%: {bio_tools.gc_content(sequence):.2f}")
print(f"Rev Comp: {bio_tools.reverse_complement(sequence)}")
```

---

## 💡 Key Takeaways

1. **Modules are Python files** - Any `.py` file can be imported
2. **`import` makes code available** - Use `module.function()` syntax
3. **`if __name__ == "__main__":` is crucial** - Separates testing from importing
4. **Modules promote reusability** - Write once, use everywhere
5. **Organization matters** - Group related functions together
6. **Standard import is clearest** - `import module` then `module.function()`
7. **Avoid `import *`** - Pollutes namespace, causes confusion
8. **Use docstrings** - Document module and functions
9. **Test in main block** - Show example usage
10. **Modules are building blocks** - Foundation for larger applications

---

## 📚 Quick Reference

| Task | Syntax |
|------|--------|
| Create module | Save functions in `module.py` |
| Import module | `import module` |
| Use function | `module.function()` |
| Import specific | `from module import function` |
| Import with alias | `import module as m` |
| Test module | `if __name__ == "__main__":` |
| Check `__name__` | `print(__name__)` |

---

*Modules transform isolated scripts into reusable libraries. Master them to build professional Python applications!*
