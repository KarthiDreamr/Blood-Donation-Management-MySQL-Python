import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()  # take environment variables from .env.

def db_creation_connection():
  # Connect to the MySQL database
  connection = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
  )

  return connection

def db_connection():
  # Connect to the MySQL database
  connection = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE"),
  )

  return connection