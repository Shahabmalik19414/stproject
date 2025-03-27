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
st.markdown(""""Playground
           **You can do :rainbow[many things] here**
            Lets try some :sparkles[markdown]""")
st.write("___________________________________")
if st.button("Hit Balloon"):
  st.balloons()

  import streamlit as st
import pandas as pd
import numpy as np

st.write("Streamlit supports a wide range of data visualizations, including [Plotly, Altair, and Bokeh charts](https://docs.streamlit.io/develop/api-reference/charts). 📊 And with over 20 input widgets, you can easily make your data interactive!")

all_users = ["Alice", "Bob", "Charly"]
with st.container(border=True):
    users = st.multiselect("Users", all_users, default=all_users)
    rolling_average = st.toggle("Rolling average")

np.random.seed(42)
data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)
if rolling_average:
    data = data.rolling(7).mean().dropna()

tab1, tab2 = st.tabs(["Chart", "Dataframe"])
tab1.line_chart(data, height=250)
tab2.dataframe(data, height=250, use_container_width=True)