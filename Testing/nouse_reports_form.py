import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title("Reports Form")

# Create a frame to hold the widgets
frame = ttk.Frame(window, padding=10)
frame.grid()

# Create labels and entries for each column in the table

#row 1

width_combobox = 17
padding_xaxis = 10
padding_yaxis = 5

Date = ttk.Label(frame, text="Date")
Date.grid(row=0, column=0, sticky=tk.W)

Date_entry = ttk.Entry(frame)
Date_entry.grid(row=0, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

#row 2
time = ttk.Label(frame, text="Time")
time.grid(row=1, column=0, sticky=tk.W)

time_entry = ttk.Entry(frame)
time_entry.grid(row=1, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

#row 3
units_donated = ttk.Label(frame, text="Units Donated")
units_donated.grid(row=2, column=0, sticky=tk.W)

units_donated_entry = ttk.Entry(frame)
units_donated_entry.grid(row=2, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

#row 4
hospital_id = ttk.Label(frame, text="Hospital ID")
hospital_id.grid(row=3, column=0, sticky=tk.W)

hospital_id_entry = ttk.Combobox(frame, width = width_combobox, textvariable = tk.StringVar())
hospital_id_entry.grid(row=3, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

#row 5
aadhaar_id = ttk.Label(frame, text="Aadhaar ID")
aadhaar_id.grid(row=4, column=0, sticky=tk.W)

aadhaar_id_entry = ttk.Entry(frame)
aadhaar_id_entry.grid(row=4, column=1, sticky=tk.W,padx= padding_xaxis,pady= padding_yaxis)

# Create a button to submit the form
btn = ttk.Button(frame, text="Submit")

# Start the main loop
window.mainloop()
