## DATA TYPES ##
my_age =35 #integer
pi_value =3.144335 #float
user_name ="Akanksha" #String
is_learning= True #Boolean
database_result = None #NoneType

## PRINT FUNCTION ##
print(my_age)
print(pi_value)
print(user_name)
print(is_learning)
print(database_result)

# Printing with labels (more descriptive)
print("My age is: ", my_age)
print("The value of pi is: ", pi_value)
print("Your user name is: ", user_name)
print("Am I learning new things: ", is_learning)
print("What is the result from database: ", database_result)

# Using f-strings (Formatted String Literals - Recommended for modern Python)
print(f"My name is {user_name}, and my age is {my_age}")
print(f"The value of pi is {pi_value:.3f}")

## TYPE FUNCTION ##
print(type(my_age))
print(type(pi_value))
print(type(user_name))
print(type(is_learning))
print(type(database_result))

## Dynamic Typing in Action ##
print(my_age, type(my_age))
print(user_name, type(user_name))
print(is_learning, type(is_learning))

## Type Conversion (Casting) ##
my_age= 26
my_age = int(my_age)
print(my_age, type(my_age))

#Converting int it to float
my_age = float(my_age)
print(my_age, type(my_age))

#Converting float it to string
my_age = str(my_age)
print(my_age, type(my_age))

#Converting int it to boolean  
#(Most things are True, except 0, 0.0, "", None, empty collections)

#my_age= 1
#my_age= 0
my_age = ""
my_age = bool(my_age)
print(my_age, type(my_age))


######################## Task 1: Personal Details #########################################
# Create variables to store your first_name, last_name, current_year, and birth_year.
# Calculate your approximate age using current_year and birth_year.
# Print your full name and age using an f-string.
# Example output: "My name is John Doe and I am 30 years old."

first_name = "Akanksha" 
last_name = "Sharma"
current_year = 2025
birth_year = 1998
approx_age = current_year - birth_year
print(f"My approximate age is {approx_age}")
print(f"My name is {first_name} {last_name}, and I am {approx_age} years old")


######################### Task 2: Product Information #######################################
# Create variables for a product_name (string), product_price (float), and quantity_in_stock (integer).
# Print each of these variables with a descriptive label.
# Use type() to print the data type of each variable.

product_name = "Dabur"
product_price = 30.69
quantity_in_stock = 1000
print(f"Product Name: {product_name}")
print(type(product_name))
print(f"product price: ${product_price}")
print(type(product_price))
print(f"Quantity in stock: {quantity_in_stock}")
print(type(quantity_in_stock))

########################## Task 3: Temperature Conversion ################################
# Create a variable temp_celsius and assign it a temperature in Celsius (e.g., 25.0).
# Calculate the temperature in Fahrenheit using the formula: F = (C * 9/5) + 32. Store it in a variable temp_fahrenheit.
# Print both temperatures, clearly labeling them.
# Example output: "25.0°C is 77.0°F."

temp_celsius = 24.5
temp_farenheit = ((temp_celsius * 9/5) + 32)
print(f"The temperature in Celcius is {temp_celsius}C and temperatur in farenheit is {temp_farenheit}F")

######################## Task 4: String Manipulation and Info ##############################
# Create a variable favorite_book and assign it the title of your favorite book (as a string).
# Create a variable book_published_year and assign it the year the book was published (as an integer).
# Create a variable is_fiction and assign it True if the book is fiction, False otherwise.
# Print a sentence combining this information. Example: "My favorite book, 'The Great Gatsby' (published in 1925), is a work of fiction: True."
# Print the type() of each of these three variables.

favorite_book = "Atomic habbit"
published_year = 2015
is_fiction = False
print(f"My favorite book, '{favorite_book}' (published in {published_year}), is a work of fiction: {is_fiction}")

####################### Task 5: User Input and Greeting ###################################
# Use the input() function to ask the user for their name and store it in a variable (e.g., visitor_name). Hint: input() always returns a string.
# Use input() to ask the user for their favorite number and store it in a variable.
# Convert the favorite number (which is a string from input()) to an integer.
# Print a personalized greeting: "Hello, [visitor_name]! Your favorite number is [number]."
# Print the type of the visitor_name variable and the type of the converted favorite number variable.

visitor_name = input("Please enter your name :")
print(type(visitor_name))
favorite_number = input("Please enter your favorite number")
print(type(favorite_number))
favourite_number2 = int(favorite_number)
print(type(favourite_number2))
print(f"Hello, {visitor_name}! Your favorite number is {favourite_number2}.")

####################### Task 6: Boolean Flags ################################################
# Create a variable is_logged_in and set it to True.
# Create a variable has_admin_privileges and set it to False.
# Create a variable is_weekend and set it to False.
# Print the values of these boolean variables.
# Imagine a scenario: Print "Admin access granted" ONLY IF is_logged_in AND has_admin_privileges are both True. 
# (You'll learn if statements later, for now, just think about what the combined boolean expression would be: is_logged_in and has_admin_privileges). 
# Print the result of this combined boolean expression.

is_logged_in = True
has_admin_privileges = True
is_weekend = False
print(is_logged_in)
print(has_admin_privileges)
print(is_weekend)
if (is_logged_in and has_admin_privileges):
    print(f"Admin access granted")

###################### Task 7: Reassignment and Type Change #####################################
# Create a variable item_code and assign it an integer value (e.g., 101). Print its value and type.
# Now, reassign item_code to a string value representing a code (e.g., "A101-X"). Print its new value and type.
# This demonstrates Python's dynamic typing.

item_code = 1023
print(f"the code of this item is {item_code} and its type is:", (type(item_code)))

item_code ="A101-X"
print(f"the code of this item is {item_code} and its type is:", (type(item_code)))


###################### Task 8: Simple Quotation ##################################################
# Create a variable quote and assign it a short inspiring quote as a string.
# Create a variable author and assign it the author of the quote.
# Print the quote and author in a nice format, e.g.:
# "The only way to do great work is to love what you do." - Steve Jobs
# Hint: You might need to combine strings or use f-strings.

quote = "Old is Gold"
author = "Akanksha Sharma"
print(f"'{quote}' - {author}")

#the last printed expression is assigned to the variable _ (only works in terminal)
price = 100.50
tax = 12.5 / 100
price * tax
print(_)
