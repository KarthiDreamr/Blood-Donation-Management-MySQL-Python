import tkinter as tk

def error_popup(message):

    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)
    root.destroy()