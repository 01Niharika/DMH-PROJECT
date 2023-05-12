import tkinter as tk

# Create the window
window = tk.Tk()
window.title("DEAF MUTE HELPER")
window.geometry("400x300")


# Create the button widgets
button1 = tk.Button(window, text="Open Camera")
button2 = tk.Button(window, text="Record")

# Pack the buttons using the grid layout manager to center them
#button1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
#button2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Set the row and column weights to 1 so the buttons expand to fill the space
#window.grid_rowconfigure(0, weight=1)
#window.grid_columnconfigure(0, weight=1)


# Center the button widgets
button1.pack(side=tk.LEFT, padx=20)
button2.pack(side=tk.RIGHT, padx=20)

# Run the window
window.mainloop()

