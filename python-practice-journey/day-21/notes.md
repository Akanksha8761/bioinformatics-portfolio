# Day 21: NumPy Introduction - Learning Notes

**Date:** February 6, 2026
**Topic:** NumPy - Numerical Python for Scientific Computing
**Status:** ✅ Completed
**Week:** 5 - Day 1 🎉 NEW WEEK!

---

## 📝 What I Learned Today

Today marks a HUGE milestone - **WEEK 5 begins**, and with it, the transition from core Python to the scientific computing libraries that power AI and ML! NumPy is the foundation of everything: pandas, scikit-learn, TensorFlow, PyTorch all rely on it. Today I mastered arrays, indexing, slicing, arithmetic, aggregation, and broadcasting!

---

## 🎯 Key Insights

### 1. NumPy Arrays vs Python Lists

```python
# Python list - slow, heterogeneous
py_list = [1, "hello", 3.14, True]  # Mixed types!

# NumPy array - fast, homogeneous
np_array = np.array([1, 2, 3, 4])   # Same type!
```

**Why NumPy is faster:**
- C backend (compiled, not interpreted)
- Contiguous memory layout
- Vectorized operations (no Python loops!)
- BLAS/LAPACK linear algebra routines

### 2. Array Attributes I Must Always Know

```python
arr = np.array([[1,2,3],[4,5,6]])

arr.ndim      # 2        (how many dimensions)
arr.shape     # (2, 3)   (rows, columns)
arr.size      # 6        (total elements)
arr.dtype     # int64    (what type of data)
arr.nbytes    # 48       (memory used)
```

**Always check shape and dtype!**

### 3. Creation Functions Cheat Sheet

```python
np.zeros((3,4))          # All zeros
np.ones((2,5))           # All ones
np.full((2,3), 7)        # All 7s
np.eye(3)                # Identity matrix
np.arange(0, 10, 2)      # [0,2,4,6,8] - specify step
np.linspace(0, 1, 100)   # 100 evenly spaced - specify count
np.random.rand(3, 4)     # Random [0,1)
np.random.randint(0,10,(3,4))  # Random integers
```

### 4. The CRITICAL Slice = View Gotcha!

```python
arr = np.array([[1,2,3],[4,5,6]])
view = arr[:, 0:2]   # This is a VIEW (not a copy!)

view[:,:] = 99       # This CHANGES arr too!
print(arr)           # [[99,99,3],[99,99,6]] - CHANGED!

# Want a copy? Use .copy()
copy = arr[:, 0:2].copy()
copy[:,:] = 0        # arr is safe!
```

**This caught me off guard! Always remember: slices = views!**

### 5. median is np.median() ONLY

```python
arr = np.array([1,2,3,4,5])

arr.sum()    # ✓ Works
arr.mean()   # ✓ Works
arr.min()    # ✓ Works
arr.median() # ✗ AttributeError!

np.median(arr)  # ✓ Correct way!
```

**Special case to memorize!**

### 6. axis=0 and axis=1

```python
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

arr.sum(axis=0)  # [12,15,18] - sums DOWN each column
arr.sum(axis=1)  # [6,15,24]  - sums ACROSS each row
```

**Memory trick:**
- axis=0 → collapse rows (result looks like one row)
- axis=1 → collapse columns (result looks like one column)

### 7. Broadcasting is Powerful

```python
mat = np.ones((3,3))
row = np.array([1,2,3])    # shape (3,)
col = np.array([[1],[2],[3]])  # shape (3,1)

mat + row   # Adds row to EVERY row
mat + col   # Adds col to EVERY column
```

**Broadcasting stretches smaller arrays to match larger ones!**

---

## 💪 What I Practiced Today

1. ✅ **Created 1D and 2D arrays** from lists
2. ✅ **Used creation functions** (zeros, ones, eye, arange, linspace, random)
3. ✅ **Checked all attributes** (ndim, shape, size, dtype, itemsize, nbytes)
4. ✅ **Indexed arrays** (1D and 2D, positive and negative)
5. ✅ **Sliced arrays** (1D and 2D, all patterns)
6. ✅ **Observed slice = view** behaviour
7. ✅ **Arithmetic operations** (element-wise, scalar)
8. ✅ **Applied ufuncs** (sin, cos, exp, log, sqrt)
9. ✅ **Aggregation functions** (sum, min, max, mean, std, median, var)
10. ✅ **Axis operations** on 2D arrays
11. ✅ **Broadcasting** (scalar, row vector, column vector)
12. ✅ **Handled incompatible shapes** with try-except

---

## 🤔 Challenges Faced

### 1. arange vs linspace

Both create sequences but differently:
- `arange` = specify the **step size** (like range)
- `linspace` = specify the **number of points**

```python
np.arange(0, 1, 0.1)    # step = 0.1
np.linspace(0, 1, 11)   # 11 points including both ends
```

### 2. Understanding axis parameter

Initially confusing which axis is which.

**Visualization:**
```
         col0 col1 col2
row 0  [  1,   2,   3  ]
row 1  [  4,   5,   6  ]
row 2  [  7,   8,   9  ]

axis=0 ↓ (goes down, collapses rows)
axis=1 → (goes right, collapses columns)
```

### 3. Slice as View

Spent time debugging why original array changed. Now I know - always use `.copy()` when I need an independent copy!

---

## 💡 Aha Moments

### 1. No More Loops!

**Python (slow):**
```python
result = []
for x in data:
    result.append(x ** 2)
```

**NumPy (fast!):**
```python
result = data ** 2  # That's it!
```

**Vectorized operations - no loop needed!**

### 2. Shape is Everything

Understanding shape is KEY to avoiding errors:
```python
arr.shape == (3, 3)   # 3 rows, 3 columns
arr.shape == (3,)     # 1D array with 3 elements
arr.shape == (3, 1)   # Column vector
arr.shape == (1, 3)   # Row vector
```

### 3. NumPy is the Foundation!

```
pandas    → uses NumPy arrays underneath
matplotlib → plots NumPy arrays
scikit-learn → NumPy arrays as input
TensorFlow → tensors extend NumPy concept
PyTorch    → tensors extend NumPy concept
```

**Master NumPy = better at ALL AI/ML libraries!**

### 4. Broadcasting is Vectorized Math

```python
# Normalize each gene's expression (subtract mean, divide by std)
# Without broadcasting - complex loop
# With broadcasting - one line!
normalized = (expression_matrix - mean) / std
```

**This is how real data analysis is done!**

---

## 🧬 Bioinformatics Applications

### Gene Expression Matrix
```python
# 4 genes, 3 samples
expression = np.array([
    [120.5, 88.3,  210.1],
    [45.2,  95.0,  55.7],
    [230.8, 180.3, 190.2],
    [12.5,  25.0,  18.3],
])

# Mean expression per gene
print(expression.mean(axis=1))

# Mean expression per sample
print(expression.mean(axis=0))

# Find highly expressed genes (mean > 100)
gene_means = expression.mean(axis=1)
high_expr = gene_means > 100
print(expression[high_expr])   # Boolean indexing!
```

### Methylation Analysis
```python
# 1000 CpG sites
methylation = np.random.rand(1000)

# Statistics
print(f"Mean: {methylation.mean():.3f}")
print(f"Std:  {methylation.std():.3f}")
print(f"Hypermethylated (>0.75): {(methylation > 0.75).sum()}")
print(f"Hypomethylated (<0.25):  {(methylation < 0.25).sum()}")
```

---

## 🎯 Self-Assessment

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)
**Confidence:** ⭐⭐⭐⭐⭐ (5/5)
**Application:** ⭐⭐⭐⭐⭐ (5/5)

---

## 🏆 Achievements Today

- ✅ Installed and imported NumPy
- ✅ Created arrays multiple ways
- ✅ Mastered all attributes
- ✅ Indexing and slicing (1D and 2D)
- ✅ Understood slice = view
- ✅ Vectorized arithmetic
- ✅ Applied ufuncs
- ✅ Aggregation with axes
- ✅ Broadcasting mastered
- ✅ **WEEK 5 STARTED - SCIENTIFIC COMPUTING!**

---

## 💭 Personal Reflections

### What Surprised Me

NumPy arrays are SO much more powerful than lists. No loops needed for math - it's all done automatically element-wise!

### What Excited Me

The connection to AI/ML! Everything I learn here directly applies to machine learning. This is the foundation of MethylGraph-AI!

### What Challenged Me

The slice = view behaviour was surprising. And remembering axis direction.

### What I Appreciated

How NumPy makes complex scientific operations simple and readable. What would take 20 lines of Python is 1 line of NumPy!

---

## 🚀 What's Next

Week 5 - Scientific Computing and Data Analysis!
- NumPy Advanced (reshaping, stacking, boolean indexing)
- Pandas introduction
- Data analysis and visualization
- Moving toward AI/ML!

---

## 💬 Key Quotes

> "NumPy arrays: no more loops for math!"

> "Slices are VIEWS - use .copy() for independence!"

> "axis=0 goes DOWN columns, axis=1 goes ACROSS rows!"

> "np.median() only - no array method!"

---

## 📊 Day 21 Stats

**Time Spent:** ~3 hours
**Concepts Mastered:** 11
**Array Operations:** 30+
**Confidence:** Expert!

---

*Day 21 complete! NumPy mastered! Scientific computing foundation built! Week 5 begins! 🚀*
