from DB.creation.db_creation import db_connection

def donor_existence_check(donor_id,password):
    cursor = db_connection().cursor()

    #check if given donor_id and password  exists in donor table

    cursor.execute("SELECT * FROM donor WHERE donor_id = %s AND password = %s",(donor_id,password))
    result = cursor.fetchall()
    if(len(result) == 0):
        raise TypeError("Invalid Credentials")
    else:
        return True