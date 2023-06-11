import tkinter as tk
from tkinter import ttk

from UI.form.form_validation.runtime_validation import *
from UI.form.form_validation.complete_validation import *

def donor_form_display():

    # Create a window
    donor_root = tk.Tk()
    donor_root.iconbitmap("assets/blood-donation.ico")

    donor_root.title("Donor Form")

    donor_frame = tk.Frame(donor_root, padx=10, pady=10)
    donor_frame.grid()

    #row 0
    width_combobox = 17
    padding_xaxis = 10
    padding_yaxis = 5

    first_name = ttk.Label(donor_frame, text="First Name")
    first_name.grid(row=0, column=0, sticky=tk.W)

    first_name_entry = ttk.Entry(donor_frame)
    first_name_entry.grid(row=0, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    atmost_twenty_char_onlyalpha_ensure_validator = (donor_frame.register(atmost_thirty_char_onlyalpha_ensure), "%P")

    first_name_entry.configure(validate="key", validatecommand=atmost_twenty_char_onlyalpha_ensure_validator)


    last_name = ttk.Label(donor_frame, text="Last Name")
    last_name.grid(row=0, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    last_name_entry = ttk.Entry(donor_frame)
    last_name_entry.grid(row=0, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    last_name_entry.configure(validate="key", validatecommand=atmost_twenty_char_onlyalpha_ensure_validator)

    #row 1
    aadhaar_id = ttk.Label(donor_frame, text="Aadhaar ID")
    aadhaar_id.grid(row=1, column=0, sticky=tk.W)

    aadhaar_id_entry = ttk.Entry(donor_frame)
    aadhaar_id_entry.grid(row=1, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


    atleast_twelve_digit_ensure_validate = (donor_frame.register(atmost_twelve_digit_ensure), "%P")

    aadhaar_id_entry.configure(validate="key", validatecommand=atleast_twelve_digit_ensure_validate)


    gender = ttk.Label(donor_frame,text="Gender")
    gender.grid(row=1, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    # Create a list of gender options
    gender_options = ["Male", "Female", "Nonbinary", "Other"]

    # Create a combobox with the gender_options as values
    gender = ttk.Combobox(donor_frame, width=width_combobox, textvariable=tk.StringVar(), values=gender_options, state="readonly")
    gender.current(0)
    gender.grid(row=1, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


    #row 2
    date_of_birth = ttk.Label(donor_frame, text="Date of Birth (DD)")
    date_of_birth.grid(row=2, column=0, sticky=tk.W)

    date_of_birth_entry = ttk.Entry(donor_frame)
    date_of_birth_entry.grid(row=2, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    date_of_birth_ensure_validate = (donor_frame.register(date_of_birth_ensure), "%P")
    date_of_birth_entry.configure(validate="key", validatecommand= date_of_birth_ensure_validate)


    month_of_birth = ttk.Label(donor_frame, text="Month of Birth (MM)")
    month_of_birth.grid(row=2, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    month_of_birth_entry = ttk.Entry(donor_frame)
    month_of_birth_entry.grid(row=2, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    month_of_birth_ensure_validate = (donor_frame.register(month_of_birth_ensure), "%P")
    month_of_birth_entry.configure(validate="key", validatecommand= month_of_birth_ensure_validate)

    #row 3
    year_of_birth = ttk.Label(donor_frame, text="Year of Birth (YYYY)")
    year_of_birth.grid(row=3, column=0, sticky=tk.W)

    year_of_birth_entry = ttk.Entry(donor_frame)
    year_of_birth_entry.grid(row=3, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    year_of_birth_ensure_validate = (donor_frame.register(year_of_birth_ensure), "%P")
    year_of_birth_entry.configure(validate="key", validatecommand= year_of_birth_ensure_validate)


    blood_type = ttk.Label(donor_frame, text="Blood Type")
    blood_type.grid(row=3, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    blood_type = ttk.Combobox(donor_frame, width = width_combobox, textvariable = tk.StringVar(), values=["A+","A-","B+","B-","AB+","AB-","O+","O-"], state="readonly")
    blood_type.grid(row=3, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    #row 4
    pregnancy_status = ttk.Label(donor_frame, text="Pregnancy Status")
    pregnancy_status.grid(row=4, column=0, sticky=tk.W)

    pregnancy_status = ttk.Combobox(donor_frame, width = width_combobox, textvariable = tk.StringVar(), values=["Yes","No"], state="readonly")
    pregnancy_status.grid(row=4, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


    HIV_status = ttk.Label(donor_frame, text="HIV Status")
    HIV_status.grid(row=4, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    HIV_status = ttk.Combobox(donor_frame, width = width_combobox, textvariable = tk.StringVar(), values=["Positive","Negative"], state="readonly")
    HIV_status.grid(row=4, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    #row 5
    street_name = ttk.Label(donor_frame, text="Street Name")
    street_name.grid(row=5, column=0, sticky=tk.W)

    Street_name_entry = ttk.Entry(donor_frame)
    Street_name_entry.grid(row=5, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)


    atmost_fifty_char_ensure_validator = (donor_frame.register(atmost_fifty_char_ensure), "%P")
    Street_name_entry.configure(validate="key", validatecommand=atmost_fifty_char_ensure_validator)


    city = ttk.Label(donor_frame, text="City")
    city.grid(row=5, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    city_entry = ttk.Entry(donor_frame)
    city_entry.grid(row=5, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    atmost_thirty_char_onlyalpha_ensure_validate = (donor_frame.register(atmost_thirty_char_onlyalpha_ensure), "%P")

    city_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validate)

    #row 6
    district = ttk.Label(donor_frame, text="District")
    district.grid(row=6, column=0, sticky=tk.W)

    district_entry = ttk.Entry(donor_frame)
    district_entry.grid(row=6, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)

    district_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validate)

    state = ttk.Label(donor_frame, text="State")
    state.grid(row=6, column=2, sticky=tk.W,padx=(padding_xaxis,0))


    state_entry = ttk.Entry(donor_frame)
    state_entry.grid(row=6, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    state_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validate)

    #row 7
    country = ttk.Label(donor_frame, text="Country")
    country.grid(row=7, column=0, sticky=tk.W)

    country_entry = ttk.Entry(donor_frame)
    country_entry.grid(row=7, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)


    atmost_twenty_char_ensure_validator = (donor_frame.register(atmost_thirty_char_onlyalpha_ensure), "%P")

    country_entry.configure(validate="key",validatecommand=atmost_twenty_char_ensure_validator)

    country_code = ttk.Label(donor_frame,text="Country Code (ex: +91)")
    country_code.grid(row=7, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    country_code_entry = ttk.Entry(donor_frame)
    country_code_entry.grid(row=7, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


    atmost_plus_three_char_ensure_validator = (donor_frame.register(atmost_plus_three_char_ensure), "%P")

    country_code_entry.configure(validate="key",validatecommand=atmost_plus_three_char_ensure_validator)


    #row 8
    father_name = ttk.Label(donor_frame, text="Father Name")
    father_name.grid(row=8, column=0, sticky=tk.W)

    father_name_entry = ttk.Entry(donor_frame)
    father_name_entry.grid(row=8, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)


    atmost_thirty_char__onlyalpha_ensure_validator = (donor_frame.register(atmost_thirty_char_onlyalpha_ensure), "%P")

    father_name_entry.configure(validate="key", validatecommand=atmost_thirty_char__onlyalpha_ensure_validator)


    mother_name = ttk.Label(donor_frame, text="Mother Name")
    mother_name.grid(row=8, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    mother_name_entry = ttk.Entry(donor_frame)
    mother_name_entry.grid(row=8, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    mother_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validate)


    #row 9
    guardian_name = ttk.Label(donor_frame, text="Guardian Name")
    guardian_name.grid(row=9, column=0, sticky=tk.W)

    guardian_name_entry = ttk.Entry(donor_frame)
    guardian_name_entry.grid(row=9, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)

    guardian_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_onlyalpha_ensure_validate)


    #row 10
    phone_1 = ttk.Label(donor_frame, text="Phone 1")
    phone_1.grid(row=10, column=0, sticky=tk.W)

    phone_1_entry = ttk.Entry(donor_frame)
    phone_1_entry.grid(row=10, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)



    atleast_ten_digit_ensure_validate = (donor_frame.register(atmost_ten_digit_ensure), "%P")

    phone_1_entry.configure(validate="key", validatecommand=atleast_ten_digit_ensure_validate)


    phone_2 = ttk.Label(donor_frame, text="Phone 2")
    phone_2.grid(row=10, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    phone_2_entry = ttk.Entry(donor_frame)
    phone_2_entry.grid(row=10, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    phone_2_entry.configure(validate="key", validatecommand=atleast_ten_digit_ensure_validate)

    #row 11
    hospital_ID = ttk.Label(donor_frame, text="Hospital ID")
    hospital_ID.grid(row=11, column=0, sticky=tk.W)

    hospital_ID_entry = ttk.Entry(donor_frame)
    hospital_ID_entry.grid(row=11, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)


    isdigit_ensure_validate = (donor_frame.register(digit_ensure), "%P")

    hospital_ID_entry.configure(validate="key", validatecommand=isdigit_ensure_validate)

    #row 12
    new_password = ttk.Label(donor_frame, text="New Password")
    new_password.grid(row=12, column=0, sticky=tk.W)

    new_password_entry = ttk.Entry(donor_frame)
    new_password_entry.grid(row=12, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


    atmost_thirtychar_ensure_validate = (donor_frame.register(atmost_thirty_char_ensure), "%P")

    new_password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)
    new_password_entry.configure(show="*")


    confirm_password = ttk.Label(donor_frame, text="Confirm Password")
    confirm_password.grid(row=12, column=2, sticky=tk.W,padx=(padding_xaxis,0))

    confirm_password_entry = ttk.Entry(donor_frame)
    confirm_password_entry.grid(row=12, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    confirm_password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)
    confirm_password_entry.configure(show="*")

    # Create a button to submit the form

    back_button = tk.Button(donor_frame, text="back", command=lambda: donor_root.destroy()) 
    back_button.grid(row=13, column=0, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    submit_button = ttk.Button(donor_frame,text="Submit")
    submit_button = ttk.Button(donor_frame,text="Submit",command=lambda: donor_registration_validator(
        donor_root,
        first_name_entry.get(),
        last_name_entry.get(),
        aadhaar_id_entry.get(),
        date_of_birth_entry.get(),
        month_of_birth_entry.get(),
        year_of_birth_entry.get(),
        Street_name_entry.get(),
        city_entry.get(),
        district_entry.get(),
        state_entry.get(),
        country_entry.get(),
        country_code_entry.get(),
        father_name_entry.get(),
        mother_name_entry.get(),
        guardian_name_entry.get(),
        phone_1_entry.get(),
        phone_2_entry.get(),
        hospital_ID_entry.get(),
        new_password_entry.get(),
        confirm_password_entry.get()
    ) )

    submit_button.grid(row=13, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

    # Start the main loop
    donor_root.mainloop() 

    donor_frame.mainloop()