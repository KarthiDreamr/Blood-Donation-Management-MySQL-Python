import tkinter as tk
from tkinter import ttk

from form_validation.donor_validation.runtime_validation import atmost_twenty_char_onlyalpha_ensure, atleast_twelve_digit_ensure, date_of_birth_ensure, atmost_fifty_char_ensure, atmost_thirty_char_ensure, atmost_twenty_char_ensure, atmost_plus_three_char_ensure, atmost_thirty_char_onlyalpha_ensure, atleast_ten_digit_ensure, isdigit_ensure, atmost_thirtychar_ensure
# from form_validation.donor_validation.complete_validation import *

# Create a window
root = tk.Tk()
root.iconbitmap("assets/blood-donation.ico")

print(root.winfo_reqwidth(), root.winfo_reqheight() )
print(root.winfo_screenwidth(), root.winfo_screenheight() )

# root.resizable(False, False)  # This code helps to disable windows from resizing

root.geometry("618x450+500+150")
root.title("Donor Form")

width = 771
height = 600

# Create a frame to hold the widgets
# frame = tk.Frame(root, bg='grey', width = 500, height=50,padx=20, pady=20)
donor_frame = tk.Frame(root,padx=20, pady=15,width=500,height=500)

# Create labels and l̥entries for eal̥ch column in the table

#row 1
width_combobox = 17
padding_xaxis = 10
padding_yaxis = 5

first_name = ttk.Label(donor_frame, text="First Name")
first_name.grid(row=0, column=0, sticky=tk.W)

first_name_entry = ttk.Entry(donor_frame)
first_name_entry.grid(row=0, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)



atmost_twenty_char_onlyalpha_validator = (donor_frame.register(atmost_twenty_char_onlyalpha_ensure), "%P")

first_name_entry.configure(validate="key", validatecommand=atmost_twenty_char_onlyalpha_validator)


last_name = ttk.Label(donor_frame, text="Last Name")
last_name.grid(row=0, column=2, sticky=tk.W,padx=(padding_xaxis,0))

last_name_entry = ttk.Entry(donor_frame)
last_name_entry.grid(row=0, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

last_name_entry.configure(validate="key", validatecommand=atmost_twenty_char_onlyalpha_validator)

#row 2
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


#row 3
Date_of_birth = ttk.Label(donor_frame, text="Date of Birth (DD/MM/YYYY)")
Date_of_birth.grid(row=2, column=0, sticky=tk.W)

Date_of_birth_entry = ttk.Entry(donor_frame)
Date_of_birth_entry.grid(row=2, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)



date_of_birth_validate = (donor_frame.register(date_of_birth_ensure), "%P")

Date_of_birth_entry.configure(validate="key", validatecommand=date_of_birth_validate)


Blood_type = ttk.Label(donor_frame, text="Blood Type")
Blood_type.grid(row=2, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Blood_type = ttk.Combobox(donor_frame, width = width_combobox, textvariable = tk.StringVar(), values=["A+","A-","B+","B-","AB+","AB-","O+","O-"])
Blood_type.grid(row=2, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


#row 4
Pregnancy_status = ttk.Label(donor_frame, text="Pregnancy Status")
Pregnancy_status.grid(row=3, column=0, sticky=tk.W)

Pregnancy_status = ttk.Combobox(donor_frame, width = width_combobox, textvariable = tk.StringVar(), values=["Yes","No"])
Pregnancy_status.grid(row=3, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


HIV_status = ttk.Label(donor_frame, text="HIV Status")
HIV_status.grid(row=3, column=2, sticky=tk.W,padx=(padding_xaxis,0))

HIV_status = ttk.Combobox(donor_frame, width = width_combobox, textvariable = tk.StringVar(), values=["Positive","Negative"])
HIV_status.grid(row=3, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


#row 5
Street_name = ttk.Label(donor_frame, text="Street Name")
Street_name.grid(row=4, column=0, sticky=tk.W)

Street_name_entry = ttk.Entry(donor_frame)
Street_name_entry.grid(row=4, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)



street_address_validator = (donor_frame.register(atmost_fifty_char_ensure), "%P")

Street_name_entry.configure(validate="key", validatecommand=street_address_validator)


City = ttk.Label(donor_frame, text="City")
City.grid(row=4, column=2, sticky=tk.W,padx=(padding_xaxis,0))

City_entry = ttk.Entry(donor_frame)
City_entry.grid(row=4, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)



atmost_thirty_char_ensure_validator = (donor_frame.register(atmost_thirty_char_ensure), "%P")

City_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validator)


#row 6
District = ttk.Label(donor_frame, text="District")
District.grid(row=5, column=0, sticky=tk.W)

District_entry = ttk.Entry(donor_frame)
District_entry.grid(row=5, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

District_entry.configure(validate="key",validatecommand=atmost_thirty_char_ensure_validator)

State = ttk.Label(donor_frame, text="State")
State.grid(row=5, column=2, sticky=tk.W,padx=(padding_xaxis,0))

State_entry = ttk.Entry(donor_frame)
State_entry.grid(row=5, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

State_entry.configure(validate="key",validatecommand=atmost_thirty_char_ensure_validator)

#row 7
Country = ttk.Label(donor_frame, text="Country")
Country.grid(row=6, column=0, sticky=tk.W)

Country_entry = ttk.Entry(donor_frame)
Country_entry.grid(row=6, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


atmost_twenty_char_ensure_validator = (donor_frame.register(atmost_twenty_char_ensure), "%P")

Country_entry.configure(validate="key",validatecommand=atmost_twenty_char_ensure_validator)

Country_code = ttk.Label(donor_frame,text="Country Code (ex: +91)")
Country_code.grid(row=6, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Country_code_entry = ttk.Entry(donor_frame)
Country_code_entry.grid(row=6, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)



atmost_plus_three_char_ensure_validator = (donor_frame.register(atmost_plus_three_char_ensure), "%P")

Country_code_entry.configure(validate="key",validatecommand=atmost_plus_three_char_ensure_validator)


#row 8
Father_name = ttk.Label(donor_frame, text="Father Name")
Father_name.grid(row=7, column=0, sticky=tk.W)

Father_name_entry = ttk.Entry(donor_frame)
Father_name_entry.grid(row=7, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)



atmost_thirty_char__onlyalpha_ensure_validator = (donor_frame.register(atmost_thirty_char_onlyalpha_ensure), "%P")

Father_name_entry.configure(validate="key", validatecommand=atmost_thirty_char__onlyalpha_ensure_validator)


Mother_name = ttk.Label(donor_frame, text="Mother Name")
Mother_name.grid(row=7, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Mother_name_entry = ttk.Entry(donor_frame)
Mother_name_entry.grid(row=7, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Mother_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validator)


#row 9
Guardian_name = ttk.Label(donor_frame, text="Guardian Name")
Guardian_name.grid(row=8, column=0, sticky=tk.W)

Guardian_name_entry = ttk.Entry(donor_frame)
Guardian_name_entry.grid(row=8, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)

Guardian_name_entry.configure(validate="key", validatecommand=atmost_thirty_char_ensure_validator)


#row 10
Phone_1 = ttk.Label(donor_frame, text="Phone 1")
Phone_1.grid(row=9, column=0, sticky=tk.W)

Phone_1_entry = ttk.Entry(donor_frame)
Phone_1_entry.grid(row=9, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)



atleast_ten_digit_ensure_validate = (donor_frame.register(atleast_ten_digit_ensure), "%P")

Phone_1_entry.configure(validate="key", validatecommand=atleast_ten_digit_ensure_validate)


Phone_2 = ttk.Label(donor_frame, text="Phone 2")
Phone_2.grid(row=9, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Phone_2_entry = ttk.Entry(donor_frame)
Phone_2_entry.grid(row=9, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Phone_2_entry.configure(validate="key", validatecommand=atleast_ten_digit_ensure_validate)

#row 11
Hospital_ID = ttk.Label(donor_frame, text="Hospital ID")
Hospital_ID.grid(row=10, column=0, sticky=tk.W)

Hospital_ID_entry = ttk.Entry(donor_frame)
Hospital_ID_entry.grid(row=10, column=1, sticky=tk.W ,padx= padding_xaxis,pady= padding_yaxis)


isdigit_ensure_validate = (donor_frame.register(isdigit_ensure), "%P")

Hospital_ID_entry.configure(validate="key", validatecommand=isdigit_ensure_validate)

#row 12
New_Password = ttk.Label(donor_frame, text="New Password")
New_Password.grid(row=11, column=0, sticky=tk.W)

New_Password_entry = ttk.Entry(donor_frame)
New_Password_entry.grid(row=11, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)


atmost_thirtychar_ensure_validate = (donor_frame.register(atmost_thirtychar_ensure), "%P")

New_Password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)


Password = ttk.Label(donor_frame, text="Confirm Password")
Password.grid(row=11, column=2, sticky=tk.W,padx=(padding_xaxis,0))

Password_entry = ttk.Entry(donor_frame)
Password_entry.grid(row=11, column=3, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

Password_entry.configure(validate="key", validatecommand=atmost_thirtychar_ensure_validate)


# Create a button to submit the form

# back_button = tk.Button(donor_frame, text="back", command=lambda: root.destroy()) 
# back_button.grid(row=12, column=0, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

# # submit_button = ttk.Button(donor_frame,text="Submit",command=form_validator)
# submit_button = ttk.Button(donor_frame,text="Submit")
# submit_button.grid(row=12, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)
# # btn.grid(row=12, column=1, sticky=tk.W,pady= (0,20),padx=(230,220))


donor_frame.grid()

# Start the main loop
root.mainloop() 