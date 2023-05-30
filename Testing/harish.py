import tkinter as tk

from tkinter import ttk

padding_xaxis = 10
padding_yaxis = 5
width_combobox = 17

window = tk.Tk()

window.title("Harish oru ")

frame = tk.Frame(window,padx=20, pady=20)

frame.grid()

First_name = ttk.Label(frame, text="First Name")
First_name.grid(row=0, column=0)

First_name_entry = ttk.Entry(frame)
First_name_entry.grid(row=0, column=1,padx= padding_xaxis,pady= padding_yaxis)

#row 4
Pregnancy_status = ttk.Label(frame, text="Pregnancy Status")
Pregnancy_status.grid(row=3, column=0)

Pregnancy_status = ttk.Combobox(frame, width = width_combobox, textvariable = tk.StringVar(), values=["Yes","No"] )
Pregnancy_status.grid(row=3, column=1,padx= padding_xaxis,pady= padding_yaxis)

window.mainloop()