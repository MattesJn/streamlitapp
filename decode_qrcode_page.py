import streamlit as st
import numpy as np
import cv2


def decode_qrcode():
    st.header("Decode the QR Code")

    qrcode = st.file_uploader("Upload your QR Code",
                     type=["jpg", "png", "jpeg", "gif"])

    if qrcode:
        #annoying code to convert the uploaded qrcode image into an image that decodes
        file_bytes = np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        #place the qrcode
        st.image(opencv_image)

        #decode the qrcode
        detector = cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your qrcode contained: {decoded_info}")
        #st.write(point)
        #st.write(staight_qr)