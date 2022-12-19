from tkinter import *
from tkinter import messagebox


#def reset():
    #height.delete(0, 'end')
    #weight.delete(0, 'end')


def bmi_cal():
    kg = int(weight.get())
    m = int(height.get())
    bmi = kg / m ** 2
    bmi = round(bmi, 1)
    bmi_index(bmi)


def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI', f'BMI = {bmi} is Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI', f'BMI = {bmi} is Overweight')
    elif bmi > 29.9:
        messagebox.showinfo('BMI', f'BMI = {bmi} is Obesity')
    else:
        messagebox.showerror('BMI', 'something went wrong!')

root = Tk()
root.title("BMI Calculator")

var = IntVar()

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

sex = Label(frame, text="Select Your Gender:")
sex.grid(row=2, column=1)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=10)

male = Radiobutton(frame2, text="Male", variable=var, value=1)
male.pack(side=RIGHT)
female = Radiobutton(frame2, text="Female", variable=var, value=0)
female.pack(side=LEFT)

height_label = Label(frame, text="Enter your Height in CM:")
height_label.grid(row=3, column=1)
weight_label = Label(frame, text="Enter your Weight in KG:")
weight_label.grid(row=4, column=1)

height = Entry(frame)
height.grid(row=3, column=2, pady=5)
root.mainloop()
