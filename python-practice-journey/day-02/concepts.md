# Day 2: Strings and Manipulation - Concepts

## 📌 Core Concepts Covered

### 1. String Concatenation

**Concatenation** means joining strings together to create a new string.

#### **Using the + Operator**
```python
greeting = "Hello"
name = "Akanksha"
separator = ", "
exclamation = "!"

message = greeting + separator + name + exclamation
# Result: "Hello, Akanksha!"
```

#### **Important Rules:**
- You can only concatenate strings with strings
- To concatenate numbers, convert them to strings first using `str()`

```python
age = 30
# This causes an error:
# print("My age is " + age)  # TypeError!

# This works:
print("My age is " + str(age))  # "My age is 30"
```

#### **Using F-Strings (Better Method)**
```python
name = "Bob"
age = 23
city = "New York"

# F-string handles type conversion automatically
greeting = f"My name is {name}, I am {age} years old and I live in {city}"
```

---

### 2. String Multiplication

You can repeat a string multiple times using the `*` operator.

```python
message = "Hello! "
repeated = message * 3
# Result: "Hello! Hello! Hello! "

separator = "=" * 30
# Result: "=============================="
```

**Use Cases:**
- Creating decorative lines
- Generating patterns
- Creating repeated text

---

### 3. String Indexing

Strings are **sequences** of characters. Each character has a position (index).

#### **Positive Indexing** (starts at 0)
```python
name = "Akanksha"
#       01234567

print(name[0])   # 'A' (first character)
print(name[4])   # 'n'
print(name[7])   # 'a' (last character)
```

#### **Negative Indexing** (starts at -1)
```python
name = "Akanksha"
#       -8-7-6-5-4-3-2-1

print(name[-1])  # 'a' (last character)
print(name[-2])  # 'h' (second to last)
print(name[-8])  # 'A' (first character)
```

**Why Negative Indexing?**
- Easy access to characters from the end
- Don't need to know the string length
- `name[-1]` always gets the last character

---

### 4. String Slicing

**Slicing** extracts a portion (substring) of a string.

#### **Basic Syntax: `string[start:stop]`**
```python
text = "My name is Akanksha"
#       0123456789...

substring = text[3:7]  # 'name'
# Starts at index 3, stops BEFORE index 7
```

**Important:** The `stop` index is **exclusive** (not included).

#### **Slicing Variations**

**Omitting Start (begins at 0):**
```python
text = "Python"
print(text[:3])   # 'Pyt'
```

**Omitting Stop (goes to end):**
```python
text = "Python"
print(text[3:])   # 'hon'
```

**Using Step: `string[start:stop:step]`**
```python
text = "Hello World"

# Every other character
print(text[::2])    # 'HloWrd'

# Every third character
print(text[::3])    # 'HlWl'
```

#### **Reversing a String**
```python
text = "Hello"
reversed_text = text[::-1]  # 'olleH'
```

**How it works:** Negative step (-1) means go backwards through the string.

#### **Copying a String**
```python
text = "Python"
copy = text[:]  # Creates a copy
```

---

### 5. String Length with len()

The `len()` function returns the number of characters in a string.

```python
text = "My name is Akanksha, this is my third python class"
length = len(text)  # 51

name = "Bob"
print(len(name))    # 3
```

**Use Cases:**
- Validate input length
- Loop through strings
- Calculate string properties

---

### 6. Escape Sequences

**Escape sequences** are special characters that start with a backslash `\`.

#### **Common Escape Sequences**

| Sequence | Meaning | Example |
|----------|---------|---------|
| `\n` | New line | `"Hello\nWorld"` |
| `\t` | Tab | `"Name:\tBob"` |
| `\'` | Single quote | `'doesn\'t'` |
| `\"` | Double quote | `"He said \"Hi\""` |
| `\\` | Backslash | `"C:\\Users"` |

```python
# Quoting quotes
print('doesn\'t')           # doesn't
print("\"Yes,\" they said") # "Yes," they said

# New line example
print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2

# Tab example
print("Name:\tAkanksha")    # Name:    Akanksha
```

---

### 7. Raw Strings

**Raw strings** treat backslashes as literal characters, not escape sequences.

```python
# Without raw string - \n is interpreted as newline
print('C:\some\name')   # C:\some
                        # ame (newline after \n)

# With raw string - r prefix
print(r'C:\some\name')  # C:\some\name
```

**Use Cases:**
- File paths (especially on Windows)
- Regular expressions
- When you need literal backslashes

---

## 🎯 String Slicing Cheat Sheet

```python
text = "Python Programming"

# Basic slicing
text[0:6]      # 'Python'
text[7:18]     # 'Programming'

# Omitting indices
text[:6]       # 'Python' (start to index 6)
text[7:]       # 'Programming' (index 7 to end)
text[:]        # 'Python Programming' (entire string)

# Using step
text[::2]      # 'Pto rgamn' (every 2nd char)
text[1::2]     # 'yhnPoraig' (every 2nd char starting at 1)

# Reversing
text[::-1]     # 'gnimmargorP nohtyP'

# Negative indices
text[-11:]     # 'Programming' (last 11 chars)
text[:-12]     # 'Python' (everything except last 12 chars)
text[-11:-7]   # 'Prog'
```

---

## 💡 Key Takeaways

1. **Concatenation**: Join strings with `+` or use f-strings
2. **Multiplication**: Repeat strings with `*`
3. **Indexing**: Access individual characters (positive or negative)
4. **Slicing**: Extract substrings with `[start:stop:step]`
5. **Length**: Use `len()` to get string length
6. **Escape Sequences**: Special characters starting with `\`
7. **Raw Strings**: Prefix with `r` to treat backslashes literally

---

## 🔍 Common Patterns

**Get first character:**
```python
text[0]
```

**Get last character:**
```python
text[-1]
```

**Get first 5 characters:**
```python
text[:5]
```

**Get last 5 characters:**
```python
text[-5:]
```

**Reverse a string:**
```python
text[::-1]
```

**Every other character:**
```python
text[::2]
```

---

## 📚 Practice Tips

1. Remember: slicing is `[start:stop:step]` where stop is **exclusive**
2. Negative indices count from the end: `-1` is last, `-2` is second to last
3. F-strings automatically handle type conversion
4. Use raw strings (`r""`) for file paths
5. String indices start at 0, not 1

---

## 🎓 Advanced Note

Strings in Python are **immutable** - you cannot change individual characters:

```python
name = "Bob"
# name[0] = "R"  # This causes an error!

# Instead, create a new string:
name = "R" + name[1:]  # "Rob"
```

---

## 📚 Further Reading

- [Python String Documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- [String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings)
