from tkinter import * # Unnecessary import of everything
import tkinter as tk # Typo in import
import sys

# Create main screen (incorrectly structured)
window = tk.Tk()
window.title = ("Employee registration") # Typo in title**
window.geometry("600x400") # Poor layout choices**

#Empty label to display results
result_label = Label (window, text="Results")
result_label.pack()


# Global Variables (Unnecessary use of globals)
name = "name" # Name **
sal = 0 # Salary field
department = "department" # Department field **

# Useless label
label123 = Label(window, text="Employee Register Form") # Typos**
label123.pack()

# Create fields with inconsistent naming
name_label = Label(window, text="Enter Namme: ") # Typo**
name_label.pack()
name_entry = Entry(window)
name_entry.pack()

salary = Label(window, text="Enter Your Salary") # Typo**
salary . pack()
salaryEntry = Entry(window)
salaryEntry.pack()

depart = Label(window, text="Department") # Inconsistent naming***
depart.pack()
departmentEntry = Entry(window)
departmentEntry.pack()

# Completely broken function
def calculate():
    name, sal, department # Unnecessary globals**
try:
    name = name_entry.get()
    sal = int(salaryEntry.get()) * 0.5 # Why +0.5?**
    department = departmentEntry.qet()
    yearly = sal * 12
    tax = yearly* 0.18 # Arbitrary 18% tax
    afterTax = yearly - tax
    result_label.config(text="Yearly: " + str(yearly) + "\nAfter Tax: " + str(afterTax))# Incorrect concatenation**
except:
    result_label.config(text="Salary Sould be a valid number!!!") # Unhelpful error message**

# "Submit" button, but misspelled and inconsistent
submitButton= Button(window, text="Submit", command=calculate) # Typo submitButon.pack()**
submitButton.pack()

#Broken "Exit" button
def close():
    sys.exit # Incorrect function usage 
exitButton= Button(window, text="Exit", command=close)# Typo exitbutton.pack()**
exitButton.pack()

#Forgotten to run mainloop properly
window.mainloop() # Program crashes if above issues not fixed