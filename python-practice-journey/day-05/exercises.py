#Conditional operators
print(5==5)
print(5==6)
print("apple" != "orange")
print(5!=5)
print(5>6)
print(5<6)
print(5<=6)
print(5>=6)
print(10==10.0)
print("A">"B")
print(True == 1)
print(False == 0)

#if-statements
number = input("Enter a number: ")
number = float(number)
if number > 0:
    print(f"The number is positive")
if number == 0:
    print(f"The number is zero")
else:
    print(f"The number is negative")

#Checking for Equality
password = input("Please enter your password: ")
correct_password = "123456"
if password == correct_password:
    print("Access granted")
else:
    print(f"Incorrect password!!!!! Access denied")

#Combining Multiple Conditions 
exp = input("Enter patient's gene expression level: ")
exp = float(exp)
if exp == 0.0:
    print(f"The patient has low gene expression")
if exp > 0.0:
    print(f"The patient has high gene expression")
if exp < 0.0:
    print(f"The patient has no gene expression")

#else-statement
#Adult or Minor
age = input("Enter your age: ")
age = int(age)
if age >=18:
    print(f"You are an adult")
else:
    print(f"You are a minor")

#Even or Odd Check
number = input("Please enter a number: ")
number = int(number)
if number %2 ==0:
    print(f"Even")
else:
    print(f"Odd")

############# Write a simple program that asks the user for a numeric score (e.g., out of 100). ###############
# Use an if/else statement to check if the score is passing (let's say, 70 or higher).
# Print "Pass" if the score is 70 or more, and "Fail" otherwise.
score= input("Please enter your scores (out of 100): ")
score = float(score)
if score >=70:
    print("Pass")
else:
    print("Fail")
