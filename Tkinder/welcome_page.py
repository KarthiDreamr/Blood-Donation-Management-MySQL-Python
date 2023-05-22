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



import tkinter as tk

def enter_app():
    # Function to handle the button click event
    # Add your code to proceed to the main application here
    print("Entering the main application...")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Welcome Page")

# Set the window size to fullscreen


# Create a canvas widget to hold the background image
canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)

# Load the background image
background_image = tk.PhotoImage(file="Tkinder/picture.png")

# Set the background image
canvas.create_image(0, 0, anchor="nw", image=background_image)

# Create a label widget with a welcome message
label = tk.Label(window, text="BLOOD DONATION MANAGEMENT SYSTEM", font=("Helvetica", 24))
label.place(relx=0.1, rely=0.4, anchor="n")

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.place(relx=0.5, rely=0.6, anchor="center")

# Create the buttons within the frame
donor = tk.Button(button_frame, text="DONOR", command=enter_app, bg="red")
donor.pack(side="top", pady=10)

hospital = tk.Button(button_frame, text="HOSPITAL", command=enter_app, bg="green")
hospital.pack(side="top", pady=10)

admin = tk.Button(button_frame, text="ADMIN", command=enter_app, bg="blue")
admin.pack(side="top", pady=10)

# Start the Tkinter event loop
window.mainloop()
