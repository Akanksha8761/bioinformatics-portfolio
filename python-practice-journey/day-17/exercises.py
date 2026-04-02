############## Writing Text to a File ############
print("-------------Starting to write text to a file-------------")

# 1. Open the file in write mode
file_object = open('first_file.txt', 'w')

# 2. Write some lines to the file
file_object.write("Hello from Python!\n")
file_object.write("This is the first line of text.\n")

gene_name = 'MYB77'
expression = 30.25
file_object.write(f"The second line in the file is gene {gene_name} and its expression is {expression}\n")

# 3. Closing a text file
file_object.close()
print("-------------Finished writing text to a file-------------")

################ Reading Text from a File ################
print("\n-------------Starting to read text from a file-------------")

# Method 1: Read entire file at once
file_object = open("first_file.txt", 'r')
reading = file_object.read()
print(reading)
file_object.close()

print("\n--- Reading line by line ---")
# Method 2: Read line by line
file_object = open("first_file.txt", 'r')
for line in file_object:
    clean_line = line.strip()  # Remove whitespace from start and end
    print(clean_line)
file_object.close()

print("-------------Finished reading text from a file-------------")

################# Appending Text to a File (Adding to the End) #################################
print("\n--- Starting to append to a file ---")

# 1. Opening a file in append mode
file_object = open("first_file.txt", 'a')

# 2. Writing to the file (adds to end)
file_object.write("\nThis is third line which I am appending to the file\n")

# 3. Closing the file
file_object.close()
print("-------------Finished appending text to a file-------------")

################# The Safer Way: The with Statement ###############################
print("\n-------------Starting to use the with statement-------------")

output_file_name = "second_file.txt"
content_to_write = ["This file is being written using with statement.\nIt's a safer and cleaner way!\nPython handles closing of file automatically"]

print("-------------Writing with 'with' statement-------------")
with open(output_file_name, 'w') as f:
    for text in content_to_write:
        f.write(text)
# File automatically closed here!

print("-------------Reading with 'with' statement-------------")
with open(output_file_name, 'r') as f:
    for text in f:
        clean = text.strip()
        print(clean)
# File automatically closed here too!

print("-------------Finished with statement examples-------------")

################# TASK 1: Create gene_list.txt #################
print("\n--- TASK 1: Creating gene_list.txt ---")

# Better to use 'with' statement
with open("gene_list.txt", 'w') as file_object:
    file_object.write('TP53\nBRCA1\nmyc\nEGFR\nKRAS\nakt1\n')

print("gene_list.txt created successfully!")

################# TASK 2: Process genes and create selected_genes.txt #################
print("\n--- TASK 2: Processing genes ---")

# Clear the output file first (if it exists from previous runs)
with open('selected_genes.txt', 'w') as f:
    f.write('')  # Clear file

# Read, process, and write selected genes
with open('gene_list.txt', 'r') as f:
    for line in f:
        # Remove whitespace and convert to uppercase
        clean = line.strip().upper()
        print(f"Processing: {clean}")
        
        # Write genes starting with 'A' or 'T'
        if clean.startswith('A') or clean.startswith('T'):
            with open('selected_genes.txt', 'a') as output:
                output.write(f"{clean}\n")

print("\n--- Reading selected_genes.txt ---")
with open('selected_genes.txt', 'r') as f:
    content = f.read()
    print(content)

print("Task 2 complete!")

################# Additional Concepts #################
print("\n--- Additional File Handling Concepts ---")

# File modes reference
print("\nFile Modes:")
print("'r' - Read (default)")
print("'w' - Write (overwrites)")
print("'a' - Append (adds to end)")
print("'r+' - Read and write")
print("'w+' - Write and read (overwrites)")
print("'a+' - Append and read")

# Reading methods
print("\nReading Methods:")
with open('first_file.txt', 'r') as f:
    # read() - entire file as string
    f.seek(0)  # Go back to start
    content = f.read()
    print(f"read() returns: {len(content)} characters")
    
    # readline() - one line at a time
    f.seek(0)
    first_line = f.readline()
    print(f"readline() returns: {first_line.strip()}")
    
    # readlines() - list of lines
    f.seek(0)
    all_lines = f.readlines()
    print(f"readlines() returns: {len(all_lines)} lines")

print("\n--- File Handling Complete! ---")
