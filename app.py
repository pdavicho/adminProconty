import streamlit as st
from appMops import mainMops
from appIps import mainJunos

st.sidebar.image('proconty.png')
#st.sidebar.title("Pasos a Producción")
menuPrincipal = st.sidebar.radio('Menu Principal', ['Información','1. Junos', '2. Mops'])

if menuPrincipal == 'Información':
    st.title("Pasos a Producción")
    st.write("""Seleccionar en el Menu Principal, una de las siguientes opciones:""")
    st.subheader(' 1. Junos ')
    st.write('(Permite generar archivo .csv para cargar las IPs maliciosas en el FW Atlas, así como la comparación de nuevas IPs con la base de datos)')
    st.subheader('2. Mops ')
    st.write('(Permite generar MOPs genéricos para la gestión por parte de N2 o Proveedores)')
        
elif menuPrincipal == '1. Junos':
    #st.sidebar.text("JUNOS")
    st.title('[Archivo CSV para IPs Maliciosas]')
    mainJunos()
    
elif menuPrincipal == '2. Mops':
    #st.sidebar.text("MOPS")
    st.title('[MOPs Gestión - Preaprobadas]')
    mainMops()

st.sidebar.write('All rights reserved. Developed by **[David Minango]**')
        
