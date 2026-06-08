# Day 23: Pandas Introduction - Learning Notes

**Date:** February 8, 2026
**Topic:** Pandas - Series, DataFrames, Indexing, CSV Loading
**Status:** ✅ Completed
**Week:** 5 - Day 3

---

## 📝 What I Learned Today

Today I started **Pandas** - the most important data analysis library in Python! If NumPy is the engine, Pandas is the car. It makes working with real-world tabular data intuitive. DataFrames feel like Excel but with the full power of Python!

---

## 🎯 Key Insights

### 1. Series: NumPy Array with Labels

```python
# NumPy - only positions
arr = np.array([120.5, 88.3, 210.1])
arr[0]   # 120.5 (by position only)

# Pandas Series - named labels!
s = pd.Series([120.5, 88.3, 210.1],
              index=['BRCA1', 'TP53', 'MYC'])
s['TP53']   # 88.3 (by name - so much clearer!)
```

**Labels make code self-documenting!**

### 2. DataFrame: Labelled 2D Table

```python
# Like Excel, but better!
df = pd.DataFrame({
    'Gene':       ['BRCA1', 'TP53', 'MYC'],
    'Expression': [120.5,    88.3,  210.1],
    'Chromosome': ['chr17', 'chr17', 'chr8']
})
```

**Each column can have a different dtype!**

### 3. .loc vs .iloc - CRITICAL Distinction

```python
df = pd.DataFrame(..., index=['S1','S2','S3','S4'])

df.loc['S2']       # Label  → by NAME
df.iloc[1]         # Integer → by POSITION

# They often give the same result, but NOT always!
# Always be explicit about which you want
```

### 4. Slicing GOTCHA: Labels are INCLUSIVE!

```python
s = pd.Series([1,2,3,4], index=['a','b','c','d'])

s[:3]        # [a,b,c] - position, exclusive end (like Python)
s['a':'c']   # [a,b,c] - label, INCLUSIVE end (unique to pandas!)
```

**This trips up EVERYONE at first!**

### 5. Single vs Double Brackets

```python
df['Age']          # → Series (single column)
df[['Age']]        # → DataFrame (still 1 column!)
df[['Age','Name']] # → DataFrame (multiple columns)
```

**Double brackets always return DataFrame!**

### 6. Missing Data → NaN Automatically

```python
data = [
    {'gene': 'TP53', 'expr': 120.5},          # No 'chrom'
    {'gene': 'MYC',  'expr': 88.3, 'chrom': 'chr8'},
]
pd.DataFrame(data)
# TP53's 'chrom' becomes NaN automatically!
```

**Pandas handles real-world messy data!**

---

## 💪 What I Practiced Today

1. ✅ Creating Series (list, dict, NumPy, custom index)
2. ✅ Series attributes (values, index, dtype, shape, etc.)
3. ✅ Series indexing (.loc vs .iloc)
4. ✅ Label vs position slicing
5. ✅ Vectorized operations on Series
6. ✅ Boolean filtering on Series
7. ✅ Creating DataFrames (dict, list of dicts, NumPy, Series)
8. ✅ DataFrame attributes and inspection
9. ✅ Column selection (single and multiple)
10. ✅ .loc[] row/column selection
11. ✅ .iloc[] row/column selection
12. ✅ Boolean indexing on DataFrames
13. ✅ Loading CSV with pd.read_csv()

---

## 🤔 Challenges Faced

### 1. Series[1] KeyError

When Series has string labels:
```python
s = pd.Series([1,2,3], index=['a','b','c'])
s[1]       # KeyError! '1' is not in ['a','b','c']
s.iloc[1]  # ✓ Use .iloc for position
```

**Lesson: ALWAYS use .iloc for positions!**

### 2. Label Slicing Inclusive End

Initially expected Python behaviour, but:
```python
s['a':'c']   # Returns a, b, c (includes 'c'!)
```

**Pandas is different - inclusive at both ends!**

### 3. .info() vs .describe()

- `.info()` → structural overview (dtypes, non-null counts)
- `.describe()` → statistical summary (mean, std, etc.)

**Different tools for different purposes!**

---

## 💡 Aha Moments

### 1. DataFrames Are Built From Series!

Each **column** in a DataFrame IS a Series. A DataFrame is just multiple Series sharing the same index!

```python
df['Gene'] → pd.Series(['BRCA1', 'TP53', 'MYC'])
```

### 2. .loc with Boolean + Column Selection

```python
# This is SO powerful!
df.loc[df['Age'] > 25, ['Name', 'Age']]
# Filter rows AND select columns in one line!
```

**This pattern is used constantly in data science!**

### 3. pd.read_csv() Opens Any Tabular Data

```python
# Research data, clinical trials, genomics...
df = pd.read_csv('methylation_data.csv',
                 index_col='CpG_Site',
                 usecols=['CpG_Site', 'Sample1', 'Sample2'])
```

**One line to load a whole dataset!**

### 4. Missing Data is First-Class

Pandas was designed for real-world messy data. NaN is not an afterthought — it's built in everywhere!

---

## 🧬 Bioinformatics Applications

```python
# Load gene expression data
df = pd.read_csv('expression.csv', index_col='Gene')

# High expression tumor suppressors
high_ts = df.loc[
    (df['Sample1_Expr'] > 100) & (df['Is_Tumor_Suppressor'] == True)
]
print(f"High-expression tumor suppressors:\n{high_ts}")

# Chromosome 17 genes
chr17 = df.loc[df['Chromosome'] == 'chr17']
print(f"Chr17 genes:\n{chr17}")

# Mean expression across samples
expr_cols = ['Sample1_Expr', 'Sample2_Expr', 'Sample3_Expr']
df['Mean_Expr'] = df[expr_cols].mean(axis=1)
```

---

## 🎯 Self-Assessment

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)
**Confidence:** ⭐⭐⭐⭐⭐ (5/5)
**Application:** ⭐⭐⭐⭐⭐ (5/5)

---

## 🏆 Achievements Today

- ✅ Series creation and attributes
- ✅ .loc vs .iloc mastered
- ✅ Label slicing inclusive behaviour
- ✅ DataFrame creation (4 ways)
- ✅ Boolean indexing on DataFrames
- ✅ CSV loading with pd.read_csv()
- ✅ **PANDAS STARTED!**

---

## 🚀 What's Next

- Pandas data manipulation (groupby, merge, pivot)
- Handling missing data
- Data visualization with Matplotlib
- Real datasets for bioinformatics

---

## 💬 Key Quotes

> "Series = NumPy array with named index"

> "DataFrame = dict of Series with shared index"

> "ALWAYS use .loc for labels, .iloc for positions"

> "Label slices are INCLUSIVE - different from Python!"

> "Double brackets always return DataFrame!"

---

## 📊 Day 23 Stats

**Time Spent:** ~3 hours
**Concepts Mastered:** 13
**Operations Practiced:** 35+
**Confidence:** Expert!

---

*Day 23 complete! Pandas foundation built! Tabular data mastered! 🐼*
