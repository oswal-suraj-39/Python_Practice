# Write Python GUI program to take accept your birthdate 
# and output your age when a button is pressed.

from tkinter import Tk, Label, Entry, Button

def calculate_age():
    from datetime import date
    today = date.today()
    
    birth_day = int(day.get())
    birth_month = int(month.get())
    birth_year = int(year.get())

    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

    from tkinter import messagebox
    messagebox.showinfo("Age", f"You are {age} years old.")

top = Tk()
top.geometry("300x200")
top.title("Age Calculator")

label1 = Label(top, text="Enter your Day:")
day = Entry(top)

label2 = Label(top, text="Enter your Month:")
month = Entry(top)

label3 = Label(top, text="Enter your Year:")
year = Entry(top)

button = Button(top, text="Calculate Age", command=calculate_age)

label1.grid(row=0, column=0)
day.grid(row=0, column=1)

label2.grid(row=1, column=0)
month.grid(row=1, column=1)

label3.grid(row=2, column=0)
year.grid(row=2, column=1)

button.grid(row=3, columnspan=2)

top.mainloop()