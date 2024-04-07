import streamlit as st
import streamlit as st
import requests
# Connect to the MongoDB database
data = requests.get("http://100.111.60.93:8052/gatodb")
print(data.json())