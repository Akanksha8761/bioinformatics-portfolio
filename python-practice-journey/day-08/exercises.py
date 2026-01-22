################################### TASK 1 ########################################################
# Write an if/elif/else structure that takes a numerical score (you can define a variable score = ...) and prints:
# "Excellent" if the score is 90 or higher.
# "Good" if the score is between 70 and 89 (inclusive).
# "Okay" if the score is between 50 and 69 (inclusive).
# "Needs Improvement" if the score is below 50.

score = input("Enter your score: ")
score = float(score)

if score >= 90:
    print(f"Excellent")
elif score >= 70 and score <= 89:
    print("Good")
elif score >= 50 and score <= 69:
    print("Okay")
elif score < 50:
    print("Needs improvement")

# Note: Can simplify the elif conditions since they're checked in order:
# elif score >= 70:  # We already know score < 90 from previous if
#     print("Good")
# elif score >= 50:  # We already know score < 70 from previous elif
#     print("Okay")
# else:  # Everything else is < 50
#     print("Needs improvement")

################################### TASK 2 ########################################################
# Write a for loop that iterates through the numbers from 1 to 10 (inclusive) and prints only the even numbers. 
# (Hint: The modulo operator % might be useful to check for evenness).

for i in range(1, 11):
    if i % 2 == 0:
        print(f"The number {i} is even")

################################### TASK 3 ########################################################
# Write a while loop that starts with a variable bottles = 5 and prints "There are [number] bottles on the wall!" 
# repeatedly, decreasing the bottles count by 1 each time, until bottles is 0. (You don't need to print the final "0 bottles").

bottles = 5
while bottles > 0:  # Changed from >= to > to avoid printing 0 bottles
    print(f"There are {bottles} bottles on the wall!")
    bottles -= 1
