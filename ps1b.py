# Name: Nikhil Padarthi
# Assignment 1 - Part B
# Collaborators: None

# problem 2
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi- annual raise, as a decimal: "))

down_payment = total_cost * 0.25
current_savings = 0.0
annual_return = 0.04
months = 0

monthly_return_rate = annual_return / 12

while current_savings < down_payment:
    monthly_salary = annual_salary / 12

    # monthly growth
    intrest = current_savings * monthly_return_rate
    monthly_saving = monthly_salary * portion_saved
    current_savings = current_savings + intrest + monthly_saving

    months = months + 1
    # Salary update every 6 months
    if months % 6 == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
print("Number of months: ",months)