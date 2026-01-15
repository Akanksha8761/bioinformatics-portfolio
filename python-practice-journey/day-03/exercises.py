a = 10
b =48

#Addition
c =a+b
print(f"The value addition of A and B is {c}")

#Subtraction
d =a-b
print(f"The value subtraction of A and B is {d}")

#Multiplication
e = a*b
print(f"The value multiplication of A and B is {e}")

#Division
f = a/b
print(f"The value division of A and B is {f}")

#Integer Division

a=10
b=3
c=-7
d=2
g =a//b
print(f"The floor division of A and B is {g}")

#Modulus
a=10
b=3
h =a%b
print(f"The modulus of A and B is {h}")

#Exponentiation
a= 10
b=2
i =a ** b
print(f"The exponentiation of A and B is {i}")

#For square root
k=9
j = k ** 0.5
print(f"The square root of {k} is {j}")

#BODMAS
result1 =10+3*2
print(f"{result1}")

result2 =(10+3)*2
print(f"{result2}")

result3 = 100/10*2
print(f"{result3}")

result4 = 100/(10*2)
print(f"{result4}")

result5 = 2**3**2
print(f"{result5}")


# Simple Sum Calculator

print(f"--------------------SIMPLE SUM CALCULATOR -------------------")
user_input= input("Enter your first number: ")
print(f"You entered {user_input} and its type is {type(user_input)}")

user_input2= input("Enter your second number: ")
print(f"You entered {user_input2} and its type is {type(user_input2)}")

#Converting into string 
num1 = float(user_input)
num2 = float(user_input2)

print(f"After conversion the first number is {num1} and its type is {type(num1)} and second number is {num2} and its type is {type(num2)}")

#Addition
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")

################################ Task 1: All-in-One Operator Practice ################################################################
# Create two variables, x = 15 and y = 4.
# Calculate and print the results of x + y, x - y, x * y, x / y, x // y, x % y, and x ** y.
# Label each output clearly using f-strings (e.g., f"{x} + {y} = {x+y}").

x =15
y=4
#Addition
a= x+y
print(f"The addition of {x} + {y} gives {a}")
#Subtraction
b= x-y
print(f"The subtraction of {x} - {y} gives {b}")
#Multiplication
c= x*y
print(f"The multiplication of {x} * {y} gives {c}")
#Division
d= x/y
print(f"The division of {x} / {y} gives {d}")
#Floor Division
e= x//y
print(f"The floor division of {x} // {y} gives {e}")
#Modulus
f= x%y
print(f"The modulus of {x} % {y} gives {f}")
#Exponentiation
g= x**y
print(f"The exponentiation of {x} ** {y} gives {g}")

############################## Task 2: Division Differences & Types ################################################################
# Define num_a = 20 and num_b = 5.
# Calculate div_float = num_a / num_b. Print div_float and its type.
# Calculate div_int = num_a // num_b. Print div_int and its type.
# Now, change num_b = 6.
# Recalculate div_float = num_a / num_b. Print div_float and its type.
# Recalculate div_int = num_a // num_b. Print div_int and its type.
# Observe and make a mental note of the differences in results and types.

num_a= 20
num_b =5
#Division
div_float = num_a / num_b
print(f"The value of Division is {div_float} and its type is {type(div_float)}")
#Floor Division
div_int = num_a // num_b
print(f"The value of Floor Division is {div_int} and its type is {type(div_int)}")
num_b= 6
#Division
div_float = num_a / num_b
print(f"The value of Division is {div_float} and its type is {type(div_float)}")
#Floor Division
div_int = num_a // num_b
print(f"The value of Floor Division is {div_int} and its type is {type(div_int)}")

########################### Task 3: Modulus for Even/Odd Checker (User Input) #########################################################
# Ask the user to input a whole number using input("Enter a whole number: ").
# Convert the input to an integer.
# Calculate the remainder when the number is divided by 2. Store it in a variable called remainder.
# Print a message using an f-string: f"The number {user_number} % 2 is {remainder}."
# Then, print a separate line stating: "This number is even." if the remainder is 0, or "This number is odd." if the remainder is not 0. 
# (You can just use your knowledge for now, we'll make this conditional with if statements later).

num_1= input("Enter a whole number: ")
num_1= int(num_1)
if (num_1% 2 == 1):
    num2= num_1%2
    print(f"The number {num_1} % 2 is {num2}.")
else:
    print(f"This number is even.")

########################## Task 4: Power Play (User Input) ############################################################################
# Ask the user to enter a "base number".
# Ask the user to enter an "exponent".
# Convert both inputs to float to allow for decimal bases/exponents.
# Calculate base_number raised to the power of exponent.
# Print the result in a user-friendly way, e.g., "2.5 to the power of 2.0 is 6.25".

base_number = input("Enter base number: ")
exponent = input("Enter exponent: ")
base_number = float(base_number)
exponent =float(exponent)
result = base_number ** exponent
print(f"{base_number} to the power of {exponent} is {result}")

######################## Task 5: Mini Area & Perimeter Calculator (Rectangle - User Input)  ##########################################
# Ask the user to enter the length of a rectangle.
# Ask the user to enter the width of a rectangle.
# Convert both inputs to floats.
# Calculate the area of the rectangle (Area = length * width).
# Calculate the perimeter of the rectangle (Perimeter = 2 * (length + width)).
# Print the calculated area and perimeter, clearly labeled.

length = input("Enter the value of length: ")
width = input("Enter the value of width: ")
length = float(length)
width= float(width)

area = length*width

perimeter = 2*(length+width)

print(f"The area of rectangle is {area} and perimeter is {perimeter}")

######################## Task 6: Order of Operations Exploration #######################################################################
# Predict the output of the following expressions before running the code. Then, write Python code to calculate each and print the result.
# result_a = 100 - 5 * 3 / (2 + 3) ** 2 + 10
# result_b = (100 - 5) * 3 / 2 + 3 ** 2 + 10
# result_c = 12 / 4 * 2 + 5 - 1
# For each, print the expression as a string and then its result, e.g., print(f"100 - 5 * 3 / (2 + 3) ** 2 + 10 = {result_a}")

result_a = 100 - 5 * 3 / (2 + 3) ** 2 + 10
print(f"100 - 5 * 3 / (2 + 3) ** 2 + 10 = {result_a}")

result_b = (100 - 5) * 3 / 2 + 3 ** 2 + 10
print(f"(100 - 5) * 3 / 2 + 3 ** 2 + 10 = {result_b}")

result_c = 12 / 4 * 2 + 5 - 1
print(f"12 / 4 * 2 + 5 - 1 = {result_c}")


#################### Task 7: Simple Interest Calculator (User Input) ############################################################
# The formula for simple interest is: Interest = (Principal * Rate * Time) / 100
# Ask the user to input:
# Principal amount (P) - the initial sum of money
# Annual rate of interest (R) - e.g., enter 5 for 5%
# Time period in years (T)
# Convert all inputs to float.
# Calculate the simple interest.
# Print the calculated interest.
# Bonus: Also calculate and print the total amount (Principal + Interest).

principle = input("Enter principle amount (P): ")
rate = input("Enter annual rate of interest (R): ")
time = input("Enter the time period in years (T): ")
#Converting into float 
principle = float(principle)
rate = float(rate)
time = float(time)

#Calculating simple interest
interest = (principle * rate * time) / 100
print(f"Simple interest {interest}")

#Calculating total amount
total = principle + interest
print(f"The total amount is {total}") 

###################### Task 8: Tip Calculator ####################################################################################
# Ask the user for the total bill amount (e.g., 55.75).
# Ask the user for the tip percentage they'd like to give (e.g., 15 for 15%).
# Convert inputs to floats.
# Calculate the tip amount: tip_amount = bill_amount * (tip_percentage / 100)
# Calculate the total amount to pay: total_pay = bill_amount + tip_amount
# Print the bill amount, tip percentage, tip amount, and total amount to pay, clearly labeled.

total_bill = input("Enter the total bill amount: ")
tip_percent = input("Enter the tip percentage you'd like to give: ")

#Converting to float
total_bill = float(total_bill)
tip_percent = float(tip_percent)
#Calculating tip amount
tip_amount = total_bill *(tip_percent/100)
#Calculating total amount to pay
total_pay = total_bill + tip_amount

print(f"The total bill amount is ${total_bill}, tip percentage {tip_percent} and total amount to pay is ${total_pay}")
