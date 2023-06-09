import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title("Donor Authentication")

# Set the window size
window.geometry("400x200")

# Set the window background color
window.config(bg="#f2f2f2")

# Create a label for the title
title_label = tk.Label(window, text="Choose from below options", font=("Arial", 16), bg="#f2f2f2", fg="#333")
title_label.pack(pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(window, bg="#f2f2f2")
button_frame.pack(pady=10)

# Create a button for new registration
new_reg_button = tk.Button(button_frame, text="New Registration", font=("Arial", 12), width=15, height=2, bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff")
new_reg_button.pack(side=tk.LEFT, padx=10)

# Create a button for registered donor
reg_donor_button = tk.Button(button_frame, text="Sign In", font=("Arial", 12), width=15, height=2, bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff")
reg_donor_button.pack(side=tk.LEFT, padx=10)

# Start the Tkinter event loop
window.mainloop()