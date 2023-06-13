import tkinter as tk

def enter_donor_form(root):
    from UI.form.registration.donor_reg import donor_form_display
    root.destroy()
    donor_form_display()

def enter_hospital_form(root):
    from UI.form.registration.hospital_reg import hospital_form_display
    root.destroy()
    hospital_form_display()

def enter_admin_form(root):
    from UI.form.registration.admin_reg import admin_form_display
    root.destroy()
    admin_form_display()

def enter_donor_table(root):
    from UI.table.donor_table import donor_table_display
    root.destroy()
    donor_table_display()

def enter_hospital_table(root):
    from UI.table.hospital_table import hospital_table_display
    root.destroy()
    hospital_table_display()

def enter_admin_table(root):
    from UI.table.admin_table import admin_table_display
    root.destroy()
    admin_table_display()


def admin_dashboard_display():
    # Create a new Tkinter window
    root = tk.Tk()

    # Set the window title
    root.title("Admin Dashboard")

    # Set the window background color
    root.config(bg="#f2f2f2")

    # Create a label for the title
    title_label = tk.Label(root, text="Choose from below options", font=("Arial", 16), bg="#f2f2f2", fg="#333")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Create a frame for the buttons
    button_frame = tk.Frame(root, bg="#f2f2f2")
    button_frame.grid(row=1, column=0, padx=10)

    # Create a button for new registration
    new_reg_button = tk.Button(button_frame, text="New Donor", font=("Arial", 12), width=15, height=2, 
                               bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                               command=lambda: enter_donor_form(root) )
    new_reg_button.grid(row=0, column=0, pady=5)

    # Create a button for registered donor
    reg_donor_button = tk.Button(button_frame, text="New Hospital", font=("Arial", 12), width=15, height=2, 
                                 bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                                 command=lambda: enter_hospital_form(root)  )
    reg_donor_button.grid(row=1, column=0, pady=5)

    reg_donor_button = tk.Button(button_frame, text="New Admin", font=("Arial", 12), width=15, height=2, 
                                 bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                                 command=lambda: enter_admin_form(root)  )
    reg_donor_button.grid(row=2, column=0,  pady=(5,15))

    # Create a frame for the buttons
    view_button_frame = tk.Frame(root, bg="#f2f2f2")
    view_button_frame.grid(row=1, column=1, padx=10)

    view_reg_button = tk.Button(view_button_frame, text="View Donor", font=("Arial", 12), width=15, height=2, 
                               bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                               command=lambda: enter_donor_table(root)  )
    view_reg_button.grid(row=0, column=0, pady=5)

    # Create a button for registered donor
    view_donor_button = tk.Button(view_button_frame, text="View Hospital", font=("Arial", 12), width=15, height=2, 
                                 bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                                 command=lambda: enter_hospital_table(root) )
    view_donor_button.grid(row=1, column=0, pady=5)

    view_donor_button = tk.Button(view_button_frame, text="View Admin", font=("Arial", 12), width=15, height=2, 
                                 bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                                 command=lambda: enter_admin_table(root)  )
    view_donor_button.grid(row=2, column=0,  pady=(5,15))

    # Start the Tkinter event loop
    root.mainloop() 