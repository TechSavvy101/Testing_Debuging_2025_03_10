# Get user input
monthly_salary = float(input("Enter your monthly salary: ")) 
salary = float(input("Enter your annual salary: "))
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
daily_hours = float(input("Enter your daily working hours: "))
days_worked = int(input("Enter the number of days worked: "))

# Normal functions
# Original function
def yearly_salary(monthly_salary):
    return monthly_salary * 12

# Refactored to lambda
yearly_salary = lambda monthly_salary: monthly_salary * 12


# Original function
def is_eligible_for_bonus(salary):
    return salary > 50000

# Refactored to lambda
is_eligible_for_bonus = lambda salary: salary > 50000


# Original function
def format_name(first_name, last_name):
    return f"{last_name}, {first_name}"

# Refactored to lambda
format_name = lambda first_name, last_name: f"{last_name}, {first_name}"


# Original function
def total_work_hours(daily_hours, days_worked):
    return daily_hours * days_worked

# Refactored to lambda
total_work_hours = lambda daily_hours, days_worked: daily_hours * days_worked


# Original function
def apply_tax(salary):
    return salary - (salary * 0.15)

# Refactored to lambda
apply_tax = lambda salary: salary - (salary * 0.15)

# Display results
print (f"Yearly Salary: {yearly_salary(monthly_salary)}")
print(f"Eligible for Bonus: {'Yes' if is_eligible_for_bonus(salary) else 'No'}")
print(f"Formatted Name: {format_name(first_name, last_name)}")
print(f"Total Work Hours: {total_work_hours(daily_hours, days_worked) }")
print(f"Salary after Tax Deduction: {apply_tax(salary)}")
