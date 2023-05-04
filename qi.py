from tkinter import *
from PIL import ImageTk, Image

# Create the window
root = Tk()

# Set the window title
root.title("DEAF MUTE HELPER ")

# Set the window size
root.geometry("500x500")

# Load the background image
bg_images = Image.open(nature.jpg)
bg_image = bg_images.resize((500, 500), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)

# Create a Label widget to display the background image
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a rounded button with an icon on it
icon_image = Image.open("(•_•)")
icon_image = icon_image.resize((50, 50), Image.ANTIALIAS)
icon_image = ImageTk.PhotoImage(icon_image)

button = Button(root, text="Button", image=icon_image, bg="white", bd=0, borderwidth=0, highlightthickness=0)
button.config(width=60, height=60)
button.place(x=220, y=220)

# Start the main loop
root.mainloop()
