import mysql.connector

## insertt in hospital table first lol

database_name = 'bdonation'

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yh1pwth@t",
    # database=database_name
)

# # for dhanesh
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Yh1pwth@t",
#     database="donation"
# ) 

# Create a cursor object to execute SQL queries
cursor = conn.cursor()


# Check if the database exists
cursor.execute("SHOW DATABASES LIKE '{}'".format(database_name)) 
database_exists = cursor.fetchone()

if not database_exists:
    cursor.execute("CREATE DATABASE {}".format(database_name))

cursor.execute("USE bdonation")

print("complete")


cursor.execute("SHOW TABLES LIKE 'hospital'")
hospital_exists = cursor.fetchone()

if not hospital_exists:
    cursor.execute(
        """ CREATE TABLE hospital (
                hid INT NOT NULL ,
                hname VARCHAR(30) NOT NULL,
                password VARCHAR(30) NOT NULL,
                total_capacity INT NOT NULL,
                quantity_required INT NOT NULL,
                contact_no BIGINT NOT NULL,
                street_name VARCHAR(50) NOT NULL,
                city VARCHAR(30) NOT NULL,
                district VARCHAR(30) NOT NULL,
                state VARCHAR(30) NOT NULL,
                country VARCHAR(20) NOT NULL,
                o_plus_available INT NOT NULL,
                a_plus_available INT NOT NULL,
                b_plus_available INT NOT NULL,
                ab_plus_available INT NOT NULL,
                o_minus_available INT NOT NULL,
                a_minus_available INT NOT NULL,
                b_minus_available INT NOT NULL,
                ab_minus_available INT NOT NULL,
                o_plus_maximum INT NOT NULL,
                a_plus_maximum INT NOT NULL,
                b_plus_maximum INT NOT NULL,
                ab_plus_maximum INT NOT NULL,
                o_minus_maximum INT NOT NULL,
                a_minus_maximum INT NOT NULL,
                b_minus_maximum INT NOT NULL,
                ab_minus_maximum INT NOT NULL,
                PRIMARY KEY (hid)
                );
        """ 
)


# Check if the table exists
cursor.execute("SHOW TABLES LIKE 'donor'")
donor_exists = cursor.fetchone()

if not donor_exists:
    cursor.execute(
        """ CREATE TABLE donor (
                aadhaar_id bigint NOT NULL PRIMARY KEY,
                gender varchar(25) NOT NULL,
                first_name varchar(20) NOT NULL,
                lname_name varchar(20),
                dob date NOT NULL,
                blood_type varchar(3) NOT NULL,
                pregnancy_status BOOL NOT NULL,
                HIV BOOL NOT NULL,
                street_name varchar(50) NOT NULL,
                city varchar(30) NOT NULL,
                district varchar(30) NOT NULL,
                state varchar(30) NOT NULL,
                country varchar(20) NOT NULL,
                country_code varchar(3) NOT NULL,
                password varchar(30) NOT NULL,
                father_name varchar(30),
                mother_name varchar(30),
                gaurdian_name varchar(30),
                ph1 bigint NOT NULL,
                ph2 bigint,
                hid int NOT NULL,
                FOREIGN KEY ( hid) REFERENCES hospital(hid)
                );
        """ 
)


cursor.execute("SHOW TABLES LIKE 'admin'")
admin_exists = cursor.fetchone()

if not admin_exists:
    cursor.execute(
        """ 
            CREATE TABLE admin (
                admin_name varchar(50),
                admin_id INT NOT NULL,
                password VARCHAR(30) NOT NULL,
                PRIMARY KEY (admin_id)
                );
        """ 
)

cursor.execute("SHOW TABLES LIKE 'reports'")
reports_exists = cursor.fetchone()

if not reports_exists:
    cursor.execute(
        """ 
            CREATE TABLE reports (
                date DATE NOT NULL,
                time TIME NOT NULL,
                no_units_donated INT NOT NULL,
                hid INT NOT NULL, 
                aadhaar_id bigint NOT NULL,
                FOREIGN KEY (aadhaar_id) REFERENCES donor(aadhaar_id),
                FOREIGN KEY (hid) REFERENCES hospital(hid)
                );
        """
)
    
# Define a list of tuples to insert
data = [
 (123456789012, 'Male', 'John', 'Doe', '1990-01-01', 'A+', False, False, '123 Main St', 'Mumbai', 'Mumbai Suburban', 'Maharashtra', 'India', '+91','P@ssw0rd', 'Jack Doe', 'Jane Doe', None, 9876543210, None, 1),
 (234567890123, 'Female', 'Mary', 'Smith', '1991-02-02', 'B-', False, False, '456 Main St', 'Delhi', 'New Delhi', 'Delhi', 'India', '+91','P@ssw0rd1', 'John Smith', 'Jane Smith', None, 8765432109, None, 2),
 (345678901234, 'Male', 'Harry', 'Potter', '1992-03-03', 'O+', False, False, '789 Main St', 'Kolkata', 'Kolkata', 'West Bengal', 'India', '+91','P@ssw0rd2', 'James Potter', 'Lily Potter', None, 7654321098, None, 3)
]

# Define the query string with placeholders
query = """
 INSERT INTO donor (aadhaar_id, gender, first_name, lname_name, dob, blood_type, pregnancy_status, HIV, street_name, city, district, state, country, country_code, password, father_name, mother_name, gaurdian_name, ph1, ph2, hid) 
 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
 """

# Execute the query multiple times with different parameters
cursor.executemany(query,data)

        
# Close the cursor and the connection
cursor.close()
conn.close()