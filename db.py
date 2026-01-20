import streamlit as st


import mysql.connector
import datetime
from mysql.connector import Error
import streamlit

# Second backup
# hostname = "0-igg.h.filess.io"
# database = "storage_costtownon"
# port = "61002"
# username = "storage_costtownon"
# password = "c06342c974f010f014d095af8ebf435cbfd5beca"



# Primary
hostname = "mysql.db.mdbgo.com"
database = "adaanaknya_stufan"
port = "3306"
username = "adaanaknya_stufanorg"
password = "Terserahluu123."

# hostname = "sql211.hstn.me"
# database = "mseet_39090657_sutfan"
# port = "3306"
# username = "mseet_39090657"
# password = " jIdThfWubQnK!E@d"
creation_dates=  datetime.datetime.now()
creation_date_format = creation_dates.strftime('%Y%m%d%H%M%S')
sysdate = creation_dates.strftime('%Y-%m-%d %H:%M:%S')
effective_start= creation_dates.strftime('%Y-%m-%d')
effective_end_dates = "4712-12-31"
effective_end_date = datetime.datetime.strptime(effective_end_dates, "%Y-%m-%d").date()


def get_connection():
    return mysql.connector.connect(
        host=hostname,
        database=database,
        user=username,
        password=password,
        port=port
    )
    
# try:
#     connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
#     if connection.is_connected():
#         db_Info = connection.server_info
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)
# except Error as e:
#     print("Error while connecting to MySQL", e)
# conn = st.connection("my_sql_connection", type="sql")

 
 
    
def lov_nama(sysdate):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
            cursor.execute("SELECT id_talent, nama FROM list_talent WHERE  %s between effective_start_date and effective_end_date order by nama", (sysdate,))
            write = cursor.fetchall()
        connection.close() 
        return {name: id_talent for id_talent, name in write}
    except Exception as e:
        print(f"Error {e}")
  
        
 

 

def history_kas(period,tahun):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
            if tahun:
                cursor.execute(''' select nama,keterangan,harga,jumlah,tanggal,component,total from (select nama,keterangan,format(harga,0) harga,jumlah,tanggal,'Kas Masuk' component,format(harga * jumlah,0) total from kas_masuk
union all
select nama,keterangan,format(harga,0) harga,jumlah,tanggal,'Kas Keluar' component,format (harga * jumlah,0) total from kas_keluar) sum where 1=1 
and DATE_FORMAT(tanggal, '%m') = %s and year(tanggal)= %s order by sum.tanggal asc
''',(period,tahun))
            else:
                cursor.execute(''' select nama,keterangan,harga,jumlah,tanggal,component,total from (select nama,keterangan,format(harga,0) harga,jumlah,tanggal,'Kas Masuk' component,format(harga * jumlah,0) total from kas_masuk
union all
select nama,keterangan,format(harga,0) harga,jumlah,tanggal,'Kas Keluar' component,format (harga * jumlah,0) total from kas_keluar) sum where 1=1 
and DATE_FORMAT(tanggal, '%m') = %s  order by sum.tanggal asc''',(period,))

            grade = cursor.fetchall()
           
        connection.close()     
        return grade
    except Exception as e:
        print(f"Error {e}")
        
 
        
def pay_amount(id):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
          
            cursor.execute('''select format( tg.tagihan - ifnull(pa.nominal,0),0) from 
(SELECT  lt.id_talent,lt.nama, sum(ab.tagihan) tagihan 
FROM list_talent lt join absence ab on lt.id_talent = ab.id_talent where  ab.period_start between lt.effective_start_date and lt.effective_end_date group by  lt.id_talent,lt.nama) tg 
left join 
(select p.id_talent, sum(p.nominal) nominal  from payroll p where 1=1 group by p.id_talent) pa on tg.id_talent = pa.id_talent where  tg.id_talent = %s  order by tg.nama  ''',(id,))
            
            pay = cursor.fetchall()[0]
        
        connection.close()     
        return pay[0]
    except Exception as e:
        print(f"Error  dsadsadsa {e}")
        
def tagihan_period_ess(nama):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
             
            cursor.execute("SELECT lt.nama, lt.grade, ab.periode, YEAR(ab.period_start) tahun, FORMAT(SUM(ab.tagihan), 0) tagihan FROM list_talent lt, absence ab WHERE lt.id_talent = ab.id_talent AND ab.period_start BETWEEN lt.effective_start_date AND lt.effective_end_date AND lt.id_talent = %s GROUP BY lt.nama, lt.grade, ab.periode, YEAR(ab.period_start) ORDER BY YEAR(ab.period_start), CASE ab.periode WHEN 'Januari' THEN 1 WHEN 'Februari' THEN 2 WHEN 'Maret' THEN 3 WHEN 'April' THEN 4 WHEN 'Mei' THEN 5 WHEN 'Juni' THEN 6 WHEN 'Juli' THEN 7 WHEN 'Agustus' THEN 8 WHEN 'September' THEN 9 WHEN 'Oktober' THEN 10 WHEN 'November' THEN 11 WHEN 'Desember' THEN 12 END ASC " ,(nama,))
            
            grade = cursor.fetchall()
        
        connection.close()     
        return grade
    except Exception as e:
        print(f"Error {e}")