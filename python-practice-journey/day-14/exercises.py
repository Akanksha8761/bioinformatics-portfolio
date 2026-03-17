################################################ Tasks - Lists ################################################################################

# Task 1.1: Create and Access
# Create a list called gene_expression_values with 5 floating-point numbers representing expression levels (e.g., [120.5, 88.3, 210.1, 55.7, 15.9]).
# Print the entire list.
# Print the expression level of the third gene (using index).
# Print the last expression level (using negative index).
# Print a slice containing the middle three expression levels.
gene_expression_value = [120.5, 88.3, 210.1, 55.7, 15.9]
print(f"The list containing gene expression is: {gene_expression_value}")
print(f"The expression level of the third gene is {gene_expression_value[2]}")  # Index 2 is third element
print(f"The expression level of last gene is {gene_expression_value[-1]}")
print(f"The expression level of middle three genes are {gene_expression_value[1:4]}")

# Task 1.2: Modify and Extend
# Using the gene_expression_values list from Task 1.1:
# Change the second expression value to 92.1. Print the list.
# Add a new expression value 305.0 to the end of the list. Print the list.
# Insert an expression value 5.2 at the beginning of the list. Print the list.
gene_expression_value[1] = 92.1  # Change second element (index 1)
print(f"The list after changing the expression level of 2nd element is: {gene_expression_value}")
gene_expression_value.append(305.0)
print(f"The list after adding the expression level is: {gene_expression_value}")
gene_expression_value.insert(0, 5.2)
print(f"The list after inserting at beginning is: {gene_expression_value}")

# Task 1.3: Remove and Check
# Using the modified gene_expression_values list:
# Remove the expression value 55.7 by its value. Print the list.
# Remove the item at index 2 using .pop(). Print the removed value and the list.
# Check if the value 92.1 is still in the list and print True or False.
gene_expression_value.remove(55.7)
print(f"The list after removing 55.7 expression level: {gene_expression_value}")
removed = gene_expression_value.pop(2)
print(f"Removed value: {removed}")
print(f"The list after using pop(2): {gene_expression_value}")
print(f"Is 92.1 in list? {92.1 in gene_expression_value}")

####################################### Tasks - Tuples ################################################################################

# Task 2.1: Create and Access
# Create a tuple called genomic_coordinate representing a region ("chr17", 76735400, 76760000) (Chromosome, Start, End).
# Print the tuple.
# Print the chromosome name.
# Print the start and end coordinates as a slice (should result in a new tuple).
genomic_coordinate = ("chr17", 76735400, 76760000)
print(f"The genomic coordinates are {genomic_coordinate} and its type is {type(genomic_coordinate)}")
print(f"The chromosome name is {genomic_coordinate[0]}")
print(f"The start and end of the tuple is {genomic_coordinate[1:3]}")

# Task 2.2: Immutability
# Using the genomic_coordinate tuple:
# Attempt to change the chromosome name to "chr1". Comment out the line that causes the error but explain in a comment why it errors.
# Attempt to add a strand indicator "+" to the tuple. Comment out the line and explain why it errors.

# genomic_coordinate[0] = "chr1"  # TypeError! Tuples are IMMUTABLE - cannot modify elements
# genomic_coordinate.append("+")  # AttributeError! Tuples don't have append() - they're immutable

# Task 2.3: Unpacking and Membership
# Using the genomic_coordinate tuple:
# Unpack the tuple into three variables: chromosome, start, end. Print the values of these new variables.
# Check if the number 76735400 is present in the genomic_coordinate tuple and print the boolean result.
chrm, start, end = genomic_coordinate
print(f"The chromosome name is {chrm}, the start is {start} and the end is {end}")
print(f"Is 76735400 in tuple? {76735400 in genomic_coordinate}")

########################################################## Tasks - Dictionaries #########################################################

# Task 3.1: Create and Access
# Create a dictionary called patient_info storing metadata for a patient: keys could be strings like "patient_id", "age", "diagnosis", "is_treated". Choose appropriate values.
# Print the entire dictionary.
# Access and print the patient's diagnosis using square brackets [].
# Attempt to access a key that doesn't exist (e.g., "treatment_date") using .get(). Print the result (should be None).
# Attempt the same access using .get(), but provide a default value like "Not Available". Print the result.

patient_info = {"patient_id": "patient_1", "age": 26, "diagnosis": "cancer", "is_treated": False}
print(f"The metadata of patient is {patient_info} and its type is {type(patient_info)}")
print(f"The patient diagnosis is {patient_info['diagnosis']}")
print(f"The gender of patient is {patient_info.get('gender')}")
print(f"The gender of patient is {patient_info.get('gender', 'Not Available')}")

# Task 3.2: Modify and Add
# Using the patient_info dictionary:
# Update the value for "is_treated" to True. Print the dictionary.
# Add a new key-value pair for "tumor_stage" with an appropriate value (e.g., "Stage II"). Print the dictionary.
patient_info['is_treated'] = True
print(f"The updated version is {patient_info}")

patient_info['tumor_stage'] = "Stage II"
print(f"After adding tumor_stage: {patient_info}")

# Task 3.3: Remove and Iterate
# Using the patient_info dictionary:
# Remove the "age" entry using del. Print the dictionary.
# Remove the "tumor_stage" entry using .pop() and store the removed value in a variable. Print the removed value and the dictionary.
# Iterate through the remaining items in the dictionary and print each key-value pair using an f-string (e.g., "Key: value").
del patient_info['age']
print(f"Dictionary after removing age is {patient_info}")
removed_stage = patient_info.pop('tumor_stage')
print(f"Removed tumor_stage: {removed_stage}")
print(f"Dictionary after popping: {patient_info}")
for key, value in patient_info.items():
    print(f"Key: {key} and value: {value}")

####################################################### Tasks - Sets #############################################################

# Task 4.1: Create and Add
# Create a list called raw_mutation_types with some duplicate string entries (e.g., ["Missense", "Silent", "Missense", "Frameshift", "Silent", "Nonsense"]).
# Convert this list into a set called unique_mutation_types. Print the set. Note how duplicates are handled.
# Add a new mutation type "Splice Site" to the unique_mutation_types set. Print the set.
raw_mutation_types = ["Missense", "Silent", "Missense", "Frameshift", "Silent", "Nonsense"]
unique_mutation_types = set(raw_mutation_types)
print(f"The values in unique mutation set are: {unique_mutation_types} and its type is {type(unique_mutation_types)}")
unique_mutation_types.add("Splice Site")
print(f"After adding 'Splice Site': {unique_mutation_types}")

# Task 4.2: Remove and Membership
# Using the unique_mutation_types set:
# Remove "Silent" using .remove(). Print the set.
# Attempt to remove "Indel" using .discard(). Print the set (should be unchanged, no error).
# Check if "Missense" is in the set and print the boolean result.
unique_mutation_types.remove("Silent")
print(f"After removing 'Silent': {unique_mutation_types}")
unique_mutation_types.discard("Indel")  # No error even if not found
print(f"After discard('Indel'): {unique_mutation_types}")
print(f"Is 'Missense' in set? {'Missense' in unique_mutation_types}")

# Task 4.3: Set Operations
# Create two sets: genes_in_pathway1 = {"TP53", "MYC", "KRAS", "PTEN"} and genes_in_pathway2 = {"MYC", "EGFR", "BRAF", "PTEN"}.
# Find and print the union of the two sets (genes in either pathway).
# Find and print the intersection of the two sets (genes common to both pathways).
# Find and print the difference (genes in pathway1 but not in pathway2).
# Find and print the symmetric difference (genes in either pathway, but not both).
genes_in_pathway1 = {"TP53", "MYC", "KRAS", "PTEN"}
genes_in_pathway2 = {"MYC", "EGFR", "BRAF", "PTEN"}
print(f"The union of two sets is {genes_in_pathway1 | genes_in_pathway2}")
print(f"The intersection of two sets is {genes_in_pathway1 & genes_in_pathway2}")
print(f"The difference of two sets is {genes_in_pathway1 - genes_in_pathway2}")
print(f"The symmetric difference of two sets is {genes_in_pathway1 ^ genes_in_pathway2}")

########################################### Tasks - List Comprehensions #####################################################

# Task 5.1: Basic Transformation
# Create a list of numbers from 1 to 10.
# Use a list comprehension to create a new list where each number is multiplied by 2. Print the new list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional loop
doubled_loop = []
for i in numbers:
    doubled_loop.append(i * 2)
print(f"Doubled (loop): {doubled_loop}")

# List comprehension
doubled = [i * 2 for i in numbers]
print(f"Doubled (list comprehension): {doubled}")

# Task 5.2: Filtering
# Use a list comprehension on the list from Task 5.1 to create a new list containing only the numbers greater than 10. Print the new list.
test_numbers = [1, 3, 5, 6, 3, 8, 10, 20, 35]

# Traditional loop
greater_loop = []
for i in test_numbers:
    if i > 10:
        greater_loop.append(i)
print(f"Greater than 10 (loop): {greater_loop}")

# List comprehension
greater = [i for i in test_numbers if i > 10]
print(f"Greater than 10 (list comprehension): {greater}")

# Task 5.3: Conditional Expression
# Use a list comprehension on the list from Task 5.1 to create a new list of strings. If a number is even, the string should be "Even"; otherwise, it should be "Odd". Print the new list.
test_numbers = [1, 3, 5, 6, 3, 8, 10, 20, 35]

# Traditional loop
labels_loop = []
for i in test_numbers:
    if i % 2 == 0:
        labels_loop.append("Even")
    else:
        labels_loop.append("Odd")
print(f"Labels (loop): {labels_loop}")

# List comprehension
labels = ["Even" if i % 2 == 0 else "Odd" for i in test_numbers]
print(f"Labels (list comprehension): {labels}")

# Task 5.4: Nested Comprehension
# Create a list of lists representing data rows: data_rows = [[1, 5, 8], [12, 3, 6], [9, 15, 2]].
# Use a nested list comprehension to flatten this list of lists into a single list of all numbers. Print the flattened list.
data_rows = [[1, 5, 8], [12, 3, 6], [9, 15, 2]]

# Traditional nested loop
flattened_loop = []
for row in data_rows:
    for num in row:
        flattened_loop.append(num)
print(f"Flattened (loop): {flattened_loop}")

# Nested list comprehension
flattened = [num for row in data_rows for num in row]
print(f"Flattened (list comprehension): {flattened}")

####################################### Section 6: Integrated Tasks (Combining Structures & Comprehensions) #######################################

# Task 6.1: Dictionary Values to List (Filtered)
# You have a dictionary gene_counts = {"GeneA": 150, "GeneB": 80, "GeneC": 220, "GeneD": 45, "GeneE": 180}.
# Use a list comprehension on the values of this dictionary to create a list containing only the counts that are greater than 100. Print the resulting list.
gene_counts = {"GeneA": 150, "GeneB": 80, "GeneC": 220, "GeneD": 45, "GeneE": 180}

# Traditional loop (items)
high_counts_loop = []
for gene, count in gene_counts.items():
    if count > 100:
        high_counts_loop.append((gene, count))
print(f"High counts (loop): {high_counts_loop}")

# List comprehension
high_counts = [(gene, count) for gene, count in gene_counts.items() if count > 100]
print(f"High counts (list comprehension): {high_counts}")

# Task 6.2: Extract Keys based on Value Condition
# Using the same gene_counts dictionary.
# Use a list comprehension on the items of this dictionary to create a list containing the names (keys) of genes whose count is greater than 100. Print the resulting list.
gene_counts = {"GeneA": 150, "GeneB": 80, "GeneC": 220, "GeneD": 45, "GeneE": 180}

# Traditional loop
high_genes_loop = []
for gene, count in gene_counts.items():
    if count > 100:
        high_genes_loop.append(gene)
print(f"High genes (loop): {high_genes_loop}")

# List comprehension
high_genes = [gene for gene, count in gene_counts.items() if count > 100]
print(f"High genes (list comprehension): {high_genes}")

# Task 6.3: Finding Common Elements (List -> Set -> Operation)
# You have two lists of sample IDs that passed initial QC: qc_pass_batch1 = ["Sample_01", "Sample_03", "Sample_05", "Sample_07"] and qc_pass_batch2 = ["Sample_02", "Sample_03", "Sample_06", "Sample_07", "Sample_08"].
# Use sets to find the sample IDs that passed QC in both batches. Print the result.
qc_pass_batch1 = ["Sample_01", "Sample_03", "Sample_05", "Sample_07"]
qc_pass_batch2 = ["Sample_02", "Sample_03", "Sample_06", "Sample_07", "Sample_08"]

# Convert to sets and find intersection
qc_batch1_set = set(qc_pass_batch1)
qc_batch2_set = set(qc_pass_batch2)
common_samples = qc_batch1_set & qc_batch2_set
print(f"Samples that passed QC in both batches: {common_samples}")

# Task 6.4: Create a Dictionary from Lists using Comprehension (Advanced)
# You have a list of gene names: genes = ["GeneX", "GeneY", "GeneZ"]
# You have a corresponding list of expression values: expression_levels = [10.5, 25.2, 8.1]
# Use a dictionary comprehension (similar syntax to list comprehension but with {} and a key: value expression) to create a dictionary mapping each gene name to its expression level. Print the dictionary.
# Hint: The syntax is {key_expression: value_expression for item in iterable} or {key_expression: value_expression for item1, item2 in zip(iterable1, iterable2)}. zip() is a built-in function that pairs up elements from multiple iterables.
genes = ["GeneX", "GeneY", "GeneZ"]
expression_levels = [10.5, 25.2, 8.1]

# Using zip() and dict()
gene_expression_dict = dict(zip(genes, expression_levels))
print(f"The dictionary (using dict + zip): {gene_expression_dict} and its type is {type(gene_expression_dict)}")

# Using dictionary comprehension
gene_expression_dict_comp = {gene: level for gene, level in zip(genes, expression_levels)}
print(f"The dictionary (using dict comprehension): {gene_expression_dict_comp}")
