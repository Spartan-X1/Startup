import streamlit as st
import pandas as pd
import time
st.title('Startup-Dashboard')
st.header('I am learning streamlit')
st.subheader('& I am loving it!')
st.write('This is normal text')
st.markdown("""
### These are my favourite mangas 
- Kaguya sama love is war 
- From me to you
- The class president is a maid
- The Fragrant flower blooms with dignity
- Clannad
            """)
st.code(""" 
def info(no):
        return no*10
x=info(5) 
        """)

st.latex('x^2+y^2=10')
df=pd.DataFrame({
    'Name':['Ankit','Nitish','Aryan'],
    'Marks':[20,10,50],
    'Package(Cr)':[14,5,25]
})
st.dataframe(df)
st.metric('Revenue','Rs 3L','10%')
st.sidebar.title('Choose your poison')
col1,col2=st.columns(2)
with col2:
    st.image('Wierd shit.jpg')
with col1:
    st.video('Butterfly.mp4')
st.error('Bhai tera kat gaya')
st.success('Atleast issi bahane UPSE to nikal gaya')
st.info('Kisiko bhi dekh kai latuu mat ho')
st.warning('Bhai ye vali sai thoda bach kai ')
bar=st.progress(0)
for i in range(1,101):
    time.sleep(0.05)
    bar.progress(i)
Num=st.number_input('Enter your age')
if 0<Num<18:
    st.warning('Come back when you are grown up')
elif (Num>90) & (Num<100):
    st.info('Better start Digging a grave for yourself')
elif Num>=100:
    st.error('A spirit has entered the Chat')
Date=st.date_input('Enter Date of birth')
Email=st.text_input('Enter your mail ID')
Pass=st.number_input('Enter your Pass_key')
st.selectbox('Select gender',['Male','Female','Apachi helicopter','Walmart Bag','soggy sock','Patagobhi','Haryanvi ladki','Emo girl','League player','Bitchless','Poopy Diapers','Ayuesh the Woman Repelent'])
btn=st.button('Login karo')

if btn :
    if Email =="Lonelyfucker@milfnearme.com" and Pass==696969:
        st.success('Go fuck some bitches homey')
    else :
        st.warning('you ain\'t my nigga')
file=st.file_uploader('Upload a CSV file')

if file is not None:
    st.dataframe(pd.read_csv(file))
                      