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
    scol1.metric("Cost per Share", f"{round(stocks['today'],1)}$")
    scol3.metric("One Week Ago", f"{stocks['one_week_ago']}$", f"{abs(round(stocks['today']-stocks['one_week_ago'],2))}%")
    scol2.metric("One month ago",f"{stocks['one_month_ago']}$", f"{abs(round(stocks['today']-stocks['one_month_ago'],2))}%")
    st.subheader("",divider='rainbow')
    st.subheader("Financial Data")
    cont = col1.container()
    financials = data['financial_status']
    st.text(f"Gross Profit Margin: {round(financials['gross_profit_margin'],2)}%")
    st.text(f"Operating Margin: {round(financials['operating_margin'],2)}%")
    st.text(f"Net Profit Margin: {round(financials['net_profit_margin'],2)}%")
    st.text(f"Ebitda Margin: {round(financials['ebitda_margin'],2)}%")
    st.text(f"Financial Health: {'Good' if financials['grim'] == False else 'Poor'}")



    # Calculate lay off risk percentage based on stock drop
    stock_drop_threshold = 3  # Set the threshold for stock drop percentage
    stock_drop_percentage = abs((stocks['today'] - stocks['one_month_ago']) / stocks['one_month_ago']) * 100
    print(stock_drop_percentage)
    lay_off_risk_percentage = 0  # Initialize lay off risk percentage

    if stock_drop_percentage >= stock_drop_threshold:
        lay_off_risk_percentage = 15  # Add 5% to lay off risk if stock drop exceeds threshold

    # Display lay off risk percentage
    st.subheader("Lay Off Risk")
    cont = col1.container()
    cont.text(f"Chance of Getting Laid Off: {lay_off_risk_percentage}%")

    # Check if location is in California
    if data['location'] == 'California':
        lay_off_risk_percentage += 10  # Add 5% to lay off risk if location is in California
        cont.text(f"with California factor: + 10%")
    else:
        cont.text(f"with California factor:  ~ 0%")
    # Display updated lay off risk percentage
    stability = data['stability']
    if stability['stability'] == False:
        lay_off_risk_percentage += 15
        cont.text(f"with Stability factor: + 15%")
    else:
        cont.text(f"with Stability factor:  ~ 0%")
    
    # Calculate grim factor based on financial health
    grim_factor = 0  # Initialize grim factor
    if financials['grim']:
        lay_off_risk_percentage += 20
    # Display grim factor
        cont.text(f"Company Quarterly:  + 20%")
    else:
        cont.text(f"Company Quarterly:  ~ 0%")
    # Calculate total lay off risk percentage
    cont.text(f"Total Lay Off Risk: {lay_off_risk_percentage}%")



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
    st.write(f"Reasoning: {stability['explanation']}")





st.sidebar.markdown("# Main page 🎈")

