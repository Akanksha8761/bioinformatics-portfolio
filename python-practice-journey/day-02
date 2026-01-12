# Day 2: The "Word Frequency Counter" Challenge

## 🎯 Challenge Description

### The Scenario
You are building a basic search engine. You have a string of text, and you need to count how many times each word appears to determine its "weight."

### The Task
Given this string:
```python
text = "Python is amazing. Python is fast. Is python easy? YES!"
```

Create a dictionary called `word_counts` where:
1. The keys are the words (lowercase)
2. The values are the number of times that word appears
3. Punctuation must be ignored (e.g., "amazing." and "amazing" should be treated as the same word)

### The Constraint
Try to solve this using:
- The `.get()` method for dictionaries, OR
- The `collections.Counter` class from Python's standard library

## 📚 Concepts Covered

- **String Methods**:
  - `.translate()`: Transforms strings based on a translation table
  - `.maketrans()`: Creates translation tables for `.translate()`
  - `.lower()`: Converts to lowercase
  - `.split()`: Splits string into a list of words
- **Dictionary Methods**:
  - `.get()`: Safely retrieves values with a default
- **Collections Module**:
  - `Counter`: A specialized dictionary for counting hashable objects
- **String Module**:
  - `string.punctuation`: Pre-defined punctuation characters

## 💡 Solution Approaches

### Approach 1: Using `Counter` (Most Pythonic)
```python
from collections import Counter
import string

text = "Python is amazing. Python is fast. Is python easy? YES!"

# Remove punctuation and convert to lowercase
clean_text = text.translate(str.maketrans('', '', string.punctuation))
text_lower = clean_text.lower()

# Split into words and count
words = text_lower.split()
word_counts = Counter(words)

print(word_counts)
```

**Output:**
```
Counter({'python': 3, 'is': 3, 'amazing': 1, 'fast': 1, 'easy': 1, 'yes': 1})
```

### Approach 2: Using Dictionary `.get()` Method
```python
import string

text = "Python is amazing. Python is fast. Is python easy? YES!"

# Remove punctuation and convert to lowercase
clean_text = text.translate(str.maketrans('', '', string.punctuation))
words = clean_text.lower().split()

# Count using .get() method
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
```

**Output:**
```
{'python': 3, 'is': 3, 'amazing': 1, 'fast': 1, 'easy': 1, 'yes': 1}
```

### Approach 3: Using `defaultdict`
```python
from collections import defaultdict
import string

text = "Python is amazing. Python is fast. Is python easy? YES!"

# Remove punctuation and convert to lowercase
clean_text = text.translate(str.maketrans('', '', string.punctuation))
words = clean_text.lower().split()

# Count using defaultdict
word_counts = defaultdict(int)
for word in words:
    word_counts[word] += 1

print(dict(word_counts))
```

### Approach 4: Using Regular Expressions (Advanced)
```python
import re
from collections import Counter

text = "Python is amazing. Python is fast. Is python easy? YES!"

# Use regex to extract words (automatically handles punctuation)
words = re.findall(r'\b\w+\b', text.lower())
word_counts = Counter(words)

print(word_counts)
```

## 🔍 Code Breakdown

### Your Solution Analysis:
```python
from collections import Counter
import string

text = "Python is amazing. Python is fast. Is python easy? YES!"
clean_text = text.translate(str.maketrans('', '', string.punctuation))
#           │                │              │  │  └─ Remove these chars
#           │                │              │  └─ Replace with these
#           │                │              └─ Replace these characters
#           │                └─ Create translation table
#           └─ Apply translation to remove punctuation

text = clean_text.lower()  # Convert to lowercase
print(text)  # "python is amazing python is fast is python easy yes"

new = text.split()  # Split into list of words
print(new)  # ['python', 'is', 'amazing', 'python', 'is', 'fast', ...]

word_count = Counter(new)  # Count occurrences
print(word_count)  # Counter({'python': 3, 'is': 3, ...})
```

### Understanding `str.maketrans()` and `.translate()`:

```python
# What string.punctuation contains:
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# How maketrans works:
translation_table = str.maketrans('', '', string.punctuation)
# Args: (replace_from, replace_to, delete_these)

# Apply translation:
"Hello, World!".translate(translation_table)  # "Hello World"
```

### Understanding `.get()` Method:

```python
word_counts = {}

# Without .get() - risky:
word_counts[word] = word_counts[word] + 1  # KeyError if word not in dict!

# With .get() - safe:
word_counts[word] = word_counts.get(word, 0) + 1
#                                    │     │
#                                    │     └─ Default value if key doesn't exist
#                                    └─ Key to look up
```

## 🎓 Key Takeaways

1. **`Counter` is purpose-built** for counting - use it when appropriate
2. **`.get()` prevents KeyError** when accessing dictionary keys that might not exist
3. **Method chaining** (`.lower().split()`) makes code more concise
4. **`string.punctuation`** is a convenient constant for all punctuation
5. **Multiple approaches exist** - choose based on readability and requirements

## 🚀 Variations to Try

### Challenge Yourself:

1. **Find the most common word**
2. **Count only words longer than 3 characters**
3. **Create a function that accepts any text**
4. **Sort words by frequency (descending)**
5. **Ignore common "stop words" (the, is, a, etc.)**

### Example Solutions:

**Most Common Word:**
```python
most_common = word_counts.most_common(1)  # [('python', 3)]
# or
max_word = max(word_counts, key=word_counts.get)  # 'python'
```

**Words Longer Than 3 Characters:**
```python
long_words = {word: count for word, count in word_counts.items() if len(word) > 3}
# or with Counter
words_filtered = [w for w in words if len(w) > 3]
word_counts = Counter(words_filtered)
```

**As a Reusable Function:**
```python
def count_words(text, min_length=1, ignore_case=True):
    """
    Count word frequencies in text.
    
    Args:
        text (str): Text to analyze
        min_length (int): Minimum word length to count
        ignore_case (bool): Whether to ignore case
    
    Returns:
        Counter: Word frequency counter
    """
    # Remove punctuation
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Handle case
    if ignore_case:
        clean_text = clean_text.lower()
    
    # Split and filter by length
    words = [w for w in clean_text.split() if len(w) >= min_length]
    
    return Counter(words)
```

**Sorted by Frequency:**
```python
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
# or
sorted_words = word_counts.most_common()  # Returns list of tuples
```

**Ignore Stop Words:**
```python
stop_words = {'is', 'a', 'an', 'the', 'in', 'on', 'at'}
filtered_counts = {word: count for word, count in word_counts.items() 
                   if word not in stop_words}
```

## 📊 Performance Comparison

| Approach | Lines | Readability | Performance | Best For |
|----------|-------|-------------|-------------|----------|
| `Counter` | 3 | Excellent | O(n) | Quick counting tasks |
| `.get()` | 4 | Good | O(n) | Learning fundamentals |
| `defaultdict` | 4 | Good | O(n) | Complex counting logic |
| Regex | 2 | Advanced | O(n) | Complex text patterns |

## 🧪 Testing Your Solution

```python
# Test cases
test_cases = [
    ("Hello world", {'hello': 1, 'world': 1}),
    ("Test test TEST", {'test': 3}),
    ("One, two... three!!!", {'one': 1, 'two': 1, 'three': 1}),
]

for text, expected in test_cases:
    result = dict(count_words(text))
    assert result == expected, f"Failed for: {text}"
    print(f"✓ Passed: {text}")
```

## 🔗 Related Topics to Explore

- Natural Language Processing (NLP) basics
- TF-IDF (Term Frequency-Inverse Document Frequency)
- Text preprocessing and tokenization
- Regular expressions for advanced text processing
- Word clouds and data visualization

## 💡 Real-World Applications

- **Search engines**: Ranking documents by keyword relevance
- **SEO analysis**: Identifying keyword density
- **Text analytics**: Finding common themes in reviews/feedback
- **Chatbot training**: Understanding frequent user queries
- **Content analysis**: Detecting writing patterns

---

**Date Completed:** Day 2  
**Difficulty:** ⭐⭐☆☆☆ (Beginner)  
**Time Spent:** ~45 minutes  
**Skills Gained:** String manipulation, dictionaries, Counter, text processing
