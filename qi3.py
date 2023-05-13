import tkinter as tk
from tkinter import PhotoImage
import os
import subprocess

# Create a window with a background image
window = tk.Tk()
window.geometry("500x500")
window.title("DEAF MUTE HELPER")

bg_image = PhotoImage(file="static/images/ml.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create two rounded buttons with icons
camera_icon = PhotoImage(file="static/images/ml.png")
audio_icon = PhotoImage(file="static/images/ml.png")

camera_button = tk.Button(window, image=camera_icon, bg="white", bd=0, command=lambda: launch_webcam())
camera_button.place(x=100, y=200)

audio_button = tk.Button(window, image=audio_icon, bg="white", bd=0, command=lambda: start_audio_recording())
audio_button.place(x=300, y=200)

# Define a function to start audio recording
def start_audio_recording():

    pass

def launch_webcam():
    pass

# Run the window
window.mainloop()
