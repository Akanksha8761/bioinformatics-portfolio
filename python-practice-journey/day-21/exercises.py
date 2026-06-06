import numpy as np
print(f"NumPy Version: {np.__version__}")

################# Creating NumPy Arrays ##########################

print("\n--- Creating Arrays from Python Lists ---")

# 1. Creating a 1-D array (vector)
python_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original python list: {python_list}")
print(f"Type: {type(python_list)}")

array_1d = np.array(python_list)
print(f"1D NumPy array: {array_1d}")
print(f"Type: {type(array_1d)}")
print(f"Shape: {array_1d.shape}")       # (10,) - 10 elements
print(f"dtype: {array_1d.dtype}")       # int64

# 2. Creating a 2-D array (matrix) from a list of lists
python_list_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\nOriginal list of lists: {python_list_2D}")
print(f"Type: {type(python_list_2D)}")

array_2d = np.array(python_list_2D)
print(f"2D NumPy array:\n{array_2d}")
print(f"Type: {type(array_2d)}")
print(f"Shape: {array_2d.shape}")       # (3, 3) - 3 rows, 3 columns
print(f"dtype: {array_2d.dtype}")

# 3. Specifying the data type during creation
array_float = np.array([1, 2, 3], dtype=float)
print(f"\nFloat array: {array_float}")
print(f"dtype: {array_float.dtype}")    # float64

# 4. Creating an array of complex datatype
array_complex = np.array([1+2j, 2+4j, 3+6j], dtype=complex)
print(f"\nComplex array: {array_complex}")
print(f"dtype: {array_complex.dtype}")  # complex128

######################## Creating Arrays with Built-in NumPy Functions #####

print("\n--- Creating Arrays with NumPy Functions ---")

# 1. Array of zeros
zero_array = np.zeros(5)
print(f"1D zeros: {zero_array}")
print(f"dtype: {zero_array.dtype}")  # float64 by default

zero_2d = np.zeros((3, 4), dtype=int)
print(f"2D zeros (3x4):\n{zero_2d}")
print(f"Shape: {zero_2d.shape}")

# 2. Array of ones
ones_array = np.ones(5)
print(f"\n1D ones: {ones_array}")

ones_2d = np.ones((2, 5), dtype=np.int16)
print(f"2D ones (2x5) int16:\n{ones_2d}")

# 3. Array with a constant value
array_constant = np.full((2, 5), 6)
print(f"\nConstant array (value=6):\n{array_constant}")

# 4. Identity matrix (1s on diagonal, 0s elsewhere)
identity_matrix = np.eye(3)
print(f"\n3x3 Identity matrix:\n{identity_matrix}")

# 5. Array with a range of numbers (like Python's range)
range_array = np.arange(10)
print(f"\narange(10): {range_array}")

range_array = np.arange(0, 21, 2)
print(f"arange(0, 21, 2): {range_array}")

range_array = np.arange(0, 1, 0.2)
print(f"arange(0, 1, 0.2): {range_array}")

# 6. Array with evenly spaced numbers (np.linspace)
linspace_array = np.linspace(0, 10, 50)  # Default: 50 points
print(f"\nlinspace(0, 10) - 50 points, first 5: {linspace_array[:5]}")

linspace_array = np.linspace(0, 10, 10)
print(f"linspace(0, 10, 10): {linspace_array}")

linspace_array = np.linspace(0, 10, 10, endpoint=False)
print(f"linspace(0, 10, 10, endpoint=False): {linspace_array}")

# 7. Array with random numbers
print("\n--- Random Arrays ---")
random_uniform = np.random.rand(5)
print(f"rand(5) - uniform [0,1): {random_uniform}")

random_matrix = np.random.rand(2, 5)
print(f"rand(2,5) - 2D uniform:\n{random_matrix}")

# Standard normal distribution (mean=0, std=1)
random_normal = np.random.randn(5)
print(f"randn(5) - standard normal: {random_normal}")

# Random integers
random_int = np.random.randint(0, 10, 5)
print(f"randint(0, 10, 5): {random_int}")

random_int_2d = np.random.randint(0, 10, size=(5, 3))
print(f"randint(0, 10, size=(5,3)):\n{random_int_2d}")

################################### Array Attributes ##############################

print("\n--- Array Attributes ---")
test_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array:\n{test_array}")

print(f"ndim   (dimensions):  {test_array.ndim}")    # 2
print(f"shape  (rows,cols):   {test_array.shape}")   # (3, 3)
print(f"size   (total elems): {test_array.size}")    # 9
print(f"dtype  (data type):   {test_array.dtype}")   # int64
print(f"itemsize (bytes/elem):{test_array.itemsize}")# 8
print(f"nbytes (total bytes): {test_array.nbytes}")  # 72

print("\n--- 1D Array Attributes ---")
new_1d = np.arange(5)
print(f"Array: {new_1d}")
print(f"ndim:     {new_1d.ndim}")      # 1
print(f"shape:    {new_1d.shape}")     # (5,)
print(f"size:     {new_1d.size}")      # 5
print(f"dtype:    {new_1d.dtype}")     # int64
print(f"itemsize: {new_1d.itemsize}")  # 8
print(f"nbytes:   {new_1d.nbytes}")    # 40

################### Indexing (Accessing Elements) #########################

print("\n--- 1D Array Indexing ---")
test_1d = np.arange(10, 20)
print(f"Array: {test_1d}")
print(f"Index 0:  {test_1d[0]}")     # 10
print(f"Index 7:  {test_1d[7]}")     # 17
print(f"Index -1: {test_1d[-1]}")    # 19

# Modifying an element
test_1d[0] = 200
print(f"After test_1d[0] = 200: {test_1d}")

print("\n--- 2D Array Indexing ---")
test_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array:\n{test_2d}")
print(f"[0, 0]: {test_2d[0, 0]}")   # 1  (row 0, col 0)
print(f"[1, 2]: {test_2d[1, 2]}")   # 6  (row 1, col 2)

# Modifying an element
test_2d[1, 2] = 17
print(f"After test_2d[1,2] = 17:\n{test_2d}")

############## Slicing (Accessing Sub-arrays) ############################

print("\n--- 1D Array Slicing ---")
slice_1d = np.arange(21)
print(f"Array: {slice_1d}")
print(f"[5:11]:   {slice_1d[5:11]}")     # indices 5 to 10
print(f"[:11]:    {slice_1d[:11]}")      # start to 10
print(f"[5:]:     {slice_1d[5:]}")       # 5 to end
print(f"[::2]:    {slice_1d[::2]}")      # every 2nd element
print(f"[::-1]:   {slice_1d[::-1]}")     # reversed

print("\n--- 2D Array Slicing ---")
slice_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Array:\n{slice_2d}")
print(f"First 2 rows:\n{slice_2d[0:2]}")
print(f"All rows, cols 0-1:\n{slice_2d[:, 0:2]}")
print(f"Rows 1-2, cols 0-1:\n{slice_2d[1:3, 0:2]}")
print(f"Row 1 (1D result): {slice_2d[1, :]}")

# IMPORTANT: Slices are VIEWS, not copies!
print("\n--- Slice Modification (Views!) ---")
print(f"Original:\n{slice_2d}")
modified = slice_2d[:, 0:2]
print(f"Slice:\n{modified}")
modified[:, :] = 99  # Modifies ORIGINAL too!
print(f"After modifying slice:\n{modified}")
print(f"Original also changed:\n{slice_2d}")  # Changed!

##################### Arithmetic Operations ############################

print("\n--- Arithmetic Operations (Element-wise) ---")
a = np.arange(1, 11)    # [1..10] - avoid division by zero
b = np.arange(10, 20)   # [10..19]
print(f"a: {a}")
print(f"b: {b}")

print(f"a + b:  {a + b}")
print(f"b - a:  {b - a}")
print(f"a * b:  {a * b}")
print(f"b / a:  {b / a}")
print(f"a ** 2: {a ** 2}")

# Scalar operations (broadcasting)
print(f"\na + 5:  {a + 5}")
print(f"a * 5:  {a * 5}")

# Comparison (returns boolean array)
a = np.arange(10)
print(f"\na > 2:  {a > 2}")
print(f"a == 5: {a == 5}")

############################ Universal Functions (ufuncs) ################

print("\n--- Universal Functions (ufuncs) ---")

# Trigonometric
x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
print(f"Angles (radians): {x}")
print(f"sin: {np.round(np.sin(x), 4)}")
print(f"cos: {np.round(np.cos(x), 4)}")

# Exponential and logarithmic
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"\nArray: {x}")
print(f"exp:     {np.exp(x)}")
print(f"log (natural): {np.round(np.log(x), 4)}")
print(f"log10:   {np.round(np.log10(x), 4)}")
print(f"sqrt:    {np.sqrt(x)}")

######################## Aggregation Functions ###########################

print("\n--- Aggregation Functions ---")
x = np.arange(21)
print(f"Array: {x}")
print(f"sum:    {x.sum()}")
print(f"min:    {x.min()}")
print(f"max:    {x.max()}")
print(f"mean:   {x.mean()}")
print(f"std:    {x.std():.4f}")
print(f"median: {np.median(x)}")        # Only np.median(), no .median() method
print(f"var:    {x.var():.4f}")

# Important! median is only np.median() not array.median()
# array.median() -> AttributeError!

print("\n--- 2D Aggregations Along Axes ---")
data_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matrix:\n{data_2d}")
print(f"Total sum:    {data_2d.sum()}")
print(f"Col sums (axis=0): {data_2d.sum(axis=0)}")   # [12, 15, 18]
print(f"Row sums (axis=1): {data_2d.sum(axis=1)}")   # [6, 15, 24]
print(f"Col min (axis=0):  {data_2d.min(axis=0)}")
print(f"Row min (axis=1):  {data_2d.min(axis=1)}")
print(f"Col max (axis=0):  {data_2d.max(axis=0)}")
print(f"Row max (axis=1):  {data_2d.max(axis=1)}")
print(f"Col mean (axis=0): {data_2d.mean(axis=0)}")
print(f"Row mean (axis=1): {data_2d.mean(axis=1)}")
print(f"Col median (axis=0): {np.median(data_2d, axis=0)}")
print(f"Row median (axis=1): {np.median(data_2d, axis=1)}")

# axis=0: operates DOWN columns (result has same number of columns)
# axis=1: operates ACROSS rows (result has same number of rows)

############################ Broadcasting ############################

print("\n--- Broadcasting ---")

# Rule: Arrays are compatible if dimensions are equal OR one of them is 1

# Example 1: Scalar broadcasting
arr = np.arange(3)
print(f"Array: {arr}, shape: {arr.shape}")
print(f"Array + 5: {arr + 5}")

# Example 2: 2D + 1D (row vector broadcast to each row)
bc_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_vector = np.array([10, 20, 30])
print(f"\n2D array:\n{bc_2d}, shape: {bc_2d.shape}")
print(f"Row vector: {row_vector}, shape: {row_vector.shape}")
print(f"2D + row vector:\n{bc_2d + row_vector}")

# Example 3: 2D + column vector (col vector broadcast to each column)
col_vector = np.array([[0], [10], [20]])   # shape (3,1)
print(f"\nCol vector:\n{col_vector}, shape: {col_vector.shape}")
print(f"2D + col vector:\n{bc_2d + col_vector}")

# Example 4: Incompatible shapes - handled gracefully with try-except
incompat_1d = np.array([1, 2, 3, 4])     # shape (4,)
incompat_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # shape (3,3)
print(f"\nShape mismatch: {incompat_1d.shape} + {incompat_2d.shape}")
try:
    result = incompat_1d + incompat_2d
except ValueError as e:
    print(f"ValueError caught: {e}")

######################## Speed: Python List vs NumPy Array #####################

print("\n--- Speed Comparison: Python List vs NumPy ---")
import time

SIZE = 2000

# Python for loop approach
list_a = list(range(SIZE))
list_b = list(range(SIZE))
list_c = [0] * SIZE

start_time = time.time()
for i in range(SIZE):
    list_c[i] = list_a[i] + list_b[i]
end_time = time.time()
python_time = end_time - start_time
print(f"Python for loop time:  {python_time:.8f} seconds")

# NumPy vectorized approach
numpy_array_a = np.arange(SIZE)
numpy_array_b = np.arange(SIZE)

start_time = time.time()
numpy_array_c = numpy_array_a + numpy_array_b
end_time = time.time()
numpy_time = end_time - start_time
print(f"NumPy vectorized time: {numpy_time:.8f} seconds")

# How many times faster?
if numpy_time > 0:
    speedup = python_time / numpy_time
    print(f"NumPy is ~{speedup:.1f}x faster!")
else:
    print("NumPy is too fast to measure at this scale!")

# Scale up to see bigger difference
print("\n--- Larger Scale (1,000,000 elements) ---")
SIZE_BIG = 1_000_000

list_big_a = list(range(SIZE_BIG))
list_big_b = list(range(SIZE_BIG))
list_big_c = [0] * SIZE_BIG

start_time = time.time()
for i in range(SIZE_BIG):
    list_big_c[i] = list_big_a[i] + list_big_b[i]
python_big_time = time.time() - start_time
print(f"Python loop (1M):  {python_big_time:.4f} seconds")

np_big_a = np.arange(SIZE_BIG)
np_big_b = np.arange(SIZE_BIG)

start_time = time.time()
np_big_c = np_big_a + np_big_b
numpy_big_time = time.time() - start_time
print(f"NumPy vector (1M): {numpy_big_time:.4f} seconds")

if numpy_big_time > 0:
    speedup_big = python_big_time / numpy_big_time
    print(f"NumPy is ~{speedup_big:.0f}x faster at 1M elements!")

print("""
Key Takeaway:
- Python loop: each element processed one at a time (interpreted)
- NumPy vector: ALL elements processed at once (C backend, SIMD)
- Difference grows larger with bigger arrays
- This is WHY NumPy is essential for data science & AI/ML!
""")

print("\n--- Day 21 Complete! NumPy Foundation Built! ---")
