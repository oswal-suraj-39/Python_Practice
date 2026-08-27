# Write Python GUI program to take accept your birthdate 
# and output your age when a button is pressed.

from tkinter import Tk, Label, Entry, Button

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

top.mainloop()