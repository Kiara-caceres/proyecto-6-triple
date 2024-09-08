import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
st.header(' Venta de Coches')

build_histogram = st.checkbox('Construir un histograma')#construir casilla

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
hist_button2 = st.button('Construir grafica de dispersion') # crear un botón
        
if hist_button2: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de una grafica de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # crear un grafica
    fig = px.scatter(car_data, y="price", x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
