import tkinter as tk
from tkinter import PhotoImage
import os
import subprocess

# Create a window with a background image
window = tk.Tk()
window.geometry("500x500")
window.title("DEAF MUTE HELPER")

bg_image = PhotoImage(file="background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create two rounded buttons with icons
camera_icon = PhotoImage(file="camera.png")
audio_icon = PhotoImage(file="microphone.png")

camera_button = tk.Button(window, image=camera_icon, bg="white", bd=0, command=lambda: os.system("start /b /wait explorer.exe shell:::{0DE09814-9E36-4F19-AF2D-3DCEC6FE5C88}"))
camera_button.place(x=100, y=200)

audio_button = tk.Button(window, image=audio_icon, bg="white", bd=0, command=lambda: start_audio_recording())
audio_button.place(x=300, y=200)

# Define a function to start audio recording
def start_audio_recording():
    subprocess.Popen(["powershell", "-Command", "Start-Process", "-FilePath", "cmd.exe", "-ArgumentList", "/C", "echo Audio recording started && timeout 5"])

# Run the window
window.mainloop()
