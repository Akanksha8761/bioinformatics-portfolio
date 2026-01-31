#Create a list of integers
my_numbers = [10, 20, 30, 40, 50]
print(f"My number list: {my_numbers}")
print(type(my_numbers))

#Create a list of strings
my_strings = ["apple", "banana", "cherry"]
print(f"My string list: {my_strings}")

#Creating a mixed list
my_mixed_list = [10, "apple", 20, "banana", 30, "cherry", 40]
print(f"My mixed list: {my_mixed_list}")

#Creating an empty list
my_empty_list = []
print(f"My empty list: {my_empty_list}")

###### Indexing #############

my_strings = ["apple", "banana", "cherry"]

# Access the first element
first_item = my_strings[0]
print(f"The first item in list is {first_item}")

# Access the third element
third_item = my_strings[2]
print(f"The third item in list is {third_item}")

# Access the last element using negative indexing
last_item = my_strings[-1]
print(f"The last item in list is {last_item}")

# Access the second to last element
second_last_item = my_strings[-2]
print(f"The second last item in list is {second_last_item}")

# What happens if you try to access an index that doesn't exist?
# not_present = my_strings[3]
# print(f"The item not_present in list is {not_present}")  # IndexError!

# What happens if you try to access a negative index beyond the list start?
# not_present = my_strings[-5]
# print(f"The item not_present in list is {not_present}")  # IndexError!

####### Slicing ############

my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

# Get items from index 1 up to (but not including) index 4
list2 = my_list[1:4]
print(f"{list2}")

# Get items from the beginning up to index 3 (exclusive)
list3 = my_list[:3]
print(f"{list3}")

# Get items from index 2 to the end
list4 = my_list[2:]
print(f"{list4}")

# Get a copy of the entire list
list5 = my_list[:]
print(f"{list5}")

# Get every second item starting from the beginning
list6 = my_list[::2]
print(f"{list6}")

# Get items from index 1 to 6, stepping by 2
list7 = my_list[1:6:2]
print(f"{list7}")

# Reverse the list using slicing
list8 = my_list[::-1]
print(f"{list8}")

############# Mutability #####################

gene_list = ["TP53", "BRCA1", "PTEN", "KRAS"]
print(f"The Gene list is: {gene_list}")

# Change the second element (at index 1)
gene_list[1] = 'MYC12'
print(f"The new list is {gene_list}")

# Change a slice (replaces elements in the slice with new elements)
# Note: The number of replacement elements doesn't have to match the slice size
gene_list[1:3] = ['ABC', 'DEF', 'GHI', 'JKL']
print(f"The new list is {gene_list}")


############## Adding Elements ###########
sample = [1, 2, 3, 4, 5]
print(f"Original List: {sample}")

# Add an item to the end
sample.append(6)
print(f"New List: {sample}")

# Insert an item at a specific index
sample.insert(2, 2.5)
print(f"Second New List: {sample}")

# Insert an item at the end (equivalent to append if index is len(list))
sample.insert(len(sample), 7)
print(f"Third New List: {sample}")

############## Removing Elements ################
experiment_steps = ["Start", "Process", "Analyze", "Visualize", "Clean Up"]
print(f"Original List: {experiment_steps}")

# Remove the item at index 2 using pop()
removed = experiment_steps.pop(2)
print(f"Removed item: {removed}")
print(f"The new list is {experiment_steps}")

# Remove the last item using pop() without an index
removed = experiment_steps.pop()
print(f"Removed item: {removed}")
print(f"The new list is {experiment_steps}")

# Remove a specific value using remove()
experiment_steps.remove("Start")
print(f"The new list is {experiment_steps}")

# What happens if you try to remove a value that isn't in the list?
# experiment_steps.remove("Missing Step")  # ValueError!
# print(f"The new list is {experiment_steps}")

################## Useful List Functions and Methods ####################
data_values = [5, 2, 8, 1, 9, 4]
print(f"Original List: {data_values}")
num = len(data_values)
print(f"The length of the list is {num}")
data_values.sort()
print(f"The sorted list is {data_values}")

# Sort in reverse order
data_values.sort(reverse=True)
print(f"The reverse sorted list is {data_values}")

# Check if an item is in a list
gene_status = ["Mutated", "Normal", "Amplified"]
print(f"Is 'Mutated' in the list? {('Mutated' in gene_status)}")
print(f"Is 'Deleted' in the list? {('Deleted' in gene_status)}")


############### Iterating Through a List #############################
methylation_values = [0.5, 1, 0.22, 0.58, 0.45, 0.78]
print(f"Processing methylation values:")
for i in methylation_values:
    print(f"Methylation value: {i}")

# Example: Check if any value is above a threshold
threshold = 0.6
print(f"Checking if any value is above {threshold}:")
for i in methylation_values:
    if i > threshold:
        print(f"Value {i} is above the threshold")
