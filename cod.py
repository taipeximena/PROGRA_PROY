import pandas as pd
import streamlit as st
import numpy as np
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

st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"SENACE"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"El Servicio Nacional de Certificación Ambiental para las Inversiones Sostenibles (Senace) es un organismo público técnico especializado, adscrito al Ministerio del Ambiente, que evalúa la viabilidad ambiental de los proyectos de inversión más complejos del país, con solidez técnica y participación ciudadana efectiva, generando confianza de la población en el proceso de evaluación ambiental."}</h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"PUPCA"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"El Procedimiento Único del Proceso de Certificación Ambiental (PUPCA) del Senace entró en vigencia desde el jueves 21 de julio del 2022."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"El PUPCA regula 10 procedimientos administrativos de competencia del Senace, entre ellos, la aprobación y modificación de Estudios de Impacto Ambiental detallados (EIA-d) e Estudios de Impacto Ambiental Semidetallados (EIA-sd), los Informes Técnicos Sustentatorios, la clasificación de proyectos de inversión, la aprobación de Términos de Referencia y Planes de Participación Ciudadana."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Asimismo, regula las acciones de acompañamiento y el proceso de participación ciudadana,  promoviendo la eficiencia y transparencia de la gestión ambiental a cargo del Senace."}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Las disposiciones del PUPCA fueron aprobadas por Decreto Supremo N° 004-2022-MINAM en enero de este año. De este modo, reduce la dispersión normativa y contribuye a brindar un servicio de certificación ambiental ágil que garantice calidad y eficacia."}</h1>', unsafe_allow_html=True)

#IMPORT DATA

#aprobados
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Aprobados"}</h1>', unsafe_allow_html=True)
dfa = pd.read_csv("https://raw.githubusercontent.com/taipeximena/PROGRA_PROY/main/Reporte_Proyecto_APROBADO%20(4).csv")
# Mostrar el DataFrame en la aplicación de Streamlit
st.write(dfa)
#desaprobados
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Desaprobados"}</h1>', unsafe_allow_html=True)
dfd = pd.read_csv("https://raw.githubusercontent.com/taipeximena/PROGRA_PROY/main/Reporte_Proyecto_DESAPROBADO.csv")
# Mostrar el DataFrame en la aplicación de Streamlit
st.write(dfd)

#evaluacion
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Evaluación"}</h1>', unsafe_allow_html=True)
dfe = pd.read_csv("https://github.com/taipeximena/PROGRA_PROY/raw/main/Reporte_Proyecto_EN%20EVALUACION.csv")
# Mostrar el DataFrame en la aplicación de Streamlit
st.write(dfe)

freq = dfa.groupby(['ACTIVIDAD']).size() 
st.bar_chart(freq)
st.bar_chart(data=dfa,x="TITULO_PROYECTO",y="ACTIVIDAD")

freq2 = dfd.groupby(['ACTIVIDAD']).size() 
st.bar_chart(freq2)
st.bar_chart(data=dfd,x="ACTIVIDAD",y="ID")

freq3= dfe.groupby(['ACTIVIDAD']).size() 
st.bar_chart(freq3)
st.bar_chart(data=dfe,x="ACTIVIDAD",y="ID")

st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"BIBLIOGRAFÍA"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Certificación Ambiental. (s. f.). Sistema Nacional de Evaluación de Impacto Ambiental. https://www.minam.gob.pe/seia/que-es-la-certificacion-ambiental/"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:15px;">{"Hoy entra en vigencia nuevo procedimiento único de certificación ambiental del Senace. (s. f.). Noticias - Servicio Nacional de Certificación Ambiental para las Inversiones Sostenibles - Plataforma del Estado Peruano. https://www.gob.pe/institucion/senace/noticias/633916-hoy-entra-en-vigencia-nuevo-procedimiento-unico-de-certificacion-ambiental-del-senace"}</h1>', unsafe_allow_html=True)
