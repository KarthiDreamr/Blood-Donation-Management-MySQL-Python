from DB.db_creation import db_connection

# def donor_table_show():
#     connection = db_connection()
#     cursor = connection.cursor()

#     donor_table = cursor.execute("SELECT * from donor limit 10")
    
#     for i in donor_table:
#         for j in i:
#             print(j)
#         print("\n")

connection = db_connection()
cursor = connection.cursor()

donor_table = cursor.execute("SELECT * from donor limit 10")

for i in donor_table:
    for j in i:
        print(j)
    print("\n")