
from tkinter import*
import tkinter
from tkinter import messagebox


interface = Tk()
interface.geometry("600x400")
interface.title("Adding two numbers")
def add_num():
    total = entry1.get()+entry2.get()
    entry3.insert(0, total)


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


def exit():
    return interface.destroy()


space = Label(interface, text="   ")
label1 = Label(interface, text="Please enter your first number", font="Times 16 bold", fg="green")
label1.place(x=40, y=40)
entry1 = Entry(interface)
entry1.place(x=360, y=45)

label2 = Label(interface, text="Please enter your second number",  font="Times 16 bold", fg="green")
label2.place(x=40, y=80)

entry2 = Entry(interface)
entry2.place(x=360, y=80)

label3 = Label(interface, text="Your answer", font="Times 16 bold", fg="green")
label3.place(x=200, y=120)

entry3 = Entry(interface)
entry3.place(x=360, y=125)

button1 = Button(interface, text="Add", command=add_num)
button1.place(x=360, y=200)

button2 = Button(interface, text="Clear", command=clear)
button2.place(x=300, y=200)

button3 = Button(interface, text="Exit", command=exit)
button3.place(x=250, y=200)

interface.mainloop()
