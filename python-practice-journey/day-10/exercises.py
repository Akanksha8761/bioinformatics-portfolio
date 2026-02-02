############################# Creating a dictionary ###########################
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")
print(f"Type of Empty dictionary: {type(empty_dict)}")

# Creating a dictionary with initial data
gene_expression = {'TP53': 150.5, 'BRCA1': 85.2, 'MYC': 210.0, 'KRAS': 55.08}
print(f"Gene expression dictionary: {gene_expression}")

# Example: Storing metadata for a patient sample
sample_info = {'sample_id': 'patient1', 'age': 30, 'gender': 'female', 'disease': 'breast_cancer', 'is_treated': True}
print(f"Patient info: {sample_info}")

# Dictionary with mixed value types
sample_info = {'sample_id': 'patient1', 'age': 30, 'gender': 'female', 'disease': 'breast_cancer', 'is_treated': True, 'treatment_files': ['file1.csv', 'file2.csv']}
print(f"Patient info with mixed values: {sample_info}")

# Using dict() constructor (less common for simple creation, but useful)
another_dict = dict(gene="TP53", count=10, active=True)  # Note: keys are passed without quotes like variable names
print("\nCreated with dict():", another_dict)

sample_info = dict(sample_id='patient1', age=30, gender='female', disease='breast_cancer', is_treated=True, treatment_files=['file1.csv', 'file2.csv'])
print(f"Patient info with dict(): {sample_info}")

##################### Accessing Values ##########################################
gene_expression = {'TP53': 150.5, 'BRCA1': 85.2, 'MYC': 210.0, 'KRAS': 55.08}

# 1. Accessing a value using square brackets []
expression_tp53 = gene_expression['TP53']
print(f"Expression of TP53: {expression_tp53}")

# 2. Accessing a value that might not exist - using [] causes KeyError
# expression_brca2 = gene_expression['BRCA2']  # KeyError!
# print(f"Expression of BRCA2: {expression_brca2}")

# 3. Accessing a value using .get() - safer for keys that might not exist
expression_brca2 = gene_expression.get('BRCA2')
print(f"Expression of BRCA2: {expression_brca2}")  # Returns None

# 4. Providing a default value with .get()
expression_brca3_default = gene_expression.get('BRCA3', 0.56)
print(f"Expression of BRCA3 (default): {expression_brca3_default}")

# Default is ignored if key exists
existing_expression_tp53 = gene_expression.get('TP53', 0.035)
print(f"Expression of TP53 (existing): {existing_expression_tp53}")

# 5. Accessing values from the sample_info dictionary
sample_info = {'sample_id': 'patient1', 'age': 30, 'gender': 'female', 'disease': 'breast_cancer', 'is_treated': True}
patient_id = sample_info.get('sample_id')
print(f"Patient ID is: {patient_id}")
patient_age = sample_info.get('age')
print(f"Patient age is: {patient_age}")

######################## Adding and Modifying Items ############################
gene_expression = {'TP53': 150.5, 'BRCA1': 85.2, 'MYC': 210.0, 'KRAS': 55.08}

# 1. Adding a new key-value pair
gene_expression['BRCA4'] = 10.67
print(f"Expression of BRCA4: {gene_expression['BRCA4']}")
print(f"Gene expression dictionary: {gene_expression}")

# 2. Modifying an existing value
gene_expression['MYC'] = 99.56
print(f"Expression of MYC (modified): {gene_expression['MYC']}")
print(f"Gene expression dictionary: {gene_expression}")

# 3. Adding multiple items using update()
add_more_genes = {'PTEN': 785.6, 'EGFR': 45.2}
gene_expression.update(add_more_genes)
print(f"Gene expression dictionary after update: {gene_expression}")

# You can also update with key=value arguments
gene_expression.update(MYC=215.5, KRAS=60.0)  # Note: keys are variable names here
print(f"Gene expression dictionary after second update: {gene_expression}")

############################### Removing Items ################################
sample_info = {'sample_id': 'patient1', 'age': 30, 'gender': 'female', 'disease': 'breast_cancer', 'is_treated': True}
print(f'The original dictionary: {sample_info}')

# 1. Removing an item using del
del sample_info['age']
print(f'The dictionary after deleting "age": {sample_info}')

# KeyError if you try to delete a non-existent key
# del sample_info['city']  # KeyError!

# 2. Removing an item using .pop() - returns the value of the removed item
removed_gender = sample_info.pop('gender')
print(f'Removed gender: {removed_gender}')
print(f'The dictionary after removing "gender": {sample_info}')

# 3. Using .pop(key, default) - useful if key might not exist
removed_tissue = sample_info.pop('tissue', 'skin')
print(f"Removed tissue (default): {removed_tissue}")
print(f'The dictionary after pop with default: {sample_info}')

removed_disease = sample_info.pop('disease', 'cancer')  # Default value is ignored
print(f"Removed disease: {removed_disease}")
print(f'The dictionary after removing "disease": {sample_info}')

# 4. .popitem() removes and returns an arbitrary (key, value) pair (last item in Python 3.7+)
gene_counts = {"A": 5, "B": 10, "C": 3}
print("\nGene counts before popitem:", gene_counts)
popped_pair = gene_counts.popitem()
print("Popped item:", popped_pair)  # Pops from last
print("Gene counts after popitem:", gene_counts)

# 5. .clear() removes all items
gene_expression_copy = {'TP53': 150.5, 'BRCA1': 85.2}
gene_expression_copy.clear()
print(f"Gene expression dictionary after clear: {gene_expression_copy}")

######################### Getting Dictionary Views (.keys(), .values(), .items()) ############################
sample_info = {'sample_id': 'patient1', 'age': 30, 'gender': 'female', 'disease': 'breast_cancer', 'is_treated': True}
print(f'The original dictionary: {sample_info}')

# 1. Get keys
keys = sample_info.keys()
print(f"Keys (view): {keys}")

# Convert keys to a list (common)
keys_list = list(keys)
print(f"Keys (list): {keys_list}")

# 2. Get values
values = sample_info.values()
print(f"Values (view): {values}")
values_list = list(values)
print(f"Values (list): {values_list}")

# 3. Get items (key-value pairs as tuples)
all_items = sample_info.items()
print(f"Items (view): {all_items}")

# Convert items view to a list of tuples
all_items_list = list(all_items)
print(f"All items (list): {all_items_list}")

# 4. Demonstrate views are dynamic (modify dictionary after getting view)
gene_counts = {"GeneA": 5, "GeneB": 10}
keys_view = gene_counts.keys()
print(f"Keys before addition: {keys_view}")
gene_counts['GeneC'] = 35
print(f"Keys after addition: {keys_view}")  # View updates automatically!

########################## Checking for Keys (using 'in') ###########################################
gene_expression = {'TP53': 150.5, 'BRCA1': 85.2, 'MYC': 210.0, 'KRAS': 55.08}
print(f"Is 'TP53' in gene expression? {'TP53' in gene_expression}")
print(f"Is 'EGFR' in gene expression? {'EGFR' in gene_expression}")
print(f"Is 'EGFR' not in gene expression? {'EGFR' not in gene_expression}")

gene_checking = "TP53"
if gene_checking in gene_expression:
    level = gene_expression[gene_checking]
    print(f"Gene {gene_checking} is present in the dictionary")
    print(f"Found with level: {level}")
else:
    print(f"Not found")

gene_checking = "MYC33"
if gene_checking in gene_expression:
    level = gene_expression[gene_checking]
    print(f"Gene {gene_checking} is present in the dictionary")
    print(f"Found with level: {level}")
else:
    print(f"Gene {gene_checking} not found")

############################ Iterating Through Dictionaries #########################################
gene_expression = {'TP53': 150.5, 'BRCA1': 85.2, 'MYC': 210.0, 'KRAS': 55.08}

# 1. Iterate through keys (this is the default behavior)
print("\nIterating through keys:")
for gene in gene_expression.keys():
    level = gene_expression[gene]
    print(f"Gene: {gene}, Level: {level}")

# 2. Iterate through values
print("\nIterating through values:")
for value in gene_expression.values():
    print(f"Level: {value}")

# 3. Iterate through items (keys and values together) - VERY COMMON and USEFUL!
print("\nIterating through items:")
for gene, level in gene_expression.items():
    print(f"Gene: {gene}, Level: {level}")

# Example: Find genes above a threshold
threshold = 100
print(f"\nGenes above threshold {threshold}:")
for gene, level in gene_expression.items():
    if level > threshold:
        print(f"Gene: {gene}, Level: {level}")

############# Mini-Project: Simple Data Summary using a Dictionary #################################

# Let's simulate processing some methylation site data and counting how many sites are hypermethylated (methylation > 0.75).
methylation_sites_data = [
    ("site_A_chr1:100", 0.1),
    ("site_B_chr1:250", 0.8),
    ("site_C_chr2:500", 0.3),
    ("site_D_chr1:300", 0.9),
    ("site_E_chr3:120", 0.2),
    ("site_F_chr2:600", 0.85),
    ("site_G_chr1:150", 0.4)
]

hyper_methylation_threshold = 0.75
hyper_methylated_sites = {}
print(f"\nProcessing methylation sites...")
for site, level in methylation_sites_data:
    if level > hyper_methylation_threshold:
        hyper_methylated_sites[site] = level
        print(f"Hyper-methylated site - {site}, Level: {level}")

print(f"\nProcessing finished!")
print("Dictionary of hypermethylated sites:", hyper_methylated_sites)

# Summarize the findings
total_methylation = len(methylation_sites_data)
total_hyper_methylation = len(hyper_methylated_sites)
print(f"Total methylation sites: {total_methylation}")
print(f"Total hyper-methylation sites: {total_hyper_methylation}")
