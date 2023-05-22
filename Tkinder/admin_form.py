import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title("Admin Form")

# Create a frame to hold the widgets
frame = ttk.Frame(window, padding=10)
frame.grid()

# Create labels and entries for each column in the table

#row 1

width_combobox = 17

Admin_name = ttk.Label(frame, text="Admin Name")
Admin_name.grid(row=0, column=0, sticky=tk.W)

Admin_name_entry = ttk.Entry(frame)
Admin_name_entry.grid(row=0, column=1)

def atmost_fifty_char_onlyalpha_ensure(input):
    return len(input) <= 50 or input == "" and input.isalpha()

atmost_fifty_char_onlyalpha_ensure_validator = (frame.register(atmost_fifty_char_onlyalpha_ensure), "%P")

Admin_name_entry.configure(validate="key", validatecommand=atmost_fifty_char_onlyalpha_ensure_validator)


Admin_id = ttk.Label(frame, text="Admin ID")
Admin_id.grid(row=0, column=2, sticky=tk.W)

Admin_id_entry = ttk.Entry(frame)
Admin_id_entry.grid(row=0, column=3)

#row 2

password = ttk.Label(frame, text="Password")
password.grid(row=1, column=0, sticky=tk.W)

password_entry = ttk.Entry(frame)
password_entry.grid(row=1, column=1)

def atleast_eight_atmost_thirtychar_ensure(input):
    return len(input) <= 30 and len(input) >= 8 or input == ""

atleast_eight_atmost_thirtychar_ensure_validate = (frame.register(atleast_eight_atmost_thirtychar_ensure), "%P")

password_entry.configure(validate="key", validatecommand=atleast_eight_atmost_thirtychar_ensure_validate)

# Create a button to submit the form
btn = ttk.Button(frame, text="Submit")
btn.grid(row=2)

# Start the main loop
window.mainloop()
