import tkinter as tk
from UI.form.form_validation.runtime_validation import *
from UI.form.form_validation.complete_validation import *

def dlogin_submit():
    print("Hospital Login Submit")

def donor_login_display():
    donor_login_root = tk.Tk()
    donor_login_root.geometry("300x300")
    donor_login_root.title("Donor Login")
    donor_login_root.iconbitmap("assets/blood-donation.ico")


    # Defining the first row
    aadhaar_id = tk.Label(donor_login_root, text ="Enter Aadhaar ID", )
    aadhaar_id.place(x = 50, y = 20)

    aadhaar_id_entry = tk.Entry(donor_login_root, width = 35)
    aadhaar_id_entry.place(x = 150, y = 20, width = 100)

    
    atleast_twelve_digit_ensure_validate = (donor_login_root.register(atmost_twelve_digit_ensure), "%P")

    aadhaar_id_entry.configure(validate="key", validatecommand=atleast_twelve_digit_ensure_validate)


    password = tk.Label(donor_login_root, text ="Enter Password")
    password.place(x = 50, y = 50)


    password_entry = tk.Entry(donor_login_root, width = 35)
    password_entry.place(x = 150, y = 50, width = 100)

    atmost_thirtychar_ensure_validate = (donor_login_root.register(atmost_thirty_char_ensure), "%P")

    password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)


    submitbtn = tk.Button(donor_login_root, text ="Login", command = lambda: donor_login_validator(donor_login_root,aadhaar_id_entry.get(), password_entry.get()))
    submitbtn.place(x = 150, y = 135, width = 55)

    donor_login_root.mainloop()

