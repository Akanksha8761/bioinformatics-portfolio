# Day 22: NumPy Advanced - Learning Notes

**Date:** February 7, 2026
**Topic:** NumPy Advanced - Reshaping, Masking, Stacking, File I/O, Linear Algebra
**Status:** ✅ Completed
**Week:** 5 - Day 2

---

## 📝 What I Learned Today

Today I went DEEP into NumPy! Reshaping, flattening, boolean masking, stacking, splitting, file I/O, and linear algebra. These are the tools that make real data science and AI/ML possible. Every concept today directly connects to how pandas, scikit-learn, and TensorFlow work!

---

## 🎯 Key Insights

### 1. Reshape: Shape Changes, Data Stays

```python
arr = np.arange(20)        # [0,1,...,19]

arr.reshape(4, 5)          # 4×5 grid
arr.reshape(2, 2, 5)       # 3D: 2 blocks × 2 rows × 5 cols
arr.reshape(-1, 4)         # Auto-infer rows = 5
```

**Rule: total elements must match!**
3×5=15 ≠ 20 → ValueError!

### 2. The -1 Trick is Incredibly Useful

```python
images = np.random.rand(100, 28, 28)  # 100 images, 28×28
flat = images.reshape(100, -1)         # → (100, 784)
# NumPy calculates: 28×28 = 784 for me!
```

**Used constantly in ML to flatten feature arrays!**

### 3. ravel vs flatten - Critical Difference

```python
arr = np.array([[1,2,3],[4,5,6]])

r = arr.ravel()     # VIEW - fast, shares memory
r[0] = 99           # arr ALSO changes!

f = arr.flatten()   # COPY - safe, independent
f[0] = 99           # arr unchanged
```

**Rule: ravel = risky (view), flatten = safe (copy)**

### 4. Boolean Masking - The Data Science Superpower

```python
# No loops needed for filtering!
data = np.array([...])

# Basic
high = data[data > 100]

# Compound - MUST use & | ~ not and/or/not!
selected = data[(data > 50) & (data < 200)]

# Modify in place
data[data < 0] = 0   # Replace negatives with 0
```

**This replaces for loops for filtering!**

### 5. Stacking Functions

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

np.vstack((a, b))          # [[1,2,3],[4,5,6]] shape (2,3) - adds rows
np.hstack((a, b))          # [1,2,3,4,5,6] shape (6,) - flat for 1D
np.column_stack((a, b))    # [[1,4],[2,5],[3,6]] shape (3,2) - as columns!
```

**column_stack** was the surprise - it treats 1D arrays as columns!

### 6. File I/O - Saving Real Results

```python
# Binary (fast, preserves dtype)
np.save("results.npy", arr)
arr = np.load("results.npy")

# Multiple arrays
np.savez("dataset.npz", X=features, y=labels)
data = np.load("dataset.npz")
X, y = data['X'], data['y']
data.close()

# CSV (human-readable)
np.savetxt("data.csv", arr, delimiter=",")
arr = np.loadtxt("data.csv", delimiter=",", skiprows=1)
```

### 7. Linear Algebra Connects to AI/ML

```python
# This is what neural networks do at each layer!
output = weights @ input + bias

# This is PCA!
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
```

---

## 💪 What I Practiced Today

1. ✅ Reshape (2D, 3D, -1 inference)
2. ✅ ravel() vs flatten() (view vs copy)
3. ✅ Boolean masking (simple and compound)
4. ✅ vstack, hstack, column_stack
5. ✅ hsplit, vsplit, split
6. ✅ File I/O (.npy, .npz, .csv, genfromtxt)
7. ✅ Linear algebra (dot, @, inv, eig, trace)

---

## 🤔 Challenges Faced

### 1. column_stack vs hstack for 1D

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

np.hstack((a, b))         # [1,2,3,4,5,6]  - flat!
np.column_stack((a, b))   # [[1,4],[2,5],[3,6]] - as columns!
```

**Different results for 1D arrays!**

### 2. Boolean operators

Python's `and`/`or`/`not` don't work with arrays!
Must use `&`, `|`, `~` with parentheses:

```python
# WRONG:
arr[arr > 3 and arr < 7]

# RIGHT:
arr[(arr > 3) & (arr < 7)]
```

### 3. Understanding Matrix Rank

The 3×3 matrix `[[7,8,9],[10,11,12],[13,14,15]]` has rank 2, not 3! Rows are linearly dependent (row3 = row2 + row1 difference). This means the matrix is singular (no inverse)!

---

## 💡 Aha Moments

### 1. reshape(-1, 784) in ML!

```python
# Images in ML
X_train = images.reshape(n_samples, -1)   # Flatten each image!
# This is done in EVERY image classification tutorial!
```

**NOW I understand why!**

### 2. Boolean Masking = Vectorized Filtering

```python
# Python (slow):
result = [x for x in data if x > threshold]

# NumPy (fast, elegant):
result = data[data > threshold]
```

**Same result, but NumPy is orders of magnitude faster!**

### 3. @ is Matrix Multiply, * is Element-wise

```python
A @ B     # Matrix multiplication (rows × cols)
A * B     # Element-wise multiplication (same shape)
```

**Critical distinction in AI/ML!**

### 4. .npz Files Are Like Dictionaries

```python
np.savez("dataset.npz", X=features, y=labels, info=metadata)
data = np.load("dataset.npz")
# Access by name, just like a dict!
X = data['X']
```

**Perfect for saving complete datasets!**

---

## 🧬 Bioinformatics Applications

### Reshape for Analysis
```python
# 1000 genes, 3 samples - reshape for different analyses
expr = np.random.rand(1000, 3)
expr_flat = expr.ravel()         # All values as 1D

# Batch processing - reshape to groups of 100
batches = expr.reshape(10, 100, 3)   # 10 batches × 100 genes × 3 samples
```

### Boolean Masking for Gene Filtering
```python
expression = np.array([120.5, 45.2, 230.8, 12.5, 180.3])

# High expression genes
high = expression[expression > 100]     # [120.5, 230.8, 180.3]

# Dysregulated genes
dysregulated = expression[(expression < 20) | (expression > 200)]
```

### Save/Load Datasets
```python
# Save complete experiment
np.savez("methylation_study.npz",
         methylation=meth_values,
         gene_names=gene_ids,
         sample_ids=sample_names)

# Load next session
study = np.load("methylation_study.npz")
meth = study['methylation']
study.close()
```

---

## 🎯 Self-Assessment

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)
**Confidence:** ⭐⭐⭐⭐⭐ (5/5)
**Application:** ⭐⭐⭐⭐⭐ (5/5)

---

## 🏆 Achievements Today

- ✅ Reshape mastery (including -1 trick)
- ✅ ravel vs flatten distinction
- ✅ Boolean masking
- ✅ All stacking functions
- ✅ File I/O (.npy, .npz, .csv)
- ✅ Linear algebra foundations
- ✅ **NUMPY COMPLETE!**

---

## 🚀 What's Next

- **Pandas** - DataFrames for structured data
- **Matplotlib** - Data visualization
- Moving toward ML applications!

---

## 💬 Key Quotes

> "reshape(-1, n) - let NumPy figure out the other dimension!"

> "ravel=view (fast), flatten=copy (safe)"

> "Boolean masking: vectorized filtering, no loops!"

> "@ is matrix multiply, * is element-wise"

> ".npz files = NumPy's dictionary for arrays"

---

## 📊 Day 22 Stats

**Time Spent:** ~3 hours
**Concepts Mastered:** 12
**Operations Practiced:** 40+
**Confidence:** Expert!

---

*Day 22 complete! NumPy Advanced mastered! Ready for Pandas! 🚀*
