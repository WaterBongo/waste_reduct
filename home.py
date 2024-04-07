import streamlit as st
from io import BytesIO
import requests



st.set_page_config(page_title="Aura")
st.title("Upload Data :)")
st.write("Enter simple information to add food to the database")
name = st.text_input("Name")
description = st.text_input("Job title")
company = st.text_input("Company")
NASAQ = st.text_input("NASAQ")
location = st.text_input("location")
performance = st.text_input("Performance")

if st.button("Submit"):
    print("hi :0")
    with st.status("Scraping Data....", expanded=True) as status:
        st.write("Searching for data...")
        r = requests.get("http://localhost:8080/stock/"+NASAQ)
        print(r.text)
        st.write("Stock Data found")
        st.write("Searching for financial status...")
        r1 = requests.get("http://localhost:8080/financial_status/"+NASAQ).json()
        st.write("Financial Status Found")
        st.write("Searching for stability data (Patience!)...")
        r2 = requests.get("http://localhost:8080/product_stabilitiy/"+company+"/"+name+"/"+NASAQ).json()
    st.success('Quarterly Results Found!', icon="✅")
    print(r.text)
    data = r.json()
    payload = {
        "name": name,
        "description": description,
        "company": company,
        "NASAQ": NASAQ,
        "location": location,
        "performance": performance,
        "stock": data,
        "financial_status": r1,
        "stability": r2
    }
    r = requests.post('http://localhost:8052/gatodb', json=payload)
    


st.sidebar.markdown("# Main page 🎈")
