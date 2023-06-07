import tkinter as tk

def error_popup(error_message="Invalid Input value",error_title="Error"):
    popup = tk.Toplevel()
    # popup.geometry("200x100")
    popup.title("Error")

    label = tk.Label(popup, text="hello")
    label.pack(pady=10)

def form_validator(hospital_id_entry,
                   hospital_name_entry,
                   password_entry,
                   total_capacity_entry,
                   quantity_required_entry,
                   contact_number_entry,
                   street_name_entry,
                   city_entry,
                   state_entry,
                   district_entry,
                   country_entry,
                   o_positive_available_entry,
                   o_negative_available_entry,
                   a_positive_available_entry,
                   a_negative_available_entry,
                   b_positive_available_entry,
                   b_negative_available_entry,
                   ab_positive_available_entry,
                   ab_negative_available_entry,
                   o_positive_maximum_entry,
                   o_negative_maximum_entry,
                   a_positive_maximum_entry,
                   a_negative_maximum_entry,
                   b_positive_maximum_entry,
                   b_negative_maximum_entry,
                   ab_positive_maximum_entry,
                   ab_negative_maximum_entry):    
    pass
    # if(hospital_id_entry.get()==""):
    #     print("Hospital id cannot be empty")
    #     error_popup("Hospital id cannot be empty")
    #     return
