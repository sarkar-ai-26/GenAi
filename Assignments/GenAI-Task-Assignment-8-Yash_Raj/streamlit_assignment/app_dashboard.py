import streamlit as st

st.title("Simple Sales Dashboard")
st.text("Discription ------------------------------------ XX")

months = ["January","Febraury","March","April"]
sales = {
    "January":1200,
    "Febraury":1500,
    "March":900,
    "April":2000
}

sales_month = st.selectbox("Month",months)

if sales_month:
    st.metric(sales_month,sales[sales_month])

st.bar_chart(list(sales.values()))
