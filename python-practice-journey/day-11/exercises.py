# Creating Tuples
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))
print(my_tuple)

# Create a tuple using tuple packing (parentheses optional)
my_tuple = 1, 2, 3, 4, 5
print(type(my_tuple))
print(my_tuple)

# Create a tuple with a single element - requires a trailing comma!
# my_tuple = (1)  # This will give int data type, not tuple!
my_tuple = (1,)
print(type(my_tuple))
print(my_tuple)

# Create an empty tuple
my_tuple = ()
print(type(my_tuple))
print(my_tuple)

# --- Indexing ---
# Accessing Tuple Elements (Indexing & Slicing)
my_data_tuple = ("Chromosome1", 150000, 150500, "Chromosome2", "Chromosome3")

# Access the first element (Chromosome name)
print(my_data_tuple[0])

# Access the fourth element
print(my_data_tuple[3])

# Access the last element using negative indexing
print(my_data_tuple[-1])

# Access the second to last element
print(my_data_tuple[-2])

# Indexing errors work the same as lists: tuple index out of range
# print(my_data_tuple[-10])  # IndexError!
# print(my_data_tuple[10])   # IndexError!

# --- Slicing ---
# Get elements from index 1 up to (but not including) index 3
print(my_data_tuple[1:3])

# Get elements from the beginning up to index 4 (exclusive)
print(my_data_tuple[:4])

# Get elements from index 2 to the end
print(my_data_tuple[2:])

# Get a copy of the entire tuple
print(my_data_tuple[:])

# Reverse the tuple using slicing
print(my_data_tuple[::-1])

# --- Immutability ---
immutable_tuple = ("data1", "data2", "data3")
print(f"My tuple is {immutable_tuple} with type {type(immutable_tuple)}")

# Tuples are IMMUTABLE - these operations will cause errors:
# immutable_tuple.append(5)       # AttributeError!
# immutable_tuple.insert(2, 6)    # AttributeError!
# immutable_tuple.pop(2)          # AttributeError!
# immutable_tuple.remove("data1") # AttributeError!

# Note: While you can't *change* a tuple, you *can* create a *new* tuple
# based on an existing one (e.g., by combining tuples)
tuple_part1 = (1, 2)
tuple_part2 = (3, 4)
new_combined_tuple = tuple_part1 + tuple_part2
print(f'Combined tuple: {new_combined_tuple}')
print(f"Original tuple_part1: {tuple_part1}")
print(f"Original tuple_part2: {tuple_part2}")

# --- Tuple Unpacking ---
# Assign elements of a tuple to multiple variables
x = (1, 2)
y, z = x
print(f"Tuple: {x}")
print(f"y = {y}")
print(f"z = {z}")

# Example with different data types
data = (10, 'data1', 2, 'data2')
w, x, y, z = data
print(f"w = {w}")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

# What happens if the number of variables doesn't match the number of tuple elements?
# x, y, z = data  # ValueError: too many values to unpack (expected 3)

# --- Useful Tuple Functions and Methods ---
sample_ids = ("Patient1", "Patient2", "Patient3", "Patient1", "Patient4")

# Get the number of items (using the built-in len() function)
num_samples = len(sample_ids)
print(f"Number of samples: {num_samples}")

# Check if an item is in a tuple (using the 'in' operator)
print(f"Is 'Patient5' in tuple? {'Patient5' in sample_ids}")
print(f"Is 'Patient1' in tuple? {'Patient1' in sample_ids}")

# Count occurrences of a value (using the .count() method)
count_patient = sample_ids.count("Patient1")
print(f"Patient1 appears {count_patient} times")

# Find the index of the first occurrence of a value (using the .index() method)
try:
    patient1_index = sample_ids.index("Patient1")
    print(f"Patient1 first appears at index: {patient1_index}")
    
    # This will raise ValueError
    # patient6_index = sample_ids.index("Patient6")
    # print(f"Patient6 index: {patient6_index}")
except ValueError as e:
    print(f"Error finding item: {e}")  # Error finding item: tuple.index(x): x not in tuple
