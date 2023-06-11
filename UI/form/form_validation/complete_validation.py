from DB.insertion.donor_insertion import insert_donor
from DB.insertion.hospital_insertion import insert_hospital
from DB.insertion.admin_insertion import insert_admin

from DB.existence_checking.donor_existence_checking import donor_existence_check
from DB.existence_checking.hospital_existence_checking import hospital_existence_check
from DB.existence_checking.admin_existence_checking import admin_existence_check

from UI.error import error_popup

def notnull_validator(field_name,string,max_length=30,minlength=1):
    if(string == "" and string <= max_length and string >= minlength):
        #error_popup("Field cannot be empty in "+field_name)
        raise TypeError("Field cannot be empty in "+field_name)

def alpha_validator(field_name,string, length,notnull=True):
    if(notnull and string == "" ):
        raise TypeError("Field cannot be empty in "+field_name)
    if( string.isalpha() == False):
        raise TypeError("Only alphabets are allowed in  "+field_name)
    if( len(string) > length ):
        # error_popup("Only "+str(length)+" characters are allowed in  "+field_name)
        raise TypeError("Only "+str(length)+" characters are allowed in  "+field_name)
    
def notnull_integer_validator(field_name,string,length=10):

    if(string == ""):
        #error_popup("Field cannot be empty in "+field_name)
        raise TypeError("Field cannot be empty in "+field_name)
    if(string.isnumeric() == False):
        #error_popup("Only numbers are allowed in  "+field_name)
        raise TypeError("Only numbers are allowed in  "+field_name)
    if(len(string) > length):
        #error_popup("Only "+str(length)+" characters are allowed in  "+field_name)
        raise TypeError("Only "+str(length)+" characters are allowed in  "+field_name)
    
def bigint_validator(field_name,string,notnull=True,length=10):
    if(notnull and string == "" ):
        #error_popup("Field cannot be empty in "+field_name)
        raise TypeError("Field cannot be empty in "+field_name)
    if(string.isnumeric() == False):
        #error_popup("Only numbers are allowed in  "+field_name)
        raise TypeError("Only numbers are allowed in  "+field_name)
    if(len(string) > length):
        #error_popup("Only "+str(length)+" characters are allowed in  "+field_name)
        raise TypeError("Only "+str(length)+" characters are allowed in  "+field_name)
    

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

        alpha_validator("hospital_name",hospital_name,30)
        notnull_validator("password",password,30) 
        alpha_validator("street_name",street_name,50)
        alpha_validator("city",city,30)
        alpha_validator("district",district,30)
        alpha_validator("state",state,30)
        alpha_validator("country",country,30)

        notnull_integer_validator("hospital_id",hospital_id)
        notnull_integer_validator("total_capacity",total_capacity)
        notnull_integer_validator("quantity_required",quantity_required)
        notnull_integer_validator("o_positive_available",o_positive_available)
        notnull_integer_validator("o_negative_available",o_negative_available)
        notnull_integer_validator("a_positive_available",a_positive_available)
        notnull_integer_validator("a_negative_available",a_negative_available)
        notnull_integer_validator("b_positive_available",b_positive_available)
        notnull_integer_validator("b_negative_available",b_negative_available)
        notnull_integer_validator("ab_positive_available",ab_positive_available)
        notnull_integer_validator("ab_negative_available",ab_negative_available)
        notnull_integer_validator("o_positive_maximum",o_positive_maximum)
        notnull_integer_validator("o_negative_maximum",o_negative_maximum)
        notnull_integer_validator("a_positive_maximum",a_positive_maximum)
        notnull_integer_validator("a_negative_maximum",a_negative_maximum)
        notnull_integer_validator("b_positive_maximum",b_positive_maximum)
        notnull_integer_validator("b_negative_maximum",b_negative_maximum)
        notnull_integer_validator("ab_positive_maximum",ab_positive_maximum)
        notnull_integer_validator("ab_negative_maximum",ab_negative_maximum)

        bigint_validator("contact_number",contact_number)

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
    aadhaar_id,
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
    gender,
    pregnancy_status,
    HIV,
    blood_type
    ):
    
    try:

        alpha_validator("first_name",first_name,30)
        alpha_validator("last_name",last_name,30)
        alpha_validator("street_name",street_name,50)
        alpha_validator("city",city,30)
        alpha_validator("district",district,30)
        alpha_validator("state",state,30)
        alpha_validator("country",country,30)
        alpha_validator("father_name",father_name,30)
        alpha_validator("mother_name",mother_name,30)
        alpha_validator("guardian_name",guardian_name,30)

        notnull_validator("country_code",country_code,3)

        notnull_validator("confirm_password",confirm_password,30,4)
        notnull_validator("new_password",new_password,30,4)

        notnull_integer_validator("hospital_ID",hospital_ID)
        notnull_integer_validator("date_of_birth",date_of_birth,2)
        notnull_integer_validator("month_of_birth",month_of_birth,2)
        notnull_integer_validator("year_of_birth",year_of_birth,4)

        notnull_integer_validator("phone_1",phone_1,10)
        notnull_integer_validator("phone_2",phone_2,10)
        notnull_integer_validator("aadhaar_id",aadhaar_id,12)

        if(new_password!=confirm_password):
            #error_popup("Passwords do not match")
            raise TypeError("Passwords do not match")
        
        # gender,
        # pregnancy_status,
        # HIV,
        # blood_type

        if pregnancy_status not in ["Yes","No"]:
            raise TypeError("Pregnancy Status must be Yes or No")
        elif (pregnancy_status=="Yes"):
            pregnancy_status=True
        else:
            pregnancy_status=False

        if HIV not in ["Positive","Negative"]:
            raise TypeError("HIV Status must be Positive or Negative")
        elif (HIV=="Positive"):
            HIV=True
        else:
            HIV=False
    
        donor_data = (  
                        aadhaar_id,
                        gender,
                        first_name,
                        last_name,
                        int(date_of_birth),
                        int(month_of_birth),
                        int(year_of_birth),
                        blood_type,
                        pregnancy_status,
                        HIV,
                        street_name,
                        city,
                        district,
                        state,
                        country,
                        country_code,
                        new_password,
                        father_name,
                        mother_name,
                        guardian_name,
                        int(phone_1),
                        int(phone_2),
                        int(hospital_ID),
                        
                        )
        
        insert_donor(donor_data)

        donor_root.destroy()
    
    except TypeError as e:
        error_popup(e)
        return


def admin_registration_validator(admin_root,admin_name,admin_id,password ):
    try:
        alpha_validator("admin_name",admin_name,50)
        notnull_integer_validator("admin_id",admin_id)
        alpha_validator("password",password,30)

        admin_data = (admin_name,admin_id,password)

        insert_admin(admin_data)

        admin_root.destroy()

    except TypeError as e:
        error_popup(e)
        return
    

#login validators

def donor_login_validator(donor_login_root,donor_id,password):
    try:
        notnull_integer_validator("donor_id",donor_id)
        notnull_validator("password",password,30)

        donor_existence_check(donor_id,password)
        donor_login_root.destroy()

    except TypeError as e:
        error_popup(e)
        return
    
def hospital_login_validator(hospital_login_root ,hospital_id,password):
    try:
        notnull_integer_validator("hospital_id",hospital_id)
        notnull_validator("password",password,30)

        hospital_existence_check(hospital_id,password)
        hospital_login_root.destroy()

    except TypeError as e:
        error_popup(e)
        return
    
def admin_login_validator(admin_login_root,admin_id,password):
    try:
        notnull_integer_validator("admin_id",admin_id)
        notnull_validator("password",password,30)

        admin_existence_check(admin_id,password)
        admin_login_root.destroy()
        
    except TypeError as e:
        error_popup(e)
        return
    
