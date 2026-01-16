############################################ Task 1: Personal Information (Variables & Types) ####################################################
# Goal: Practice creating variables of different types and printing them.
# Instructions:
# Create a variable my_name and assign your name (string).
# Create a variable my_favorite_number and assign an integer.
# Create a variable my_height_meters and assign your height in meters (float).
# Create a variable is_a_learner and assign True (boolean).
# Use print() to display the value and the type of each variable.

my_name ="Akanksha Sharma"
my_favorite_number = 15
my_height_meters = 1.6002
is_a_learner = True

print(f"My name is {my_name} and its type is {type(my_name)}")
print(f"My favorite number is {my_favorite_number} and its type is {type(my_favorite_number)}")
print(f"My height in meters is {my_height_meters} and its type is {type(my_height_meters)}")
print(f"Am I a learner : {is_a_learner} and its type is {type(is_a_learner)}")


########################################## Task 2: Simple Geometry Calculation (Arithmetic) ######################################################
# Goal: Practice arithmetic operators.
# Instructions:
# Create variables length and width (use floats).
# Calculate the area of a rectangle (length * width).
# Calculate the perimeter of a rectangle (2 * (length + width))
# Print the calculated area and perimeter with descriptive text (e.g., "The area is: ...").

length = 1.600
width = 3.65

area = length * width
print(f"The area of rectangle with length of {length} and width of {width} is {area}")

perimeter = 2*(length + width)
print(f"The perimeter of rectangle with length of {length} and width of {width} is {perimeter}")


########################################## Task 3: Average Score Calculator (Input & Conversion) ################################################
# Goal: Combine input(), type conversion, and arithmetic.
# Instructions:
# Use input() three times to ask the user for three test scores. Store them in variables (remember input() returns strings).
# Convert the input strings to numbers (use float() to allow decimal scores).
# Calculate the average of the three scores.
# Print the average score, clearly labeled.

test_1 = input("Enter your scores in Test 1: ")
test_2 = input("Enter your scores in Test 2: ")
test_3 = input("Enter your scores in Test 3: ")

#Conversion from string to float
test_1 = float(test_1)
test_2 = float(test_2)
test_3 = float(test_3)

#Calculating average
average =(test_1 + test_2 + test_3) /3
print(f"The average of your 3 test scores is : {average}")


######################################### Task 4: Custom Welcome Message (Strings & f-strings) ##################################################
# Goal: Practice string formatting.
# Instructions:
# Ask the user for their name using input().
# Ask the user for their city using input().
# Create a welcome message using an f-string that incorporates their name and city.
# Print the welcome message.
# Example f-string syntax: message = f"Hello {name}! Welcome from {city}."

name = input("Please input your name: ")
city = input("Please input the city you currently live in: ")
message = f"Hello {name}!, Welcome from {city}."
print(message)


######################################## Task 5: Integrated Mini-Challenge (Combining Concepts) ####################################################
# Goal: Put multiple week 1 concepts together.
# Instructions:
# Ask the user for their name.
# Ask the user for their birth_year.
# Calculate their approximate age (assume the current year is 2023 or 2024 - no need for perfect date handling yet).
# Print a summary like: "Hello [Name]! You were born in [Birth Year], so you are approximately [Age] years old."
# Use string multiplication to print a line of asterisks * before and after the summary.

name = input("Plaese enter your name: ")
birth_year = input("Please input your birth year: ")
approx_age = 2024- float(birth_year)
summary = f"Hello {name}! You were born in {birth_year}, so you are approximately {approx_age} years old"
seperator = "*" * 30
print(f"{seperator}\n{summary}\n{seperator}")


###################################### Task 6: DNA Sequence Analysis ##############################################################################
# Write a Python script that:
# Defines a DNA sequence as a string
# Calculates the length of the sequence
# Counts the number of each nucleotide (A, T, G, C)
# Calculates the GC content percentage
# Prints out all these details

sequence = input("Enter your DNA sequence: ")

length = len(sequence)
count_A = sequence.count('A')
count_T = sequence.count('T')
count_C = sequence.count('C')
count_G = sequence.count('G')
gc_percent = ((count_C + count_G)/ length) * 100

print(f"The length of DNA sequnce is {length}")
print(f"The total no. of A of DNA sequnce is {count_A}")
print(f"The total no. of T of DNA sequnce is {count_T}")
print(f"The total no. of C of DNA sequnce is {count_C}")
print(f"The total no. of G of DNA sequnce is {count_G}")
print(f"The GC percentage in DNA sequence is {gc_percent}")


################################### Task 7: Amino Acid Composition #################################################################################
# Goal: Analyze the composition of a short protein sequence.
# Relevance: Understanding the frequency of different amino acids is the first step in characterizing a protein's properties (e.g., hydrophobicity, charge).
# Instructions:
# Define a protein sequence as a string. Protein sequences are represented using single-letter codes for amino acids (e.g., 'M', 'A', 'G', 'S', 'T', 'C', 'P', 'V', 'I', 'L', 'F', 'Y', 'W', 'H', 'K', 'R', 'D', 'E', 'N', 'Q'). Use a simple, short sequence for practice, like "MAGSTSCPYV".
# Calculate the total length of the protein sequence using len().
# Count the occurrences of a few specific amino acids (e.g., 'M', 'S', 'C') using the string's .count() method.
# Print the total length and the counts of the specified amino acids.
# Example Sequence: protein_seq = "MAGSTSCPYV"

protein_seq = input("Enter your protein sequence: ")

length = len(protein_seq)
count_A = protein_seq.count('A')
count_T = protein_seq.count('T')
count_C = protein_seq.count('C')
count_G = protein_seq.count('G')
count_M = protein_seq.count('M')
count_S = protein_seq.count('S')
count_P = protein_seq.count('P')
count_Y = protein_seq.count('Y')
count_V = protein_seq.count('V')

gc_percent = ((count_C + count_G)/ length) * 100

print(f"The length of protein sequnce is {length}")
print(f"The total no. of A of protein sequnce is {count_A}")
print(f"The total no. of T of protein sequnce is {count_T}")
print(f"The total no. of C of protein sequnce is {count_C}")
print(f"The total no. of G of protein sequnce is {count_G}")
print(f"The total no. of M of protein sequnce is {count_M}")
print(f"The total no. of S of protein sequnce is {count_S}")
print(f"The total no. of P of protein sequnce is {count_P}")
print(f"The total no. of Y of protein sequnce is {count_Y}")
print(f"The total no. of V of protein sequnce is {count_V}")


# ############################################ Task 8: Simple Molecular Weight Calculation (DNA) ########################################################
# Goal: Calculate the approximate molecular weight of a short DNA sequence based on its base composition.
# Relevance: Molecular weight is a fundamental property of DNA molecules, important for procedures like gel electrophoresis or calculating molar concentrations.
# Instructions:
# Define a short DNA sequence string (e.g., "AGCTAGCT").
# Define the approximate average molecular weight for each nucleotide base as floats (these are simplified values):
# Adenine (A): 313.2
# Thymine (T): 304.2
# Cytosine (C): 289.2
# Guanine (G): 329.2
# (Note: DNA molecular weight calculation is slightly more complex in reality, considering phosphorylation and the sugar-phosphate backbone, 
# but this simplified version uses only base composition and is good for practicing multiplication/addition)
# Count the occurrences of each base (A, T, C, G) in the DNA sequence using .count().
# Calculate the total molecular weight by summing the product of the count of each base and its respective weight.
# MW = (count_A * weight_A) + (count_T * weight_T) + (count_C * weight_C) + (count_G * weight_G)
# Print the DNA sequence and its calculated approximate molecular weight.
# Example Sequence: dna_sequence = "ATGC"


dna_seq = "ATGC"
mw_A = 313.2
mw_T = 304.2
mw_C = 289.2
mw_G = 329.2

count_A = dna_seq.count('A')
count_T = dna_seq.count('T')
count_C = dna_seq.count('C')
count_G = dna_seq.count('G')

total_molecular_weight = (count_A * mw_A) + (count_T * mw_T) + (count_C * mw_C) + (count_G * mw_G)

print(f"The total molecular weight of DNA sequence {dna_seq} is {total_molecular_weight}")
