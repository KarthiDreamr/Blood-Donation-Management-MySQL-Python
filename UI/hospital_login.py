import tkinter as tk
from UI.form.form_validation.runtime_validation import *
from UI.form.form_validation.complete_validation import *

def hlogin_submit():
    print("Hospital Login Submit")

def hospital_login_display():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Hospital Login")
    root.iconbitmap("assets/blood-donation.ico")


    # Defining the first row
    hospital_id = tk.Label(root, text ="Enter Hospital ID", )
    hospital_id.place(x = 50, y = 20)

    hospital_id_entry = tk.Entry(root, width = 35)
    hospital_id_entry.place(x = 150, y = 20, width = 100)

    isdigit_ensure_validate = (root.register(digit_ensure), "%P")
    hospital_id_entry.configure(validate="key", validatecommand=isdigit_ensure_validate)


    password = tk.Label(root, text ="Enter Password")
    password.place(x = 50, y = 50)

    password_entry = tk.Entry(root, width = 35)
    password_entry.place(x = 150, y = 50, width = 100)

    atmost_thirty_char_ensure_validate = (root.register(atmost_thirty_char_ensure), "%P")
    password_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validate,show="*")

    submitbtn = tk.Button(root, text ="Login", command = lambda: hlogin_submit()    )
    submitbtn.place(x = 150, y = 135, width = 55)

    root.mainloop()

