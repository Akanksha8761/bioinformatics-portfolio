# Day 22: NumPy Advanced - Concepts

## 📌 Core Concepts Covered

Building on Day 21's foundation, today we master reshaping, flattening, boolean masking, fancy indexing, file I/O, and linear algebra — the tools professionals use every day in data science and AI/ML!

---

## 1. Reshaping Arrays

Changing the **shape** of an array WITHOUT changing its data.

### **Key Rule: Total elements must match!**
```python
arr = np.arange(20)   # 20 elements

arr.reshape(5, 4)     # 5×4  = 20 ✓
arr.reshape(4, 5)     # 4×5  = 20 ✓
arr.reshape(2, 2, 5)  # 2×2×5 = 20 ✓
arr.reshape(3, 5)     # 3×5  = 15 ✗ ValueError!
```

### **The -1 Trick (Auto-infer dimension):**
```python
arr = np.arange(20)

arr.reshape(10, -1)   # -1 → infers 2  (20/10=2) → shape (10,2)
arr.reshape(-1, 10)   # -1 → infers 2  (20/10=2) → shape (2,10)
arr.reshape(-1, 4)    # -1 → infers 5  (20/4=5)  → shape (5,4)
arr.reshape(2, 2, -1) # -1 → infers 5  (20/4=5)  → shape (2,2,5)
```

**Only ONE -1 allowed per reshape!**

### **reshape returns a VIEW:**
```python
arr = np.arange(20)
view = arr.reshape(4, 5)
view[0, 0] = 99        # Modifies arr too!
print(arr[0])          # 99
```

---

## 2. Flattening: ravel() vs flatten()

Both convert multi-dimensional arrays to 1D:

| Feature | `ravel()` | `flatten()` |
|---------|-----------|-------------|
| Returns | VIEW (if possible) | Always COPY |
| Memory | Efficient | Independent |
| Speed | Faster | Slightly slower |
| Safety | Modifies original | Original safe |

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

# ravel - VIEW
r = arr.ravel()
r[0] = 99    # arr ALSO changes!

# flatten - COPY
f = arr.flatten()
f[0] = 99    # arr UNCHANGED

# Ordering options
arr.flatten('C')   # Row-major (C order)   [1,2,3,4,5,6]
arr.flatten('F')   # Col-major (Fortran)   [1,4,2,5,3,6]
```

---

## 3. Boolean Array Masking

One of NumPy's most powerful features - filter data without loops!

### **Basic Masking:**
```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

mask = arr > 5             # [F, F, F, F, F, T, T, T, T]
arr[mask]                  # [6, 7, 8, 9]

# Inline (more common)
arr[arr > 5]               # Same result
```

### **Compound Conditions:**
```python
arr = np.arange(10)

# MUST use & | ~ (NOT Python's and/or/not!)
arr[(arr > 3) & (arr < 7)]   # AND: [4, 5, 6]
arr[(arr < 3) | (arr > 7)]   # OR:  [0, 1, 2, 8, 9]
arr[~(arr > 5)]              # NOT: [0, 1, 2, 3, 4, 5]
```

### **Modifying with Boolean Indexing:**
```python
arr = np.arange(20)
arr[arr > 10] = 0       # Set all elements > 10 to 0

mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat[mat > 5] = 100      # Works on 2D too!
```

### **⚠️ Use & | ~ not and/or/not!**
```python
arr[(arr > 3) and (arr < 7)]   # TypeError!
arr[(arr > 3) & (arr < 7)]     # Correct ✓
```

---

## 4. Stacking Arrays

### **vstack (vertical - adds rows):**
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.vstack((a, b))    # [[1,2,3],   shape (2,3)
                     #  [4,5,6]]
```

### **hstack (horizontal - adds columns):**
```python
np.hstack((a, b))    # [1,2,3,4,5,6]  shape (6,) for 1D
                     # For 2D: extends columns
```

### **column_stack (1D arrays become columns):**
```python
np.column_stack((a, b))  # [[1,4],   shape (3,2)
                          #  [2,5],
                          #  [3,6]]
```

### **concatenate (most general):**
```python
np.concatenate((a, b), axis=0)    # Like hstack for 1D
np.concatenate((A, B), axis=0)    # Stack rows (like vstack)
np.concatenate((A, B), axis=1)    # Stack cols (like hstack)
```

### **Summary table:**

| Function | 1D result | 2D result |
|----------|-----------|-----------|
| `vstack` | Stacks as rows | Adds rows |
| `hstack` | Concatenates flat | Adds columns |
| `column_stack` | Treats as columns | Adds columns |
| `concatenate` | Flexible with axis | Flexible with axis |

---

## 5. Splitting Arrays

### **hsplit (split columns):**
```python
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

np.hsplit(arr, 4)       # 4 equal column slices
np.hsplit(arr, [1, 3])  # Split at col 1 and col 3
```

### **vsplit (split rows):**
```python
np.vsplit(arr, 3)       # 3 equal row slices
np.vsplit(arr, [1, 2])  # Split at row 1 and row 2
```

### **split (general):**
```python
np.split(arr, 3, axis=0)       # 3 equal row splits
np.split(arr, [1, 2], axis=0)  # Split at rows 1 and 2
np.split(arr, 2, axis=1)       # 2 equal column splits
```

---

## 6. Fancy Indexing

Using **arrays of indices** to select elements:

### **1D Fancy Indexing:**
```python
arr = np.arange(10, 20)    # [10,11,...,19]

arr[[0, 3, 7]]             # [10, 13, 17]

# 2D index array - result shape matches index shape!
idx = np.array([[0, 1], [2, 3]])
arr[idx]                   # shape (2,2)
```

### **2D Fancy Indexing:**
```python
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])

mat[[0, 2], :]         # Rows 0 and 2
mat[:, [0, 2]]         # Columns 0 and 2

# Specific (row,col) pairs:
mat[[0, 1, 2], [2, 0, 1]]   # [mat[0,2], mat[1,0], mat[2,1]]
                              # [3, 4, 8]
```

### **Boolean vs Fancy Indexing:**
```python
# Boolean - condition-based filtering
arr[arr > 5]            # Returns elements matching condition

# Fancy - index-based selection
arr[[0, 2, 4]]          # Returns elements at specific indices
```

---

## 7. NumPy File I/O

### **Binary Format (.npy) - Single Array:**
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

np.save("data.npy", arr)         # Save
loaded = np.load("data.npy")     # Load

np.array_equal(arr, loaded)      # True
```

### **Binary Format (.npz) - Multiple Arrays:**
```python
np.savez("data.npz",
         gene_names=names,
         expression=values,
         metadata=meta)

loaded = np.load("data.npz")
print(list(loaded.keys()))       # ['gene_names', 'expression', 'metadata']
expression = loaded['expression']
loaded.close()                   # Important!
```

### **Text Format (.csv/.txt):**
```python
# Save CSV
np.savetxt("data.csv", arr,
           delimiter=",",
           fmt="%.4f",
           header="col1,col2,col3",
           comments="")

# Load CSV
loaded = np.loadtxt("data.csv",
                    delimiter=",",
                    skiprows=1,
                    dtype=float)
```

### **Handling Missing Values:**
```python
# genfromtxt handles NaN gracefully
loaded = np.genfromtxt("data_with_missing.txt",
                        delimiter=",")   # NaN for missing

# Replace NaN
cleaned = np.nan_to_num(loaded, nan=0)
```

### **Format Comparison:**

| Format | Function | Binary? | Multiple? | Human-readable? |
|--------|----------|---------|-----------|-----------------|
| .npy | save/load | Yes | No | No |
| .npz | savez/load | Yes | Yes | No |
| .csv/.txt | savetxt/loadtxt | No | No | Yes |

---

## 8. Linear Algebra (np.linalg)

### **Dot Product:**
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.dot(a, b)    # 1×4 + 2×5 + 3×6 = 32
```

### **Matrix Multiplication:**
```python
A = np.array([[1,2],[3,4]])   # (2×2)
B = np.array([[5,6],[7,8]])   # (2×2)

A @ B             # (2×2) result - preferred
np.matmul(A, B)   # Same result
# Note: np.dot() also works for 2D but @ is cleaner
```

### **Transpose:**
```python
arr.T             # Transpose
```

### **Inverse:**
```python
inv = np.linalg.inv(A)       # A must be square and invertible
A @ inv                       # Should give identity matrix
```

### **Determinant:**
```python
det = np.linalg.det(A)
```

### **Eigenvalues & Eigenvectors:**
```python
values, vectors = np.linalg.eig(A)
```

### **Matrix Rank:**
```python
rank = np.linalg.matrix_rank(A)
```

### **Trace:**
```python
np.trace(A)    # Sum of diagonal elements
```

### **Why Linear Algebra Matters for AI/ML:**
- **Neural networks**: weight matrix multiplication
- **PCA**: eigenvalues for dimensionality reduction
- **Least squares**: solving systems of equations
- **Covariance matrices**: data statistics

---

## 💡 Key Takeaways

1. **reshape** changes shape without changing data (must match total elements)
2. **-1 in reshape** lets NumPy infer that dimension
3. **reshape returns a VIEW** - modifying it modifies original!
4. **ravel() = view**, **flatten() = copy** - know the difference!
5. **Boolean masking** filters arrays with conditions (no loops!)
6. **Use & | ~ not and/or/not** with boolean arrays
7. **vstack adds rows**, **hstack adds columns**
8. **column_stack** turns 1D arrays into columns of a 2D array
9. **Fancy indexing** selects specific elements by index
10. **.npy/.npz for binary**, **.csv for text**, **genfromtxt for messy data**
11. **np.linalg** provides all linear algebra operations
12. **Matrix multiply** uses @ operator (not *)

---

## 📚 Quick Reference

| Task | Code |
|------|------|
| Reshape | `arr.reshape(3, 4)` |
| Infer dim | `arr.reshape(-1, 4)` |
| Flatten (view) | `arr.ravel()` |
| Flatten (copy) | `arr.flatten()` |
| Boolean filter | `arr[arr > 5]` |
| AND condition | `arr[(arr>3) & (arr<7)]` |
| Fancy index | `arr[[0, 2, 5]]` |
| Stack rows | `np.vstack((a, b))` |
| Stack cols | `np.hstack((a, b))` |
| 1D → columns | `np.column_stack((a, b))` |
| Split cols | `np.hsplit(arr, n)` |
| Split rows | `np.vsplit(arr, n)` |
| Save binary | `np.save("f.npy", arr)` |
| Load binary | `np.load("f.npy")` |
| Save multi | `np.savez("f.npz", a=arr1, b=arr2)` |
| Save text | `np.savetxt("f.csv", arr, delimiter=",")` |
| Dot product | `np.dot(a, b)` |
| Matrix mult | `A @ B` |
| Inverse | `np.linalg.inv(A)` |
| Eigenvalues | `np.linalg.eig(A)` |

---

*NumPy advanced features are the backbone of all scientific computing and AI/ML in Python. Master them to work with real data efficiently!*
