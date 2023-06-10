import tkinter as tk
from UI.form.form_validation.runtime_validation import *
from UI.form.form_validation.complete_validation import *

def dlogin_submit():
    print("Hospital Login Submit")

def donor_login_display():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Donor Login Page")
    root.iconbitmap("assets/blood-donation.ico")


    # Defining the first row
    aadhaar_id = tk.Label(root, text ="Enter Aadhaar ID", )
    aadhaar_id.place(x = 50, y = 20)

    aadhaar_id_entry = tk.Entry(root, width = 35)
    aadhaar_id_entry.place(x = 150, y = 20, width = 100)

    
    atleast_twelve_digit_ensure_validate = (root.register(atmost_twelve_digit_ensure), "%P")

    aadhaar_id_entry.configure(validate="key", validatecommand=atleast_twelve_digit_ensure_validate)


    password = tk.Label(root, text ="Enter Password")
    password.place(x = 50, y = 50)


    password_entry = tk.Entry(root, width = 35)
    password_entry.place(x = 150, y = 50, width = 100)

    atmost_thirtychar_ensure_validate = (root.register(atmost_thirty_char_ensure), "%P")

    password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)


    submitbtn = tk.Button(root, text ="Login", command = dlogin_submit)
    submitbtn.place(x = 150, y = 135, width = 55)

    root.mainloop()

