import pandas as pd
import streamlit as st
import numpy as np
import plotly.figure_factory as ff

#Fondo pagina
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://apcp.es/wp-content/uploads/2021/07/source.gif");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

#Encabezado
col1, col2 = st.columns(2)

with col1:
   st.image("https://media4.giphy.com/media/H6bfmCcehzqEfWQjqk/giphy.gif?cid=d849cd2fbtiom74nexur4kxq22l6btpq6pxu6whee4sv52by&rid=giphy.gif&ct=g", width=200)
  
with col2:
   st.image("https://enlinea.senace.gob.pe/logo_senace.png", width=200)

#Título
st.markdown(f'<h1 style="color:#fafdfa;font-size:50px;">{"Certificación Ambiental"}</h1>', unsafe_allow_html=True)
st.image("https://cdn.www.gob.pe/uploads/document/file/3438583/standard_.jpg", width=600)

st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"La certificación ambiental es el instrumento previo que todo proyecto de inversión debe elaborar antes de ser ejecutado, previendo los impactos ambientales negativos significativos que podría generar. Equivale a la hoja de ruta del proyecto, donde están contenidos los requisitos y obligaciones del titular, así como las actividades que deberá llevar a cabo para remediar los impactos negativos."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Toda persona natural o jurídica, de derecho público o privado, nacional o extranjera, que pretenda desarrollar un proyecto de inversión en el Perú que sea susceptible de generar impactos ambientales negativos de carácter significativo, debe gestionar una certificación ambiental ante la autoridad correspondiente."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"No podrá iniciarse la ejecución de los proyectos ni las actividades de servicios y comercio y ninguna autoridad nacional, sectorial, regional o local podrá aprobarlas, autorizarlas, permitirlas, concederlas o habilitarlas si previamente no cuentan con la certificación ambiental."}</h1>', unsafe_allow_html=True)

THEMES = [
    "light",
    "dark",
    "green",
    "blue",
]
GITHUB_OWNER = "streamlit"

# Show thumbnails for available themes.
# As html img tags here, so we can add links on them.
cols = st.beta_columns(len(THEMES))
for col, theme in zip(cols, THEMES):

    # Get repo name for this theme (to link to correct deployed app)-
    if theme == "light":
        repo = "theming-showcase"
    else:
        repo = f"theming-showcase-{theme}"

    # Set border of current theme to red, otherwise black or white
    if theme == CURRENT_THEME:
        border_color = "red"
    else:
        border_color = "lightgrey" if IS_DARK_THEME else "black"

    col.markdown(
        # f'<p align=center><a href="https://share.streamlit.io/{GITHUB_OWNER}/{repo}/main"><img style="border: 1px solid {border_color}" alt="{theme}" src="https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/main/thumbnails/{theme}.png" width=150></a></p>',
        f'<p align=center><a href="https://apps.streamlitusercontent.com/{GITHUB_OWNER}/{repo}/main/streamlit_app.py/+/"><img style="border: 1px solid {border_color}" alt="{theme}" src="https://raw.githubusercontent.com/{GITHUB_OWNER}/theming-showcase/main/thumbnails/{theme}.png" width=150></a></p>',
        unsafe_allow_html=True,
    )
    if theme in ["light", "dark"]:
        theme_descriptor = theme.capitalize() + " theme"
    else:
        theme_descriptor = "Custom theme"
    col.write(f"<p align=center>{theme_descriptor}</p>", unsafe_allow_html=True)
