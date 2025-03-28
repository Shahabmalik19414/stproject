import streamlit as st
from stproject import calculatorfile as calc

# Streamlit App UI
st.title(":rainbow[Simple Calculator App]")
st.write("Perform basic arithmetic operations")

# Input Fields
num1 = st.number_input("Enter First Number", value=0.0, format="%.2f")
num2 = st.number_input("Enter Second Number", value=0.0, format="%.2f")

# Operation Selection
operation = st.selectbox("Choose an operation", ["+", "-", "*", "/"])

# Calculate Button
if st.button("Calculate"):
    if operation == "+":
        result = calc.add(num1, num2)
    elif operation == "-":
        result = calc.sub(num1, num2)
    elif operation == "*":
        result = calc.multiply(num1, num2)
    elif operation == "/":
        result = calc.divide(num1, num2)
    
    st.success(f"Result: {result}")
