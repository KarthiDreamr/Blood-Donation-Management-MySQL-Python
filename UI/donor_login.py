import tkinter as tk
import mysql.connector

def dlogin_submit():
    print("Hospital Login Submit")

root = tk.Tk()
root.geometry("300x300")
root.title("Donor Login Page")
root.iconbitmap("assets/blood-donation.ico")


# Defining the first row
lblfrstrow = tk.Label(root, text ="Enter Aadhaar ID", )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Enter Password")
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login", command = dlogin_submit)
submitbtn.place(x = 150, y = 135, width = 55)

root.mainloop()

