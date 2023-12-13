import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.set_page_config(layout='wide',page_title='Startup Analysis')

df=pd.read_csv('Startup_cleaned.csv')
df['Investor']=df['Investor'].fillna('Undisclosed')
MoM_Startup=df.groupby(['Year','Month'])['Startup'].count().reset_index()


def load_investor_detail(investor):
    st.title(investor)
    #Load the recent 5 ventures if the investor
    st.subheader('Recent Ventures')
    last_5=df[df['Investor'].str.contains(investor)].head()[['Date','Startup','Vertical','City','Investment','Amount']]
    st.dataframe(last_5)
    col1,col2=st.columns(2)
    with col1:
        #Biggest amount of Investment 
        st.subheader('Top 5 Investments(Cr)')
        Investment=df[df['Investor'].str.contains(investor)].groupby('Startup')['Amount'].sum().sort_values(ascending=False).head()
        fig,ax =plt.subplots()
        ax.bar(Investment.index,Investment.values)
        st.pyplot(fig)
    with col2:
        #Sector of Investment 
        st.subheader('Sectors Invested In')
        Sectors=df[df['Investor'].str.contains(investor)].groupby('Vertical')['Amount'].sum().sort_values(ascending=False)
        fig1,ax1 =plt.subplots()
        ax1.pie(Sectors,labels=Sectors.index,autopct="%0.01f%%")
        st.pyplot(fig1)
    col3,col4=st.columns(2)
    with col3:
        #Investment in Rounds 
        st.subheader('Rounds')
        Round=df[df['Investor'].str.contains(investor)].groupby('Investment')['Amount'].sum().sort_values(ascending=False)
        fig2,ax2 =plt.subplots()
        ax2.pie(Round,labels=Round.index,autopct="%0.01f%%")
        st.pyplot(fig2)
    with col4:
        #Investment in Rounds 
        st.subheader('City(HQ)')
        City_in=df[df['Investor'].str.contains(investor)].groupby('City')['Amount'].sum().sort_values(ascending=False)
        fig3,ax3 =plt.subplots()
        ax3.pie(City_in,labels=City_in.index,autopct="%0.01f%%")
        st.pyplot(fig3)
    #Year on Year Money invested in Indian Startups
    st.subheader('YoY Investment growth')
    YoY=df[df['Investor'].str.contains(investor)].groupby('Year')['Amount'].sum()
    fig4,ax4 =plt.subplots()
    ax4.plot(YoY.index,YoY.values)
    st.pyplot(fig4)
def load_overall_analysis():
    st.title('Overall Analysis')
    #Total amount of Money Poured in India
    total=round(df['Amount'].sum())
    #Max amount funded to a startup in one round
    max_fund=round(df.groupby('Startup')['Amount'].max().sort_values(ascending=False).head(1).values[0])
    #Average Ticket size
    Avg=round(df.groupby('Startup')['Amount'].sum().mean())
    #No of unique startup's that recieved funding
    count=df['Startup'].nunique()

    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.subheader('Total Invested')
        st.metric('Total',str(total)+'Cr')
    with col2:
        st.subheader('Max Funding')
        st.metric('One round',str(max_fund)+'Cr')
    with col3:
        st.subheader('Average funding')
        st.metric('Avg Fund',str(Avg)+'Cr')
    with col4:
        st.subheader('Total Startup funded')
        st.metric('Startup count',str(count))
    #MoM investment on in this 
    st.header('MoM graph')
    selected_option=st.selectbox('Select Type',['Total','Count'])
    if selected_option=='Total':
        temp_df=df.groupby(['Year','Month'])['Amount'].sum().reset_index()
    else:
        temp_df=df.groupby(['Year','Month'])['Amount'].count().reset_index()
    temp_df['x-axis']=temp_df['Month'].astype(str)+'-'+temp_df['Year'].astype(str)
    fig5,ax5=plt.subplots()
    ax5.plot(temp_df['x-axis'],temp_df['Amount'])
    st.pyplot(fig5)



st.sidebar.title('Startup Funding Analysis')   
option=st.sidebar.selectbox('Type of Analysis',[None,'Overall','Startup','Investor'])

if option=='Overall':
    load_overall_analysis()
elif option=='Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['Startup'].unique().tolist()))
    btn1=st.sidebar.button('Find Startup Details')
    if btn1:
        st.title('Startup Analysis')   
elif option=='Investor':
    selected_investor=st.sidebar.selectbox('Select Investor',sorted(set(df['Investor'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_detail(selected_investor)

