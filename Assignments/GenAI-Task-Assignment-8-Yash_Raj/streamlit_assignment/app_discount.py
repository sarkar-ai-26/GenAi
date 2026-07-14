import streamlit as st

st.title("Price Calculator")

price = st.text_input("Enter Price : ")

discount = st.slider("Select Discount Percentage : ",0,100,50)

if st.button("Calculate Discounted Price"):
    discountted_price = int(price) - (int(price) * (int(discount)/100))
    st.write(f"Discounted Price : {discountted_price}")
    st.success(discountted_price)