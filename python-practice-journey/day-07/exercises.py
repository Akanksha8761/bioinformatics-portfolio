#print hello 5 times
for i in range(5):
    print(f"Hello")

#Counting from 2 to 10
for i in range(2, 11):
    print(i)

#Print even no.
for i in range(0, 11, 2):
    print(i)

#Count backwards from 10 to 1
for i in range(11, 0, -1):
    print(i)

#Print each character in a word.
word = "Methylation"
for i in word:
    print(i)

#Combining for and if
# Loop through numbers 1-10 and print if each is even or odd 
# (revisiting your excellent previous example, but now formally inside a loop).

for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

#Print numbers from 0 up to 4 using while
i = 0
while i <= 5: # if i >= 5 infinite loop
    print(i)
    i += 1 #if comment out infinite loop
print("Loop finished.")

#Keep asking the user for input until they type "quit".
print(f"Type 'quit' to exit")
user = ''
while user != 'quit':
    print(f"You typed: {user}")
    user = input("Please type a no: ")
print("Done")

#Loop through numbers 1-10, but stop as soon as you find the number 5.
for i in range(1, 11):
    print(f"The number is {i}")
    if i == 5:
        print(f"Found the number 5, stopping now.")
        break
print(f"Loop ends!")

#Loop through numbers 1-10, but only print the even numbers (skip the odd ones).
for i in range(1, 11):
    if i % 2 == 0:
        continue
    else:
        print(f"The number {i} is odd")
print(f"Loop ends!")

#################### TASK 1 #######################################################
# Write a for loop using range() to print the squares of numbers from 1 to 7 
# (i.e., 1, 4, 9, 16, 25, 36, 49)

for i in range(1, 8):
    print(f"The square of {i} is {i * i}")


#################### TASK 2 #######################################################
# Write a while loop that starts with a balance = 100 and subtracts 20 in each iteration, 
# printing the remaining balance, until the balance is 0 or less. (Hint: while balance > 0: ... balance -= 20).

balance = 100
while balance > 0:
    print(f"Balance is {balance}")
    balance = balance - 20


#################### TASK 3 #######################################################
# Loop through numbers from 50 down to 20 (inclusive). Print only the numbers that are divisible by 5.
for i in range(50, 19, -1):
    if i % 5 == 0:
        print(f"The no. {i} is divisible by 5")
    else:
        print(f"The no. {i} is not divisible by 5")


#################### TASK 4 #######################################################
# Write a while True: loop that asks the user for a number. If the number is greater than 100, print "Too high!" 
# and break the loop. Otherwise, print "Nice number!" and continue.

print("\nTask 4: Enter a number (or type 'quit' to exit the program).")
while True:
    user_input_str = input("Enter a number: ")
    if user_input_str.lower() == 'quit':
        print("Exiting program.")
        break 
    user_number = int(user_input_str) 

    if user_number > 100:
        print("Too high!")
        break 
    else: 
        print("Nice number!")

print("Program finished.") 

#Loop through numbers from 1 to 20. If the number is divisible by 3, use continue to skip printing it. Print all other numbers.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(f"The number {i} is not divisible by 3")


#################### TASK 5 #######################################################
# Multiples Finder (using for and if):
# Write a for loop that iterates through numbers from 1 to 50 (inclusive).
# Inside the loop, use an if statement to check if the current number is a multiple of 7. (Hint: Use the modulus operator %).
# If it is a multiple of 7, print the number with a message like: "[Number] is a multiple of 7".

for i in range(1, 51):
    if i % 7 == 0:
        print(f"The number {i} is a multiple of 7")


#################### TASK 6 #######################################################
# Set a variable correct_password = "dna123".
# Use a for loop to give the user 3 attempts to enter the password. (Hint: range(3) or range(1, 4)).
# Inside the loop, prompt the user to enter the password using input().
# Use an if statement to check if the entered password matches correct_password.
# If it matches, print "Login Successful!" and use break to exit the loop immediately.
# If the loop finishes without the password being correct (i.e., break was never hit after 3 attempts), print "Too many failed attempts. Account locked."

correct_password = "dna123"
print(f"Type your password")
for i in range(1, 4):
    user = input("Enter your password: ")
    if user == correct_password:
        print("Login Successful!")
        break
    else:
        print(f"Incorrect password!!! Try again")
    
    if i == 3:
        print(f"Too many failed attempts. Account locked.")


#################### TASK 7 #######################################################
# Skipping Multiples (using for and continue):
# Write a for loop that iterates through numbers from 1 to 30 (inclusive).
# Inside the loop, use an if statement to check if the number is divisible by BOTH 2 AND 3. (Hint: Use the and logical operator).
# If the number is divisible by both 2 and 3 (meaning it's a multiple of 6), use continue to skip the rest of the loop's code for that number.
# If continue is not executed, print the number.
# Result: You should see all numbers from 1 to 30 except 6, 12, 18, 24, 30.

for i in range(1, 31):
    if i % 3 == 0 and i % 2 == 0:
        continue 
    print(f"The number {i}")


#################### TASK 8 #######################################################
# Simulating Genome Scan (Simple Bio-themed for loop):
# Human cells have 23 pairs of chromosomes, so let's think of them as Chromosome 1 through Chromosome 23 (ignoring X/Y for simplicity).
# Write a for loop that iterates through the numbers 1 to 23.
# Inside the loop, print a message indicating you are processing that chromosome, for example: print(f"Processing DNA on Chromosome {chromosome_number}...").
# After the loop finishes, print "Genome scan complete."

for i in range(1, 24):
    print(f"Processing DNA on Chromosome {i}...")
print("Genome scan complete.")
