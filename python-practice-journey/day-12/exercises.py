##################### Creating Sets #############################################
new_set = {1, 2, 3, 4, 5, 5, 7, 8, 9, 10}
print(f"My set is: {new_set} and its type is {type(new_set)}")

# Creating a set from a list 
new_set2 = ["GeneA", "GeneB", "GeneC", "GeneA"]
print(f"My list is: {new_set2} and its type is {type(new_set2)}")
unique_set2 = set(new_set2) 
print(f"My set is: {unique_set2} and its type is {type(unique_set2)}")

# Creating a set from a tuple
new_set3 = ("GeneA", "GeneB", "GeneC", "GeneA")
print(f"My tuple is: {new_set3} and its type is {type(new_set3)}")
unique_set3 = set(new_set3)
print(f"My set is: {unique_set3} and its type is {type(unique_set3)}")

# Creating an empty set
empty_set = set()
print(f"My empty set is: {empty_set} and its type is {type(empty_set)}")

# Reminder: {} creates an empty dictionary, NOT a set!
empty_dict = {}
print(f"My empty dict is: {empty_dict} and its type is {type(empty_dict)}")

############# Set Properties (Uniqueness, Unordered, No Indexing, Immutable Elements) ################
new_set = {"red", "green", "blue"}
print(f"My set is: {new_set} and its type is {type(new_set)}")

# No Indexing or Slicing!
# print(new_set[0])      # TypeError: 'set' object is not subscriptable
# print(new_set[3:5])    # TypeError: 'set' object is not subscriptable

# Elements Must Be Immutable (Hashable)
valid_set_elements = {1, "string", (1, 2)}
print(f"My set is: {valid_set_elements} and its type is {type(valid_set_elements)}")

# You CANNOT put mutable objects like lists or dictionaries into a set
# valid_set_elements2 = {1, {"key": "value"}}   # TypeError: unhashable type: 'dict'
# valid_set_elements3 = {1, ["key", "value"]}   # TypeError: unhashable type: 'list'

################################### Modifying Sets (Adding/Removing) ################################
samples = {"Sample1", "Sample2", "Sample3"}
print(f"Original dataset is: {samples} and its type is {type(samples)}")

# 1. Adding a single element using .add()
samples.add("Sample4")
print(f"New dataset after addition: {samples}")

# Adding an element that is already in the set has no effect
samples.add("Sample2")
print(f"After adding duplicate: {samples}")  # No change!

# 2. Adding multiple elements using .update()
# samples.update("Sample5")  # This takes each character as individual element!
new_sample = ["Sample5", "Sample6"] 
samples.update(new_sample)
print(f"New dataset after updating: {samples}")

# 3. Removing an element using .remove()
samples.remove("Sample2")
print(f"New dataset after removing: {samples}")

# KeyError if the item is not found
# samples.remove("Sample9")  # KeyError: 'Sample9'

# 4. Removing an element using .discard() - safer if item might not be there
samples.discard("Sample9")  # No error even if not found!
print(f"New dataset after discarding: {samples}")

# 5. Removing an arbitrary element using .pop()
# Note: Sets are unordered, so pop() removes an arbitrary element
popped = samples.pop()
print(f"Popped element: {popped}")
print(f"New dataset after popping: {samples}")

# 6. Clearing all elements using .clear()
samples_copy = {"S1", "S2", "S3"}
samples_copy.clear()
print(f"New dataset after clearing: {samples_copy}")

############################ Checking Membership (using 'in') ############################
samples = {"Sample1", "Sample2", "Sample3"}
print(f"Sample1 in samples: {'Sample1' in samples}")
print(f"Sample5 in samples: {'Sample5' in samples}")

############################ Set Operations (Union, Intersection, Difference, etc.) ######

de_genes_subtypeA = {"GeneA", "GeneB", "GeneC", "GeneD", "GeneE"}
de_genes_subtypeB = {"GeneC", "GeneD", "GeneF", "GeneG", "GeneH"}
de_genes_all_samples = {"GeneA", "GeneC", "GeneI", "GeneJ"}

# 1. Union: All unique elements from both sets (A OR B)
union_genes = de_genes_subtypeA | de_genes_subtypeB
print(f"Union of subtype A and subtype B genes: {union_genes}")

# Union with multiple sets
union_genes_all = de_genes_subtypeA | de_genes_subtypeB | de_genes_all_samples
print(f"Union of all three sets: {union_genes_all}")

# 2. Intersection: Elements common to both sets (A AND B)
intersect_genes = de_genes_subtypeA & de_genes_subtypeB
print(f"Intersection of subtype A and subtype B genes: {intersect_genes}")

# Intersection with multiple sets
intersect_genes_all = de_genes_subtypeA & de_genes_subtypeB & de_genes_all_samples
print(f"Intersection of all three sets: {intersect_genes_all}")

# 3. Difference: Elements in the first set but NOT in the second (A MINUS B)
diff_genes = de_genes_subtypeA - de_genes_subtypeB
print(f"Difference (A - B): {diff_genes}")

# 4. Symmetric Difference: Elements in either set, but NOT in both (A XOR B)
symdiff_genes = de_genes_subtypeA ^ de_genes_subtypeB
print(f"Symmetric Difference (A XOR B): {symdiff_genes}")

# 5. Subset and Superset Checks

# Subset: Is every element in set A also in set B? (A <= B)
small_set = {1, 2}
large_set = {1, 2, 3, 4, 5}
print(f"Is small_set subset of large_set? {small_set <= large_set}")  # True
print(f"Is large_set subset of small_set? {large_set <= small_set}")  # False
print(f"Is large_set proper subset of small_set? {large_set < small_set}")  # False
print(f"Is small_set proper subset of large_set? {small_set < large_set}")  # True

# Superset: Does set A contain every element of set B? (A >= B)
print(f"Is small_set superset of large_set? {small_set >= large_set}")  # False
print(f"Is large_set superset of small_set? {large_set >= small_set}")  # True
print(f"Is large_set proper superset of small_set? {large_set > small_set}")  # True
print(f"Is small_set proper superset of large_set? {small_set > large_set}")  # False

# Use .issubset() and .issuperset() methods as alternatives
print(f"Is small_set subset of large_set? {small_set.issubset(large_set)}")
print(f"Is large_set subset of small_set? {large_set.issubset(small_set)}")

print(f"Is small_set superset of large_set? {small_set.issuperset(large_set)}")
print(f"Is large_set superset of small_set? {large_set.issuperset(small_set)}")

################ Mini-Project: Finding Unique and Shared Elements ########################
# You have a list of genes found to be hypermethylated in Sample A, and another list for Sample B.
# Find:
# - The total list of all unique hypermethylated genes across both samples
# - The genes that are hypermethylated in both samples
# - The genes hypermethylated only in Sample A
# - The genes hypermethylated only in Sample B
# - Genes hypermethylated in A or B, but not both (Symmetric Difference)

sample_A = ["GeneA", "GeneB", "GeneC", "GeneD"]
sample_A = set(sample_A)
sample_B = ["GeneD", "GeneE", "GeneF"]
sample_B = set(sample_B)

unique_samples = sample_A | sample_B
print(f"\nMini-Project Results:")
print(f"Total unique hypermethylated genes across both samples: {unique_samples}")

hyper_met_both = sample_A & sample_B
print(f"Genes hypermethylated in both samples: {hyper_met_both}")

hyper_only_A = sample_A - sample_B
print(f"Genes hypermethylated only in Sample A: {hyper_only_A}")

hyper_only_B = sample_B - sample_A
print(f"Genes hypermethylated only in Sample B: {hyper_only_B}")

symdiff = sample_A ^ sample_B
print(f"Genes hypermethylated in A or B but not both: {symdiff}")

# Verification: symmetric difference should equal union of exclusive genes
print(f"\nVerification: {symdiff == (hyper_only_A | hyper_only_B)}")
