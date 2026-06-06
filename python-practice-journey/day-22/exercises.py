import numpy as np

############################## Reshaping Arrays #####################################

print("------- Reshaping Arrays --------")

array_1d = np.arange(20)
print(f"Original 1D array: {array_1d}")
print(f"Shape: {array_1d.shape}")

# 1. Reshape to 2D (5 rows, 4 columns)
array_2d = array_1d.reshape(5, 4)
print(f"\nReshaped to (5,4):\n{array_2d}")

# 2. Reshape to 2D (4 rows, 5 columns)
array_2d = array_1d.reshape(4, 5)
print(f"\nReshaped to (4,5):\n{array_2d}")

# 3. Reshape to 3D (2 blocks, 2 rows, 5 columns)
array_3d = array_1d.reshape(2, 2, 5)
print(f"\nReshaped to (2,2,5) - 3D:\n{array_3d}")
print(f"Shape: {array_3d.shape}")   # (2, 2, 5)

# 4. Using -1: NumPy INFERS that dimension automatically
array_infer = array_1d.reshape(10, -1)      # -1 → infers 2 columns (20/10=2)
print(f"\nreshape(10, -1): shape={array_infer.shape}\n{array_infer}")

array_infer2 = array_1d.reshape(-1, 10)     # -1 → infers 2 rows (20/10=2)
print(f"\nreshape(-1, 10): shape={array_infer2.shape}\n{array_infer2}")

array_infer3 = array_1d.reshape(-1, 2)      # -1 → infers 10 rows (20/2=10)
print(f"\nreshape(-1, 2): shape={array_infer3.shape}\n{array_infer3}")

# 5. reshape returns a VIEW if possible (shares memory with original)
array_view = array_1d.reshape(4, 5)
array_view[0, 0] = 99
print(f"\nAfter modifying reshaped view[0,0]=99:")
print(f"Reshaped:\n{array_view}")
print(f"Original 1D (also changed!): {array_1d}")   # Changed - it's a view!

# 6. Incompatible reshape → ValueError
try:
    array_incompat = array_1d.reshape(3, 5)   # 3×5=15 ≠ 20
    print(f"Incompatible: {array_incompat}")
except ValueError as e:
    print(f"\nIncompatible reshape caught: {e}")

##################### Flattening Arrays (ravel vs flatten) #######################

print("\n------- Flattening Arrays --------")
array_2d_flat = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original 2D:\n{array_2d_flat}")

# 1. ravel() → returns a VIEW if possible (memory efficient)
# "Ravel" means to untangle or unknot
raveled = array_2d_flat.ravel()
print(f"\nravel() (view): {raveled}")
raveled[0] = 100
print(f"After raveled[0]=100 → raveled: {raveled}")
print(f"Original ALSO changed: \n{array_2d_flat}")   # VIEW!

# 2. flatten() → always returns a COPY (safe to modify)
array_2d_flat2 = np.array([[1, 2, 3], [4, 5, 6]])
flattened = array_2d_flat2.flatten()
print(f"\nflatten() (copy): {flattened}")
flattened[0] = 100
print(f"After flattened[0]=100 → flattened: {flattened}")
print(f"Original UNCHANGED: \n{array_2d_flat2}")     # COPY!

# Order options
print(f"\nflatten('C') row-major (default): {array_2d_flat2.flatten('C')}")
print(f"flatten('F') col-major:           {array_2d_flat2.flatten('F')}")

# Key difference:
# ravel()   → VIEW (fast, memory efficient, modifies original)
# flatten() → COPY (safe, always independent)

#################### Boolean Array Masking ###############################

print("\n------- Boolean Array Masking --------")

array_A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"Original array: {array_A}")
print(f"Shape: {array_A.shape}, ndim: {array_A.ndim}, dtype: {array_A.dtype}")

# Create a boolean mask (same shape as array)
mask = array_A > 5
print(f"\nMask (array_A > 5): {mask}")
print(f"Masked elements:    {array_A[mask]}")   # Returns only True elements

#################### Combining and Splitting Arrays ###############################

print("\n------- Stacking Arrays --------")
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(f"1D array1: {array1}  shape: {array1.shape}")
print(f"1D array2: {array2}  shape: {array2.shape}")

# 1. vstack / row_stack - stack as rows (increases row count)
vstack_result = np.vstack((array1, array2))
print(f"\nvstack → shape {vstack_result.shape}:\n{vstack_result}")
print(f"row_stack → same as vstack:\n{np.row_stack((array1, array2))}")

# vstack with 2D arrays
array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([[7, 8, 9], [10, 11, 12]])
vstack_2d = np.vstack((array3, array4))
print(f"\nvstack 2D arrays → shape {vstack_2d.shape}:\n{vstack_2d}")

# 2. hstack - stack side by side (increases column count)
hstack_1d = np.hstack((array1, array2))
print(f"\nhstack 1D → shape {hstack_1d.shape}: {hstack_1d}")  # Concatenates flat

hstack_2d = np.hstack((array3, array4))
print(f"hstack 2D → shape {hstack_2d.shape}:\n{hstack_2d}")

# column_stack - treat 1D arrays as columns (different from hstack for 1D!)
col_stack = np.column_stack((array1, array2))
print(f"\ncolumn_stack 1D → shape {col_stack.shape}:\n{col_stack}")  # 3×2 matrix!
# Useful for building feature matrices from 1D arrays

# 3. concatenate - most general (specify axis)
concat_1d = np.concatenate((array1, array2), axis=0)
print(f"\nconcatenate 1D axis=0: {concat_1d}")

concat_2d_col = np.concatenate((array3, array4), axis=1)   # side by side
concat_2d_row = np.concatenate((array3, array4), axis=0)   # on top of each other
print(f"concatenate 2D axis=1 → shape {concat_2d_col.shape}:\n{concat_2d_col}")
print(f"concatenate 2D axis=0 → shape {concat_2d_row.shape}:\n{concat_2d_row}")

# Incompatible shapes
try:
    bad = np.concatenate((np.array([1,2,3,4,5,6]), array4), axis=0)
except ValueError:
    print("\nIncompatible concatenate shapes caught!")

# ---- Splitting Arrays ----
print("\n------- Splitting Arrays --------")
array_split = np.array([[1, 2, 3, 10],
                         [4, 5, 6, 11],
                         [7, 8, 9, 12]])
print(f"Array:\n{array_split}  shape: {array_split.shape}")

# 1. hsplit - split horizontally (along columns)
h_split4 = np.hsplit(array_split, 4)    # 4 equal column slices
print(f"\nhsplit(4) → {len(h_split4)} parts:")
for i, part in enumerate(h_split4):
    print(f"  Part {i}: shape {part.shape}\n{part}")

h_split_idx = np.hsplit(array_split, [1, 2])  # Split at col 1 and col 2
print(f"\nhsplit([1,2]) → {len(h_split_idx)} parts:")
for i, part in enumerate(h_split_idx):
    print(f"  Part {i}: shape {part.shape}")

# 2. vsplit - split vertically (along rows)
v_split3 = np.vsplit(array_split, 3)    # 3 equal row slices
print(f"\nvsplit(3) → {len(v_split3)} parts:")
for i, part in enumerate(v_split3):
    print(f"  Part {i}: {part}")

# 3. split - general (with axis)
split_rows = np.split(array_split, [1, 2], axis=0)   # Split at row 1, row 2
print(f"\nnp.split([1,2], axis=0) → {len(split_rows)} parts:")
for i, part in enumerate(split_rows):
    print(f"  Part {i}: shape {part.shape}\n{part}")

split_cols = np.split(array_split, 2, axis=1)    # 2 equal col halves
print(f"\nnp.split(2, axis=1) → {len(split_cols)} parts:")
for part in split_cols:
    print(f"  shape {part.shape}\n{part}")

######################### Boolean Indexing & Fancy Indexing #######################

print("\n------------- Boolean Array Indexing -----------------")
bool_array = np.arange(10)
print(f"Array: {bool_array}")

# Basic boolean condition
print(f"\nbool_array > 5:          {bool_array > 5}")
print(f"Elements where > 5:      {bool_array[bool_array > 5]}")

# Compound conditions  (use & | ~ NOT Python's and/or/not!)
print(f"\nAND (>3 & <6):           {bool_array[(bool_array > 3) & (bool_array < 6)]}")
print(f"OR  (<3 | >7):           {bool_array[(bool_array < 3) | (bool_array > 7)]}")
print(f"NOT (~>3):               {bool_array[~(bool_array > 3)]}")

# Modifying with boolean indexing
modify_array = np.arange(20)
print(f"\nOriginal: {modify_array}")
modify_array[modify_array > 5] = 100
print(f"After [>5] = 100: {modify_array}")

# Boolean indexing on 2D arrays
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D array:\n{mat}")
print(f"Elements > 5: {mat[mat > 5]}")  # Returns 1D result

mat_copy = mat.copy()
mat_copy[mat_copy > 5] = 100
print(f"After [>5] = 100:\n{mat_copy}")

mat_copy2 = mat.copy()
mat_copy2[mat_copy2 < 5] = 0
print(f"After [<5] = 0:\n{mat_copy2}")

##################### Fancy Indexing #############################

print(f"\n--------- Fancy Indexing ---------------")
# Fancy indexing: use LIST/ARRAY of indices to select elements
fancy_1d = np.arange(20, 31)
print(f"1D array: {fancy_1d}")

# Select elements at specific indices
idx = [0, 5, 8]
print(f"\nElements at indices {idx}: {fancy_1d[idx]}")  # [20, 25, 28]

# 2D index array - result shape matches index shape
idx_2d = np.array([[1, 2], [3, 6]])
print(f"\n2D index:\n{idx_2d}")
print(f"Result shape matches index shape: {fancy_1d[idx_2d].shape}")
print(f"Result:\n{fancy_1d[idx_2d]}")

# Fancy indexing on 2D array
mat_fancy = np.array([[1, 2, 8], [3, 6, 9], [4, 5, 10]])
print(f"\n2D matrix:\n{mat_fancy}")

# Select specific rows
rows = [0, 2]
print(f"\nRows {rows}:\n{mat_fancy[rows, :]}")     # All columns of rows 0 and 2

# Select specific columns
cols = [0, 2]
print(f"Cols {cols}:\n{mat_fancy[:, cols]}")        # All rows of cols 0 and 2

# Select specific (row, col) pairs
row_idx = np.array([0, 1, 2])
col_idx = np.array([0, 2, 1])
print(f"\nElement pairs (row,col)={(list(zip(row_idx,col_idx)))}:")
print(f"  → {mat_fancy[row_idx, col_idx]}")         # [mat[0,0], mat[1,2], mat[2,1]]

# Modifying with fancy indexing
modify_fancy = np.arange(20, 31)
print(f"\nOriginal: {modify_fancy}")
modify_fancy[[2, 5, 8]] = 56
print(f"After setting indices [2,5,8]=56: {modify_fancy}")

######################### NumPy File I/O #######################################

print(f"\n----- NumPy File I/O --------")

# 1. Save/Load single array (.npy binary)
array_to_save = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
np.save("2d_array_save.npy", array_to_save)
print(f"Saved .npy. Array:\n{array_to_save}")

loaded_npy = np.load("2d_array_save.npy")
print(f"Loaded .npy:\n{loaded_npy}")
print(f"Arrays equal: {np.array_equal(array_to_save, loaded_npy)}")

# 2. Save/Load multiple arrays (.npz archive)
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d_A = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr_2d_B = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])

np.savez("multiple_arrays_save.npz", arrA=arr_1d, arrB=arr_2d_A, arrC=arr_2d_B)
print(f"\nSaved .npz with keys: arrA, arrB, arrC")

loaded_npz = np.load("multiple_arrays_save.npz")
print(f"Available keys: {list(loaded_npz.keys())}")
print(f"arrA: {loaded_npz['arrA']}")
print(f"arrB:\n{loaded_npz['arrB']}")
print(f"arrC:\n{loaded_npz['arrC']}")
loaded_npz.close()   # Good practice!

# 3. Save/Load text file (CSV-like)
arr_csv = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
np.savetxt("array_to_save.csv", arr_csv,
           delimiter=",",
           fmt="%.2f",
           header="Col1,Col2,Col3,Col4,Col5",
           comments="")
print(f"\nSaved .csv")

loaded_csv = np.loadtxt("array_to_save.csv", delimiter=",", skiprows=1, dtype=float)
print(f"Loaded .csv:\n{loaded_csv}")

# 4. genfromtxt - handles missing values (NaN)
with open("data_with_missing.txt", "w") as f:
    f.write("1,2,nan\n4,nan,6")

loaded_missing = np.genfromtxt("data_with_missing.txt", delimiter=",")
print(f"\nLoaded with NaN:\n{loaded_missing}")

# Replace NaN with 0 (or any value)
cleaned = np.nan_to_num(loaded_missing, nan=0)
print(f"After nan_to_num(nan=0):\n{cleaned}")

############## Basic Linear Algebra ##################################

print("\n--- Basic Linear Algebra (np.linalg) ---")

array1 = np.array([1, 2, 3, 4, 5, 6])
array2 = np.array([7, 8, 9, 10, 11, 12])
array3 = np.array([[1, 2, 3], [4, 5, 6]])          # shape (2,3)
array4 = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])  # shape (3,3)

# 1. Dot product (sum of element-wise products)
dot = np.dot(array1, array2)
print(f"Dot product {array1} · {array2} = {dot}")

# 2. Matrix multiplication (@ operator or np.matmul)
# Requires: cols of A == rows of B   (2×3) @ (3×3) → (2×3)
mat_mul = array3 @ array4
print(f"\nMatrix multiply (2×3) @ (3×3) → (2×3):\n{mat_mul}")

# 3. Transpose
print(f"\narray3.T (transpose):\n{array3.T}")   # shape (3,2)

# 4. Matrix inverse (square matrix only)
square = np.array([[1, 2], [3, 4]])
inv = np.linalg.inv(square)
print(f"\nMatrix:\n{square}")
print(f"Inverse:\n{inv}")
print(f"M @ M_inv (should be identity):\n{np.round(square @ inv)}")

# 5. Determinant
det = np.linalg.det(square)
print(f"\nDeterminant: {det:.2f}")

# 6. Eigenvalues and Eigenvectors
eig_mat = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])
eigenvalues, eigenvectors = np.linalg.eig(eig_mat)
print(f"\nEigenvalues: {np.round(eigenvalues, 4)}")
print(f"Eigenvectors:\n{np.round(eigenvectors, 4)}")

# 7. Matrix rank
rank = np.linalg.matrix_rank(eig_mat)
print(f"\nMatrix rank: {rank}")   # 2 (rank-deficient!)

# 8. Trace (sum of diagonal elements)
print(f"Trace: {np.trace(eig_mat)}")   # 7+11+15 = 33

print("\n--- Day 22 Complete! NumPy Advanced Mastered! ---")
