import streamlit as st
import time
import requests


st.set_page_config(page_title="My pet app",
                   page_icon="🐈‍⬛🐕")
st.title("Pet app")

def get_cat_image():
    url = "https://cataas.com//cat"
    contents = requests.get(url)
    return contents.content

def get_dog_image_url():
    url = "https://random.dog/woof.json"
    contents = requests.get(url).json()
    dog_image_url = contents["url"]
    return dog_image_url

c1, c2 = st.columns(2)

with c1:
    cat_button = st.button("Click here for a cat image")
    if cat_button:
        cat_image = get_cat_image()
        st.image(cat_image, width=300, caption="My cat image")

with c2:
    dog_button = st.button("Click here for a dog image")
    if dog_button:
        dog_image_url = get_dog_image_url()
        while dog_image_url[-4:] == ".mp4":
            get_dog_image_url()

        st.image(dog_image_url, width=300, caption="My dog image")


