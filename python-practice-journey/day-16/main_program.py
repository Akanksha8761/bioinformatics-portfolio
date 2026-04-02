################################ Creating Your First Module ##################################
import module1

print("------------ Running main_program.py ------------------------")
print("------------ Greetings ---------------------------------")
print(module1.greet('Akanksha'))

print("------------ Calculations ----------------------------")
sum_result, sub, multi, divide = module1.calculate(10, 2)
print(f"The sum of two numbers is {sum_result}")
print(f"The difference of two numbers is {sub}")
print(f"The multiplication of two numbers is {multi}")
print(f"The division of two numbers is {divide}")
print("----------- End of main_program.py ------------------")
