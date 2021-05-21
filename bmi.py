
# BMI Calculator
from tkinter import *
import tkinter as tk

from future.moves.tkinter import messagebox

window = tk.Tk()
window.geometry("600x600")
window.title("BMI Calculator")
window.config(bg="lightblue")


# Labels
label_weight = tk.Label(window, text="Weight:", bg="royalblue")
label_weight.place(x=60, y=20, height=50, width=120)
label_Kg = tk.Label(window, text="Kg", bg="royalblue")
label_Kg.place(x=380, y=30)
label_height = tk.Label(window, text="Height:", bg="royalblue")
label_height.place(x=60, y=80, height=50, width=120)
label_cm = tk.Label(window, text="cm", bg="royalblue")
label_cm.place(x=380, y=90)
label_gender = tk.Label(window, text="Gender:", bg="royalblue")
label_gender.place(x=60, y=140, height=50, width=120)
label_age = tk.Label(window, text="Age:", bg="royalblue")
label_age.place(x=60, y=200, height=50, width=120)
label_bmi = tk.Label(window, text="BMI:", bg="royalblue")
label_bmi.place(x=60, y=400, height=50, width=120)
label_ideal_bmi = tk.Label(window, text="Ideal BMI:", bg="royalblue")
label_ideal_bmi.place(x=350, y=400, height=50, width=120)

# Entries
weight = tk.Entry(window)
weight.place(x=250, y=20, height=50, width=120)
height = tk.Entry(window)
height.place(x=250, y=80, height=50, width=120)
age = tk.Entry(window, state="readonly")
age.place(x=250, y=200, height=50, width=120)
bmi = tk.Entry(window, state="readonly")
bmi.place(x=200, y=400, height=50, width=100)
ideal_bmi = tk.Entry(window, state="readonly")
ideal_bmi.place(x=490, y=400, height=50, width=100)

# Gender Entry
options = ['Select...', 'Male', "Female"]
variable = StringVar(window)
variable.set(options[0])


# my active menu function
def activate(value):
    variable.set(value)
    if value != "Select...":
        age.config(state='normal')
    else:
        age.config(state='readonly')


# my clear function
def clear():
    weight.delete(0, END)
    height.delete(0, END)
    age.config(state="normal")
    bmi.config(state="normal")
    ideal_bmi.config(state="normal")
    age.delete(0, END)
    bmi.delete(0, END)
    ideal_bmi.delete(0, END)
    age.config(state="readonly")
    bmi.config(state="readonly")
    ideal_bmi.config(state="readonly")
    variable.set(options[0])


# my calculation function
def calculate():
    try:
        int(weight.get())
        int(height.get())
        int(age.get())
        if variable.get() == "Select...":
            raise ValueError
        elif variable.get() == "Male":
            result = ((0.5 * int(weight.get()))) / ((int(height.get()) / 100) ** 2) + 11.5
            result = round(result, 1)
            ideal_bmi.config(state="normal")
            ideal_bmi.insert(0, result)
            ideal_bmi.config(state="readonly")
            result_bmi = int(weight.get()) / ((int(height.get()) / 100) ** 2)
            bmi.config(state="normal")
            bmi.insert(0, round(result_bmi, 1))
            bmi.config(state="readonly")
        elif variable.get() == "Female":
            result = ((0.5 * int(weight.get())) / ((int(height.get()) / 100) ** 2)) + (0.03 * int(age.get())) + 11
            result = round(result, 1)
            ideal_bmi.config(state="normal")
            ideal_bmi.insert(0, result)
            ideal_bmi.config(state="readonly")
            result_bmi = int(weight.get()) / ((int(height.get()) / 100) ** 2)
            bmi.config(state="normal")
            bmi.insert(0, round(result_bmi, 1))
            bmi.config(state="readonly")
    except ValueError:
        messagebox.showerror(title=None, message="Gender was not specified or invalid entry was given")


gender = OptionMenu(window, variable, *options, command=activate)
gender.place(x=250, y=140, height=50, width=120)
# Clear btn will clear all your date in your entry
delete = Button(window, text="Clear", command=clear, bg="orange")
delete.place(x=450, y=500)
# Exit btn will exit the program
quit = Button(window, text="EXIT", command="exit", bg="red")
quit.place(x=100, y=500)

calculate_bmi = Button(window, text="Calculate BMI", command=calculate, bg="green")
calculate_bmi.place(x=250, y=300, height=50, width=150)


mainloop()