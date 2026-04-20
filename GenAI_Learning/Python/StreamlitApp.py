import streamlit as st

st.title("YashApp")
st.write("NewApp -- ")
st.header("WelcomeGuys")

#interactive
agree = st.checkbox("142")
if agree:
    st.write("Checked")

if st.button("NewButton"):
    st.write("Button Clicked")