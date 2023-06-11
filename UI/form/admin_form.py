import tkinter as tk
from tkinter import ttk

from form_validation.runtime_validation import *
from form_validation.complete_validation import *

# Create a window
admin_root = tk.Tk()
admin_root.iconbitmap("assets/blood-donation.ico")

admin_root.title("Admin Form")

padding_xaxis = 10
padding_yaxis = 5

# Create a frame to hold the widgets
admin_frame = ttk.Frame(admin_root, padding=10)
admin_frame.grid()

# Create labels and entries for each column in the table

#row 0
width_combobox = 17

admin_name = ttk.Label(admin_frame, text="Admin Name")
admin_name.grid(row=0, column=0, sticky=tk.W)

admin_name_entry = ttk.Entry(admin_frame)
admin_name_entry.grid(row=0, column=1, padx=padding_xaxis, pady=padding_yaxis)

#row 1
atmost_fifty_char_onlyalpha_ensure_validator = (admin_frame.register(atmost_fifty_char_onlyalpha_ensure), "%P")

admin_name_entry.configure(validate="key", validatecommand=atmost_fifty_char_onlyalpha_ensure_validator)


admin_id = ttk.Label(admin_frame, text="Admin ID")
admin_id.grid(row=1, column=0, sticky=tk.W)

admin_id_entry = ttk.Entry(admin_frame)
admin_id_entry.grid(row=1, column=1, padx=padding_xaxis, pady=padding_yaxis)

#row 2
password = ttk.Label(admin_frame, text="Password")
password.grid(row=3, column=0, sticky=tk.W)

password_entry = ttk.Entry(admin_frame)
password_entry.grid(row=3, column=1, padx=padding_xaxis, pady=padding_yaxis)

#row 3
back_button = tk.Button(admin_frame, text="back", command=lambda: admin_root.destroy()) 
back_button.grid(row=4, column=0, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

submit_button = ttk.Button(admin_frame,text="Submit",command=lambda: admin_registration_validator(admin_name_entry.get(),admin_id_entry.get(),password_entry.get()) )
submit_button.grid(row=4, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


atleast_eight_atmost_thirtychar_ensure_validate = (admin_frame.register(atmost_thirty_char_ensure), "%P")

password_entry.configure(validate="key", validatecommand=atleast_eight_atmost_thirtychar_ensure_validate)

admin_frame.mainloop()
# Start the main loop
admin_root.mainloop()
