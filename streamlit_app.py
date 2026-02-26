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
