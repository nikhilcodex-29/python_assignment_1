# Name:Nikhil Padarthi
# Assignment 1 - Part A
# Collaborators: None

# problem: 1
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))

down_payment = total_cost * 0.25
current_savings = 0.0
annual_return = 0.04
months = 0

monthly_income = annual_salary /12
monthly_rate_of_return = annual_return / 12
while current_savings <down_payment:
    # Add monthly investment return
    interest = current_savings * monthly_rate_of_return

    # Add monthly savings from salary
    monthly_saving = monthly_income * portion_saved

    # Update total savings
    current_savings = current_savings + interest + monthly_saving

    months = months + 1

    print("Number of months:", months)