import tkinter as tk

def enter_app(frame):
    frame.tkraise()

window = tk.Tk()
# Set the window title
window.title("Welcome Page")

# Set the window size to fullscreen


# Create a canvas widget to hold the background image
canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)

# Load the background image
background_image = tk.PhotoImage(file="Testing/blood-donation_new.png")

# Set the background image
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Create multiple frames for each page
donor_frame = tk.Frame(window)
donor_frame.pack(fill="both", expand=True)

hospital_frame = tk.Frame(window)
hospital_frame.pack(fill="both", expand=True)

admin_frame = tk.Frame(window)
admin_frame.pack(fill="both", expand=True)

# Create buttons in the welcome frame
donor_button = tk.Button(window, text="DONOR", command=lambda: enter_app(donor_frame), bg="red")
donor_button.place(relx=0.5, rely=0.5, anchor="center")

hospital_button = tk.Button(window, text="HOSPITAL", command=lambda: enter_app(hospital_frame), bg="green")
hospital_button.place(relx=0.5, rely=0.6, anchor="center")

admin_button = tk.Button(window, text="ADMIN", command=lambda: enter_app(admin_frame), bg="blue")
admin_button.place(relx=0.5, rely=0.7, anchor="center")

# Hide all frames initially
donor_frame.tkraise()
hospital_frame.pack_forget()
admin_frame.pack_forget()

# Start the Tkinter event loop
window.mainloop()
