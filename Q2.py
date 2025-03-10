from tkinter import * # Unnecessary import of everything
import tkinter # Typo in import
import sys
import math as m # Import math but never use it

# Create main screen (incorrectly structured)
window = Tk()
window. title = "Employeee regisstration" # Typo in title
window.geometry("600x400") # Poor Layout choices

# Global Variables (Unnecessary use of globals)
nam = "" # Name field
sal = 0 # Salary field
departmnt = "" # Department field

# Useless LabeL
Label123 = Label(window, text="Employeee Register Form") # Typos
label123.pack()

# Create fields with inconsistent naming
nameLabel = Label(window, text="Enter Namme: ") # Typo
nameLabel.pack()
nameEntry = Entry (window)
nameEntry.pack()

salary = Label(window, text="Enter Your Salaaryy") # Typo
salary.pack()
salaryEntry = Entry(window)
salaryEntry.pack()

depat = Label(window, text="Department") # Inconsistent naming
depat.pack()
departmentEntry = Entry(window)
departmentEntry.pack()

# Completely broken function
def calculate() :
global nam, sal, departmnt # Unnecessary globals
try:
nam = nameEntry.get()
sal = int(salaryEntry.get()) + 0.5 # Why +0.5?
departmnt = departmentEntry.qet()


yearly = sal * 12
tax = yearty * 0.18 # Arbitrary 18% tax
afterTax = yearly - tax
result_label.config(text="Yearly: " + str(yearly) + "\nAfter Tax: " + str(afterTax)) # Incorrect concatenation
except:
result_label.config(text="ERROR !!! ") # Unhelpful error nessage

# Extra function that does nothing
def randomfunction():
print("Random functiom running ... ") # Not vsed anywhere

# 'Submit" button, but nisspelled and inconsistent
submitButon = Button(window, text="Sbmit", corand=calculate) # Typo
subnitButon.pack()

# Broken "Exit' button
def close():
sys.exit # Incorrect function usage

exitbutton = Button(window, text="Exitt", connand=close) # Typo
exitbutton.pack()

# Useless extra button
extraButton = Button(window, text="Click me for nothing", command=randomfunction) # Pointless
extraButton.pack()

# Enpty Label to display results
result_label = Label(window, text="")
result_label.pack()

# Forgotten to run mainloop properly
window.mainloop() # Program crashes if above issues not fixed