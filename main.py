import langchain_helper as lch
import streamlit as st

st.title("Product Name Generator")

product_type = st.sidebar.selectbox("What is your product type?", ["B2B", "B2C"])
purpose = st.sidebar.text_area(label="What is the purpose of the product?", max_chars=15)

if st.sidebar.button("Generate Names"):
    names = lch.generate_name(product_type, purpose)
    st.write("Generated Names:")
    for name in names:
        st.write(f"- {name}")

if purpose:
    response = lch.generate_name(product_type, purpose)
    st.text(response["name"])