from DB.creation.db_creation import db_connection
from UI.dashboard.admin_dashboard import admin_dashboard_display

def admin_existence_check(admin_id,password):
    connection = db_connection()
    cursor = connection.cursor()

    #check if given admin_id and password  exists in admin table

    cursor.execute("SELECT * FROM admin WHERE admin_id = %s AND password = %s",(admin_id,password))
    result = cursor.fetchall()

    if(len(result) == 0):
        raise TypeError("Invalid Credentials")
    else:
        admin_dashboard_display()

