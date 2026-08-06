import streamlit as st
import Functions as fn
import pandas as pd

path = './data/vgsales-selected-columns.csv'

data = pd.read_csv(path)


st.set_page_config(page_title="Dashboard", layout="wide")


st.title("Los artistas más escuchado en 2025 en Spotify ")

col1, col2, col3 = st.columns(3)

with col1:
    num_stream = data.sort_values(by="Total Streams (in millions)", ascending=False)

    artist = num_stream['Artist Name'].iloc[0]
    stream = num_stream['Total Streams (in millions)'].iloc[0]

    st.text(f"Género más escuchado: {artist}")
    st.metric(label=f"Reproducciones en Millones:", value=stream, format="%.2f%")

with col2:
    fst_genre = fn.most_genre(data=data)

    genre = fst_genre['Primary Genre'].iloc[0]
    genre_prcnt = fst_genre['Percent'].iloc[0]

    st.text(f"Género más escuchado: {genre}")
    st.metric(label="Porcentaje:", value=genre_prcnt*100, format="%f%%")

with col3:
    dt_country = fn.most_country(data=data)

    country = dt_country['Country of Origin'].iloc[0]
    country_prcnt = dt_country['Percent'].iloc[0]

    st.text(f"País de orígen más escuchado: {country}")
    st.metric(label="Porcentaje:", value=country_prcnt*100, format="%f%%")


graph1, graph2 = st.columns(2)

with graph1:
    fn.graph_data(data, 0)

with graph2:
    fn.graph_data(data, 1)

graph3, graph4 = st.columns(2)

with graph3:
    fn.graph_data(data, 2)

with graph4:
    fn.graph_data(data, 3)