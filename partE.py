from tkinter import *

root = Tk()
root.geometry('300x200')

w = Label(
    root,
    text='Student options for courses',
    font=50
).pack()

cbut1 = IntVar()
cbut2 = IntVar()
cbut3 = IntVar()

but1 = Checkbutton(
    root,
    text='Online',
    variable=cbut1,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10
).pack()

but2 = Checkbutton(
    root,
    text='Onsite',
    variable=cbut2,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10
).pack()

but3 = Checkbutton(
    root,
    text='Hybrid',
    variable=cbut3,
    onvalue=1,
    offvalue=0,
    height=2,
    width=10
).pack()

root.mainloop()