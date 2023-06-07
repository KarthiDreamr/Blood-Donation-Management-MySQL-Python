import tkinter as tk

def error_popup(error_message="Invalid Input value",error_title="Error"):
    popup = tk.Toplevel()
    # popup.geometry("200x100")
    popup.title("Error")

    label = tk.Label(popup, text="hello")
    label.pack(pady=10)

def form_validator(atmost_twenty_char_onlyalpha_ensure,
                   atleast_twelve_digit_ensure,
                   date_of_birth_ensure,
                   atmost_fifty_char_ensure,
                   atmost_thirty_char_ensure,
                   atmost_twenty_char_ensure,
                   atmost_plus_three_char_ensure,
                   atmost_thirty_char_onlyalpha_ensure,
                   atleast_ten_digit_ensure,
                   isdigit_ensure,
                   atmost_thirtychar_ensure):
    pass
    # if(hospital_id_entry.get()==""):
    #     print("Hospital id cannot be empty")
    #     error_popup("Hospital id cannot be empty")
    #     return
