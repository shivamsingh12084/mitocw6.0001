# The aim of this program to calculate the no of months to 
# save money to make downpayment of the house
annual_salary = float(input("Enter your annual salary: "))
potion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_rise = float(input("Enter the semi-annual rise, as a decimal: "))
current_savings = 0
portion_down_payment = total_cost * 0.25
annual_saved = annual_salary * potion_saved
monthly_salary = annual_salary / 12
no_of_months = 0

while (current_savings < portion_down_payment):
    current_savings = current_savings + (current_savings * 0.04) / 12  + (monthly_salary * potion_saved)
    no_of_months += 1
    # Increments the monthly salary after six months 
    if no_of_months % 6 == 0:
        monthly_salary = monthly_salary + (monthly_salary * semi_annual_rise)


print("No of months:", no_of_months)

