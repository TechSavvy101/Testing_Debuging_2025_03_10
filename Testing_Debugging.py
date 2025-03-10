# Get user input
monthly_salary = float(input("Enter your monthly salary: ")) 
salary = float(input("Enter your annual salary: "))
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
daily_hours = float(input("Enter your daily working hours: "))
days_worked = int(input("Enter the number of days worked: "))

# Normal functions
def yearly_salary(monthly_salary):
    return monthly_salary * 12

def is_eligible_for_bonus (salary):
    return salary > 50000

def format_name (first_name, last_name):
    return f"{last_name}, {first_name}"

def total_work_hours(daily_hours, days_worked):
    return daily_hours * days_worked

def apply_tax (salary):
    return salary - (salary * 0.15)

# Display results
print (f"Yearly Salary: {yearly_salary(monthly_salary)}")
print(f"Eligible for Bonus: {'Yes' if is_eligible_for_bonus(salary) else 'No'}")
print(f"Formatted Name: {format_name(first_name, last_name)}")
pl-int(f"Total Work Hours: {total_work_hours(daily_hours, days_worked) }")
print(f"Salary after Tax Deduction: {apply_tax(salary)}")