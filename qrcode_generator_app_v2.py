import streamlit as st
from decode_qrcode_page import decode_qrcode
from copied_generator import generator_function

st.set_page_config(
    page_title="QR Coder Generator v2",
    page_icon="💫"
)

options=["Generate QR Code", "Decode QR Code", "About me"]
page_selection = st.sidebar.selectbox("Menu", options)

if page_selection == "Generate QR Code":
    generator_function()
elif page_selection == "Decode QR Code":
    decode_qrcode()
elif page_selection == "About me":
    st.title("About me")
    st.write("Hi, my name is Mattes")
    #st.image(""
    #caption=  )

st.write(page_selection)