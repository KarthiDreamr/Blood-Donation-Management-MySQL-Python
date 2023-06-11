import tkinter as tk
from UI.form.form_validation.runtime_validation import *
from UI.form.form_validation.complete_validation import *

def alogin_submit():
    pass

def admin_login_display():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Admin Login")
    root.iconbitmap("assets/blood-donation.ico")


    # Defining the first row
    admin_id = tk.Label(root, text ="Enter Admin ID", )
    admin_id.place(x = 50, y = 20)

    admin_id_entry = tk.Entry(root, width = 35)
    admin_id_entry.place(x = 150, y = 20, width = 100)

    isdigit_ensure_validate = (root.register(digit_ensure), "%P")

    admin_id_entry.configure(validate="key", validatecommand=isdigit_ensure_validate)


    password = tk.Label(root, text ="Enter Password")
    password.place(x = 50, y = 50)

    password_entry = tk.Entry(root, width = 35)
    password_entry.place(x = 150, y = 50, width = 100)

    atmost_thirty_char_onlyalpha_ensure_validate = (root.register(atmost_thirty_char_onlyalpha_ensure), "%P")
    password_entry.configure(show="*",validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validate)

    submitbtn = tk.Button(root, text ="Login", command = alogin_submit)
    submitbtn.place(x = 150, y = 135, width = 55)

    root.mainloop()

