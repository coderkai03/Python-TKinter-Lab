import tkinter as tk
from PIL import Image, ImageTk

def update_frame(current_frame):
    try:
        # Open the GIF file
        gif.seek(current_frame)

        # Create Tkinter-compatible photo image
        photo = ImageTk.PhotoImage(gif)

        # Update the label with the new frame
        label.configure(image=photo)
        label.image = photo

        # Increment the frame index
        current_frame += 1
        if current_frame >= frames:
            current_frame = 0

        # Schedule the next frame update
        root.after(100, update_frame, current_frame)
    except IOError:
        pass

root = tk.Tk()
label = tk.Label(root)
label.pack()

# Open the GIF file
gif = Image.open("optimus-transform.gif")
frames = gif.n_frames

# Start the animation
update_frame(0)

root.mainloop()
