print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are there? "))
bill_with_tip = bill + (bill * tip_percentage / 100)

bill_per_person = bill_with_tip / people
print(f'The total amount is {bill_with_tip}, so each person should pay ${bill_per_person:.2f}')