import tkinter as tk
from tkinter import ttk

# Create a window
root = tk.Tk()
root.iconbitmap("assets/blood-donation.ico")

root.title("Admin Form")

padding_xaxis = 10
padding_yaxis = 5

# Create a frame to hold the widgets
admin_frame = ttk.Frame(root, padding=10)
admin_frame.grid()

# Create labels and entries for each column in the table

#row 1

width_combobox = 17

Admin_name = ttk.Label(admin_frame, text="Admin Name")
Admin_name.grid(row=0, column=0, sticky=tk.W)

Admin_name_entry = ttk.Entry(admin_frame)
Admin_name_entry.grid(row=0, column=1, padx=padding_xaxis, pady=padding_yaxis)

#row 2

def atmost_fifty_char_onlyalpha_ensure(input):
    return len(input) <= 50 or input == "" and input.isalpha()

atmost_fifty_char_onlyalpha_ensure_validator = (admin_frame.register(atmost_fifty_char_onlyalpha_ensure), "%P")

Admin_name_entry.configure(validate="key", validatecommand=atmost_fifty_char_onlyalpha_ensure_validator)


Admin_id = ttk.Label(admin_frame, text="Admin ID")
Admin_id.grid(row=1, column=0, sticky=tk.W)

Admin_id_entry = ttk.Entry(admin_frame)
Admin_id_entry.grid(row=1, column=1, padx=padding_xaxis, pady=padding_yaxis)

#row 3

password = ttk.Label(admin_frame, text="Password")
password.grid(row=3, column=0, sticky=tk.W)

password_entry = ttk.Entry(admin_frame)
password_entry.grid(row=3, column=1, padx=padding_xaxis, pady=padding_yaxis)

#row 4

back_button = tk.Button(admin_frame, text="back", command=lambda: root.destroy()) 
back_button.grid(row=4, column=0, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

submit_button = ttk.Button(admin_frame,text="Submit",command=lambda: root.destroy())
submit_button.grid(row=4, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

def atleast_eight_atmost_thirtychar_ensure(input):
    return len(input) <= 30 and len(input) >= 8 or input == ""

atleast_eight_atmost_thirtychar_ensure_validate = (admin_frame.register(atleast_eight_atmost_thirtychar_ensure), "%P")

password_entry.configure(validate="key", validatecommand=atleast_eight_atmost_thirtychar_ensure_validate)

# # Create a button to submit the form
# btn = ttk.Button(admin_frame, text="Submit")
# btn.grid(row=4)

# Start the main loop
root.mainloop()
