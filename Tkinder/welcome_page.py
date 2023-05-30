import tkinter as tk

# def enter_app():
#     # Function to handle the button click event
#     # Add your code to proceed to the main application here
#     print("Entering the main application...")
def enter_app():
    # Your code for handling button clicks goes here
    # You can switch frames or perform any other action based on the button clicked
    pass

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
# Create the main window
window = tk.Tk()

# Set the window title
window.title("Welcome Page")

# Set the window size to fullscreen


# Create a canvas widget to hold the background image
canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)

# Load the background image
background_image = tk.PhotoImage(file="Tkinder/blood-donation_new.png")

# Set the background image
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Create a label widget with a welcome message
label = tk.Label(window, text="BLOOD DONATION MANAGEMENT SYSTEM", font=("Helvetica", 30), bg="white",padx=4)
label.place(relx=0.5, rely=0.1, anchor="n")


# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.place(relx=0.5, rely=0.6, anchor="center")

# Create the buttons within the frame
donor = tk.Button(button_frame, text="DONOR", command=enter_app, bg="red", width=10, height=2)
donor.pack(side="top", padx=10, pady=10)

hospital = tk.Button(button_frame, text="HOSPITAL", command=enter_app, bg="lightgreen",width=10, height=2)
hospital.pack(side="top",padx=10, pady=10)

admin = tk.Button(button_frame, text="ADMIN", command=enter_app, bg="orange",width=10, height=2)
admin.pack(side="top", padx=10,pady=10)

root = tk.Tk()

# Create multiple frames for each page
button_frame = tk.Frame(root)
button_frame.pack()

donor_frame = tk.Frame(root)
donor_frame.pack()

hospital_frame = tk.Frame(root)
hospital_frame.pack()

admin_frame = tk.Frame(root)
admin_frame.pack()

# Create buttons in the button frame
donor_button = tk.Button(button_frame, text="DONOR", command=lambda: show_frame(donor_frame), bg="red")
donor_button.pack(side="top", padx=10, pady=10)

hospital_button = tk.Button(button_frame, text="HOSPITAL", command=lambda: show_frame(hospital_frame), bg="green")
hospital_button.pack(side="top", padx=10, pady=10)

admin_button = tk.Button(button_frame, text="ADMIN", command=lambda: show_frame(admin_frame), bg="blue")
admin_button.pack(side="top", padx=10, pady=10)

# Hide all frames initially
donor_frame.grid(row=0, column=0, sticky="nsew")
hospital_frame.grid(row=0, column=0, sticky="nsew")
admin_frame.grid(row=0, column=0, sticky="nsew")

# Raise the button frame initially
show_frame(button_frame)

root.mainloop()











window.mainloop()








# import tkinter as tk
# def enter_app():
#     # Function to handle the button click event
#     # Add your code to proceed to the main application here
#     print("Entering the main application...")

# # Create the main window
# window = tk.Tk()

# # Set the window title
# window.title("Welcome Page")

# # Set the window size
# window.geometry("8000x5000")

# # Create a canvas widget to hold the background image
# canvas = tk.Canvas(window, width=600, height=400)
# canvas.pack()

# # Load the background image
# background_image = tk.PhotoImage(file="pict.png")

# # Set the background image
# canvas.create_image(0, 0, anchor="nw", image=background_image)

# # Create a label widget with a welcome message
# label = tk.Label(window, text="BLOOD DONATION MANAGEMENT SYSTEM", font=("Helvetica", 24))
# label.place(relx=0.5, rely=0.4, anchor="center")

# # Create a button widget to enter the application
# donor= tk.Button(window, text="DONOR", command=enter_app)
# donor.place(relx=0.5, rely=0.6, anchor="center")
# hospital= tk.Button(window, text="HOSPITAL",command=enter_app)
# hospital.place(relx=0.7, rely=0.8, anchor="center")
# admin= tk.Button(window, text="ADMIN",command=enter_app)
# admin.place(relx=0.9, rely=1.0, anchor="center")


# # Start the Tkinter event loop
# window.mainloop()

