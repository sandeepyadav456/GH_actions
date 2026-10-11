import streamlit as st

# Define core logic so it can be easily tested
def add_number(a, b):
    return a + b

# Page configuration
st.set_page_config(
    page_title="My First CI/CD Pipeline", page_icon="🚀", layout="centered"
)

# App Header
st.title("🚀 My First CI/CD Pipeline")
st.write("A simple addition calculator built with Streamlit.")

st.divider()

# Input Section
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("First Number", value=0.0, format="%.2f")
with col2:
    num2 = st.number_input("Second Number", value=0.0, format="%.2f")

# Calculation & Output
if st.button("Calculate Sum", type="primary"):
    total = add_number(num1, num2)
    st.success(f"The sum of {num1} and {num2} is **{total}**")

st.markdown("---")
st.caption("Powered by Streamlit & Python")