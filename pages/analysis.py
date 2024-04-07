import streamlit as st
from io import BytesIO
import requests



st.set_page_config(page_title="Aura")
st.title("Project Page :)")
st.write("Enter name for analysis")
name = st.text_input("Name")
try:
    r = requests.get("http://localhost:8052/get/"+name)
except:
    pass

data = r.json()

col1, col2 = st.columns(2)

with col1:
    st.header("Stock Data")
    cont = col1.container()
    stocks = data['stock']
    scol1, scol2, scol3 = st.columns(3)
    scol1.metric("Cost per Share", f"{round(stocks['today'],1)}%")
    scol3.metric("One Week Ago", f"{stocks['one_week_ago']}%", f"{abs(round(stocks['today']-stocks['one_week_ago'],2))}%")
    scol2.metric("One month ago",f"{stocks['one_month_ago']}%", f"{abs(round(stocks['today']-stocks['one_month_ago'],2))}%")
    st.subheader("",divider='rainbow')
    st.subheader("Financial Data")
    cont = col1.container()
    financials = data['financial_status']
    st.text(f"Gross Profit Margin: {round(financials['gross_profit_margin'],2)}%")
    st.text(f"Operating Margin: {round(financials['operating_margin'],2)}%")
    st.text(f"Net Profit Margin: {round(financials['net_profit_margin'],2)}%")
    st.text(f"Ebitda Margin: {round(financials['ebitda_margin'],2)}%")
    st.text(f"Financial Health: {'Good' if financials['grim'] == False else 'Poor'}")
with col2:
    st.header(f"{name}'s Profile")
    cont = col2.container()
    cont.text("Position: "+data['description'])
    cont.text("NASDAQ: "+data['NASAQ'])
    cont.text("Company: "+data['company'])
    st.subheader("",divider='rainbow')
    st.subheader("Stability Data")
    cont = col2.container()
    stability = data['stability']
    st.text(f"Safe Position: {stability['stability']}")
    




st.sidebar.markdown("# Main page 🎈")

