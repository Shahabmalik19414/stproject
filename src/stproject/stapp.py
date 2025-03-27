import streamlit as st
import pandas as pd
import numpy as np

st.title("      ***->WELCOME<-***")
st.header("This app is created by **Saurabh**")
mydata = {"name": ["Saurabh", "Rahul", "Rohit", "Rajesh", "Ramesh"],
          "age": [25, 26, 27, 28, 29],
          "city": ["Pune", "Mumbai", "Delhi", "Kolkata", "Chennai"]}
st.table(mydata)
st.dataframe(mydata)
st.write("___________________________________")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
chart_data
st.line_chart(chart_data)