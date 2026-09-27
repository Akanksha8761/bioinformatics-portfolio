import numpy as np
import pandas as pd

####################### Handling Missing Data #########################################

print("----------------- Handling Missing Data ---------------------------")

data_missing = {
    'A': [1,       2,       np.nan, 4,       5      ],
    'B': [np.nan,  7,       8,      np.nan,  10     ],
    'C': [11,      12,      13,     14,      15     ],
    'D': [16,      17,      18,     19,      np.nan ],
    'E': [np.nan,  np.nan,  np.nan, np.nan,  np.nan ],
}
df_miss = pd.DataFrame(data_missing, index=['R1','R2','R3','R4','R5'])
print(f"Original DataFrame:\n{df_miss}")

# --- Detecting missing values ---
print(f"\nisnull():\n{df_miss.isnull()}")
print(f"\nnotnull():\n{df_miss.notnull()}")
print(f"\nMissing per column:\n{df_miss.isnull().sum()}")
print(f"\nTotal missing: {df_miss.isnull().sum().sum()}")

# --- Dropping missing values ---
# Drop rows with ANY NaN (default)
print(f"\ndropna() - rows with any NaN:\n{df_miss.dropna()}")

# Drop columns with ANY NaN
print(f"\ndropna(axis=1) - cols with any NaN:\n{df_miss.dropna(axis=1)}")

# Drop rows where ALL values are NaN
print(f"\ndropna(how='all') - rows where ALL are NaN:\n{df_miss.dropna(how='all')}")

# Keep rows with at least 'thresh' non-NaN values
print(f"\ndropna(thresh=4) - keep rows with ≥4 non-NaN:\n{df_miss.dropna(thresh=4)}")

# --- Filling missing values ---
print(f"\nfillna(0) - fill all NaN with 0:\n{df_miss.fillna(0)}")

# Fill with column mean
copy_for_mean = df_miss.copy()
for col in copy_for_mean.columns:
    col_mean = copy_for_mean[col].mean()     # mean() skips NaN automatically
    copy_for_mean[col] = copy_for_mean[col].fillna(col_mean)
print(f"\nFilled with column mean:\n{copy_for_mean}")

# Forward fill (ffill) - propagate last valid value forward
print(f"\nffill (forward fill):\n{df_miss.ffill()}")

# Backward fill (bfill) - propagate next valid value backward
print(f"\nbfill (backward fill):\n{df_miss.bfill()}")

# Limit fills
print(f"\nffill(limit=1) - fill only 1 consecutive NaN:\n{df_miss.ffill(limit=1)}")

# Fill different columns with different values
print(f"\nfillna per column:\n{df_miss.fillna({'A': 0, 'B': 1, 'C': 2, 'D': 10})}")

# NOTE: Most operations return a NEW DataFrame.
# Use inplace=True (or reassign) to modify the original:
# df_miss.fillna(0, inplace=True)    # modifies df_miss directly

################################ Data Cleaning and Transformation ################################

print("\n\n--- Data Cleaning and Transformation ---")

data = pd.DataFrame({
    'A': [1,    2,    3,    4,    5   ],
    'B': [6.1,  7.2,  8.3,  9.5,  10.5],
    'C': [True, True, False,True, False],
    'D': ['cat1','cat2','cat1','cat3','cat5']
})
print(f"Original DataFrame:\n{data}")
print(f"dtypes:\n{data.dtypes}")

# Convert column types with .astype()
data['D'] = data['D'].astype(str)           # object → str (same, but explicit)
print(f"\nAfter D → str: D dtype = {data['D'].dtype}")

data['A'] = data['A'].astype(float)         # int → float
print(f"After A → float: A dtype = {data['A'].dtype}")

data['D'] = data['D'].astype('category')    # str → category (memory efficient!)
print(f"After D → category: D dtype = {data['D'].dtype}")
# category is ideal when a column has few unique string values

# Error handling: try to convert 'D' (category) to int
try:
    data['D'] = data['D'].astype(int)
except (ValueError, TypeError) as e:
    print(f"\nConversion error (expected): {e}")

################################ Removing Duplicates ############################################

print("\n\n--- Removing Duplicates ---")

df_dup = pd.DataFrame({
    'A': [1, 2, 2, 3, 4, 1, 1],
    'B': ['A','B','C','B','A','D','A'],
    'C': [100, 200, 100, 300, 200, 100, 100]
})
print(f"Original DataFrame:\n{df_dup}")

# duplicated() - returns boolean Series
# keep='first' (default): marks duplicates after the first occurrence as True
print(f"\nduplicated(keep='first'):\n{df_dup.duplicated()}")

# keep='last': marks all but the LAST occurrence as True
print(f"\nduplicated(keep='last'):\n{df_dup.duplicated(keep='last')}")

# keep=False: marks ALL occurrences as True
print(f"\nduplicated(keep=False):\n{df_dup.duplicated(keep=False)}")

# Drop duplicates
print(f"\ndrop_duplicates() - keep first:\n{df_dup.drop_duplicates()}")
print(f"\ndrop_duplicates(keep='last'):\n{df_dup.drop_duplicates(keep='last')}")

# Drop duplicates based on specific column subset
print(f"\ndrop_duplicates(subset=['A','B'], keep='last'):\n{df_dup.drop_duplicates(subset=['A','B'], keep='last')}")
print(f"\ndrop_duplicates(subset=['A','B'], keep='first'):\n{df_dup.drop_duplicates(subset=['A','B'], keep='first')}")

################################ Applying Functions (.apply(), .map(), .applymap()) ################################

print(f"\n--------- Applying Functions ---------------")

data2 = pd.DataFrame(np.random.randint(0, 10, size=(3,4)), columns=['W','X','Y','Z'])
print(f"Original DataFrame:\n{data2}")

# 1. apply() - applies function to each column (axis=0) or row (axis=1)
print(f"\napply(lambda i: i+2) on columns (axis=0):\n{data2.apply(lambda i: i + 2)}")
print(f"\napply(lambda i: i+1) on rows (axis=1):\n{data2.apply(lambda i: i + 1, axis=1)}")

# Custom aggregation with apply
print(f"\napply(max - min) per column:\n{data2.apply(lambda x: x.max() - x.min())}")

# 2. applymap() / map() (element-wise on DataFrame)
# Note: applymap() was renamed to map() in pandas 2.1.0
def multiply(x):
    return x * 5

try:
    # pandas >= 2.1.0
    print(f"\nmap(multiply) element-wise:\n{data2.map(multiply)}")
except AttributeError:
    # pandas < 2.1.0
    print(f"\napplymap(multiply) element-wise:\n{data2.applymap(multiply)}")

# 3. Series.map() - element-wise on Series (uses function OR dict)
series_codes = pd.Series([1, 2, 3, 4, 5], name="Codes")
print(f"\nOriginal Series:\n{series_codes}")

# Map with lambda
print(f"\nSeries.map(lambda): {series_codes.map(lambda x: f'Code-{x}').tolist()}")

# Map with dictionary
code_dict = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}
print(f"\nSeries.map(dict):\n{series_codes.map(code_dict)}")

################################ Replacing Values (.replace()) ################################

print(f"\n\n----------- Replacing Values ---------------")

df_replace = pd.DataFrame({
    'Category': ['A','B','C','A','D','B'],
    'Value':    [10, 20, 15, 10, 25, 200]
})
print(f"Original DataFrame:\n{df_replace}")

print(f"\nreplace('A', 'V'):\n{df_replace.replace('A', 'V')}")
print(f"\nreplace(['A','B'], 'Group1'):\n{df_replace.replace(['A','B'], 'Group1')}")
print(f"\nreplace(dict {{20:22}}):\n{df_replace.replace({20: 22})}")
print(f"\nColumn-level replace Value 10 → 1000:\n{df_replace['Value'].replace(10, 1000)}")

########################################## Sorting Data ########################################

print(f"\n\n----------- Sorting Data ---------------")

df_sort = pd.DataFrame(
    {'colB': [4,7,1,8,5], 'colA': [10,2,5,3,9]},
    index=['R3','R1','R5','R2','R4']
)
print(f"Original DataFrame:\n{df_sort}")

# Sort by index (row labels)
print(f"\nsort_index() ascending:\n{df_sort.sort_index()}")
print(f"\nsort_index(ascending=False):\n{df_sort.sort_index(ascending=False)}")

# Sort by column labels
print(f"\nsort_index(axis=1) - column labels:\n{df_sort.sort_index(axis=1)}")

# Sort by values
print(f"\nsort_values('colA'):\n{df_sort.sort_values(by='colA')}")
print(f"\nsort_values('colB'):\n{df_sort.sort_values(by='colB')}")

# Multi-column sort: colA ascending, colB descending
print(f"\nsort_values(['colA','colB'], ascending=[True,False]):\n{df_sort.sort_values(by=['colA','colB'], ascending=[True,False])}")

##########################################  Grouping Data (.groupby()) ##########################################

print(f"\n\n----------- Grouping Data (.groupby()) ---------------")

df_group = pd.DataFrame({
    'Animal':   ['Cat','Dog','Cat','Dog','Cat','Dog','Bird','Bird'],
    'MaxSpeed': [48,   70,   45,   65,   50,   80,   25,    30  ],
    'Weight':   [4.0,  12.0, 3.5,  10.0, 4.2,  25.0, 0.5,  0.6 ]
})
print(f"Original DataFrame:\n{df_group}")

# Group by single column
grouped = df_group.groupby('Animal')
print(f"\nType of groupby object: {type(grouped)}")

print(f"\nMean by animal:\n{grouped.mean(numeric_only=True)}")
print(f"\nMean MaxSpeed by animal:\n{grouped['MaxSpeed'].mean()}")
print(f"\nSize (count) per group:\n{grouped.size()}")
print(f"\nSum of Weight by animal:\n{grouped['Weight'].sum()}")
print(f"\nMax speed by animal:\n{grouped['MaxSpeed'].max()}")
print(f"\nMin speed by animal:\n{grouped['MaxSpeed'].min()}")
print(f"\nStd of Weight by animal:\n{grouped['Weight'].std()}")

# Group by multiple columns
df_group['Diet'] = ['Carnivore','Omnivore','Carnivore','Omnivore','Carnivore','Omnivore','Herbivore','Herbivore']
print(f"\nDataFrame with Diet column:\n{df_group}")

multi_grouped = df_group.groupby(['Animal','Diet'])
print(f"\nMean by Animal + Diet:\n{multi_grouped.mean(numeric_only=True)}")

# Multiple aggregations with .agg()
print(f"\nMultiple agg on MaxSpeed:\n{df_group.groupby('Animal')['MaxSpeed'].agg(['mean','std','count'])}")

custom_agg = {'MaxSpeed': ['mean','max'], 'Weight': ['sum','min','count']}
print(f"\nCustom agg:\n{grouped.agg(custom_agg)}")

# Iterating through groups
print(f"\nIterating groups:")
for name, group_df in grouped:
    print(f"  Group '{name}' — shape {group_df.shape}")
    print(group_df[['Animal','MaxSpeed']].head(2))

##########################################  Concatenation ##########################################

print("\n\n--- Combining DataFrames: Concatenation ---")

df1 = pd.DataFrame({'A':['A0','A1'], 'B':['B0','B1']}, index=[0,1])
df2 = pd.DataFrame({'A':['A2','A3'], 'B':['B2','B3']}, index=[2,3])
df3 = pd.DataFrame({'C':['C0','C1'], 'D':['D0','D1']}, index=[0,1])
print(f"df1:\n{df1}\n\ndf2:\n{df2}\n\ndf3:\n{df3}")

# Vertical concat (axis=0) - stack rows
print(f"\npd.concat([df1,df2]) - rows:\n{pd.concat([df1,df2])}")

# Different columns → NaN where missing
print(f"\npd.concat([df1,df2,df3]) - mismatched cols → NaN:\n{pd.concat([df1,df2,df3])}")

# ignore_index=True - reset row index
print(f"\nignore_index=True:\n{pd.concat([df1,df2,df3], ignore_index=True)}")

# Horizontal concat (axis=1) - side by side
print(f"\npd.concat([df1,df2], axis=1):\n{pd.concat([df1,df2], axis=1)}")

# Partial index overlap with axis=1
df4 = pd.DataFrame({'A':['A4','A5'], 'B':['B4','B5']}, index=[0,2])
print(f"\ndf4 (index [0,2]):\n{df4}")
print(f"\npd.concat([df1,df4], axis=1) - partial overlap → NaN:\n{pd.concat([df1,df4], axis=1)}")

########################################## Merging DataFrames (pd.merge()) ##########################################

print("\n\n--- Combining DataFrames: Merging/Joining ---")

left_df = pd.DataFrame({
    'key': ['K0','K1','K2','K3'],
    'A':   ['A0','A1','A2','A3'],
    'B':   ['B0','B1','B2','B3']
})
right_df = pd.DataFrame({
    'key': ['K0','K1','K4','K5'],   # K2,K3 missing; K4,K5 extra
    'C':   ['C0','C1','C4','C5'],
    'D':   ['D0','D1','D4','D5']
})
print(f"Left:\n{left_df}\n\nRight:\n{right_df}")

# INNER join - only matching keys
print(f"\nINNER join (default):\n{pd.merge(left_df, right_df, on='key')}")

# OUTER join - all keys, NaN where no match
print(f"\nOUTER join (how='outer'):\n{pd.merge(left_df, right_df, on='key', how='outer')}")

# LEFT join - all left keys, NaN for unmatched right
print(f"\nLEFT join (how='left'):\n{pd.merge(left_df, right_df, on='key', how='left')}")

# RIGHT join - all right keys, NaN for unmatched left
print(f"\nRIGHT join (how='right'):\n{pd.merge(left_df, right_df, on='key', how='right')}")

# Merge on MULTIPLE keys
left_multi = pd.DataFrame({
    'key1': ['K0','K0','K1','K2'],
    'key2': ['X0','X1','X0','X1'],
    'A':    ['A0','A1','A2','A3']
})
right_multi = pd.DataFrame({
    'key1': ['K0','K1','K1','K2'],
    'key2': ['X1','X0','X0','X0'],
    'B':    ['B0','B1','B2','B3']
})
print(f"\nMulti-key INNER merge:\n{pd.merge(left_multi, right_multi, on=['key1','key2'], how='inner')}")

# Merge on INDEX
left_idx  = pd.DataFrame({'X': ['X0','X1']}, index=['K0','K1'])
right_idx = pd.DataFrame({'Y': ['Y0','Y2']}, index=['K0','K2'])
print(f"\nMerge on index (how='outer'):\n{pd.merge(left_idx, right_idx, left_index=True, right_index=True, how='outer')}")

print("\n--- Day 24 Complete! Advanced Pandas Mastered! ---")
