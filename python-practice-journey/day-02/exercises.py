#Concatenation => Joining strings
greeting ="Hello"
name ="Akanksha"
seperator =", "
exclaimation = "!"

message = greeting + seperator + name + exclaimation
print(message)

age = 30
# print(f"My age is " + age) Creates an error, only string are concatenated with another string
print(f"My age is " + str(age))

repeated_message = message * 2
print(repeated_message)

#String Indexing
name = "Akanksha"
print(f"First Character: {name[0]}") 
print(f"Last Character: {name[-2]}") 

#Slicing 
text ="My name is Akanksha, this is my third python class"
substring_1 = text[3:7] #Consider space during indexing
print(substring_1)
print(f"{text[3:7]}")

#Only giving start no stop
print(f"{text[3:]}")

#Slicing with step
print(f"{text[0::2]}") #Print every other character

#Reversing 
print(f"{text[::-1]}") 

#Copying a string 
print(f"{text[:]}") 

#Length of string
print(f"Length of string {len(text)}") 

#Formatted string literals
name = "Bob"
age = 23
city = "New York"

greetings = f"My name is {name}, I am {age} years old and I live in city {city}"
print(greetings)

#Concatenation using f-string 
a =10
b =40
print(f"The sum of A and B is {a+b}")

#To quote a quote, we need to "escape" it (For Terminal)

'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

#If you don't want characters prefaced by \ to be interpreted as special characters
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

####################################### Task 1: Personalized Greeting #########################################################
# Create two variables: firstName = "YourFirstName" and lastName = "YourLastName".
# Concatenate them to create a fullName with a space in between.
# Create a greeting message using the fullName, like "Hello, [YourFullName]! Welcome to Day 6."
# Print the greeting.
firstName = "Akanksha"
lastName = "Sharma"
fullName = firstName+ " " + lastName
print(f"Hello, {fullName}! Welcome to Day 6")

####################################### Task 2: Decorative Separator #########################################################
# Create a symbol variable (e.g., symbol = "*" or symbol = "#=").
# Create a separator_line by multiplying the symbol by 30.
# Print the separator_line.

symbol = "*"
separator_line = symbol * 30
print(separator_line)

##################################### Task 3: Character Extractor ############################################################
# Define a string: word = "Fundamentals".
# Print the first character of word.
# Print the last character of word using negative indexing.
# Print the character at index 4 of word.

word ="Fundamentals"
print(f"First character is {word[0]}")
print(f"Last character is {word[-1]}")
print(f"Character in 4th index is {word[4]}")

################################### Task 4: Substring Creator ################################################################
# Use the same word = "Fundamentals" string from Task 3.
# Extract and print the substring "Fund".
# Extract and print the substring "mental".
# Extract and print the substring "Fndmntls" (every other character from the start).

word = "Fundamentals"
print(f"{word[0:4]}")
print(f"{word[5:11]}")
print(f"{word[::2]}")

################################ Task 5: Name and Length ####################################################################
# Ask the user for their favorite movie using input("What is your favorite movie? "). Store it in a variable fav_movie.
# Calculate the length of fav_movie and store it in movie_length.
# Using an f-string, print a message: "Your favorite movie, '[MovieName]', has [Length] characters."

fav_movie = input("What is your favorite movie? ")
movie_length = len(fav_movie)
print(f"Your favorite movie, {fav_movie}, has {movie_length} characters")

############################### Task 6: Simple User Profile ###############################################################
# Create variables: username = "CodeMaster23", join_year = 2024.
# Create a profile summary string using f-strings:
# profile_summary = f"User: {username}\nJoined: {join_year}\n--- Profile End ---"
# Print the profile_summary. Note the use of \n for a new line.

username = "CodeMaster23"
join_year = 2024
profile_summary = f"User: {username}\nJoined: {join_year}\n--- Profile End ---"
print(profile_summary)

############################## Task 7: Reversible Fun #####################################################################
# Take a word from user input: user_word = input("Enter a short word: ").
# Create a palindrome_check string by concatenating the user_word, the string " <-> ", and the reversed version of user_word.
# Hint: You can reverse a string using slicing: string[::-1].
# Print the palindrome_check string.
# Example input: madam
# Example output: madam <-> madam
# Example input: hello
# Example output: hello <-> olleh

user_word = input("Enter a short word: ")
palindrome_check = f"{user_word} <-> "
print(palindrome_check)
reverse_string = user_word[::-1]
palindrome_check = user_word + " <-> " + reverse_string # Using concatenation

print(f"{palindrome_check}")
