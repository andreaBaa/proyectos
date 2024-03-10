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
  st.subheader("¿Te gustaría recibir notificaciones por correo?")
  st.write("Será por lo menos 1 mensaje al mes.")
  resp = st.checkbox("")
  if resp:
      st.write("Correcto")

with col2: 
  st.subheader("Esta es la segunda columna")
  modo = st.radio("¿Sobre qué mas te gustaría aprender?", ("Visual", "Auditiva", "Táctil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audición es fundamental para tu interfaz")
  if modo == "Táctil":
    st.write("Lo táctil es fundamental para tu interfaz")


st.subheader("¿Te ha sido útil la información?")
if st.button("Sí"):
  st.write("Gracias por tu valoración 😊")
else:
  st.write("Cuéntanos tu opinión")




  

