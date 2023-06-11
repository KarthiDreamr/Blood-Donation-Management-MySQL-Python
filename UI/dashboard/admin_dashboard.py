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

def admin_dashboard_display():
    # Create a new Tkinter window
    root = tk.Tk()

    # Set the window title
    root.title("Admin Dashboard")

    # Set the window background color
    root.config(bg="#f2f2f2")

    # Create a label for the title
    title_label = tk.Label(root, text="Choose from below options", font=("Arial", 16), bg="#f2f2f2", fg="#333")
    title_label.pack(pady=10)

    # Create a frame for the buttons
    button_frame = tk.Frame(root, bg="#f2f2f2")
    button_frame.pack(pady=10)

    # Create a button for new registration
    new_reg_button = tk.Button(button_frame, text="New Donor", font=("Arial", 12), width=15, height=2, 
                               bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                               command=lambda: enter_donor_form(root) )
    new_reg_button.pack(side=tk.LEFT, padx=10)

    # Create a button for registered donor
    reg_donor_button = tk.Button(button_frame, text="New Hospital", font=("Arial", 12), width=15, height=2, 
                                 bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                                 command=lambda: enter_hospital_form(root)  )
    reg_donor_button.pack(side=tk.LEFT, padx=10)

    reg_donor_button = tk.Button(button_frame, text="New Admin", font=("Arial", 12), width=15, height=2, 
                                 bg="#333", fg="#fff", activebackground="#555", activeforeground="#fff",
                                 command=lambda: enter_admin_form(root)  )
    reg_donor_button.pack(side=tk.LEFT, padx=10)

    # Start the Tkinter event loop
    root.mainloop() 