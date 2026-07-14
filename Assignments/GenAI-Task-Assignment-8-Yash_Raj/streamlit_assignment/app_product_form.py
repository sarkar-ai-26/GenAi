import streamlit as st
from types import SimpleNamespace

var = st.sidebar
product = []
productname = var.text_input("Enter Product Name : ")
check = ["Pen","Pencil","Laptop","Car"]

var.write("Category")
for item in check:
    var.checkbox(item)

productprice = var.number_input("Enter Product Price : ")
product_o = SimpleNamespace(name=productname,price=productprice)
product.append(product_o)

if st.button("Add Product"):
    st.success("Product Added!")

    for item in product:
        st.write(f"Product Name : {item.name}")
        st.write(f"Product Price : {item.price}")
