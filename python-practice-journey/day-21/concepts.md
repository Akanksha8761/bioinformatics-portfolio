# Day 21: NumPy Introduction - Concepts

## 📌 Core Concepts Covered

NumPy (Numerical Python) is the foundational library for scientific computing in Python. It provides powerful N-dimensional arrays, mathematical functions, and tools for working with numerical data. It is the backbone of pandas, scikit-learn, TensorFlow, and virtually every data science and AI/ML library!

---

## 1. Why NumPy?

### **Python Lists vs NumPy Arrays:**

| Feature | Python List | NumPy Array |
|---------|-------------|-------------|
| Type | Heterogeneous | Homogeneous |
| Speed | Slow | Fast (C backend) |
| Memory | High | Low |
| Math | Manual loops | Built-in vectorized |
| Dimensions | Nested lists | True N-D arrays |

### **Speed Comparison:**
```python
import numpy as np
import time

# Python list - slow
py_list = list(range(1_000_000))
start = time.time()
result = [x**2 for x in py_list]
print(f"List: {time.time() - start:.4f}s")

# NumPy - fast!
np_array = np.arange(1_000_000)
start = time.time()
result = np_array ** 2
print(f"NumPy: {time.time() - start:.4f}s")
# NumPy is typically 10-100x faster!
```

---

## 2. Creating NumPy Arrays

### **From Python Lists:**
```python
# 1D array (vector)
arr_1d = np.array([1, 2, 3, 4, 5])
# Shape: (5,)

# 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# Shape: (2, 3)

# Specifying dtype
arr_float = np.array([1, 2, 3], dtype=float)
arr_complex = np.array([1+2j, 2+4j], dtype=complex)
```

### **Built-in Creation Functions:**

| Function | Description | Example |
|----------|-------------|---------|
| `np.zeros(n)` | Array of zeros | `np.zeros(5)` → `[0. 0. 0. 0. 0.]` |
| `np.ones(n)` | Array of ones | `np.ones(3)` → `[1. 1. 1.]` |
| `np.full(shape, val)` | Array filled with value | `np.full((2,3), 7)` |
| `np.eye(n)` | Identity matrix | `np.eye(3)` |
| `np.arange(start, stop, step)` | Like Python range | `np.arange(0, 10, 2)` |
| `np.linspace(start, stop, n)` | n evenly spaced points | `np.linspace(0, 1, 5)` |
| `np.random.rand(n)` | Uniform [0,1) | `np.random.rand(5)` |
| `np.random.randn(n)` | Standard normal | `np.random.randn(5)` |
| `np.random.randint(low, high, size)` | Random integers | `np.random.randint(0, 10, 5)` |

### **arange vs linspace:**
```python
np.arange(0, 1, 0.2)   # [0.0, 0.2, 0.4, 0.6, 0.8] - specify STEP
np.linspace(0, 1, 5)   # [0.0, 0.25, 0.5, 0.75, 1.0] - specify COUNT
```

---

## 3. Array Attributes

Every NumPy array has these key attributes:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.ndim      # 2       - number of dimensions
arr.shape     # (2, 3)  - (rows, columns)
arr.size      # 6       - total elements
arr.dtype     # int64   - element data type
arr.itemsize  # 8       - bytes per element
arr.nbytes    # 48      - total bytes (size × itemsize)
```

### **Common dtypes:**

| dtype | Description |
|-------|-------------|
| `int32`, `int64` | Integer |
| `float32`, `float64` | Floating point |
| `complex64`, `complex128` | Complex number |
| `bool` | Boolean |
| `np.int16` | 16-bit integer (less memory) |

---

## 4. Indexing

### **1D Indexing:**
```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]    # 10   (first element)
arr[-1]   # 50   (last element)
arr[2]    # 30   (third element)

arr[0] = 99      # Modify element - arrays are MUTABLE
```

### **2D Indexing:**
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

arr[0, 0]  # 1  (row 0, col 0)
arr[1, 2]  # 6  (row 1, col 2)
arr[-1, -1]  # 9  (last row, last col)

arr[1, 2] = 99  # Modify element
```

---

## 5. Slicing

### **1D Slicing:**
```python
arr = np.arange(10)  # [0, 1, 2, ..., 9]

arr[2:5]    # [2, 3, 4]        (index 2 to 4)
arr[:5]     # [0, 1, 2, 3, 4]  (start to 4)
arr[5:]     # [5, 6, 7, 8, 9]  (5 to end)
arr[::2]    # [0, 2, 4, 6, 8]  (every 2nd)
arr[::-1]   # [9, 8, ..., 0]   (reversed!)
```

### **2D Slicing:**
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

arr[0:2]         # First 2 rows: [[1,2,3],[4,5,6]]
arr[:, 0:2]      # All rows, first 2 cols
arr[1:3, 0:2]    # Rows 1-2, cols 0-1 (sub-matrix)
arr[1, :]        # Row 1 as 1D: [4, 5, 6]
arr[:, 1]        # Col 1 as 1D: [2, 5, 8]
```

### **⚠️ CRITICAL: Slices are VIEWS, not copies!**
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
view = arr[:, 0:2]   # This is a VIEW

view[:, :] = 99      # Modifies ORIGINAL arr too!
print(arr)           # [[99, 99, 3], [99, 99, 6]]

# To make a copy:
copy = arr[:, 0:2].copy()
copy[:, :] = 0       # Does NOT affect arr
```

---

## 6. Arithmetic Operations (Vectorized)

NumPy operations are **element-wise** by default:

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

a + b   # [11, 22, 33, 44, 55]
b - a   # [9, 18, 27, 36, 45]
a * b   # [10, 40, 90, 160, 250]
b / a   # [10.0, 10.0, 10.0, 10.0, 10.0]
a ** 2  # [1, 4, 9, 16, 25]
```

### **Scalar Operations:**
```python
a + 5   # [6, 7, 8, 9, 10]   (adds 5 to every element)
a * 2   # [2, 4, 6, 8, 10]   (multiplies every element)
```

### **Comparison Operations:**
```python
a > 2   # [False, False, True, True, True]
a == 3  # [False, False, True, False, False]
```

---

## 7. Universal Functions (ufuncs)

Mathematical functions applied element-wise:

### **Trigonometric:**
```python
x = np.array([0, np.pi/2, np.pi])
np.sin(x)   # [0.0, 1.0, 0.0] (approx)
np.cos(x)   # [1.0, 0.0, -1.0] (approx)
np.tan(x)
```

### **Exponential & Logarithmic:**
```python
x = np.array([1, 2, 3])
np.exp(x)    # [2.718, 7.389, 20.086]  (e^x)
np.log(x)    # [0.0, 0.693, 1.099]     (natural log)
np.log10(x)  # [0.0, 0.301, 0.477]     (base 10 log)
np.log2(x)   # [0.0, 1.0, 1.585]       (base 2 log)
np.sqrt(x)   # [1.0, 1.414, 1.732]
```

### **Others:**
```python
np.abs(x)    # Absolute value
np.round(x)  # Round to nearest integer
np.floor(x)  # Round down
np.ceil(x)   # Round up
```

---

## 8. Aggregation Functions

Compute statistics over arrays:

```python
arr = np.array([1, 2, 3, 4, 5])

arr.sum()       # 15
arr.min()       # 1
arr.max()       # 5
arr.mean()      # 3.0
arr.std()       # standard deviation
arr.var()       # variance
np.median(arr)  # 3.0  ← Only via np.median(), NOT arr.median()!

# argmin/argmax return INDEX of min/max
arr.argmin()    # 0  (index of minimum)
arr.argmax()    # 4  (index of maximum)
```

### **⚠️ median has no array method!**
```python
arr.median()     # AttributeError! 
np.median(arr)   # ✓ Correct!
```

### **Axis parameter for 2D:**
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

arr.sum()           # 45  (all elements)
arr.sum(axis=0)     # [12, 15, 18] (sum DOWN columns)
arr.sum(axis=1)     # [6, 15, 24]  (sum ACROSS rows)
arr.mean(axis=0)    # [4., 5., 6.] (mean of each column)
arr.mean(axis=1)    # [2., 5., 8.] (mean of each row)
```

**Axis Memory Aid:**
- `axis=0` → collapses rows → result has shape of columns
- `axis=1` → collapses columns → result has shape of rows

---

## 9. Broadcasting

Broadcasting allows operations between arrays of **different shapes**.

### **Rules:**
1. Arrays are compared dimension by dimension (right to left)
2. Dimensions are compatible if they are **equal** or one is **1**
3. The array with dimension 1 is "stretched" to match

### **Examples:**

```python
# Scalar broadcast
arr = np.array([1, 2, 3])   # shape (3,)
arr + 10                     # 10 → shape (1,) → stretched to (3,)
# Result: [11, 12, 13]

# 2D + 1D row vector
mat = np.ones((3, 3))        # shape (3, 3)
row = np.array([1, 2, 3])   # shape (3,)    → broadcast to (3, 3)
mat + row
# [[2, 3, 4],
#  [2, 3, 4],
#  [2, 3, 4]]

# 2D + 1D column vector
col = np.array([[10], [20], [30]])  # shape (3, 1) → broadcast to (3, 3)
mat + col
# [[11, 11, 11],
#  [21, 21, 21],
#  [31, 31, 31]]
```

### **Incompatible shapes → ValueError:**
```python
a = np.array([1, 2, 3, 4])    # shape (4,)
b = np.array([[1, 2, 3]])     # shape (1, 3)
a + b   # ValueError! (4 ≠ 3, neither is 1)

# Handle with try-except:
try:
    result = a + b
except ValueError as e:
    print(f"Shape error: {e}")
```

---

## 10. Bioinformatics with NumPy

### **Gene Expression Analysis:**
```python
# Store expression values for multiple genes/samples
expression_matrix = np.array([
    [120.5, 88.3, 210.1],   # Gene 1 across 3 samples
    [45.2,  95.0,  55.7],   # Gene 2
    [230.8, 180.3, 190.2],  # Gene 3
])

# Statistics per gene (axis=1)
mean_per_gene = expression_matrix.mean(axis=1)
std_per_gene = expression_matrix.std(axis=1)

# Statistics per sample (axis=0)
mean_per_sample = expression_matrix.mean(axis=0)

# Normalize (z-score)
gene_means = expression_matrix.mean(axis=1, keepdims=True)
gene_stds = expression_matrix.std(axis=1, keepdims=True)
normalized = (expression_matrix - gene_means) / gene_stds
```

### **Methylation Data:**
```python
methylation = np.random.rand(1000)    # 1000 CpG sites

high_meth = methylation[methylation > 0.75]    # Boolean indexing!
low_meth  = methylation[methylation < 0.25]

print(f"Hypermethylated: {len(high_meth)}")
print(f"Hypomethylated:  {len(low_meth)}")
print(f"Mean: {methylation.mean():.3f}")
```

---

## 💡 Key Takeaways

1. **NumPy arrays are faster and more memory-efficient** than Python lists
2. **Arrays are homogeneous** - all elements same type
3. **Element-wise operations** - no loops needed!
4. **Shape and dtype** - always check these attributes
5. **Slices are views** - modifications affect original!
6. **median only via np.median()** - no array method
7. **axis=0 → down columns**, axis=1 → across rows
8. **Broadcasting** allows flexible array math
9. **ufuncs** apply functions element-wise efficiently
10. **Foundation of all AI/ML libraries** - master this!

---

## 📚 Quick Reference

| Task | Code |
|------|------|
| Create from list | `np.array([1,2,3])` |
| Create zeros | `np.zeros((3,4))` |
| Create range | `np.arange(0,10,2)` |
| Create linspace | `np.linspace(0,1,100)` |
| Shape | `arr.shape` |
| Total elements | `arr.size` |
| Data type | `arr.dtype` |
| Sum all | `arr.sum()` |
| Sum columns | `arr.sum(axis=0)` |
| Sum rows | `arr.sum(axis=1)` |
| Median | `np.median(arr)` |
| Slice view | `arr[1:3, 0:2]` |
| Copy | `arr.copy()` |

---

*NumPy is the foundation of Python's entire scientific and AI/ML ecosystem. Everything builds on it!*
