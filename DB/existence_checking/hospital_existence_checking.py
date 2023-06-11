from DB.creation.db_creation import db_connection

def hospital_existence_check(hospital_id,password):
    cursor = db_connection().cursor()

    #check if given hospital_id and password  exists in hospital table

    cursor.execute("SELECT * FROM hospital WHERE hospital_id = %s AND password = %s",(hospital_id,password))
    result = cursor.fetchall()
    if(len(result) == 0):
        raise TypeError("Invalid Credentials")
    else:
        return True