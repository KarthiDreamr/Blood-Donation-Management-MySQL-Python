def error_popup(message):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)
    root.destroy()

def alpha_validator(string, length,notnull=True):
    if(notnull and string == "" ):
        error_popup("Field cannot be empty")
    if( string.isalpha()):
        error_popup("Only alphabets are allowed")
    if( len(string) > length ):
        error_popup("Only "+str(length)+" characters are allowed")
    
def notnull_integer_validator(string,length=9):

    if(string == ""):
        error_popup("Field cannot be empty")
    if(string.isnumeric() == False):
        error_popup("Only numbers are allowed")
    if(len(string) > length):
        error_popup("Only "+str(length)+" characters are allowed")

def bigint_validator(string,notnull=True,length=10):
    if(notnull and string == "" ):
        error_popup("Field cannot be empty")
    if(string.isnumeric() == False):
        error_popup("Only numbers are allowed")
    if(len(string) > length):
        error_popup("Only "+str(length)+" characters are allowed")


def hospital_form_validator(
    Hospital_id_entry,
    Hospital_name_entry,
    Password_entry,
    total_capacity_entry,
    quantity_required_entry,
    contact_number_entry,
    Street_name_entry,
    City_entry,
    District_entry,
    State_entry,
    Country_entry,
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
    ab_negative_maximum_entry

    ):


    alpha_validator(Hospital_name_entry,30)
    alpha_validator(Password_entry,30)  
    alpha_validator(Street_name_entry,50)
    alpha_validator(City_entry,30)
    alpha_validator(District_entry,30)
    alpha_validator(State_entry,30)
    alpha_validator(Country_entry,30)

    notnull_integer_validator(Hospital_id_entry)
    notnull_integer_validator(total_capacity_entry)
    notnull_integer_validator(quantity_required_entry)
    notnull_integer_validator(o_positive_available_entry)
    notnull_integer_validator(o_negative_available_entry)
    notnull_integer_validator(a_positive_available_entry)
    notnull_integer_validator(a_negative_available_entry)
    notnull_integer_validator(b_positive_available_entry)
    notnull_integer_validator(b_negative_available_entry)
    notnull_integer_validator(ab_positive_available_entry)
    notnull_integer_validator(ab_negative_available_entry)
    notnull_integer_validator(o_positive_maximum_entry)
    notnull_integer_validator(o_negative_maximum_entry)
    notnull_integer_validator(a_positive_maximum_entry)
    notnull_integer_validator(a_negative_maximum_entry)
    notnull_integer_validator(b_positive_maximum_entry)
    notnull_integer_validator(b_negative_maximum_entry)
    notnull_integer_validator(ab_positive_maximum_entry)
    notnull_integer_validator(ab_negative_maximum_entry)

    bigint_validator(contact_number_entry)


def admin_form_validator( Admin_name_entry,Admin_id_entry,
                          password_entry ):
    alpha_validator(Admin_name_entry,50)
    notnull_integer_validator(Admin_id_entry)
    alpha_validator(password_entry,30)
    pass

def donor_form_validator(
    first_name_entry,
    last_name_entry,
    adhaar_id_entry,
    date_of_birth_entry,
    month_of_birth_entry,
    year_of_birth_entry,
    Street_name_entry,
    City_entry,
    District_entry,
    State_entry,
    Country_entry,
    Country_code_entry,
    Father_name_entry,
    Mother_name_entry,
    Guardian_name_entry,
    Phone_1_entry,
    Phone_2_entry,
    Hospital_ID_entry,
    New_Password_entry,
    Password_entry
    ):
    
    alpha_validator(first_name_entry,30)
    alpha_validator(last_name_entry,30)
    alpha_validator(Street_name_entry,50)
    alpha_validator(City_entry,30)
    alpha_validator(District_entry,30)
    alpha_validator(State_entry,30)
    alpha_validator(Country_entry,30)
    alpha_validator(Country_code_entry,3)
    alpha_validator(Father_name_entry,30)
    alpha_validator(Mother_name_entry,30)
    alpha_validator(Guardian_name_entry,30)
    alpha_validator(Password_entry,30)
    alpha_validator(New_Password_entry,30)

    notnull_integer_validator(Hospital_ID_entry)
    notnull_integer_validator(date_of_birth_entry,2)
    notnull_integer_validator(month_of_birth_entry,2)
    notnull_integer_validator(year_of_birth_entry,4)

    bigint_validator(adhaar_id_entry,length=12)
    bigint_validator(Phone_1_entry)
    bigint_validator(Phone_2_entry,notnull=False)









