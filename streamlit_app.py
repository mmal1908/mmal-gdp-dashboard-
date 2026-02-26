import streamlit as st
import pandas as pd
import math
from pathlib import Path
from PIL import Image

st.title("Esta es mi primera app en la nubeee")

st.header("En este espacio desarrollo mi app.")

st.write("Crear frontend y backend")

image = Image.open("imagen1.jpg")

st.image(image, caption='Interfaces Multimodales')

texto = st.text_input('Escribe algo', 'este es el textooo')

st.write('El texto escrito es:', texto)

st.subheader("Ahora usemos dos columnas:")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write('¡Correcto!')
