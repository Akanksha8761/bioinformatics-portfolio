# Day 17: File Handling - Concepts

## 📌 Core Concepts Covered

File handling is the ability to read from and write to files on your computer's file system. This is essential for data processing, analysis, and building real-world applications. Today we learn how to open, read, write, and manage files in Python!

---

## 1. Why File Handling?

**File handling enables:**
- **Data Persistence**: Save data beyond program execution
- **Data Processing**: Read large datasets for analysis
- **Configuration**: Store and read settings
- **Logging**: Record program activity
- **Data Exchange**: Share data between programs
- **Real-world Applications**: Process CSV, text, JSON files

**Example Use Cases:**
- Reading gene sequences from FASTA files
- Processing CSV data files
- Storing analysis results
- Reading configuration files
- Logging experimental data

---

## 2. File Modes

When opening a file, you specify a **mode** that determines what operations are allowed.

### **Common File Modes:**

| Mode | Name | Description | Creates File? | Overwrites? |
|------|------|-------------|---------------|-------------|
| `'r'` | Read | Read only (default) | No | - |
| `'w'` | Write | Write only | Yes | **Yes** |
| `'a'` | Append | Add to end | Yes | No |
| `'r+'` | Read+Write | Read and write | No | No |
| `'w+'` | Write+Read | Write and read | Yes | **Yes** |
| `'a+'` | Append+Read | Append and read | Yes | No |

**Key Points:**
- `'w'` mode **OVERWRITES** existing files - use carefully!
- `'a'` mode **adds** to the end without deleting
- `'r'` mode raises error if file doesn't exist
- `'w'` and `'a'` create file if it doesn't exist

---

## 3. Basic File Operations

### **The Three Steps:**
1. **Open** the file
2. **Read/Write** data
3. **Close** the file

### **Opening a File:**
```python
file_object = open('filename.txt', 'mode')
```

### **Closing a File:**
```python
file_object.close()
```

**Why close files?**
- Frees system resources
- Ensures data is written
- Prevents file corruption
- Good practice!

---

## 4. Writing to Files

### **Basic Write:**
```python
# Open in write mode
file_object = open('output.txt', 'w')

# Write text (doesn't add newline automatically!)
file_object.write("Hello, World!\n")
file_object.write("Second line\n")

# Close the file
file_object.close()
```

**Important:**
- `write()` does NOT add newline - you must add `\n`
- `'w'` mode overwrites existing content
- Multiple `write()` calls append to each other

### **Writing Variables:**
```python
gene_name = 'TP53'
expression = 42.5

file_object = open('data.txt', 'w')
file_object.write(f"Gene: {gene_name}\n")
file_object.write(f"Expression: {expression}\n")
file_object.close()
```

### **Writing Lists:**
```python
genes = ['TP53', 'BRCA1', 'MYC']

file_object = open('genes.txt', 'w')
for gene in genes:
    file_object.write(f"{gene}\n")
file_object.close()
```

---

## 5. Reading from Files

### **Method 1: Read Entire File**
```python
file_object = open('data.txt', 'r')
content = file_object.read()  # Returns entire file as string
print(content)
file_object.close()
```

### **Method 2: Read Line by Line (Best for Large Files)**
```python
file_object = open('data.txt', 'r')
for line in file_object:
    clean_line = line.strip()  # Remove whitespace
    print(clean_line)
file_object.close()
```

### **Method 3: readline() - One Line at a Time**
```python
file_object = open('data.txt', 'r')
first_line = file_object.readline()  # First line
second_line = file_object.readline()  # Second line
file_object.close()
```

### **Method 4: readlines() - List of Lines**
```python
file_object = open('data.txt', 'r')
all_lines = file_object.readlines()  # Returns list
for line in all_lines:
    print(line.strip())
file_object.close()
```

**Comparison:**

| Method | Returns | Use When |
|--------|---------|----------|
| `read()` | String (entire file) | Small files |
| `readline()` | String (one line) | Need one line |
| `readlines()` | List of strings | Need list |
| `for line in file` | Iterator | Large files (best!) |

---

## 6. Appending to Files

**Append mode (`'a'`) adds to the end without deleting existing content:**

```python
# Add new data to existing file
file_object = open('log.txt', 'a')
file_object.write("New log entry\n")
file_object.close()
```

**Example - Building a log:**
```python
# First run
file_object = open('experiment.log', 'a')
file_object.write("2026-02-02: Experiment started\n")
file_object.close()

# Second run (later)
file_object = open('experiment.log', 'a')
file_object.write("2026-02-02: Data collected\n")
file_object.close()

# Result: Both lines are in the file!
```

---

## 7. The `with` Statement (BEST PRACTICE!)

**The Problem:**
```python
file_object = open('data.txt', 'r')
content = file_object.read()
# If error happens here, file never closes!
file_object.close()
```

**The Solution:**
```python
with open('data.txt', 'r') as file_object:
    content = file_object.read()
    # Do work here
# File AUTOMATICALLY closed here, even if error occurs!
```

### **Why Use `with`?**
- **Automatic closing** - Even if error occurs
- **Cleaner code** - No explicit close() needed
- **Safer** - Prevents resource leaks
- **Professional** - Industry standard

### **Writing with `with`:**
```python
with open('output.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
```

### **Reading with `with`:**
```python
with open('input.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

### **Appending with `with`:**
```python
with open('log.txt', 'a') as f:
    f.write("New entry\n")
```

**Always use `with` for file operations!**

---

## 8. Common String Methods for File Processing

### **strip() - Remove Whitespace**
```python
line = "  Hello  \n"
clean = line.strip()  # "Hello"
```

**Variants:**
- `lstrip()` - Remove from left
- `rstrip()` - Remove from right

### **split() - Split into List**
```python
line = "Gene,Expression,Condition"
parts = line.split(',')  # ['Gene', 'Expression', 'Condition']
```

### **startswith() and endswith()**
```python
gene = "TP53"
if gene.startswith('T'):
    print("Starts with T!")
    
filename = "data.txt"
if filename.endswith('.txt'):
    print("Text file!")
```

### **upper() and lower()**
```python
gene = "myc"
gene_upper = gene.upper()  # "MYC"
```

---

## 9. File Paths

### **Relative Paths:**
Relative to current directory:
```python
'data.txt'           # Same directory
'data/genes.txt'     # data subdirectory
'../other/file.txt'  # Parent directory
```

### **Absolute Paths:**
Full path from root:
```python
# Windows
'C:\\Users\\Name\\data.txt'

# Linux/Mac
'/home/username/data.txt'
```

**Best Practice:** Use relative paths for portability!

---

## 10. Practical Patterns

### **Pattern 1: Process and Filter**
```python
# Read file, process, write results
with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        for line in infile:
            processed = line.strip().upper()
            if processed.startswith('A'):
                outfile.write(f"{processed}\n")
```

### **Pattern 2: Count Items**
```python
count = 0
with open('genes.txt', 'r') as f:
    for line in f:
        count += 1
print(f"Total genes: {count}")
```

### **Pattern 3: Collect into List**
```python
genes = []
with open('genes.txt', 'r') as f:
    for line in f:
        gene = line.strip()
        genes.append(gene)
print(genes)
```

### **Pattern 4: CSV Processing**
```python
# Read CSV manually
with open('data.csv', 'r') as f:
    for line in f:
        values = line.strip().split(',')
        # Process values
        print(values)
```

### **Pattern 5: Check if File Exists**
```python
import os

if os.path.exists('data.txt'):
    with open('data.txt', 'r') as f:
        content = f.read()
else:
    print("File not found!")
```

---

## 11. Common Pitfalls

### **Pitfall 1: Forgetting to Close**
```python
# BAD
f = open('data.txt', 'r')
content = f.read()
# Forgot to close!

# GOOD
with open('data.txt', 'r') as f:
    content = f.read()
```

### **Pitfall 2: Overwriting with 'w'**
```python
# DANGER! This deletes all content!
with open('important.txt', 'w') as f:
    f.write("New content")
    
# Use 'a' to add instead:
with open('important.txt', 'a') as f:
    f.write("New content")
```

### **Pitfall 3: Forgetting Newlines**
```python
# BAD - All on one line
with open('data.txt', 'w') as f:
    f.write("Line 1")
    f.write("Line 2")
# Result: "Line 1Line 2"

# GOOD
with open('data.txt', 'w') as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
# Result: "Line 1\nLine 2\n"
```

### **Pitfall 4: Reading Closed File**
```python
# BAD
with open('data.txt', 'r') as f:
    content = f.read()
# f is closed here
print(f.read())  # Error!

# GOOD
with open('data.txt', 'r') as f:
    content = f.read()
print(content)  # Use saved content
```

---

## 12. Bioinformatics Example

### **Processing Gene List:**
```python
# Read genes, convert to uppercase, filter by criteria
with open('gene_list.txt', 'r') as infile:
    with open('selected_genes.txt', 'w') as outfile:
        for line in infile:
            gene = line.strip().upper()
            if gene.startswith(('T', 'A')):
                outfile.write(f"{gene}\n")
```

### **Calculate GC Content from File:**
```python
def gc_content(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    return ((g + c) / len(sequence)) * 100

# Read sequence from file
with open('sequence.txt', 'r') as f:
    seq = f.read().strip()
    gc = gc_content(seq)
    
# Write result to file
with open('results.txt', 'w') as f:
    f.write(f"Sequence: {seq}\n")
    f.write(f"GC Content: {gc:.2f}%\n")
```

---

## 💡 Key Takeaways

1. **Three steps**: Open, Read/Write, Close
2. **Always use `with`** - Automatic closing, safer code
3. **'w' overwrites** - Use carefully!
4. **'a' appends** - Adds to end
5. **'r' reads** - File must exist
6. **`strip()`** removes whitespace - Use it!
7. **`write()` doesn't add newlines** - Add `\n` yourself
8. **Iterate for large files** - `for line in file`
9. **Relative paths** - More portable
10. **File handling enables real applications** - Essential skill!

---

## 📚 Quick Reference

| Task | Code |
|------|------|
| Write | `with open('file.txt', 'w') as f: f.write(text)` |
| Read all | `with open('file.txt', 'r') as f: content = f.read()` |
| Read lines | `with open('file.txt', 'r') as f: for line in f:` |
| Append | `with open('file.txt', 'a') as f: f.write(text)` |
| Strip whitespace | `line.strip()` |
| Check exists | `import os; os.path.exists('file.txt')` |

---

*File handling transforms Python from a calculator into a real data processing tool. Master it to work with real-world data!*
