# Day 24: Advanced Pandas - Learning Notes

**Date:** February 9, 2026
**Topic:** Advanced Pandas - Cleaning, Grouping, Merging
**Status:** ✅ Completed
**Week:** 5 - Day 4

---

## 📝 What I Learned Today

Today I went deep into **Advanced Pandas** - the techniques professionals use on messy, real-world data! Missing values, duplicates, groupby, concat, merge... this is what 80% of data science actually is! The data never comes clean, and today I learned how to handle that.

---

## 🎯 Key Insights

### 1. Missing Data — The Reality of Real Datasets

```python
# Detect
df.isnull().sum()           # Count per column
df.isnull().sum().sum()     # Total

# Drop
df.dropna()                 # Any NaN in row
df.dropna(thresh=4)         # Keep rows with ≥4 valid

# Fill
df.fillna(0)                # Constant
df.ffill()                  # Forward fill (time series!)
df.bfill()                  # Backward fill
```

### 2. apply() — Column vs Row

```python
# axis=0: function sees EACH COLUMN as a Series
df.apply(lambda col: col.max() - col.min())  # Range per column

# axis=1: function sees EACH ROW as a Series
df.apply(lambda row: row.sum(), axis=1)       # Row sums
```

**Remember: axis=0 → columns, axis=1 → rows**

### 3. GroupBy — Split → Apply → Combine

```python
grouped = df.groupby('Animal')    # Split into groups

grouped.mean()                    # Apply mean to each group
grouped['Speed'].agg(['mean','std','count'])  # Multiple at once

# Custom per column
grouped.agg({
    'Speed': ['mean', 'max'],
    'Weight': ['sum', 'min']
})
```

**groupby + agg = the core of data analysis!**

### 4. Concat vs Merge

```python
# CONCAT: stack DataFrames (by rows or columns)
pd.concat([df1, df2])          # Stack rows
pd.concat([df1, df2], axis=1)  # Stack columns

# MERGE: SQL-style join on key columns
pd.merge(left, right, on='key', how='inner')
pd.merge(left, right, on='key', how='left')
pd.merge(left, right, on='key', how='outer')
```

**Use concat to stack, merge to join on keys!**

### 5. fillna Method Options Update

```python
# Note: 'method' parameter is deprecated in newer pandas
# Use .ffill() and .bfill() directly:
df.ffill()          # Forward fill (was: df.fillna(method='ffill'))
df.bfill()          # Backward fill (was: df.fillna(method='bfill'))
df.ffill(limit=1)   # Limit consecutive fills
```

---

## 💪 What I Practiced Today

1. ✅ Detecting missing values (isnull, notnull, sum)
2. ✅ Dropping NaN (any, all, thresh)
3. ✅ Filling NaN (constant, mean, ffill, bfill, per-column)
4. ✅ Type conversion with astype()
5. ✅ 'category' dtype for efficiency
6. ✅ Detecting and dropping duplicates
7. ✅ apply() on columns and rows
8. ✅ map()/applymap() element-wise
9. ✅ Series.map() with function and dict
10. ✅ replace() single, list, dict
11. ✅ sort_index() and sort_values()
12. ✅ groupby() with single and multiple keys
13. ✅ agg() with multiple and custom aggregations
14. ✅ Iterating through groups
15. ✅ pd.concat() (rows, columns, ignore_index)
16. ✅ pd.merge() (inner, outer, left, right)

---

## 🤔 Challenges Faced

### 1. apply() axis direction

Initially confused which axis does what:
- axis=0 → function applied DOWN → sees COLUMN
- axis=1 → function applied ACROSS → sees ROW

**Mnemonic: axis=0 collapses rows, axis=1 collapses columns**

### 2. applymap vs map deprecation

```python
# pandas ≥ 2.1: DataFrame element-wise is now .map()
# pandas < 2.1: it was .applymap()
# Used try/except in exercises to handle both versions
```

### 3. concat with different columns

```python
pd.concat([df1, df3])  # df1 has A,B; df3 has C,D
# Result has columns A,B,C,D with NaN in missing cells
```

**Always check columns after concat!**

### 4. Merge key matching

Inner join only keeps rows where key exists in BOTH DataFrames. K2, K3 were in left only → dropped!

---

## 💡 Aha Moments

### 1. groupby is Split→Apply→Combine!

```python
# Split: df.groupby('Animal') creates 3 sub-DataFrames
# Apply: .mean() computes mean of each sub-DataFrame
# Combine: results are assembled into final DataFrame
```

**The same pattern used in MapReduce, Spark, Hadoop!**

### 2. .agg() accepts dict for custom per-column aggregations!

```python
grouped.agg({
    'MaxSpeed': ['mean', 'max'],    # Two aggs for MaxSpeed
    'Weight': ['sum', 'min', 'count']  # Three aggs for Weight
})
```

**Incredibly powerful for summary statistics!**

### 3. pd.merge() IS SQL JOIN

```python
pd.merge(left, right, on='key')           # INNER JOIN
pd.merge(left, right, on='key', how='left')   # LEFT OUTER JOIN
pd.merge(left, right, on='key', how='outer')  # FULL OUTER JOIN
```

**If I know SQL, I know merge!**

### 4. thresh in dropna is underused!

```python
df.dropna(thresh=4)  # Keep rows with at least 4 valid values
```

**Much better than dropna() which loses everything with even 1 NaN!**

---

## 🧬 Bioinformatics Applications

```python
# Complete methylation analysis workflow

# 1. Load data
df = pd.read_csv('methylation.csv', index_col='CpG_Site')

# 2. Check missing
print(f"Missing per sample:\n{df.isnull().sum()}")

# 3. Fill missing with column mean
df_clean = df.fillna(df.mean())

# 4. Remove duplicate CpG sites
df_clean = df_clean.drop_duplicates()

# 5. Group by chromosome
chr_stats = df_clean.groupby('Chromosome').agg({
    'Beta_Value': ['mean', 'std', 'count']
})

# 6. High-methylation sites
high_meth = df_clean[df_clean['Beta_Value'] > 0.75]
high_meth = high_meth.sort_values('Beta_Value', ascending=False)

# 7. Merge with gene annotation
gene_annot = pd.read_csv('gene_annotations.csv')
merged = pd.merge(df_clean, gene_annot, on='CpG_Site', how='left')

print(f"High methylation sites:\n{high_meth.head()}")
print(f"Chromosome statistics:\n{chr_stats}")
```

---

## 🎯 Self-Assessment

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)
**Confidence:** ⭐⭐⭐⭐⭐ (5/5)
**Application:** ⭐⭐⭐⭐⭐ (5/5)

---

## 🏆 Achievements Today

- ✅ Missing data handling (complete toolkit)
- ✅ Type conversion and 'category' dtype
- ✅ Duplicate detection and removal
- ✅ apply/map/applymap mastered
- ✅ replace() for value substitution
- ✅ Sorting (index and values)
- ✅ groupby + agg (the core of data analysis!)
- ✅ concat (stack DataFrames)
- ✅ merge (SQL-style joins)
- ✅ **PANDAS ADVANCED COMPLETE!**

---

## 🚀 What's Next

- Matplotlib for data visualization
- Putting it all together: NumPy + Pandas + Matplotlib
- Moving toward ML!

---

## 💬 Key Quotes

> "Real data is messy — pandas was built for that!"

> "groupby = Split → Apply → Combine"

> "concat stacks, merge joins"

> "dropna(thresh=n) is more useful than plain dropna()"

> "category dtype: few unique strings = use category!"

---

## 📊 Day 24 Stats

**Time Spent:** ~3.5 hours
**Concepts Mastered:** 15
**Operations Practiced:** 50+
**Confidence:** Expert!

---

*Day 24 complete! Advanced Pandas mastered! Ready for visualization! 🐼*
