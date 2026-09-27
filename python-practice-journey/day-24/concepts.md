# Day 24: Advanced Pandas - Concepts

## 📌 Core Concepts Covered

Building on Day 23's foundation, today we master data cleaning, transformation, grouping, combining DataFrames — the techniques professionals use every day on real-world messy datasets!

---

## 1. Handling Missing Data

### **Detecting:**
```python
df.isnull()              # Boolean DataFrame: True where NaN
df.notnull()             # Opposite
df.isnull().sum()        # Count NaN per column
df.isnull().sum().sum()  # Total NaN in entire DataFrame
```

### **Dropping:**
```python
df.dropna()              # Drop rows with ANY NaN
df.dropna(axis=1)        # Drop columns with ANY NaN
df.dropna(how='all')     # Only drop rows where ALL are NaN
df.dropna(thresh=3)      # Keep rows with ≥3 non-NaN values
```

### **Filling:**
```python
df.fillna(0)                      # Fill all with constant
df.fillna({'A': 0, 'B': 99})      # Different fill per column
df.fillna(df.mean())              # Fill with column mean
df.ffill()                        # Forward fill
df.bfill()                        # Backward fill
df.ffill(limit=1)                 # Limit to 1 consecutive fill
```

### **⚠️ inplace vs reassign:**
```python
# Both are equivalent:
df = df.fillna(0)          # Reassign (preferred, explicit)
df.fillna(0, inplace=True) # Modify in place
```

---

## 2. Data Type Conversion (.astype())

```python
df['col'].astype(float)        # int → float
df['col'].astype(str)          # any → string
df['col'].astype(int)          # float → int (truncates!)
df['col'].astype('category')   # string → category (memory efficient!)
```

### **When to use 'category':**
- Column has few unique string values (e.g., gender, species, chromosome)
- Saves memory, speeds up groupby operations

```python
df['Animal'].astype('category')   # e.g., Cat/Dog/Bird - only 3 unique values
```

---

## 3. Removing Duplicates

```python
df.duplicated()                          # True for rows duplicated after first
df.duplicated(keep='last')               # True for all but last occurrence
df.duplicated(keep=False)                # True for ALL occurrences
df.drop_duplicates()                     # Keep first of duplicates
df.drop_duplicates(keep='last')          # Keep last
df.drop_duplicates(subset=['A','B'])     # Check only specific columns
```

---

## 4. Applying Functions

### **apply() — on columns or rows:**
```python
# Apply function to each column (axis=0, default)
df.apply(lambda col: col.max() - col.min())     # Range per column

# Apply function to each row (axis=1)
df.apply(lambda row: row.sum(), axis=1)          # Row sums
```

### **map() / applymap() — element-wise on DataFrame:**
```python
# pandas ≥ 2.1: use map()
df.map(lambda x: x * 2)

# pandas < 2.1: use applymap()
df.applymap(lambda x: x * 2)
```

### **Series.map() — element-wise on Series:**
```python
s.map(lambda x: f"Code-{x}")           # Using function
s.map({1:"One", 2:"Two", 3:"Three"})   # Using dictionary
```

### **When to use each:**
| Method | Target | Use case |
|--------|--------|----------|
| `apply()` | Row/Column | Aggregation or transformation |
| `map()`/`applymap()` | Each element | Element-wise transformation |
| `Series.map()` | Series elements | Value substitution |

---

## 5. Replacing Values

```python
df.replace('A', 'V')                    # Single value
df.replace(['A','B'], 'Group1')         # Multiple → single
df.replace({'A':'Group1', 'B':'Group2'})# Dict mapping
df['col'].replace(10, 1000)             # In specific column
```

---

## 6. Sorting

```python
# Sort by row index labels
df.sort_index()                           # Ascending (default)
df.sort_index(ascending=False)            # Descending
df.sort_index(axis=1)                     # Sort column labels

# Sort by values
df.sort_values(by='colA')                 # Single column
df.sort_values(by='colA', ascending=False)
df.sort_values(by=['colA','colB'],        # Multi-column sort
               ascending=[True, False])   # Mixed directions
```

---

## 7. GroupBy

GroupBy follows the **Split → Apply → Combine** pattern:

```
Split: divide DataFrame into groups
Apply: apply a function to each group
Combine: merge results back together
```

```python
grouped = df.groupby('Category')           # Split
grouped.mean(numeric_only=True)            # Apply + Combine
grouped['Speed'].sum()                     # Specific column

# Multiple aggregations
grouped['Speed'].agg(['mean','std','count'])

# Different agg per column
grouped.agg({'Speed': ['mean','max'], 'Weight': ['sum','min']})

# Iterate groups
for name, group in grouped:
    print(name, group.shape)
```

---

## 8. Concatenation (pd.concat)

```python
pd.concat([df1, df2])                   # Stack rows (axis=0)
pd.concat([df1, df2], axis=1)           # Stack columns
pd.concat([df1, df2], ignore_index=True)# Reset index
```

**Mismatched columns → NaN:**
```python
# df1 has cols A,B; df3 has cols C,D
pd.concat([df1, df3])   # A,B,C,D with NaN where missing
```

---

## 9. Merging (pd.merge)

Like SQL JOIN operations:

```python
pd.merge(left, right, on='key')                        # INNER (default)
pd.merge(left, right, on='key', how='outer')           # OUTER
pd.merge(left, right, on='key', how='left')            # LEFT
pd.merge(left, right, on='key', how='right')           # RIGHT
pd.merge(left, right, on=['key1','key2'])               # Multi-key
pd.merge(left, right, left_index=True, right_index=True) # On index
```

### **Join types visualised:**
```
LEFT:   A B    RIGHT:  A C      INNER: A B C (only K0, K1)
        K0 A0          K0 C0
        K1 A1          K1 C1    LEFT:  A B C (K0..K3, NaN for K2,K3 C)
        K2 A2          K4 C4
        K3 A3          K5 C5    OUTER: all keys, NaN where no match
```

---

## 10. Bioinformatics Example

```python
# Real workflow for gene expression analysis

# 1. Load data
df = pd.read_csv('expression.csv', index_col='Gene')

# 2. Handle missing
print(df.isnull().sum())
df_clean = df.fillna(df.mean())

# 3. Remove duplicates
df_clean = df_clean.drop_duplicates()

# 4. Filter high expression
high_expr = df_clean[df_clean['Sample1'] > 100]

# 5. Sort by expression
high_expr = high_expr.sort_values('Sample1', ascending=False)

# 6. Group by chromosome
chr_groups = df_clean.groupby('Chromosome')
chr_mean = chr_groups.mean(numeric_only=True)

# 7. Merge with metadata
df_meta = pd.read_csv('gene_metadata.csv', index_col='Gene')
merged = pd.merge(df_clean, df_meta, left_index=True, right_index=True)
```

---

## 💡 Key Takeaways

1. **isnull() + sum()** to find missing data quickly
2. **dropna(thresh=n)** keeps rows with enough valid data
3. **ffill/bfill** for time-series or sequential data
4. **'category' dtype** saves memory for repeated strings
5. **drop_duplicates(subset=cols)** for key-based dedup
6. **apply(axis=0)** operates per column, **apply(axis=1)** per row
7. **Series.map(dict)** for value substitution (very common!)
8. **groupby → agg** is the core of data aggregation
9. **pd.concat** for stacking, **pd.merge** for joining
10. **pd.merge how='inner/outer/left/right'** controls which rows survive

---

## 📚 Quick Reference

| Task | Code |
|------|------|
| Count NaN | `df.isnull().sum()` |
| Drop NaN rows | `df.dropna()` |
| Fill NaN | `df.fillna(value)` |
| Forward fill | `df.ffill()` |
| Convert type | `df['col'].astype(float)` |
| Find duplicates | `df.duplicated()` |
| Drop duplicates | `df.drop_duplicates()` |
| Apply per col | `df.apply(func)` |
| Map values | `series.map(dict)` |
| Replace value | `df.replace(old, new)` |
| Sort by index | `df.sort_index()` |
| Sort by value | `df.sort_values('col')` |
| Group + agg | `df.groupby('col').mean()` |
| Stack rows | `pd.concat([df1, df2])` |
| SQL join | `pd.merge(left, right, on='key')` |

---

*Advanced Pandas is the backbone of all real-world data analysis. Master these patterns and you can handle any dataset!*
