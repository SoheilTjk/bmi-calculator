from tkinter import *
from tkinter import messagebox

def reset():
    height.delete(0, 'end')
    weight.delete(0, 'end')

def bmi_cal():
    kg = int(weight.get())
    m = int(height.get())
    bmi = kg / m**2
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('bmi-pythonguides', 'something went wrong!')