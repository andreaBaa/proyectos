import streamlit as st 
from PIL import Image

st.title("Mi primera App")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Fácilmente puedo realizar backend y frontend")
image = Image.open("roma.jpg")

st.image(image, caption="Roma")


texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("El texto escrito es", texto)

st.subheader("Ahora usemos 2 columnas")


col1, col2 = st.columns(2)

witch col1: 
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
      st.write("Correcto")
