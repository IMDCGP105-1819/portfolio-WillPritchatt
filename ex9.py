current_savings = 0
R = 0.04
total_cost = 1000000
semi_annual_raise = 0.07
months = 36

annual_salary = float(input("Please enter your annual salary: "))
portion_saved = float(input("Please enter the percentage of your salary that you want to save, as a decimal: "))

portion_deposit = total_cost * 0.25
monthly_salary = annual_salary / 12

count = 0

while abs():
    current_savings += current_savings * R / 12
    current_savings += monthly_salary * portion_saved
    months -= 1
    count += 1
    if months % 6 == 0:
        monthly_salary += semi_annual_raise * monthly_salary

print("It will take you {} months to save for the deposit".format(count))
