#day 2/100 days of code
#tip calculator

print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

extra = total * (tip/100)
new_total = total + extra
each = (new_total / people)
final_each = round(each,2)


print(f"Each person should pay: ${final_each}") 

