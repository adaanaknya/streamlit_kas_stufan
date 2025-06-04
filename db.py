import streamlit as st


import mysql.connector
import datetime
from mysql.connector import Error
import streamlit

hostname = "0-igg.h.filess.io"
database = "storage_costtownon"
port = "61002"
username = "storage_costtownon"
password = "c06342c974f010f014d095af8ebf435cbfd5beca"

# hostname = "sql.freedb.tech"
# database = "freedb_stufandb"
# port = "3306"
# username = "freedb_stufan"
# password = "9d2KQKRUJ4A!E@d"

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

 

def input_talent(id, nama, grade, creation_date, effective_start_date, effective_end_date):
    
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
        # cursor = connection.cursor()
            insert = cursor.execute("INSERT INTO list_talent (id_talent, nama, grade, creation_date, effective_start_date, effective_end_date) VALUES (%s, %s, %s, %s, %s, %s)",(id, nama, grade, creation_date, effective_start_date, effective_end_date))
            connection.commit()
        connection.close()    
        return True
    except:
        print("Error")
    # return id, nama, grade, creation_date, effective_start_date, effective_end_date
    
def tampil_talent(nama,eff_date):
    
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
            if nama:  # jika ada input pencarian
                cursor.execute("SELECT id_talent, nama, grade FROM list_talent WHERE nama LIKE %s and %s between effective_start_date and effective_end_date order by nama", ('%' + nama + '%',eff_date))
            else:  # jika tidak ada input, tampilkan semua
                cursor.execute("SELECT id_talent, nama, grade FROM list_talent where %s between effective_start_date and effective_end_date order by nama",(eff_date,))

            write = cursor.fetchall()
        connection.close()    
        return write

    except Exception as e:
        st.warning(f"Error: {e}")
        return []
        
# def correct_talent(id_talent,nama,grade):
    
#     try:
#         cursor = connection.cursor()
#         cursor.execute("update list_talent set nama=%s, grade=%s where id_talent = %s",(nama,grade,id_talent))
#         connection.commit()
#     except Exception as e:
#         st.warning(f"Error {e}")
        
def update_talent(id,effective_start_date):
    
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
        # cursor = connection.cursor()
            cursor.execute("SELECT MAX(creation_date) FROM list_talent WHERE id_talent=%s",(id,))
            max_creation_date = cursor.fetchone()[0]
            print(max_creation_date)
            cursor.execute("update list_talent  set effective_end_date=%s where id_talent = %s and creation_date = %s",(effective_start_date,id,max_creation_date))
            print("Updating")
                    # insert = cursor.execute("INSERT INTO list_talent (id_talent, nama, grade, creation_date, effective_start_date, effective_end_date) VALUES (%s, %s, %s, %s, %s, %s)",(id, nama, grade, creation_date, effective_start_date, effective_end_date))
            connection.commit()
            st.success("Update Berhasil")
        connection.close()  
    except Exception as e:
        st.warning(f"Error {e}")
        
        
def correct_talent(id,grade):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            # cursor= connection.cursor
            cursor.execute("update list_talent  set grade=%s where id_talent = %s ",(id,grade))
            
            connection.commit()
            st.success("Correct Berhasil")
        connection.close() 
    except Exception as e:
        print(f"Error {e}")
        
def delete_talent(id):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor= connection.cursor
            cursor.execute("delete from list_talent   where id_talent = %s ",( id,))
            
            connection.commit()
            st.success("Delete Berhasil")
        connection.close() 
    except Exception as e:
        print(f"Error {e}")
        
        
def login(user,passw):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor= connection.cursor()
            cursor.execute("select 1 from user where username = %s and password = %s",(user,passw))
            stat = cursor.fetchone()[0]
        connection.close() 
        return stat
    except Exception as e:
        print(f"Error {e}")
        
    
def lov_nama(sysdate):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
            cursor.execute("SELECT id_talent, nama FROM list_talent WHERE  %s between effective_start_date and effective_end_date", (sysdate,))
            write = cursor.fetchall()
        connection.close() 
        return {name: id_talent for id_talent, name in write}
    except Exception as e:
        print(f"Error {e}")
        
def load_grade(sysdate,id):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
            
            cursor.execute("SELECT  grade FROM list_talent WHERE  %s between effective_start_date and effective_end_date and id_talent = %s", (sysdate,id))
            grade = cursor.fetchone()[0]
        
        connection.close()     
        return grade
    except Exception as e:
        print(f"Error {e}")
        
        

def input_absence(id,  grade, jumlah_main, creation_date,period,tagihan, effective_start_date,effective_end_date):
    
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
        # cursor = connection.cursor()
            insert = cursor.execute("INSERT INTO absence (id_talent, grade, jumlah_main, creation_date, periode,tagihan,period_start,period_end) VALUES (%s,%s,%s, %s, %s, %s, %s, %s)",(id,  grade, jumlah_main, creation_date,period,tagihan, effective_start_date,effective_end_date))
            connection.commit()
        
        connection.close() 
        return insert
    except Exception as e:
        print(f"Error {e}")
        
def tagihan_period(nama,period,tahun):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
            if nama:
                cursor.execute("SELECT  lt.nama,lt.grade,ab.periode,year(ab.period_start) tahun ,FORMAT(sum(ab.tagihan), 0) tagihan  FROM list_talent lt,absence ab where lt.id_talent = ab.id_talent and ab.period_start between lt.effective_start_date and lt.effective_end_date  and lt.nama like %s and ab.periode = %s group by lt.nama,lt.grade,ab.periode,year(ab.period_start)" ,('%'+nama+'%',period))
            elif tahun: 
                 cursor.execute("SELECT  lt.nama,lt.grade,ab.periode,year(ab.period_start) tahun ,FORMAT(sum(ab.tagihan), 0) tagihan  FROM list_talent lt,absence ab where lt.id_talent = ab.id_talent and ab.period_start between lt.effective_start_date and lt.effective_end_date  and year(ab.period_start) = %s and ab.periode = %s group by lt.nama,lt.grade,ab.periode,year(ab.period_start)",(tahun,period))
            else:
                cursor.execute("SELECT  lt.nama,lt.grade,ab.periode,year(ab.period_start) tahun ,FORMAT(sum(ab.tagihan), 0) tagihan  FROM list_talent lt,absence ab where lt.id_talent = ab.id_talent and ab.period_start between lt.effective_start_date and lt.effective_end_date and ab.periode = %s group by lt.nama,lt.grade,ab.periode,year(ab.period_start)",(period,))
        
            grade = cursor.fetchall()
        
        connection.close()     
        return grade
    except Exception as e:
        print(f"Error {e}")
        
def tagihan_total(nama):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
            if nama:
                cursor.execute('''select tg.nama,format( tg.tagihan - ifnull(pa.nominal,0),0) from 
(SELECT  lt.id_talent,lt.nama, sum(ab.tagihan) tagihan 
FROM list_talent lt join absence ab on lt.id_talent = ab.id_talent where  ab.period_start between lt.effective_start_date and lt.effective_end_date group by  lt.id_talent,lt.nama) tg 
left join 
(select p.id_talent, sum(p.nominal) nominal  from payroll p where 1=1 group by p.id_talent) pa on tg.id_talent = pa.id_talent where  tg.nama like %s  order by tg.nama  ''',('%'+nama+'%',))
            else:
                cursor.execute('''select tg.nama,format( tg.tagihan - ifnull(pa.nominal,0),0) from 
(SELECT  lt.id_talent,lt.nama, sum(ab.tagihan) tagihan 
FROM list_talent lt join absence ab on lt.id_talent = ab.id_talent where  ab.period_start between lt.effective_start_date and lt.effective_end_date group by  lt.id_talent,lt.nama) tg 
left join 
(select p.id_talent, sum(p.nominal) nominal  from payroll p where 1=1 group by p.id_talent) pa on tg.id_talent = pa.id_talent order by tg.nama ''')
    
            grade = cursor.fetchall()
        
        connection.close()     
        return grade
    except Exception as e:
        print(f"Error {e}")
        
        
def input_pembayaran(id_talent,keterangan,nominal,eff_date):
    
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
        # cursor = connection.cursor()
            insert = cursor.execute("INSERT INTO payroll (id_pembayaran, id_talent, keterangan, creation_date, nominal,effective_date) VALUES (%s,%s,%s, %s, %s,%s)",(creation_date_format,  id_talent, keterangan, sysdate,nominal,eff_date))
            connection.commit()
        
        
        connection.close()     
        return insert
    except Exception as e:
        print(f"Error {e}")
        
def history_pembayaran(nama,date_from,date_to):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
            if nama:
                cursor.execute("SELECT  lt.nama ,py.keterangan,format(py.nominal,0) nominal,py.effective_date  FROM list_talent lt , payroll py  where  %s between lt.effective_start_date and lt.effective_end_date and py.id_talent = lt.id_talent  and   lt.nama like %s  and py.effective_date between %s and %s ",(sysdate,'%'+nama+'%',date_from,date_to))
            else:
                cursor.execute("SELECT  lt.nama ,py.keterangan,format(py.nominal,0) nominal,py.effective_date  FROM list_talent lt , payroll py  where  %s between lt.effective_start_date and lt.effective_end_date and py.id_talent = lt.id_talent and  py.effective_date between %s and %s  ",(sysdate,date_from,date_to))

            grade = cursor.fetchall()
        
        connection.close()    
        return grade
    except Exception as e:
        print(f"Error {e}")


def calculate(date_from,date_to):
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
           
            cursor.execute("SELECT  format(sum(py.nominal),0) nominal  FROM list_talent lt , payroll py  where  %s between lt.effective_start_date and lt.effective_end_date and py.id_talent = lt.id_talent and  py.effective_date between %s and %s  ",(sysdate,date_from,date_to))
 
            cal = cursor.fetchall()[0]
        
        connection.close()    
        return cal[0]
    except Exception as e:
        print(f"Error {e}")
        
        
def input_kas_masuk(nama,keterangan,harga,jumlah,tanggal):
    
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
        # cursor = connection.cursor()
            insert = cursor.execute("INSERT INTO kas_masuk (id_kas_masuk, nama, keterangan, harga, jumlah,tanggal) VALUES (%s,%s,%s, %s, %s,%s)",(creation_date_format,  nama, keterangan, harga,jumlah,tanggal))
            connection.commit()
            st.success("Berhasil Input!")
            
        connection.close()     
        return insert
    except Exception as e:
        print(f"Error {e}")


def input_kas_keluar(nama,keterangan,harga,jumlah,tanggal):
    
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
        # cursor = connection.cursor()
            insert = cursor.execute("INSERT INTO kas_keluar (id_kas_keluar, nama, keterangan, harga, jumlah,tanggal) VALUES (%s,%s,%s, %s, %s,%s)",(creation_date_format,  nama, keterangan, harga,jumlah,tanggal))
            connection.commit()
            st.success("Berhasil Input!")
            
        connection.close()     
        return insert
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
        
        
def cur_amount():
    try:
        connection = get_connection() 
        with connection.cursor() as cursor:
            # cursor = connection.cursor()
           
            cursor.execute('''select format(km.total - kk.total,0) current_amount from (select sum(total) total from (select (harga * jumlah) total from kas_masuk) km) km,
(select sum(total) total from (select (harga * jumlah) total from kas_keluar) kk) kk ''')
            cur = cursor.fetchall()[0]
           
        connection.close() 
        return cur[0]
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
             
            cursor.execute("SELECT  lt.nama,lt.grade,ab.periode,year(ab.period_start) tahun ,FORMAT(sum(ab.tagihan), 0) tagihan  FROM list_talent lt,absence ab where lt.id_talent = ab.id_talent and ab.period_start between lt.effective_start_date and lt.effective_end_date  and lt.id_talent = %s   group by lt.nama,lt.grade,ab.periode,year(ab.period_start)" ,(nama,))
            
            grade = cursor.fetchall()
        
        connection.close()     
        return grade
    except Exception as e:
        print(f"Error {e}")