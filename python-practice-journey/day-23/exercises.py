import pandas as pd
import numpy as np

print(f"Pandas Version: {pd.__version__}")
print(f"NumPy Version:  {np.__version__}")

########################## Creating Pandas Series ###################################

print("\n-------- Creating Pandas Series ----------")

# 1. From a Python list (default integer index 0, 1, 2...)
python_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s_default = pd.Series(python_list)
print(f"Series from list:\n{s_default}")

# 2. From a list with custom index
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
custom_idx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s_custom = pd.Series(data=data, index=custom_idx)
print(f"\nSeries with custom index:\n{s_custom}")

# 3. From a NumPy array with custom index
numpy_array = np.arange(5)
custom_index = ['a', 'b', 'c', 'd', 'e']
s_numpy = pd.Series(numpy_array, index=custom_index)
print(f"\nSeries from NumPy array:\n{s_numpy}")

# 4. From a Python dictionary (keys → index, values → data)
python_dict = {'a': 1, 'b': 2, 'e': 3, 'c': 5}
s_dict = pd.Series(python_dict)
print(f"\nSeries from dict:\n{s_dict}")

# Specifying index with dict: missing keys → NaN
s_dict_custom = pd.Series(python_dict, index=['a', 'b', 'c', 'f'])
print(f"\nSeries from dict (with missing key 'f' → NaN):\n{s_dict_custom}")

# 5. Series with a name attribute
gene_expression = pd.Series(
    [1, 2, 3, 4, 5, 6],
    index=['GeneA', 'GeneB', 'GeneC', 'GeneD', 'GeneE', 'GeneF'],
    name='Gene Expression'
)
print(f"\nGene expression Series:\n{gene_expression}")
print(f"Series name: {gene_expression.name}")

######################## Series Attributes and Basic Operations ####################

print("\n------------- Series Attributes ---------------")
print(f"values (numpy array): {gene_expression.values}")
print(f"type of values:       {type(gene_expression.values)}")
print(f"index:                {gene_expression.index.tolist()}")
print(f"dtype:                {gene_expression.dtype}")
print(f"shape:                {gene_expression.shape}")
print(f"ndim:                 {gene_expression.ndim}")
print(f"size:                 {gene_expression.size}")
print(f"name:                 {gene_expression.name}")
print(f"hasnans:              {gene_expression.hasnans}")

# Indexing
print("\n--- Indexing ---")
print(f"By label ['GeneB']:        {gene_expression['GeneB']}")
print(f".iloc[1] (position):       {gene_expression.iloc[1]}")    # Use .iloc for positional
print(f".loc['GeneB'] (label):     {gene_expression.loc['GeneB']}")
# Note: gene_expression[1] raises KeyError when index is string labels
# Always use .iloc for positional, .loc for label-based access!

# Slicing
print("\n--- Slicing ---")
print(f"[:3] (position, exclusive end):\n{gene_expression[:3]}")
print(f"[:'GeneC'] (label, INCLUSIVE end):\n{gene_expression[:'GeneC']}")
print(f"['GeneB':'GeneE'] (label, INCLUSIVE):\n{gene_expression['GeneB':'GeneE']}")
# KEY DIFFERENCE: label slicing is INCLUSIVE at both ends!

# Vectorized operations (element-wise, no loops needed!)
print("\n--- Vectorized Operations ---")
print(f"* 2:\n{gene_expression * 2}")
print(f"+ 100:\n{gene_expression + 100}")
print(f"/ 2:\n{gene_expression / 2}")
print(f"np.exp(/ 2):\n{np.exp(gene_expression / 2)}")

# Boolean filtering
print("\n--- Boolean Filtering ---")
mask = gene_expression > 3
print(f"Mask (> 3):   {mask.tolist()}")
print(f"Filtered:\n{gene_expression[gene_expression > 3]}")

# Membership check
print(f"\n'GeneB' in series: {'GeneB' in gene_expression}")
print(f"'GeneI' in series: {'GeneI' in gene_expression}")

# .get() — avoids KeyError for missing labels
print(f"\n.get('GeneB'):              {gene_expression.get('GeneB')}")
print(f".get('GeneZ'):              {gene_expression.get('GeneZ')}")
print(f".get('GeneZ', default=5):   {gene_expression.get('GeneZ', default=5)}")

############################ Creating Pandas DataFrames ##########################

print("\n---------------------- Creating Pandas DataFrames -----------------------")

# 1. From a dictionary of lists (keys → column names)
data_dict = {
    'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'col2': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
    'col3': [True, False, True, False, True, False, True, False, True]
}
df_dict = pd.DataFrame(data_dict)
print(f"DataFrame from dict:\n{df_dict}")

# With custom row index
custom_idx = ['Row1', 'Row2', 'Row3', 'Row4', 'Row5', 'Row6', 'Row7', 'Row8', 'Row9']
df_custom_idx = pd.DataFrame(data_dict, index=custom_idx)
print(f"\nDataFrame with custom row index:\n{df_custom_idx}")

# 2. From a list of dictionaries (each dict = one row)
# Missing keys → NaN
list_of_dicts = [
    {'name': 'Alice',   'age': 30, 'city': 'New York'},
    {'name': 'Bob',     'age': 24, 'city': 'Paris',  'score': 88},
    {'name': 'Charlie', 'age': 35, 'city': 'London'}
]
df_lod = pd.DataFrame(list_of_dicts)
print(f"\nDataFrame from list of dicts (missing → NaN):\n{df_lod}")

# Control column order
df_lod_ordered = pd.DataFrame(list_of_dicts, columns=['name', 'age', 'score', 'city'])
print(f"\nWith specified column order:\n{df_lod_ordered}")

# 3. From a 2D NumPy array
array_2d = np.arange(20).reshape(4, 5)
df_np = pd.DataFrame(
    array_2d,
    index=['A', 'B', 'C', 'D'],
    columns=['V', 'W', 'X', 'Y', 'Z']
)
print(f"\nDataFrame from 2D NumPy array:\n{df_np}")

# 4. From a dictionary of Series (indices aligned automatically!)
series_A = pd.Series(np.random.randn(4), index=['idx1', 'idx2', 'idx3', 'idx4'])
series_B = pd.Series(np.random.randn(4), index=['idx1', 'idx2', 'idx3', 'idx4'])
series_C = pd.Series(np.random.randn(3), index=['idx1', 'idx2', 'idx6'])  # Different index!
df_series = pd.DataFrame({'A': series_A, 'B': series_B, 'C': series_C})
print(f"\nDataFrame from dict of Series (mismatched index → NaN):\n{df_series}")

######################## DataFrame Attributes and Inspection ######################

df = df_np.copy()   # Work with a clean copy
print("\n--- DataFrame Attributes ---")
print(f"shape:   {df.shape}")      # (rows, cols)
print(f"index:   {df.index.tolist()}")
print(f"columns: {df.columns.tolist()}")
print(f"dtypes:\n{df.dtypes}")
print(f"values:\n{df.values}")
print(f"ndim:    {df.ndim}")       # Always 2 for DataFrame
print(f"size:    {df.size}")       # rows × cols

print("\n--- Inspection Methods ---")
print(f"head(2):\n{df.head(2)}")
print(f"tail(2):\n{df.tail(2)}")
print(f"\ninfo() output:")
df.info()
print(f"\ndescribe():\n{df.describe()}")

# describe() on mixed data (include='all')
df_mixed = pd.DataFrame(list_of_dicts)
print(f"\ndescribe(include='all') on mixed data:\n{df_mixed.describe(include='all')}")
print(f"\ndescribe(include=['object']):\n{df_mixed.describe(include=['object'])}")

############################ DataFrame Indexing and Selection ####################

data_for_selection = {
    'Patient_ID':  ['P001', 'P002', 'P003', 'P004'],
    'Age':         [26,     30,     12,     18],
    'Tumor_size':  [2.5,    1.0,    3.1,    2.2],
    'Metastasis':  [True,   False,  True,   True]
}
df_patient = pd.DataFrame(data_for_selection, index=['S1', 'S2', 'S3', 'S4'])
print(f"\n--- Patient DataFrame ---\n{df_patient}")

# 1. Selecting Columns
print("\n--- Selecting Columns ---")
age_series = df_patient['Age']                      # Single column → Series
print(f"df['Age'] (Series):\n{age_series}")
print(f"Type: {type(age_series)}")

id_series = df_patient.Patient_ID                   # Attribute access (valid identifier only)
print(f"\ndf.Patient_ID:\n{id_series}")

subset = df_patient[['Age', 'Patient_ID']]          # Multiple columns → DataFrame
print(f"\ndf[['Age', 'Patient_ID']] (DataFrame):\n{subset}")

# 2. .loc[] — Label-based selection
print("\n--- .loc[] (Label-based, INCLUSIVE slicing) ---")
print(f"Single row 'S2':\n{df_patient.loc['S2']}")
print(f"\nRows ['S2','S3']:\n{df_patient.loc[['S2', 'S3']]}")
print(f"\nSlice 'S2':'S4' (inclusive):\n{df_patient.loc['S2':'S4']}")
print(f"\nRows + cols:\n{df_patient.loc[['S2','S4'], ['Age','Patient_ID']]}")
print(f"\nAll rows, specific cols:\n{df_patient.loc[:, ['Age', 'Patient_ID']]}")

# 3. .iloc[] — Integer position-based selection
print("\n--- .iloc[] (Position-based, EXCLUSIVE slicing end) ---")
print(f"Row at position 1:\n{df_patient.iloc[1]}")
print(f"\nRows at positions [1,3]:\n{df_patient.iloc[[1, 3]]}")
print(f"\nSlice positions 0:3 (exclusive end):\n{df_patient.iloc[0:3]}")
print(f"\nRows 2,3 and cols 1,2:\n{df_patient.iloc[[2, 3], [1, 2]]}")
print(f"\nAll cols, rows 2,3:\n{df_patient.iloc[[2, 3], :]}")

# 4. Boolean Indexing
print("\n--- Boolean Indexing ---")
mask = df_patient['Age'] > 10
print(f"Boolean mask (Age > 10):\n{mask}")
print(f"\nRows where Age > 10:\n{df_patient[df_patient['Age'] > 10]}")
print(f"\nUsing .loc with boolean:\n{df_patient.loc[df_patient['Age'] > 10]}")
print(f"\nSpecific cols for Age > 10:\n{df_patient.loc[df_patient['Age'] > 10, ['Patient_ID', 'Age']]}")

# KEY DISTINCTION:
# df[condition]          → filters rows
# df['ColName']          → selects column
# df[['Col1', 'Col2']]   → selects multiple columns
# .loc uses LABELS (inclusive slicing)
# .iloc uses INTEGERS (exclusive slicing, like Python)

###################### Loading Data from CSV ##############################

print("\n--- Loading Data from CSV ---")

# Create a sample CSV file
csv_content = (
    "Gene,Sample1_Expr,Sample2_Expr,Sample3_Expr,Chromosome,Is_Tumor_Suppressor\n"
    "BRCA1,120.5,110.2,130.0,chr17,True\n"
    "TP53,80.1,95.5,75.3,chr17,True\n"
    "MYC,500.7,610.1,480.9,chr8,False\n"
    "EGFR,300.0,280.5,320.6,chr7,False\n"
    "PTEN,90.6,85.2,92.3,chr10,True"
)
with open('sample.csv', 'w') as f:
    f.write(csv_content)
print("sample.csv created.")

# Read CSV
df_csv = pd.read_csv('sample.csv')
print(f"\nLoaded from CSV:\n{df_csv}")
print(f"\nhead():\n{df_csv.head()}")
print("\ninfo():")
df_csv.info()

# Use a column as the row index
df_csv_idx = pd.read_csv('sample.csv', index_col='Gene')
print(f"\nWith index_col='Gene':\n{df_csv_idx}")

# Common read_csv parameters (reference)
print("""
Common pd.read_csv() parameters:
  filepath_or_buffer  : file path or URL
  sep=','             : delimiter (use '\\t' for TSV)
  header=0            : row to use as column names
  index_col='Col'     : column to use as row index
  usecols=['A','B']   : only load specific columns
  dtype={'col': int}  : specify column dtypes
  na_values=['NA','?']: additional strings to treat as NaN
  skiprows=N          : skip first N rows
  nrows=N             : only read N rows
""")

print("\n--- Day 23 Complete! Pandas Foundation Built! ---")
