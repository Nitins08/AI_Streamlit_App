import streamlit as st

st.title("AI-enabled Web Application")

# Fixed: Placed the entire string on a single line
st.write("Welcome to the AI-enabled Web Application deployed using Streamlit Community Cloud.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    # Fixed: Added indentation here
    st.success(f"Hello, {name}! Your application is running successfully.")
