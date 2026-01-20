#Countdown 
countdown = 10
print(f"Starting countdown.....")
while countdown > 0:
    print(f"{countdown}")
    countdown -= 1
print(f"Liftoff!!!")

#Input Validation 
valid_number = None
while valid_number is None:
    user_input = input("Enter a number between 1 and 100: ")
    try:
        num = int(user_input)
        if 0 < num <= 100:
            valid_number = num
            print(f"Thank you for entering a valid number")
        else:
            print(f"Please enter a number between 1 and 100")
    except ValueError:
        print(f"Invalid input. Please enter a number")
print("Processing with valid number: ", valid_number)

# Task 1: Type and run Example 2. Test it with:
# A number within the range (e.g., 50)
# A number outside the range (e.g., 0, 101)
# Text input (e.g., "hello")
# Also accept the word "exit" (case-insensitive) at any time to quit the input process. 
# If the user types "exit", print a message and end the program 
# (you might need break here, or a flag variable).

#Searching a List (Using break in for)
gene_list = ["BRCA1", "TP53", "PTEN", "EGFR", "KRAS", "TP53"]
target_gene = "MYC"
print(f"Searching for {target_gene} in gene list.......")
for i in range(len(gene_list)):
    current = gene_list[i]
    if current == target_gene:
        print(f"Found {target_gene} at index {i}")
        break
if current != target_gene:
    print(f"Target gene {target_gene} not found in the list")
else:
    print(f"Search complete")

# Task 2A: Type and run Example 3. Observe how the loop stops after finding the first "TP53".
# Task 2B: Change target_gene to a gene that isn't in the list (e.g., "MYC"). Run the code again. 
# What is the output? Did the loop finish normally or hit the break? How does this affect the final print statement?

#Processing Data, Skipping Invalid Entries (Using continue in for)
status = ["Healthy", "Cancer", "Invalid", "Cancer", "Healthy", "Invalid", "Cancer"]
count = 0
print(f"Processing patient status.....")
for i in status:
    print(f"Checking status {i}")
    # current = status[i]
    if i == "Invalid":
        print(f"Skipping Invalid entry")
        continue
    if i == "Healthy":
        print(f"Skipping Healthy entry")
        continue   
    print(f"Processing {i}")
    count += 1
print(f"Finished processing with total {count} valid entries")

#Simple ATM Simulation
int_balance = 500
while True:
    print(f"Your current balance is ${int_balance}")
    print(f"Select the option to perform the following actions")
    action = input("Options: (d)eposit, (w)ithdraw, (q)uit: ").lower()
    if action == "q":
        print("Thank you for using the ATM")
        break
    elif action == "w":
        try:
            amount = float(input("Enter the amount to withdraw: $ "))
            if amount <= int_balance:
                int_balance = int_balance - amount 
                print(f"Withdrawal successful. Your new balance is ${int_balance}")
            else:
                print("Insufficient balance")
        except ValueError:
            print(f"Invalid input")
    elif action == "d":
        try:
            amount = float(input("Enter the amount to deposit: $ "))
            int_balance = amount + int_balance
            print(f"Deposit successful. Your new balance is ${int_balance}")
        except ValueError:
            print(f"Invalid input")
    else:
        print("Invalid option. Please choose d, w, or q")
        
print("ATM session ended.")
