current_savings = 0
R = 0.04
print("Enter the following information in Pounds, you do not need to include the sign")
total_cost = float(input("Please enter the total cost of the house: "))
annual_salary = float(input("Please enter your annual salary: "))
portion_saved = float(input("Please enter the percentage of your salary that you want to save, as a decimal: "))

portion_deposit = total_cost * 0.2
monthly_salary = annual_salary / 12

count = 0

while current_savings < portion_deposit:
    current_savings += current_savings * R / 12
    current_savings += monthly_salary * portion_saved
    count += 1

print("It will take you {} months to save for the deposit".format(count))
