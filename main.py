 
import streamlit as st
import pandas as pd
import datetime
import db
 

creation_dates=  datetime.datetime.now()
creation_date_format = creation_dates.strftime('%Y%m%d%H%M%S')
sysdate = creation_dates.strftime('%Y-%m-%d %H:%M:%S')
effective_start= creation_dates.strftime('%Y-%m-%d')
effective_end_dates = "4712-12-31"
effective_end_date = datetime.datetime.strptime(effective_end_dates, "%Y-%m-%d").date() 


 
bulan_mapping = {
    "Januari": "01",
    "Februari": "02",
    "Maret": "03",
    "April": "04",
    "Mei": "05",
    "Juni": "06",
    "Juli": "07",
    "Agustus": "08",
    "September": "09",
    "Oktober": "10",
    "November": "11",
    "Desember": "12"
}
 
def main():
 
  st.header("Marching Band Dunia Fantasi")
  st.image("stufan.jpg",caption="Stufan Dcorps")

  with st.form(key="cek"):
    
    st.subheader("Cek Tagihan Kas ")
    users_dict = db.lov_nama(sysdate)
    nama_talent = st.selectbox("Pilih Nama:", list(users_dict.keys()))
    id_talent = users_dict[nama_talent]  
   
    submit = st.form_submit_button("Cari")
    columns = ["Nama", "Grade", "Period","Tahun","Tagihan"]
    data = db.tagihan_period_ess(id_talent)
    if submit:
      if nama_talent:
        payment= db.pay_amount(id_talent)
        st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 
        if payment:
           st.write("Total Kas yang harus Kamu bayar : "+ str(payment))
        else:
           st.write("Kamu tidak ada tagihan Kas")
    else:
         st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 
         
  
        
  with st.form(key="History"):
      st.header("Pemasukan Pengeluran Uang Kas")
      period = st.selectbox(
      "Periode Bulan",
      ("Januari", "Februari", "Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"),
      )
  
      tahun = st.text_input("Tahun")
      
      columns = ["Nama", "Keterangan", "Harga / Nominal","Jumlah","Tanggal","Komponen","Total"]
      submit = st.form_submit_button("Cari") 
      if submit:
          if period in bulan_mapping:
              periods = bulan_mapping[period]
              data = db.history_kas(periods,tahun)
              if period and tahun:
                  st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 
              else:
                  st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True)   
    
       
      
if __name__ == '__main__':
 
        main()
    