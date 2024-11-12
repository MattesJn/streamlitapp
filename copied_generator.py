import streamlit as st
import segno
import time

def generator_function():
    st.header("QR Code Generator")

    st.image("images/banner.jpg")

    url = st.text_input("Please enter the data you want to encode")

    def generate_qrode(url):
        qrcode=segno.make_qr(url)
        qrcode.save("images/qrcode_streamlit.png",
                    scale=5)


    if url:
        with st.spinner("Generating QR Code"):
            time.sleep(1.5)
        generate_qrode(url)
        st.image("images/qrcode_streamlit.png",
                 caption="There it is")

    st.markdown("<br><hr><center>Design and Creation: Mattes Jansen",
                unsafe_allow_html=True)

    st.write(url)

