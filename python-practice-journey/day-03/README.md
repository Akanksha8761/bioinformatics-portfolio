# Day 3: The "Student Ranking System" Challenge

## 🎯 Challenge Description

### The Scenario
You have a list of students, where each student is represented as a dictionary with their name and their exam score.

```python
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 88},
    {"name": "Eve", "score": 79}
]
```

### The Task
1. **Filter**: Create a new list containing only students who scored above 80
2. **Sort**: Sort that filtered list by their score in descending order (highest first)
3. **Tie-breaker**: If two students have the same score (like Alice and David), sort them alphabetically by name

### The Constraint
Try to use the `sorted()` function

## 📚 Concepts Covered

- **List Filtering**: Using list comprehensions and `filter()`
- **Sorting**: Using `sorted()` function with custom key functions
- **Lambda Functions**: Anonymous functions for sorting logic
- **Tuple Sorting**: Multi-level sorting with tuples
- **Dictionary Operations**: Working with lists of dictionaries
- **Operator Module**: Using `itemgetter` for cleaner sorting

## 💡 Solution Approaches

### Approach 1: Using `sorted()` with Lambda (Recommended)
```python
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 88},
    {"name": "Eve", "score": 79}
]

# Filter students with score > 80
filtered_students = [s for s in students if s['score'] > 80]

# Sort by score (descending) then by name (ascending)
sorted_students = sorted(filtered_students, key=lambda x: (-x['score'], x['name']))

print(sorted_students)
```

**Output:**
```python
[
    {'name': 'Charlie', 'score': 95},
    {'name': 'Alice', 'score': 88},
    {'name': 'David', 'score': 88}
]
```

### Approach 2: One-Liner (Pythonic)
```python
result = sorted([s for s in students if s['score'] > 80], 
                key=lambda x: (-x['score'], x['name']))
```

### Approach 3: Using `filter()` Function
```python
# Filter using filter() function
filtered_students = list(filter(lambda s: s['score'] > 80, students))

# Sort
sorted_students = sorted(filtered_students, key=lambda x: (-x['score'], x['name']))
```

### Approach 4: Using `operator.itemgetter`
```python
from operator import itemgetter

# Filter students
filtered_students = [s for s in students if s['score'] > 80]

# Sort by score descending, then by name ascending
# Note: itemgetter can't handle negative values, so we need to sort twice
sorted_students = sorted(filtered_students, key=itemgetter('name'))
sorted_students = sorted(sorted_students, key=itemgetter('score'), reverse=True)
```

### Approach 5: Custom Sorting Function
```python
def sort_key(student):
    """Custom sorting function for students."""
    return (-student['score'], student['name'])

filtered_students = [s for s in students if s['score'] > 80]
sorted_students = sorted(filtered_students, key=sort_key)
```

## 🔍 Code Breakdown

### Understanding the Lambda Function:
```python
sorted(filtered_students, key=lambda x: (-x['score'], x['name']))
#                              │       │  │           │
#                              │       │  │           └─ Alphabetical (ascending)
#                              │       │  └─ Negative for descending sort
#                              │       └─ Parameter (each student dict)
#                              └─ Anonymous function

# The tuple (-x['score'], x['name']) creates a compound sort key:
# 1. Primary: Score in descending order (negative makes it descending)
# 2. Secondary: Name in ascending order (alphabetical)
```

### Why Use Negative for Descending?
```python
# Without negative (ascending):
scores = [88, 72, 95, 88, 79]
sorted(scores)  # [72, 79, 88, 88, 95]

# With negative (descending):
sorted(scores, key=lambda x: -x)  # [95, 88, 88, 79, 72]

# Alternative using reverse=True:
sorted(scores, reverse=True)  # [95, 88, 88, 79, 72]
```

### Understanding Tuple Sorting:
```python
# When sorting by tuples, Python compares element by element:
data = [
    (-95, 'Charlie'),  # First by score: -95 < -88, so Charlie is first
    (-88, 'Alice'),    # Same score, so compare by name: 'Alice' < 'David'
    (-88, 'David')
]
sorted(data)  # [(-95, 'Charlie'), (-88, 'Alice'), (-88, 'David')]
```

## 🎓 Key Takeaways

1. **`sorted()` vs `.sort()`**: 
   - `sorted()` returns a new list
   - `.sort()` modifies the list in place
2. **Lambda functions** are perfect for simple sorting logic
3. **Tuple sorting** allows multi-level sorting in one pass
4. **Negative values** reverse numeric sorting order
5. **List comprehensions** are efficient for filtering
6. **Operator module** provides cleaner alternatives for simple operations

## 🚀 Variations to Try

### Challenge Yourself:

1. **Add grade letters (A, B, C, etc.) based on score**
2. **Find the top N students**
3. **Group students by score ranges**
4. **Calculate class statistics (average, median)**
5. **Create a function that accepts custom thresholds**

### Example Solutions:

**Add Grade Letters:**
```python
def get_grade(score):
    if score >= 90: return 'A'
    if score >= 80: return 'B'
    if score >= 70: return 'C'
    if score >= 60: return 'D'
    return 'F'

students_with_grades = [
    {**s, 'grade': get_grade(s['score'])} for s in sorted_students
]
```

**Top N Students:**
```python
def get_top_students(students, n, min_score=0):
    filtered = [s for s in students if s['score'] > min_score]
    sorted_students = sorted(filtered, key=lambda x: (-x['score'], x['name']))
    return sorted_students[:n]

top_3 = get_top_students(students, 3, min_score=80)
```

**Group by Score Range:**
```python
from collections import defaultdict

def group_by_score_range(students, range_size=10):
    groups = defaultdict(list)
    for student in students:
        range_key = (student['score'] // range_size) * range_size
        groups[range_key].append(student)
    return dict(groups)

grouped = group_by_score_range(students)
# {70: [Bob, Eve], 80: [Alice, David], 90: [Charlie]}
```

**Class Statistics:**
```python
def calculate_stats(students):
    scores = [s['score'] for s in students]
    return {
        'average': sum(scores) / len(scores),
        'highest': max(scores),
        'lowest': min(scores),
        'median': sorted(scores)[len(scores) // 2],
        'total_students': len(students)
    }
```

**Reusable Function:**
```python
def rank_students(students, min_score=0, max_results=None):
    """
    Rank students by score with optional filtering.
    
    Args:
        students (list): List of student dictionaries
        min_score (int): Minimum score threshold (default: 0)
        max_results (int): Maximum number of results (default: None)
    
    Returns:
        list: Sorted and filtered list of students
    """
    # Filter
    filtered = [s for s in students if s['score'] > min_score]
    
    # Sort
    sorted_students = sorted(filtered, key=lambda x: (-x['score'], x['name']))
    
    # Limit results if specified
    return sorted_students[:max_results] if max_results else sorted_students
```

## 📊 Performance Comparison

| Approach | Readability | Performance | Best For |
|----------|-------------|-------------|----------|
| Lambda with tuple | Excellent | O(n log n) | Single-pass sorting |
| Double sort | Good | O(n log n) | Stable sorting needed |
| filter() + sorted() | Good | O(n log n) | Functional programming |
| itemgetter | Fair | O(n log n) | Simple key extraction |

## 🔗 Related Topics to Explore

- `operator` module (`itemgetter`, `attrgetter`)
- Stable sorting vs unstable sorting
- Custom comparison functions with `functools.cmp_to_key`
- Sorting complex nested structures
- Performance: `sorted()` vs `.sort()`
- `heapq` for finding top-k elements efficiently

## 💡 Real-World Applications

- **Leaderboards**: Game rankings, competition results
- **Academic Systems**: Student rankings, honor rolls
- **E-commerce**: Product sorting by rating and price
- **HR Systems**: Employee performance rankings
- **Analytics**: Ranking metrics with tie-breakers

## 🐛 Common Mistakes to Avoid

```python
# ❌ Wrong: Trying to use reverse with tuple sorting
sorted(students, key=lambda x: (x['score'], x['name']), reverse=True)
# This reverses BOTH score and name sorting

# ✅ Correct: Use negative for score only
sorted(students, key=lambda x: (-x['score'], x['name']))

# ❌ Wrong: Forgetting to filter
sorted_students = sorted(students, key=lambda x: (-x['score'], x['name']))
# This includes ALL students, even those with score <= 80

# ✅ Correct: Filter first
filtered = [s for s in students if s['score'] > 80]
sorted_students = sorted(filtered, key=lambda x: (-x['score'], x['name']))
```

## 🧪 Testing Your Solution

```python
# Test cases
test_students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 72},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 88},
    {"name": "Eve", "score": 79}
]

result = rank_students(test_students, min_score=80)

# Expected output
expected = [
    {"name": "Charlie", "score": 95},
    {"name": "Alice", "score": 88},
    {"name": "David", "score": 88}
]

assert result == expected, "Test failed!"
print("✅ All tests passed!")
```

---

**Date Completed:** Day 3  
**Difficulty:** ⭐⭐⭐☆☆ (Intermediate)  
**Time Spent:** ~45 minutes  
**Skills Gained:** Sorting, filtering, lambda functions, tuple sorting, multi-level sorting
