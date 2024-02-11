# Blood Donation Management System

## Project Overview

This project is a desktop application that simplifies blood donation management in hospitals. It allows donors, hospital staff, and administrators to interact with a database that stores information about blood donation processes and records. The application is written in Python and uses MySQL as the backend for data storage. The application is cross-platform and can support multiple platforms using native API calls.

![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/4f35420c-9d67-4622-b5de-11f86036390e)

![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/ad394e11-5ca4-45a5-a132-8b6eee02b023)

## Features

The application has three levels of administration privileges: Donor, Hospital, and Administrator.

- Donor: A donor can create an account, view their details, and show their willingness to donate blood. They can also update their personal information and health status.
- Hospital: A hospital staff can approve a donor's request and allot them a date for blood donation after validating their health report. They can also view the available blood stock and request blood from other hospitals if needed.
- Administrator: An administrator can view the user details, their blood donation dates, and modify their account details stored in the database. They can also remove accounts from the database or create new user, hospital, or admin accounts as needed.

After a successful donation, the donor will be provided with a proof of their blood donation in a PDF form by the application.

## System Requirements

### Hardware

- CPU: Intel CORE i3 processor (minimum)
- RAM: 1 GB (minimum)
- Display Monitor

### Software

- OS: Windows, Linux, or MacOS
- Language: MySQL and Python
- Libraries: Tkinter and mysql.connector
- Environment: Visual Studio Code Editor, MySQL Workbench, Command Prompt, and MySQL CLI

I see that you have some commands and instructions for installing and running your application. I can help you add these details to your readme file under the installation and usage section. You can also add an image of your application's user interface or a screenshot of the output to make it more appealing. Here is how you can do that:

## Installation and Usage

To install and run the application, follow these steps:

1. Clone or download this repository to your local machine.
2. Install MySQL and MySQL Workbench on your machine and create a database named `blood_donation`.
3. Import the `blood_donation.sql` file from the repository to your database using MySQL Workbench or MySQL CLI.
4. Install Python 3 and the required libraries (Tkinter and mysql.connector) on your machine.
5. Create a virtual environment using the command: `python -m venv myenv`
6. Activate the virtual environment using the command: `source myenv/bin/activate`
7. Install the packages from the `requirements.txt` file using the command: `pip install -r requirements.txt`
8. Open the `main.py` file in Visual Studio Code Editor or any other Python IDE and run it.
9. Enter your username and password to log in to the application. If you don't have an account, you can create one by clicking on the `Register` button.
10. Explore the features of the application according to your role and privileges.
11. Configure your localhost name and password in the `db_creation.py` file.

## Conclusion

This project aims to streamline blood donation management in hospitals through a desktop application. The application's user interface was created using Python libraries such as Tkinter and mysql.connector, with MySQL serving as the backend for data storage. The system is scalable, robust, and resistant to SQL injections due to strict security guidelines. The application's functionality is modular, making it easy to read and track state changes.

## Screenshots

### WELCOME PAGE:  
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/5e92ac12-cf5b-4bb0-b1b7-e5149ad08ca1)

### DONOR FORM PAGE
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/8b1f8222-8a3e-41fd-aab1-2e05a22df6c3)

### DONOR TABLE VIEW
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/2d6ec0a8-1b0c-4c6f-8fa2-dbbf58300fe8)

### DONOR TABLE VIEW
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/3e5a976e-2bc5-455d-b9ae-d2fc4fb752ec)

### HOSPITAL FORM PAGE
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/87c927a9-51e1-4a27-aca5-b39194364b16)

### HOSPITAL LOGIN PAGE
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/8d6d8435-4494-4848-b132-bef375b0c5f5)

### HOSPITAL TABLE VIEW
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/2551d967-1d5e-4af8-8b64-e6b28a76f32d)

### ADMIN DASHBOARD
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/6c51ec24-5a9f-424d-b5b5-9fe457c4f910)

### ADMIN LOGIN PAGE                       
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/17fd117b-3812-43da-a92d-9d218f48eb46)

### ADMIN TABLE VIEW
![image](https://github.com/KarthiDreamr/Blood-Donation-Management-MySQL-Python/assets/84800257/8fb5c164-1929-4923-b151-37982eecae22)


## References

- [Tkinter documentation](https://docs.python.org/3/library/tkinter.html)
- [Tkinter tutorial](https://www.geeksforgeeks.org/python-tkinter-tutorial/)
- [MySQL website](https://www.mysql.com/)
- [MySQL Connector/Python](https://www.mysql.com/products/connector/)
- [MySQL Connector/Python download](https://dev.mysql.com/downloads/connector/python/)
- [Visual Studio Code download](https://code.visualstudio.com/Download)
