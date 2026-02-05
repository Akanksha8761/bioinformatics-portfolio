############## Basic List Comprehensions (Simple Transformation) ####################

# Traditional way: Create a list of squares from a range of numbers
empty_list = []
for x in range(10):
    empty_list.append(x**2)
print(f"The squares are {empty_list}")

# Equivalent using list comprehension
squares = [x**2 for x in range(10)]
print(f"The squares using list comprehension: {squares}")

# Traditional way: Convert a list of gene names to uppercase
gene_name = ["myb77", "brca2", "wrky23", "bzip", "myc", "tp53"]
upper = []
for i in gene_name:
    upper.append(i.upper())
print(f'The gene names in uppercase: {upper}')

# Equivalent using list comprehension
upper = [i.upper() for i in gene_name]
print(f'The gene names in uppercase after list comprehension: {upper}')

# Traditional way: Add a suffix to each item in a list
gene_name = ["myb77", "brca2", "wrky23", "bzip", "myc", "tp53"]
suffix = []
for i in gene_name:
    suffix.append(i + "_processed")
print(f'The gene names with suffix "_processed": {suffix}')

# Equivalent using list comprehension
suffix = [i + "_processed" for i in gene_name]
print(f'The gene names with suffix using list comprehension: {suffix}')

########################### List Comprehensions with Filtering ####################

# Traditional way: Get only the even numbers from a range
even = []
for x in range(20):
    if x % 2 == 0:
        even.append(x)
print(f"The even numbers from 0 to 20: {even}")

# Equivalent using list comprehension
num = range(20)
even = [x for x in num if x % 2 == 0]
print(f"The even numbers using list comprehension: {even}")

# Traditional way: Filter methylation values above a threshold
methylation_values = [0.1, 0.5, 0.6, 0.9, 0.22, 1]
threshold = 0.75
hyper_meth = []
for i in methylation_values:
    if i > threshold:
        hyper_meth.append(i)
print(f"The hyper methylated expression values: {hyper_meth}")

# Equivalent using list comprehension
hyper_meth = [i for i in methylation_values if i > threshold]
print(f"The hyper methylated values using list comprehension: {hyper_meth}")

# Traditional way: Get gene names that start with 'B' or 'M'
gene_name = ["myb77", "brca2", "wrky23", "bzip", "myc", "tp53"]
gene_list = []
for i in gene_name:
    i_upper = i.upper()
    if i_upper.startswith('B') or i_upper.startswith('M'):
        gene_list.append(i)
print(f"The gene names that start with 'B' or 'M': {gene_list}")

# Equivalent using list comprehension
gene_list = [i for i in gene_name if i.upper().startswith('B') or i.upper().startswith('M')]
print(f"The gene names starting with B or M using list comprehension: {gene_list}")

################ List Comprehensions with Conditional Expression ####################

# Traditional way: Label numbers as 'Even' or 'Odd'
numbers = range(10)
new_list = []
for i in numbers:
    if i % 2 == 0:
        new_list.append('Even')
    else:
        new_list.append('Odd')
print(f"The numbers labeled as even or odd: {new_list}")

# Equivalent using list comprehension
new_list = ['Even' if i % 2 == 0 else 'Odd' for i in numbers]
print(f"Labels using list comprehension: {new_list}")

# Traditional way: Categorize gene expression as 'High' or 'Low'
methylation_values = [0.1, 0.5, 0.6, 0.9, 0.22, 1]
threshold = 0.75
new_label = []
for i in methylation_values:
    if i > threshold:
        new_label.append('High')
    else:
        new_label.append('Low')
print(f"The values labeled as High or Low: {new_label}")

# Equivalent using list comprehension
new_label = ['High' if i > threshold else 'Low' for i in methylation_values]
print(f"Labels using list comprehension: {new_label}")

# Combining transformation and filtering (filter *first*, then apply expression)
# Traditional way: Get the square ONLY for even numbers
number = range(20)
new_number = []
for i in number:
    if i % 2 == 0:
        i_squared = i**2
        new_number.append(i_squared)
print(f"The squares of even numbers: {new_number}")

# Equivalent using list comprehension
new_number = [i**2 for i in number if i % 2 == 0]
print(f"Squares of even numbers using list comprehension: {new_number}")

######################### Nested List Comprehensions ###########################################

# Traditional way: Create a list of coordinate pairs from two ranges
new_list = []
for i in range(10):
    for j in range(5):
        new_list.append((i, j))  # Tuple requires parentheses
print(f"Coordinates: {new_list}")

# Equivalent using nested list comprehension
new_list = [(i, j) for i in range(10) for j in range(5)]
print(f"Coordinates using list comprehension: {new_list}")

# Traditional way: Flatten a list of lists
list_of_list = [[1, 2], [3, 4, 5], [6, 7, 8, 9, 10]]
flatten_list = []
for i in list_of_list:
    for j in i:
        flatten_list.append(j)
print(f"The flattened list: {flatten_list}")

# Equivalent using nested list comprehension
flatten_list = [j for i in list_of_list for j in i]
print(f"Flattened list using list comprehension: {flatten_list}")

# Traditional way: Get only even numbers from flattened list
list_of_list = [[1, 2], [3, 4, 5], [6, 7, 8, 9, 10]]
even_flatten_list = []
for i in list_of_list:
    for j in i:
        if j % 2 == 0:
            even_flatten_list.append(j)
print(f"The even flattened list: {even_flatten_list}")

# Equivalent using nested list comprehension with condition
even_flatten_list = [j for i in list_of_list for j in i if j % 2 == 0]
print(f"Even flattened list using list comprehension: {even_flatten_list}")
