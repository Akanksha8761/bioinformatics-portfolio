# Day 18: Exception Handling & Debugging - Concepts

## 📌 Core Concepts Covered

Exception handling is Python's way of dealing with errors gracefully. Instead of crashing, your program can catch errors, handle them, and continue running. Debugging is the process of finding and fixing errors in code. Today we master both!

---

## 1. What Are Exceptions?

**Exceptions** are errors that occur during program execution that disrupt normal flow.

### **Common Exception Types:**

| Exception | Cause | Example |
|-----------|-------|---------|
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `ValueError` | Invalid value | `int("hello")` |
| `IndexError` | Invalid index | `list[100]` |
| `KeyError` | Invalid dict key | `dict["missing"]` |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `TypeError` | Wrong type | `"text" + 5` |
| `NameError` | Variable not defined | `print(undefined)` |

### **Without Exception Handling:**
```python
num = 10 / 0  # Program CRASHES here
print("This never executes")
```

**Output:**
```
ZeroDivisionError: division by zero
# Program terminates!
```

---

## 2. The try-except Block

**Basic pattern for handling exceptions:**

```python
try:
    # Code that might cause an error
    risky_operation()
except ExceptionType:
    # Code that runs if error occurs
    handle_error()
```

### **Example:**
```python
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
print("Program continues!")
```

**Output:**
```
Cannot divide by zero!
Program continues!
```

**Key Points:**
- Code in `try` block is executed
- If error occurs, jumps to `except` block
- Program continues after exception is handled
- Without `try-except`, program would crash

---

## 3. Catching Multiple Exceptions

### **Method 1: Separate except Blocks**
```python
try:
    # Risky code
    value = int(input())
    result = 10 / value
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### **Method 2: Tuple of Exceptions**
```python
try:
    # Risky code
    operation()
except (ValueError, TypeError, KeyError):
    print("One of several errors occurred!")
```

### **Method 3: Catch All (NOT RECOMMENDED)**
```python
try:
    risky_operation()
except Exception:  # Catches everything (too broad!)
    print("Something went wrong!")
```

**Best Practice:** Catch specific exceptions!

---

## 4. The else Block

**`else` block runs ONLY if NO exception occurred:**

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # Runs only if division succeeded
    print(f"Result: {result}")
```

**Flow:**
- Try block succeeds → else runs
- Try block fails → except runs, else skipped

**Use Case:**
```python
try:
    file = open('data.txt', 'r')
except FileNotFoundError:
    print("File not found!")
else:
    # File opened successfully
    data = file.read()
    file.close()
```

---

## 5. The finally Block

**`finally` block ALWAYS runs, whether error occurred or not:**

```python
try:
    risky_operation()
except SomeError:
    print("Error handled")
finally:
    print("This ALWAYS executes")
    cleanup_resources()
```

### **Common Use: Resource Cleanup**
```python
file = None
try:
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    if file:
        file.close()  # Always close file
        print("File closed")
```

**Flow Chart:**
```
try → success → else → finally
try → error → except → finally
```

---

## 6. Complete Exception Handling Pattern

```python
try:
    # Risky code
    result = perform_operation()
except SpecificError as e:
    # Handle specific error
    print(f"Error: {e}")
else:
    # Runs if no error
    print(f"Success: {result}")
finally:
    # Always runs
    cleanup()
```

**Example:**
```python
try:
    num = int(input("Enter number: "))
    result = 100 / num
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Operation complete")
```

---

## 7. Accessing Exception Information

**Capture exception object with `as`:**

```python
try:
    num = int("hello")
except ValueError as e:
    print(f"Error message: {e}")
    print(f"Error type: {type(e)}")
```

**Output:**
```
Error message: invalid literal for int() with base 10: 'hello'
Error type: <class 'ValueError'>
```

---

## 8. Raising Exceptions

**Use `raise` to trigger exceptions manually:**

### **Raise with Message:**
```python
def process_methylation(value):
    if not (0 <= value <= 1):
        raise ValueError(f"Value {value} out of range (0-1)")
    return value * 100
```

### **Re-raise Caught Exception:**
```python
try:
    risky_operation()
except ValueError:
    print("Logging error...")
    raise  # Re-raises the same exception
```

### **Raise Different Exception:**
```python
try:
    data = risky_read()
except IOError:
    raise RuntimeError("Failed to read data")
```

---

## 9. Common Exception Handling Patterns

### **Pattern 1: Safe Division**
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # or None, or raise with message
```

### **Pattern 2: Safe Conversion**
```python
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None
```

### **Pattern 3: Safe File Reading**
```python
def read_file_safe(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return ""
```

### **Pattern 4: Validate Input**
```python
def process_score(score):
    if not (0 <= score <= 100):
        raise ValueError("Score must be 0-100")
    # Process valid score
```

---

## 10. Debugging Techniques

### **Technique 1: Read Tracebacks**

**Traceback shows:**
- File name
- Line number
- Function name
- Error type
- Error message

**Example:**
```
Traceback (most recent call last):
  File "script.py", line 10, in <module>
    result = divide(10, 0)
  File "script.py", line 5, in divide
    return a / b
ZeroDivisionError: division by zero
```

**Read bottom-up:**
1. Error type: `ZeroDivisionError`
2. Where: line 5, function `divide`
3. Called from: line 10

### **Technique 2: print() Debugging**

**Add prints to trace execution:**

```python
def calculate_average(numbers):
    print(f"DEBUG: Input: {numbers}")
    
    if len(numbers) == 0:
        print("DEBUG: Empty list!")
        return 0
    
    total = sum(numbers)
    print(f"DEBUG: Total: {total}")
    
    avg = total / len(numbers)
    print(f"DEBUG: Average: {avg}")
    
    return avg
```

### **Technique 3: IDE Debugger**

**Features:**
- **Breakpoints** - Pause execution
- **Step Over** - Execute line
- **Step Into** - Enter function
- **Inspect** - View variables
- **Watch** - Monitor expressions

### **Technique 4: Defensive Programming**

**Check inputs:**
```python
def process_data(data):
    # Validate input
    if not isinstance(data, list):
        raise TypeError("Expected list")
    if len(data) == 0:
        raise ValueError("Empty list")
    
    # Process validated data
```

---

## 11. Best Practices

### **Exception Handling:**
1. **Catch specific exceptions** - Not `Exception`
2. **Keep try blocks small** - Only risky code
3. **Don't silence exceptions** - Handle meaningfully
4. **Use finally for cleanup** - Close files, connections
5. **Raise meaningful errors** - Include context
6. **Document exceptions** - In docstrings

### **Debugging:**
1. **Read error messages carefully**
2. **Test edge cases** - Empty lists, None, zero
3. **Use print() liberally** - Remove later
4. **Learn your debugger** - Powerful tool
5. **Write tests** - Catch bugs early
6. **Version control** - Commit working code

---

## 12. Common Pitfalls

### **Pitfall 1: Too Broad**
```python
# BAD - catches everything!
try:
    everything()
except:
    pass

# GOOD - specific
try:
    convert()
except ValueError:
    handle_bad_input()
```

### **Pitfall 2: Silencing Errors**
```python
# BAD - hides problems!
try:
    critical_operation()
except:
    pass  # Error ignored!

# GOOD - handle or log
try:
    critical_operation()
except Exception as e:
    log_error(e)
    raise
```

### **Pitfall 3: Using Exceptions for Control Flow**
```python
# BAD - slow and unclear!
try:
    return dict[key]
except KeyError:
    return default

# GOOD - use .get()
return dict.get(key, default)
```

---

## 💡 Key Takeaways

1. **try-except handles errors gracefully** - No crashes!
2. **Catch specific exceptions** - Not generic
3. **else runs on success** - No error occurred
4. **finally always runs** - Cleanup code
5. **raise triggers exceptions** - Custom errors
6. **Read tracebacks carefully** - Error location and type
7. **Use print() for debugging** - Simple but effective
8. **Test edge cases** - Empty, None, zero
9. **Exceptions are for exceptional cases** - Not control flow
10. **Defensive programming prevents bugs** - Validate inputs

---

## 📚 Quick Reference

| Concept | Syntax |
|---------|--------|
| Basic | `try: code except Error: handle` |
| Multiple | `except (Error1, Error2):` |
| Capture | `except Error as e:` |
| Else | `try: ... except: ... else: ...` |
| Finally | `try: ... except: ... finally: ...` |
| Raise | `raise ValueError("message")` |
| Re-raise | `except: log(); raise` |

---

*Exception handling transforms fragile code into robust applications. Master it to build professional, reliable programs!*
