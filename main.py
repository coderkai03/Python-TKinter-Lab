import tkinter as tk

window = tk.Tk()
window.geometry('400x400')

welcome = tk.Label(text='Hello, coders')
welcome.pack()

label = tk.Label(
    text='Hello, memers',
    foreground='yellow',
    background='black',
    width=10,
    height=10
)
label.pack()

button = tk.Button(
    text='CLICK ME!!',
    width=25,
    height=5,
    bg='white',
    fg='blue'
)
button.pack()

window.mainloop()