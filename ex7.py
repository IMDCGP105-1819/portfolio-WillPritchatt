current_savings = 0
R = 0.04
print("Enter the following information in Pounds, you do not need to include the sign")
total_cost = float(input("Please enter the total cost of the house: "))
annual_salary = float(input("Please enter your annual salary: "))
portion_saved = input("Please enter the percentage of your salary that you want to save, as a decimal: ")

portion_deposit = total_cost * 0.2
print(portion_deposit)
monthly_salary = annual_salary / 12
print(monthly_salary)

count = 0

#while current_savings < portion_deposit
for i in range(10):
    current_savings = current_savings * R / 12
    print("Return Investment: ", current_savings)
    current_savings = current_savings + monthly_salary
    count += 1
    print(current_savings, count)


