import tkinter as tk

def error_popup(message):

    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)
    root.destroy()


def alpha_validator(string, length,notnull=True):
    if(notnull and string == "" ):
        raise TypeError("Field cannot be empty")
    if( string.isalpha()):
        raise TypeError("Only alphabets are allowed")
    if( len(string) > length ):
        # error_popup("Only "+str(length)+" characters are allowed")
        raise TypeError("Only "+str(length)+" characters are allowed")
    
def notnull_integer_validator(string,length=9):

    if(string == ""):
        #error_popup("Field cannot be empty")
        raise TypeError("Field cannot be empty")
    if(string.isnumeric() == False):
        #error_popup("Only numbers are allowed")
        raise TypeError("Only numbers are allowed")
    if(len(string) > length):
        #error_popup("Only "+str(length)+" characters are allowed")
        raise TypeError("Only "+str(length)+" characters are allowed")
    
def bigint_validator(string,notnull=True,length=10):
    if(notnull and string == "" ):
        #error_popup("Field cannot be empty")
        raise TypeError("Field cannot be empty")
    if(string.isnumeric() == False):
        #error_popup("Only numbers are allowed")
        raise TypeError("Only numbers are allowed")
    if(len(string) > length):
        #error_popup("Only "+str(length)+" characters are allowed")
        raise TypeError("Only "+str(length)+" characters are allowed")
    
def hospital_registration_validator(
    hospital_id_entry,
    hospital_name_entry,
    password_entry,
    total_capacity_entry,
    quantity_required_entry,
    contact_number_entry,
    street_name_entry,
    city_entry,
    district_entry,
    state_entry,
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
    ab_negative_maximum_entry

    ):

    try:

        alpha_validator(hospital_name_entry,30)
        alpha_validator(password_entry,30)  
        alpha_validator(street_name_entry,50)
        alpha_validator(city_entry,30)
        alpha_validator(district_entry,30)
        alpha_validator(state_entry,30)
        alpha_validator(country_entry,30)

        notnull_integer_validator(hospital_id_entry)
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

    except TypeError as e:
        error_popup(e)
        return 

def admin_registration_validator( Admin_name_entry,Admin_id_entry,
                          password_entry ):
    
    alpha_validator(Admin_name_entry,50)
    notnull_integer_validator(Admin_id_entry)
    alpha_validator(password_entry,30)
 
def donor_registration_validator(
    donor_root,
    first_name_entry,
    last_name_entry,
    adhaar_id_entry,
    date_of_birth_entry,
    month_of_birth_entry,
    year_of_birth_entry,
    street_name_entry,
    city_entry,
    district_entry,
    state_entry,
    country_entry,
    country_code_entry,
    father_name_entry,
    mother_name_entry,
    guardian_name_entry,
    phone_1_entry,
    phone_2_entry,
    hospital_ID_entry,
    new_password_entry,
    current_password_entry
    ):
    
    try:
        alpha_validator(first_name_entry,30)
        alpha_validator(last_name_entry,30)
        alpha_validator(street_name_entry,30)
        alpha_validator(city_entry,30)
        alpha_validator(district_entry,30)
        alpha_validator(state_entry,30)
        alpha_validator(country_entry,30)
        alpha_validator(country_code_entry,3)
        alpha_validator(father_name_entry,30)
        alpha_validator(mother_name_entry,30)
        alpha_validator(guardian_name_entry,30)
        alpha_validator(current_password_entry,30)
        alpha_validator(new_password_entry,30)

        notnull_integer_validator(hospital_ID_entry)
        notnull_integer_validator(date_of_birth_entry,2)
        notnull_integer_validator(month_of_birth_entry,2)
        notnull_integer_validator(year_of_birth_entry,4)

        bigint_validator(adhaar_id_entry,length=12)
        bigint_validator(phone_1_entry)
        bigint_validator(phone_2_entry,notnull=False)
    
    except TypeError as e:
        error_popup(e)
        return

def admin_registration_validator(admin_name_entry,admin_id_entry,password_entry ):
    try:
        alpha_validator(admin_name_entry,50)
        notnull_integer_validator(admin_id_entry)
        alpha_validator(password_entry,30)
    except TypeError as e:
        error_popup(e)
        return
    

def donor_login_validator(donor_id_entry,password_entry):
    try:
        notnull_integer_validator(donor_id_entry)
        alpha_validator(password_entry,30)
    except TypeError as e:
        error_popup(e)
        return
    
def hospital_login_validator(hospital_id_entry,password_entry):
    try:
        notnull_integer_validator(hospital_id_entry)
        alpha_validator(password_entry,30)
    except TypeError as e:
        error_popup(e)
        return
    
def admin_login_validator(admin_id_entry,password_entry):
    try:
        notnull_integer_validator(admin_id_entry)
        alpha_validator(password_entry,30)
    except TypeError as e:
        error_popup(e)
        return
    
