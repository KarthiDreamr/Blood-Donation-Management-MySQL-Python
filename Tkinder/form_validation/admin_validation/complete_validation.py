import tkinter as tk

def error_popup(error_message="Invalid Input value",error_title="Error"):
    popup = tk.Toplevel()
    # popup.geometry("200x100")
    popup.title("Error")

    label = tk.Label(popup, text="hello")
    label.pack(pady=10)

def form_validator(atmost_fifty_char_onlyalpha_ensure,
                   atleast_eight_atmost_thirtychar_ensure):
    pass
    # if(hospital_id_entry.get()==""):
    #     print("Hospital id cannot be empty")
    #     error_popup("Hospital id cannot be empty")
    #     return
