 
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
         
   
        
    
     
  

        
if __name__ == '__main__':
 
        main()
    