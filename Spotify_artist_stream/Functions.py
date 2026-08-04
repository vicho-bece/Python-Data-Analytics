import pandas as pd
import streamlit as st
import plotly.express as px

def most_genre(data:pd.DataFrame) -> pd.DataFrame:

    generos = data.groupby(['Primary Genre']).size().reset_index(name='Quantity')
    generos = generos.sort_values(by="Quantity", ascending=False)

    total = generos['Quantity'].sum()

    generos['Percent'] = generos['Quantity'] / total

    return generos

def most_country(data:pd.DataFrame) -> pd.DataFrame:

    country = data.groupby(['Country of Origin']).size().reset_index(name='Quantity')
    country = country.sort_values(by="Quantity", ascending=False)

    total = country['Quantity'].sum()

    country['Percent'] = country['Quantity'] / total

    return country

def graph_data(data:pd.DataFrame, option):

    match option:
        case 0: 
            datos = most_genre(data)
            title = "Porcentajes de los generós escuchados en 2025"
            labelx = 'Primary Genre'
            labely = 'Percent'

        case 1:
            datos = data.groupby(['Debut Year']).size().reset_index(name='Quantity')
            datos = datos.sort_values(by="Quantity", ascending=False)

            title = "Número de artistas que consiguieron su debut según el año"
            labelx = 'Debut Year'
            labely = 'Quantity'

        case 2:
            datos = data.groupby(['Primary Language']).size().reset_index(name='Quantity')
            datos = datos.sort_values(by="Quantity", ascending=False)

            total = datos['Quantity'].sum()

            datos['Percent'] = datos['Quantity'] / total

            title = "Idioma más escuchado en 2025"
            labelx = 'Primary Language'
            labely = 'Percent'

        case 3:
            datos = data.groupby(['Sex']).size().reset_index(name='Quantity')
            datos = datos.sort_values(by="Quantity", ascending=False)

            total = datos['Quantity'].sum()

            datos['Percent'] = datos['Quantity'] / total

            title = "Género de artistas más escuchado en 2025"
            labelx = 'Sex'
            labely = 'Percent'


    st.text(title)
    fig = px.bar(datos, x=labelx, y=labely)
    st.plotly_chart(fig, width='stretch', config = {'scrollZoom': False, 'zoom': False, 'displayModeBar':False})
