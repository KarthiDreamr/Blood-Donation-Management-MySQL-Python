import tkinter as tk
from DB.db_creation import db_connection

from DB.donor_insertion import insert_donor
from DB.hospital_insertion import insert_hospital
from DB.admin_insertion import insert_admin

from UI.error import error_popup

def notnull_validator(string,length=30):
    if(string == "" and length <= 30):
        #error_popup("Field cannot be empty")
        raise TypeError("Field cannot be empty")

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
    

#registration validators

def hospital_registration_validator(
    hospital_root,
    hospital_id,
    hospital_name,
    password,
    total_capacity,
    quantity_required,
    contact_number,
    street_name,
    city,
    district,
    state,
    country,
    o_positive_available,
    o_negative_available,
    a_positive_available,
    a_negative_available,
    b_positive_available,
    b_negative_available,
    ab_positive_available,
    ab_negative_available,
    o_positive_maximum,
    o_negative_maximum,
    a_positive_maximum,
    a_negative_maximum,
    b_positive_maximum,
    b_negative_maximum,
    ab_positive_maximum,
    ab_negative_maximum
    ):

    try:

        alpha_validator(hospital_name,30)
        notnull_validator(password,30)  
        alpha_validator(street_name,50)
        alpha_validator(city,30)
        alpha_validator(district,30)
        alpha_validator(state,30)
        alpha_validator(country,30)

        notnull_integer_validator(hospital_id)
        notnull_integer_validator(total_capacity)
        notnull_integer_validator(quantity_required)
        notnull_integer_validator(o_positive_available)
        notnull_integer_validator(o_negative_available)
        notnull_integer_validator(a_positive_available)
        notnull_integer_validator(a_negative_available)
        notnull_integer_validator(b_positive_available)
        notnull_integer_validator(b_negative_available)
        notnull_integer_validator(ab_positive_available)
        notnull_integer_validator(ab_negative_available)
        notnull_integer_validator(o_positive_maximum)
        notnull_integer_validator(o_negative_maximum)
        notnull_integer_validator(a_positive_maximum)
        notnull_integer_validator(a_negative_maximum)
        notnull_integer_validator(b_positive_maximum)
        notnull_integer_validator(b_negative_maximum)
        notnull_integer_validator(ab_positive_maximum)
        notnull_integer_validator(ab_negative_maximum)

        bigint_validator(contact_number)

        hospital_data =  (
            hospital_root,
            hospital_id,
            hospital_name,
            password,
            total_capacity,
            quantity_required,
            contact_number,
            street_name,
            city,
            district,
            state,
            country,
            o_positive_available,
            o_negative_available,
            a_positive_available,
            a_negative_available,
            b_positive_available,
            b_negative_available,
            ab_positive_available,
            ab_negative_available,
            o_positive_maximum,
            o_negative_maximum,
            a_positive_maximum,
            a_negative_maximum,
            b_positive_maximum,
            b_negative_maximum,
            ab_positive_maximum,
            ab_negative_maximum
            )
        
        insert_hospital(hospital_data)

        hospital_root.destroy()

    except TypeError as e:
        error_popup(e)
        return 
 
def donor_registration_validator(
    donor_root,
    first_name,
    last_name,
    adhaar_id,
    date_of_birth,
    month_of_birth,
    year_of_birth,
    street_name,
    city,
    district,
    state,
    country,
    country_code,
    father_name,
    mother_name,
    guardian_name,
    phone_1,
    phone_2,
    hospital_ID,
    new_password,
    confirm_password,
    ):
    
    try:
        alpha_validator(first_name,30)
        alpha_validator(last_name,30)
        alpha_validator(street_name,30)
        alpha_validator(city,30)
        alpha_validator(district,30)
        alpha_validator(state,30)
        alpha_validator(country,30)
        alpha_validator(country_code,3)
        alpha_validator(father_name,30)
        alpha_validator(mother_name,30)
        alpha_validator(guardian_name,30)
        notnull_validator(confirm_password,30)
        notnull_validator(new_password,30)

        notnull_integer_validator(hospital_ID)
        notnull_integer_validator(date_of_birth,2)
        notnull_integer_validator(month_of_birth,2)
        notnull_integer_validator(year_of_birth,4)

        bigint_validator(adhaar_id,length=12)
        bigint_validator(phone_1)
        bigint_validator(phone_2,notnull=False)

        if(new_password!=confirm_password):
            #error_popup("Passwords do not match")
            raise TypeError("Passwords do not match")

        cursor = db_connection().cursor()
        
        donor_data = (  
                        first_name,
                        last_name,
                        adhaar_id,
                        date_of_birth,
                        month_of_birth,
                        year_of_birth,
                        street_name,
                        city,
                        district,
                        state,
                        country,
                        country_code,
                        father_name,
                        mother_name,
                        guardian_name,
                        phone_1,
                        phone_2,
                        hospital_ID,
                        new_password,
                        confirm_password,
                        )
        
        insert_donor(donor_data)

        donor_root.destroy()
    
    except TypeError as e:
        error_popup(e)
        return


def admin_registration_validator(admin_root,admin_name,admin_id,password ):
    try:
        alpha_validator(admin_name,50)
        notnull_integer_validator(admin_id)
        alpha_validator(password,30)

        admin_data = (admin_root,admin_name,admin_id,password)

        insert_admin(admin_data)

        admin_root.destroy()

    except TypeError as e:
        error_popup(e)
        return
    




#login validators

def donor_login_validator(donor_login_root,donor_id,password):
    try:
        notnull_integer_validator(donor_id)
        notnull_validator(password,30)

        donor_login_root.destroy()

    except TypeError as e:
        error_popup(e)
        return
    
def hospital_login_validator(hospital_login_root ,hospital_id,password):
    try:
        notnull_integer_validator(hospital_id)
        notnull_validator(password,30)

        hospital_login_root.destroy()

    except TypeError as e:
        error_popup(e)
        return
    
def admin_login_validator(admin_login_root,admin_id,password):
    try:
        notnull_integer_validator(admin_id)
        notnull_validator(password,30)

        admin_login_root.destroy()
        
    except TypeError as e:
        error_popup(e)
        return
    
