# Day 23: Pandas Introduction - Concepts

## 📌 Core Concepts Covered

Pandas is the primary data analysis library in Python. Built on top of NumPy, it provides two main data structures: **Series** (1D labelled array) and **DataFrame** (2D labelled table). Pandas is ESSENTIAL for data science, bioinformatics, and AI/ML data preparation!

---

## 1. What is Pandas?

### **Pandas vs NumPy:**

| Feature | NumPy | Pandas |
|---------|-------|--------|
| Primary structure | ndarray (homogeneous) | Series / DataFrame |
| Index | Integer position only | Labelled (any type) |
| Column names | None | Yes |
| Mixed types | No | Yes (per column) |
| Missing values | NaN (floats only) | NaN (any column) |
| Best for | Numerical computing | Tabular / structured data |

### **Import convention:**
```python
import pandas as pd
import numpy as np
```

---

## 2. Pandas Series

A **Series** is a 1D labelled array — like a NumPy array but with a named index.

### **Creating Series:**
```python
# From list (default integer index)
pd.Series([1, 2, 3, 4, 5])

# From list with custom index
pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# From NumPy array
pd.Series(np.arange(5), index=['a','b','c','d','e'])

# From dictionary (keys → index)
pd.Series({'TP53': 120.5, 'BRCA1': 88.3, 'MYC': 210.1})

# With name
pd.Series([1,2,3], name='Expression Level')
```

### **Key Attributes:**
```python
s.values     # NumPy array of values
s.index      # Index object
s.dtype      # Data type
s.shape      # (n,)
s.size       # n
s.name       # Name string
s.hasnans    # True if any NaN
```

### **Indexing:**
```python
s['label']     # Label access
s.loc['label'] # Explicit label access (preferred)
s.iloc[2]      # Position access (always use for position!)
```

### **⚠️ Label vs Position Slicing Difference:**
```python
s[:3]          # Position slice - end EXCLUSIVE (like Python)
s['a':'c']     # Label slice   - end INCLUSIVE (unique to pandas!)
```

---

## 3. Pandas DataFrame

A **DataFrame** is a 2D labelled table — like an Excel spreadsheet or SQL table.

### **Creating DataFrames:**

```python
# From dict of lists (keys → column names)
pd.DataFrame({'col1': [1,2,3], 'col2': ['a','b','c']})

# From list of dicts (each dict = one row)
pd.DataFrame([
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob',   'age': 25},
])

# From 2D NumPy array
pd.DataFrame(np.arange(12).reshape(3,4),
             index=['r1','r2','r3'],
             columns=['A','B','C','D'])

# From dict of Series (indices aligned automatically)
pd.DataFrame({'col_a': series1, 'col_b': series2})
```

### **Missing keys → NaN:**
```python
data = [
    {'name': 'Alice', 'age': 30},                  # No score
    {'name': 'Bob',   'age': 25, 'score': 88},     # Has score
]
pd.DataFrame(data)   # Alice's score = NaN
```

---

## 4. DataFrame Attributes & Inspection

```python
df.shape       # (rows, cols)
df.index       # Row index
df.columns     # Column names
df.dtypes      # Data type per column
df.values      # 2D NumPy array
df.ndim        # Always 2
df.size        # rows × cols

df.head(n)     # First n rows (default 5)
df.tail(n)     # Last n rows (default 5)
df.info()      # Summary: dtypes, non-null counts, memory
df.describe()  # Statistics for numeric columns
df.describe(include='all')         # All columns
df.describe(include=['object'])    # Only string columns
```

---

## 5. Selecting Columns

```python
# Single column → returns Series
df['Age']
df.Age          # Attribute access (only if valid identifier, no spaces/special chars)

# Multiple columns → returns DataFrame
df[['Age', 'Name']]
```

**Rule: Single string → Series. List of strings → DataFrame.**

---

## 6. .loc[] and .iloc[]

These are the two primary indexers. Always use them for row selection!

### **.loc[] — Label-based:**
```python
df.loc['S2']                    # Single row (returns Series)
df.loc[['S2', 'S3']]            # Multiple rows (returns DataFrame)
df.loc['S1':'S3']               # Slice (INCLUSIVE at both ends!)
df.loc['S2', 'Age']             # Single cell
df.loc[['S2','S4'], ['Age','Name']]  # Rows + cols by label
df.loc[:, ['Age', 'Name']]      # All rows, specific cols
```

### **.iloc[] — Integer position-based:**
```python
df.iloc[1]                      # Single row by position
df.iloc[[1, 3]]                 # Multiple rows
df.iloc[0:3]                    # Slice (EXCLUSIVE at end, like Python!)
df.iloc[1, 2]                   # Single cell (row 1, col 2)
df.iloc[[2,3], [1,2]]           # Rows + cols by position
df.iloc[:, 0:3]                 # All rows, first 3 cols
```

### **Critical difference - slicing end:**
```python
df.loc['S1':'S3']    # Includes S3 ✓ (label, inclusive)
df.iloc[0:3]         # Excludes index 3 (position, exclusive)
```

---

## 7. Boolean Indexing

Filter rows using conditions:

```python
df[df['Age'] > 25]                              # Basic filter
df.loc[df['Age'] > 25]                          # Preferred (explicit)
df.loc[df['Age'] > 25, ['Name', 'Age']]         # Filter + select cols

# Compound conditions
df.loc[(df['Age'] > 20) & (df['Tumor'] == True)]   # AND
df.loc[(df['Age'] < 20) | (df['Age'] > 60)]         # OR
```

---

## 8. Loading from CSV

```python
df = pd.read_csv('file.csv')

# Common parameters
pd.read_csv('file.csv',
    sep=',',              # Delimiter (default ','; use '\t' for TSV)
    header=0,             # Row for column names (0 = first row)
    index_col='Gene',     # Column to use as row index
    usecols=['A','B','C'],# Only load these columns
    dtype={'Age': int},   # Specify column dtype
    na_values=['NA','?'], # Extra strings to treat as NaN
    skiprows=2,           # Skip first 2 rows
    nrows=100,            # Only read first 100 rows
)
```

---

## 9. Key Gotchas

### **1. Label vs Position Indexing:**
```python
s = pd.Series([10,20,30], index=['a','b','c'])

s['b']       # 20 (label)
s.iloc[1]    # 20 (position)
s[1]         # KeyError! Index is 'a','b','c' not 0,1,2
             # ALWAYS use .iloc for position!
```

### **2. Label slicing is INCLUSIVE:**
```python
s['a':'c']   # Includes 'c'! Different from Python/NumPy!
```

### **3. Single vs Double Brackets:**
```python
df['Age']          # Returns Series
df[['Age']]        # Returns DataFrame (single column!)
```

### **4. Attribute access limitations:**
```python
df.Age             # Works if 'Age' is a valid Python identifier
df['Tumor Size']   # Must use brackets for names with spaces
df['shape']        # Must use brackets if name conflicts with df attribute
```

---

## 10. Bioinformatics Example

```python
# Gene expression data
df = pd.read_csv('expression.csv', index_col='Gene')

# Select high-expression genes (boolean indexing)
high_expr = df.loc[df['Sample1_Expr'] > 200]

# Select specific samples
tumor_suppressors = df.loc[df['Is_Tumor_Suppressor'] == True]

# Get expression values for specific genes
tp53_data = df.loc['TP53']

# Statistics per gene
stats = df[['Sample1_Expr','Sample2_Expr','Sample3_Expr']].describe()
```

---

## 💡 Key Takeaways

1. **Series = 1D labelled array**, DataFrame = **2D labelled table**
2. **From dict** → keys become column names
3. **From list of dicts** → each dict is a row, missing keys → NaN
4. **Always use .loc for labels, .iloc for positions**
5. **Label slicing is INCLUSIVE at both ends** (unique to pandas!)
6. **Position slicing is EXCLUSIVE at end** (like Python/NumPy)
7. **Single brackets** return Series, **double brackets** return DataFrame
8. **df[condition]** filters rows, **df['col']** selects column
9. **pd.read_csv()** is the most common way to load real data
10. **Pandas is built on NumPy** — all operations are vectorized!

---

## 📚 Quick Reference

| Task | Code |
|------|------|
| Create Series | `pd.Series(data, index=idx)` |
| Create DataFrame | `pd.DataFrame(dict)` |
| Select column | `df['col']` |
| Select columns | `df[['col1','col2']]` |
| Row by label | `df.loc['label']` |
| Row by position | `df.iloc[0]` |
| Slice by label | `df.loc['a':'c']` (inclusive) |
| Slice by position | `df.iloc[0:3]` (exclusive) |
| Boolean filter | `df[df['col'] > val]` |
| Filter + select | `df.loc[condition, cols]` |
| Load CSV | `pd.read_csv('file.csv')` |
| Shape | `df.shape` |
| Summary | `df.info()` |
| Statistics | `df.describe()` |

---

*Pandas is the workhorse of data science in Python. Master it to work with any structured data!*
