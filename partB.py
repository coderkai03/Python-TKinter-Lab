import tkinter as tk

counter = 0 #counting every second
def counting(label: tk):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    
    count()

root = tk.Tk()
root.title('Counting time (s)')
root.geometry('420x240')

label = tk.Label(root, fg='blue')
label.pack()

counting(label)

button = tk.Button(
    root,
    text='Stop',
    width=25,
    command=root.destroy
)
button.pack()


root.mainloop()