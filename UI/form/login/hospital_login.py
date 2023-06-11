import tkinter as tk
from UI.form.form_validation.runtime_validation import *
from UI.form.form_validation.complete_validation import *

def hlogin_submit():
    print("Hospital Login Submit")

def hospital_login_display():
    hospital_login_root = tk.Tk()
    hospital_login_root.geometry("300x300")
    hospital_login_root.title("Hospital Login")
    hospital_login_root.iconbitmap("assets/blood-donation.ico")


    # Defining the first row
    hospital_id = tk.Label(hospital_login_root, text ="Enter Hospital ID", )
    hospital_id.place(x = 50, y = 20)

    hospital_id_entry = tk.Entry(hospital_login_root, width = 35)
    hospital_id_entry.place(x = 150, y = 20, width = 100)

    isdigit_ensure_validate = (hospital_login_root.register(digit_ensure), "%P")
    hospital_id_entry.configure(validate="key", validatecommand=isdigit_ensure_validate)


    password = tk.Label(hospital_login_root, text ="Enter Password")
    password.place(x = 50, y = 50)

    password_entry = tk.Entry(hospital_login_root, width = 35)
    password_entry.place(x = 150, y = 50, width = 100)

    atmost_thirty_char_ensure_validate = (hospital_login_root.register(atmost_thirty_char_ensure), "%P")
    password_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validate,show="*")

    submitbtn = tk.Button(hospital_login_root, text ="Login", command = lambda: hospital_login_validator(hospital_login_root,hospital_id_entry.get(), password_entry.get())   )
    submitbtn.place(x = 150, y = 135, width = 55)

    hospital_login_root.mainloop()

