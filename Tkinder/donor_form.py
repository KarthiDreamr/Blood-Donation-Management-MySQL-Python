import tkinter as tk
from tkinter import ttk

from form_validation.runtime_validation import *
from form_validation.complete_validation import *

# Create a window
donor_root = tk.Tk()
donor_root.iconbitmap("assets/blood-donation.ico")

donor_root.title("Donor Form")

# Center the window on the screen
# window_width = donor_root.winfo_width()
# window_height = donor_root.winfo_height()
# screen_width = donor_root.winfo_screenwidth()
# screen_height = donor_root.winfo_screenheight()
# x_coordinate = int((screen_width/2) - (window_width/2))
# y_coordinate = int((screen_height/2) - (window_height/2))
# donor_root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

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



atmost_twenty_char_onlyalpha_validator = (donor_frame.register(atmost_thirty_char_onlyalpha_ensure), "%P")

first_name_entry.configure(validate="key", validatecommand=atmost_twenty_char_onlyalpha_validator)


last_name = ttk.Label(donor_frame, text="Last Name")
last_name.grid(row=0, column=2, sticky=tk.W,padx=(padding_xaxis,0))

last_name_entry = ttk.Entry(donor_frame)
last_name_entry.grid(row=0, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

last_name_entry.configure(validate="key", validatecommand=atmost_twenty_char_onlyalpha_validator)

#row 1
adhaar_id = ttk.Label(donor_frame, text="Aadhaar ID")
adhaar_id.grid(row=1, column=0, sticky=tk.W)

adhaar_id_entry = ttk.Entry(donor_frame)
adhaar_id_entry.grid(row=1, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)



atleast_twelve_digit_ensure_validate = (donor_frame.register(atleast_twelve_digit_ensure), "%P")

adhaar_id_entry.configure(validate="key", validatecommand=atleast_twelve_digit_ensure_validate)


gender = ttk.Label(donor_frame,text="Gender")
gender.grid(row=1, column=2, sticky=tk.W,padx=(padding_xaxis,0))

# Create a list of gender options
gender_options = ["Male", "Female", "Nonbinary", "Other"]

# Create a combobox with the gender_options as values
gender = ttk.Combobox(donor_frame, width=width_combobox, textvariable=tk.StringVar(), values=gender_options)
gender.grid(row=1, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


#row 2
date_of_birth = ttk.Label(donor_frame, text="Date of Birth (DD)")
date_of_birth.grid(row=2, column=0, sticky=tk.W)

date_of_birth_entry = ttk.Entry(donor_frame)
date_of_birth_entry.grid(row=2, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


month_of_birth = ttk.Label(donor_frame, text="Month of Birth (MM)")
month_of_birth.grid(row=2, column=2, sticky=tk.W,padx=(padding_xaxis,0))

month_of_birth_entry = ttk.Entry(donor_frame)
month_of_birth_entry.grid(row=2, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

#row 3
year_of_birth = ttk.Label(donor_frame, text="Year of Birth (YYYY)")
year_of_birth.grid(row=3, column=0, sticky=tk.W)

year_of_birth_entry = ttk.Entry(donor_frame)
year_of_birth_entry.grid(row=3, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


Blood_type = ttk.Label(donor_frame, text="Blood Type")
Blood_type.grid(row=3, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Blood_type = ttk.Combobox(donor_frame, width = width_combobox, textvariable = tk.StringVar(), values=["A+","A-","B+","B-","AB+","AB-","O+","O-"])
Blood_type.grid(row=3, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

#row 4
Pregnancy_status = ttk.Label(donor_frame, text="Pregnancy Status")
Pregnancy_status.grid(row=4, column=0, sticky=tk.W)

Pregnancy_status = ttk.Combobox(donor_frame, width = width_combobox, textvariable = tk.StringVar(), values=["Yes","No"])
Pregnancy_status.grid(row=4, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


HIV_status = ttk.Label(donor_frame, text="HIV Status")
HIV_status.grid(row=4, column=2, sticky=tk.W,padx=(padding_xaxis,0))

HIV_status = ttk.Combobox(donor_frame, width = width_combobox, textvariable = tk.StringVar(), values=["Positive","Negative"])
HIV_status.grid(row=4, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

#row 5

Street_name = ttk.Label(donor_frame, text="Street Name")
Street_name.grid(row=5, column=0, sticky=tk.W)

Street_name_entry = ttk.Entry(donor_frame)
Street_name_entry.grid(row=5, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)


street_address_validator = (donor_frame.register(atmost_fifty_char_ensure), "%P")
Street_name_entry.configure(validate="key", validatecommand=street_address_validator)


City = ttk.Label(donor_frame, text="City")
City.grid(row=5, column=2, sticky=tk.W,padx=(padding_xaxis,0))

City_entry = ttk.Entry(donor_frame)
City_entry.grid(row=5, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

atmost_thirty_char_ensure_validate = (donor_frame.register(atmost_thirty_char_ensure), "%P")

City_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validate)

#row 6
District = ttk.Label(donor_frame, text="District")
District.grid(row=6, column=0, sticky=tk.W)

District_entry = ttk.Entry(donor_frame)
District_entry.grid(row=6, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)

District_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validate)

State = ttk.Label(donor_frame, text="State")
State.grid(row=6, column=2, sticky=tk.W,padx=(padding_xaxis,0))


State_entry = ttk.Entry(donor_frame)
State_entry.grid(row=6, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

State_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validate)

#row 7
Country = ttk.Label(donor_frame, text="Country")
Country.grid(row=7, column=0, sticky=tk.W)

Country_entry = ttk.Entry(donor_frame)
Country_entry.grid(row=7, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)


atmost_twenty_char_ensure_validator = (donor_frame.register(atmost_twenty_char_ensure), "%P")

Country_entry.configure(validate="key",validatecommand=atmost_twenty_char_ensure_validator)

Country_code = ttk.Label(donor_frame,text="Country Code (ex: +91)")
Country_code.grid(row=7, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Country_code_entry = ttk.Entry(donor_frame)
Country_code_entry.grid(row=7, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


atmost_plus_three_char_ensure_validator = (donor_frame.register(atmost_plus_three_char_ensure), "%P")

Country_code_entry.configure(validate="key",validatecommand=atmost_plus_three_char_ensure_validator)


#row 8
Father_name = ttk.Label(donor_frame, text="Father Name")
Father_name.grid(row=8, column=0, sticky=tk.W)

Father_name_entry = ttk.Entry(donor_frame)
Father_name_entry.grid(row=8, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)


atmost_thirty_char__onlyalpha_ensure_validator = (donor_frame.register(atmost_thirty_char_onlyalpha_ensure), "%P")

Father_name_entry.configure(validate="key", validatecommand=atmost_thirty_char__onlyalpha_ensure_validator)


Mother_name = ttk.Label(donor_frame, text="Mother Name")
Mother_name.grid(row=8, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Mother_name_entry = ttk.Entry(donor_frame)
Mother_name_entry.grid(row=8, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Mother_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validate)


#row 9
Guardian_name = ttk.Label(donor_frame, text="Guardian Name")
Guardian_name.grid(row=9, column=0, sticky=tk.W)

Guardian_name_entry = ttk.Entry(donor_frame)
Guardian_name_entry.grid(row=9, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)

Guardian_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validate)


#row 10
Phone_1 = ttk.Label(donor_frame, text="Phone 1")
Phone_1.grid(row=10, column=0, sticky=tk.W)

Phone_1_entry = ttk.Entry(donor_frame)
Phone_1_entry.grid(row=10, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)



atleast_ten_digit_ensure_validate = (donor_frame.register(atleast_ten_digit_ensure), "%P")

Phone_1_entry.configure(validate="key", validatecommand=atleast_ten_digit_ensure_validate)


Phone_2 = ttk.Label(donor_frame, text="Phone 2")
Phone_2.grid(row=10, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Phone_2_entry = ttk.Entry(donor_frame)
Phone_2_entry.grid(row=10, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Phone_2_entry.configure(validate="key", validatecommand=atleast_ten_digit_ensure_validate)

#row 11
Hospital_ID = ttk.Label(donor_frame, text="Hospital ID")
Hospital_ID.grid(row=11, column=0, sticky=tk.W)

Hospital_ID_entry = ttk.Entry(donor_frame)
Hospital_ID_entry.grid(row=11, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)


isdigit_ensure_validate = (donor_frame.register(isdigit_ensure), "%P")

Hospital_ID_entry.configure(validate="key", validatecommand=isdigit_ensure_validate)

#row 12
New_Password = ttk.Label(donor_frame, text="New Password")
New_Password.grid(row=12, column=0, sticky=tk.W)

New_Password_entry = ttk.Entry(donor_frame)
New_Password_entry.grid(row=12, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


atmost_thirtychar_ensure_validate = (donor_frame.register(atmost_thirty_char_ensure), "%P")

New_Password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)


Password = ttk.Label(donor_frame, text="Confirm Password")
Password.grid(row=12, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Password_entry = ttk.Entry(donor_frame)
Password_entry.grid(row=12, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)


# Create a button to submit the form

back_button = tk.Button(donor_frame, text="back", command=lambda: donor_root.destroy()) 
back_button.grid(row=13, column=0, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

submit_button = ttk.Button(donor_frame,text="Submit")
submit_button = ttk.Button(donor_frame,text="Submit",command=lambda: donor_form_validator(
    first_name_entry.get(),
    last_name_entry.get(),
    adhaar_id_entry.get(),
    date_of_birth_entry.get(),
    month_of_birth_entry.get(),
    year_of_birth_entry.get(),
    Street_name_entry.get(),
    City_entry.get(),
    District_entry.get(),
    State_entry.get(),
    Country_entry.get(),
    Country_code_entry.get(),
    Father_name_entry.get(),
    Mother_name_entry.get(),
    Guardian_name_entry.get(),
    Phone_1_entry.get(),
    Phone_2_entry.get(),
    Hospital_ID_entry.get(),
    New_Password_entry.get(),
    Password_entry.get()
) )

submit_button.grid(row=13, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

# Start the main loop
donor_root.mainloop() 

donor_frame.mainloop()