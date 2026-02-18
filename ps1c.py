# Name : Nikhil Padarthi
# Assignment 1 - Part C
# Collaborators: None

# problem 3
# Name: Nikhil Padarthi
# Assignment 1 - Part C
# Collaborators: None

starting_salary = float(input("Enter the starting salary: "))

total_cost = 1000000
down_payment = total_cost * 0.25
annual_return = 0.04
semi_annual_raise = 0.07
months_limit = 36
epsilon = 100

low = 0
high = 10000
steps = 0

# First check if saving 100% salary is enough
current_savings = 0.0
salary = starting_salary

for month in range(1, months_limit + 1):
    monthly_salary = salary / 12
    interest = current_savings * (annual_return / 12)
    saving = monthly_salary * 1.0
    current_savings = current_savings + interest + saving
    
    if month % 6 == 0:
        salary = salary + (salary * semi_annual_raise)

if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    
    while True:
        steps = steps + 1
        
        mid = (low + high) // 2
        portion_saved = mid / 10000
        
        current_savings = 0.0
        salary = starting_salary
        
        # simulate 36 months
        for month in range(1, months_limit + 1):
            monthly_salary = salary / 12
            interest = current_savings * (annual_return / 12)
            saving = monthly_salary * portion_saved
            current_savings = current_savings + interest + saving
            
            if month % 6 == 0:
                salary = salary + (salary * semi_annual_raise)
        
        difference = abs(current_savings - down_payment)
        
        if difference <= epsilon:
            break
        
        if current_savings < down_payment:
            low = mid
        else:
            high = mid

    print("Best savings rate:", round(portion_saved, 4))
    print("Steps in bisection search:", steps)
