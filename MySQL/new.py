import tkinter as tk
import mysql.connector

def save_to_database():
    # Function to handle saving the value to the database
    value = entry.get()  # Get the value from the entry widget

    # Establish a connection to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dhanesh",
        database="donation"
    )
    cursor = conn.cursor()

    # Execute the SQL query to insert the value into the database
    query = "INSERT INTO customers () VALUES (%s)"
    data = (value,)
    cursor.execute(query, data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Value saved to the database successfully.")

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Save to Database")

# Create an entry widget to get a value
entry = tk.Entry(window)
entry.pack(pady=10)

# Create a button widget to save the value to the database
save_button = tk.Button(window, text="Save", command=save_to_database)
save_button.pack()

# Start the Tkinter event loop
window.mainloop()
