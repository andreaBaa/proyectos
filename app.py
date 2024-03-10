import streamlit as st 
from PIL import Image

st.title("El reseñador")
st.header("¡Aquí encontrarás próximamente reseñas acerca de tus libros favoritos! .")
st.write("El contenido se encontrará disponible a partir de abril.")
image = Image.open("roma.jpg")

st.image(image, caption="Reviews")


texto = st.text_input("Escribe tu correo electrónico", "correo@gmail.com")
st.write("Verifica, tu correo es:", texto)

st.subheader("Ahora usemos 2 columnas")


col1, col2 = st.columns(2)

with col1: 
  st.subheader("¿Te gustaría recibir novedades por correo?")
  st.write("Será por lo menos 1 mensaje al mes.")
  resp = st.checkbox("")
  if resp:
      st.write("Gracias, te estaremos contactando")

with col2: 
  st.subheader(¿Cuál es tu género favorito?")
  modo = st.radio("¿?", ("Fantasía", "Ciencia ficción", "Romance"))
  if modo == "Fantasía":
    st.write("Que buenos gustos, lo tomaremos en cuenta.")
  if modo == "Ciencia ficción":
    st.write("Gracias, lo tomaremos en cuenta.")
  if modo == "Romance":
    st.write("Con que eres romántic@, lo tomaremos en cuenta.")


st.subheader("¿Te ha sido útil la información?")
if st.button("Sí"):
  st.write("Gracias por tu valoración 😊")
else:
  st.write("Cuéntanos tu opinión")




  

