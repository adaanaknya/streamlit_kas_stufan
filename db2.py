import streamlit as st


import mysql.connector
import datetime
from mysql.connector import Error
import streamlit

hostname = "sql161120.byetcluster.com"
database = "mseet_39090657_sutfan"
port = "3306"
username = "mseet_39090657"
password = " jIdThfWubQnK!E@d"
sysdate =  datetime.datetime.now()

try:
    connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
    if connection.is_connected():
        db_Info = connection.server_info
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
# conn = st.connection("my_sql_connection", type="sql")
