import tkinter as tk

root = tk.Tk()

logo = tk.PhotoImage(file='optimus-transform.gif')

window1 = tk.Label(root, image=logo).pack(side='right')

explanation = '''Optimum Pride making his final tranformation
in the final fight against Megatron and the Decepticons.

One of the most iconic scenes in cinema during the 2000s,
and my favorite moment to witness as a child in the movie theater.'''

w2 = tk.Label(
    root,
    justify=tk.LEFT,
    padx=10,
    text=explanation
).pack(side='left')

root.mainloop()