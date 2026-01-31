# Day 9: The "Log File Parser" Challenge

## 🎯 Challenge Description

### The Scenario
You have a "log file" (simulated with a multi-line string). You need to extract specific information from it safely.

```python
log_data = """
INFO: User logged in
ERROR: Database connection failed
INFO: Search performed
ERROR: File not found
DEBUG: Cache cleared
"""
```

### The Task
Write a function called `get_errors` that:
1. Takes the `log_data` string
2. Uses a **try-except block** to handle potential issues (like if the input isn't a string)
3. Uses a **List Comprehension** to find all lines that start with "ERROR:"
4. Returns a list of just the error messages (**without** the "ERROR: " prefix)

### The Bonus
Imagine you were writing this to a real file. Use the **`with` statement** syntax to "write" the results into a file named `errors.txt`.

### Expected Behavior
```python
get_errors(log_data)  
# → ['Database connection failed', 'File not found']

get_errors(123)       
# → [] (or handle gracefully)

get_errors(None)      
# → [] (or handle gracefully)
```

## 📚 Concepts Covered

- **File I/O**: Reading and writing files
- **`with` Statement**: Context managers
- **Multi-line Strings**: Triple quotes (`"""`)
- **`.splitlines()`**: Splitting strings by newlines
- **`.startswith()`**: String prefix checking
- **`.split()`**: String splitting
- **Try-Except**: Error handling
- **Type Checking**: `isinstance()`
- **List Comprehensions**: Filtering and transformation

## 💡 Solution Approaches

### Approach 1: Simple List Comprehension (Recommended)
```python
def get_errors(log_data):
    """Extract error messages from log data."""
    try:
        # Ensure input is a string
        if not isinstance(log_data, str):
            return []
        
        # Split into lines and extract ERROR messages
        errors = [
            line.split(": ", 1)[1]  # Get text after "ERROR: "
            for line in log_data.splitlines()
            if line.strip().startswith("ERROR:")
        ]
        
        return errors
    except (IndexError, AttributeError):
        return []

# Test
log_data = """
INFO: User logged in
ERROR: Database connection failed
INFO: Search performed
ERROR: File not found
DEBUG: Cache cleared
"""

errors = get_errors(log_data)
print(errors)
# ['Database connection failed', 'File not found']

# Write to file
with open('errors.txt', 'w') as f:
    for error in errors:
        f.write(error + '\n')
```

### Approach 2: Using `.replace()` Method
```python
def get_errors(log_data):
    """Extract errors using string replace."""
    try:
        if not isinstance(log_data, str):
            return []
        
        errors = [
            line.replace("ERROR: ", "", 1).strip()
            for line in log_data.splitlines()
            if line.strip().startswith("ERROR:")
        ]
        
        return errors
    except AttributeError:
        return []
```

### Approach 3: Using Regular Expressions
```python
import re

def get_errors(log_data):
    """Extract errors using regex."""
    try:
        if not isinstance(log_data, str):
            return []
        
        # Find all lines starting with ERROR: and capture the message
        pattern = r'^ERROR:\s*(.+)$'
        errors = re.findall(pattern, log_data, re.MULTILINE)
        
        return errors
    except (TypeError, AttributeError):
        return []
```

### Approach 4: Reading from Actual File
```python
def get_errors_from_file(filename):
    """Extract errors from an actual log file."""
    try:
        errors = []
        
        with open(filename, 'r') as f:
            errors = [
                line.split(": ", 1)[1].strip()
                for line in f
                if line.strip().startswith("ERROR:")
            ]
        
        return errors
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return []
    except (IndexError, AttributeError):
        return []

# Usage
errors = get_errors_from_file('server.log')
```

### Approach 5: Complete Solution with File Writing
```python
def get_errors(log_data):
    """
    Extract error messages from log data.
    
    Args:
        log_data (str): Multi-line log string
    
    Returns:
        list: Error messages without "ERROR:" prefix
    """
    try:
        # Type validation
        if not isinstance(log_data, str):
            raise TypeError(f"Expected str, got {type(log_data).__name__}")
        
        # Extract errors
        errors = [
            line.split(": ", 1)[1].strip()
            for line in log_data.splitlines()
            if line.strip().startswith("ERROR:")
        ]
        
        return errors
        
    except (IndexError, AttributeError) as e:
        print(f"Error parsing log data: {e}")
        return []
    except TypeError as e:
        print(f"Type error: {e}")
        return []

def write_errors_to_file(errors, filename='errors.txt'):
    """Write errors to a file."""
    try:
        with open(filename, 'w') as f:
            for error in errors:
                f.write(error + '\n')
        
        print(f"✓ Wrote {len(errors)} errors to {filename}")
        
    except IOError as e:
        print(f"Error writing to file: {e}")

# Complete usage
log_data = """
INFO: User logged in
ERROR: Database connection failed
INFO: Search performed
ERROR: File not found
DEBUG: Cache cleared
"""

errors = get_errors(log_data)
write_errors_to_file(errors)
```

## 🔍 Code Breakdown

### Your Approach Analysis:

```python
# Your code creates a file first
with open('error.txt', 'w') as f:
    f.write("INFO: User logged in\nERROR: Database connection failed...")

def get_error(data):
    error = []
    
    # Reading from file (but 'data' parameter is unused!)
    with open('error.txt', 'r') as f:
        
        # Logic issue: checking if data is string first
        if isinstance(data, str):
            print(f"The input '{data}' is a string")
            # But then does nothing with it!
        
        elif not isinstance(data, str):
            try:
                # This runs only if data is NOT a string
                error = [
                    i.strip().split(": ", 1)[1] 
                    for i in f 
                    if i.startswith('ERROR')
                ]
                return error
            except (...):
                return

# Issues:
# 1. Reads from file instead of using 'data' parameter
# 2. Logic backwards: processes when NOT string
# 3. get_error(12) works but get_error('hey') doesn't
```

### Understanding `.splitlines()`:

```python
text = """
INFO: User logged in
ERROR: Database failed
DEBUG: Cache cleared
"""

# Method 1: .splitlines()
lines = text.splitlines()
# ['', 'INFO: User logged in', 'ERROR: Database failed', 'DEBUG: Cache cleared']

# Method 2: .split('\n')
lines = text.split('\n')
# Same result

# Iterate and filter
errors = [
    line for line in lines 
    if line.strip().startswith("ERROR:")
]
```

### Understanding `.split(": ", 1)`:

```python
line = "ERROR: Database connection failed"

# Method 1: split with limit
parts = line.split(": ", 1)
# ['ERROR', 'Database connection failed']
message = parts[1]

# Method 2: replace
message = line.replace("ERROR: ", "", 1)
# 'Database connection failed'

# Why split with 1?
line = "ERROR: User: John disconnected"
line.split(": ", 1)  # ['ERROR', 'User: John disconnected']
line.split(": ")     # ['ERROR', 'User', 'John disconnected'] - splits all colons!
```

### Understanding `with` Statement:

```python
# Without 'with' (manual cleanup)
f = open('file.txt', 'w')
try:
    f.write('data')
finally:
    f.close()  # Must remember to close!

# With 'with' (automatic cleanup)
with open('file.txt', 'w') as f:
    f.write('data')
# File automatically closed, even if exception occurs!

# Multiple files
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    data = infile.read()
    outfile.write(data.upper())
```

## 🎓 Key Takeaways

1. **`with` statement** ensures files are properly closed
2. **`.splitlines()`** splits string by line breaks
3. **`.split(": ", 1)`** limits splits (important for colons in message)
4. **Type checking** prevents errors (`isinstance()`)
5. **Try-except** handles unexpected input gracefully
6. **List comprehensions** concisely filter and transform
7. **Early returns** with empty lists are better than raising errors

## 🚀 Variations to Try

### Challenge Yourself:

1. **Support different log levels** (INFO, WARNING, ERROR, CRITICAL)
2. **Parse timestamps** from log entries
3. **Count error frequency** by type
4. **Filter by date range**
5. **Create log analyzer class**

### Example Solutions:

**All Log Levels:**
```python
def get_logs_by_level(log_data, level):
    """Get logs for specific level."""
    try:
        if not isinstance(log_data, str):
            return []
        
        return [
            line.split(": ", 1)[1].strip()
            for line in log_data.splitlines()
            if line.strip().startswith(f"{level}:")
        ]
    except IndexError:
        return []

# Usage
errors = get_logs_by_level(log_data, "ERROR")
infos = get_logs_by_level(log_data, "INFO")
warnings = get_logs_by_level(log_data, "WARNING")
```

**Parse with Timestamps:**
```python
import re
from datetime import datetime

def parse_log_entry(log_data):
    """Parse logs with timestamps."""
    # Format: "2024-01-20 10:30:45 ERROR: Database failed"
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+): (.+)'
    
    entries = []
    for line in log_data.splitlines():
        match = re.match(pattern, line.strip())
        if match:
            timestamp, level, message = match.groups()
            entries.append({
                'timestamp': datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S'),
                'level': level,
                'message': message
            })
    
    return entries
```

**Count Error Types:**
```python
from collections import Counter

def count_errors(log_data):
    """Count frequency of each error type."""
    try:
        errors = [
            line.split(": ", 1)[1].strip()
            for line in log_data.splitlines()
            if line.strip().startswith("ERROR:")
        ]
        
        return Counter(errors)
    except IndexError:
        return Counter()

# Usage
counts = count_errors(log_data)
# Counter({'Database connection failed': 1, 'File not found': 1})
```

**Log Analyzer Class:**
```python
class LogAnalyzer:
    """Analyze log files."""
    
    LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    
    def __init__(self, log_data):
        self.log_data = log_data
        self.entries = self._parse_logs()
    
    def _parse_logs(self):
        """Parse log data into structured format."""
        entries = []
        
        for line in self.log_data.splitlines():
            line = line.strip()
            if not line:
                continue
            
            for level in self.LEVELS:
                if line.startswith(f"{level}:"):
                    message = line.split(": ", 1)[1]
                    entries.append({'level': level, 'message': message})
                    break
        
        return entries
    
    def get_by_level(self, level):
        """Get messages for specific level."""
        return [
            entry['message'] 
            for entry in self.entries 
            if entry['level'] == level
        ]
    
    def get_errors(self):
        """Get error messages."""
        return self.get_by_level('ERROR')
    
    def count_by_level(self):
        """Count entries per level."""
        return Counter(entry['level'] for entry in self.entries)
    
    def save_errors(self, filename='errors.txt'):
        """Save errors to file."""
        errors = self.get_errors()
        with open(filename, 'w') as f:
            for error in errors:
                f.write(error + '\n')

# Usage
analyzer = LogAnalyzer(log_data)
print(analyzer.get_errors())
print(analyzer.count_by_level())
analyzer.save_errors()
```

**Filter by Date Range:**
```python
from datetime import datetime

def filter_logs_by_date(log_file, start_date, end_date):
    """Filter logs within date range."""
    # Assumes format: "2024-01-20 10:30:45 ERROR: message"
    
    filtered = []
    
    with open(log_file, 'r') as f:
        for line in f:
            try:
                # Extract timestamp
                timestamp_str = line[:19]  # First 19 chars
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                
                # Check if in range
                if start_date <= timestamp <= end_date:
                    filtered.append(line.strip())
            except ValueError:
                continue  # Skip malformed lines
    
    return filtered
```

## 📊 Performance Comparison

| Approach | Readability | Performance | Error Handling | Best For |
|----------|-------------|-------------|----------------|----------|
| List comprehension + split | Excellent | O(n) | Good | Most cases |
| Replace method | Good | O(n) | Good | Simple parsing |
| Regular expressions | Fair | O(n) slower | Excellent | Complex patterns |
| Manual loop | Good | O(n) | Excellent | Custom logic |

## 🔗 Related Topics to Explore

- `logging` module (Python's built-in logger)
- `pathlib` for modern file paths
- `json` for structured logs
- `csv` module for CSV logs
- `gzip` for compressed logs
- Log rotation and management
- Asynchronous file I/O

## 💡 Real-World Applications

- **System Monitoring**: Parse server logs
- **Error Tracking**: Extract and categorize errors
- **Security Audits**: Analyze access logs
- **Performance Analysis**: Parse timing data
- **Debugging**: Filter relevant log entries
- **Compliance**: Log retention and analysis

## 🐛 Common Mistakes to Avoid

```python
# ❌ Wrong: Not using 'with' statement
f = open('file.txt', 'w')
f.write('data')
# Forgot to close! File may not be written

# ✅ Correct: Use 'with' statement
with open('file.txt', 'w') as f:
    f.write('data')

# ❌ Wrong: Split without limit
line = "ERROR: User: John failed: timeout"
message = line.split(": ")[1]  # Only gets "User"!

# ✅ Correct: Use limit parameter
message = line.split(": ", 1)[1]  # Gets "User: John failed: timeout"

# ❌ Wrong: Not handling empty lines
errors = [
    line.split(": ")[1]
    for line in log_data.splitlines()
    if "ERROR" in line  # Will crash on "ERROR" without colon
]

# ✅ Correct: Use .startswith() and handle errors
errors = [
    line.split(": ", 1)[1]
    for line in log_data.splitlines()
    if line.strip().startswith("ERROR:")
]

# ❌ Wrong: Reading entire file into memory
with open('huge.log', 'r') as f:
    data = f.read()  # Loads entire file!
    errors = get_errors(data)

# ✅ Correct: Process line by line
errors = []
with open('huge.log', 'r') as f:
    for line in f:  # Reads one line at a time
        if line.strip().startswith("ERROR:"):
            errors.append(line.split(": ", 1)[1].strip())

# ❌ Wrong: Not checking if parameter is used
def get_error(data):
    with open('error.txt', 'r') as f:  # Ignores 'data' parameter!
        # Process file instead of data
        ...

# ✅ Correct: Use the parameter
def get_errors(data):
    # Process 'data' parameter
    errors = [...]
    return errors
```

## 🧪 Testing Your Solution

```python
def test_get_errors():
    """Comprehensive test suite."""
    
    # Test 1: Normal log data
    log_data = """
INFO: User logged in
ERROR: Database connection failed
ERROR: File not found
"""
    result = get_errors(log_data)
    assert result == ['Database connection failed', 'File not found']
    print("✅ Test 1: Normal log data")
    
    # Test 2: No errors
    log_data = """
INFO: User logged in
DEBUG: Cache cleared
"""
    result = get_errors(log_data)
    assert result == []
    print("✅ Test 2: No errors")
    
    # Test 3: Empty string
    result = get_errors("")
    assert result == []
    print("✅ Test 3: Empty string")
    
    # Test 4: Non-string input
    result = get_errors(123)
    assert result == []
    print("✅ Test 4: Non-string input")
    
    # Test 5: None input
    result = get_errors(None)
    assert result == []
    print("✅ Test 5: None input")
    
    # Test 6: Errors with colons in message
    log_data = "ERROR: User: John failed: timeout"
    result = get_errors(log_data)
    assert result == ['User: John failed: timeout']
    print("✅ Test 6: Colons in message")
    
    # Test 7: Mixed whitespace
    log_data = "  ERROR: Whitespace test  \n\nERROR: Another error  "
    result = get_errors(log_data)
    assert len(result) == 2
    print("✅ Test 7: Mixed whitespace")
    
    print("\n🎉 All tests passed!")

test_get_errors()
```

---

**Date Completed:** Day 9  
**Difficulty:** ⭐⭐⭐☆☆ (Intermediate)  
**Time Spent:** ~50 minutes  
**Skills Gained:** File I/O, `with` statement, `.splitlines()`, `.split()`, log parsing, error handling
