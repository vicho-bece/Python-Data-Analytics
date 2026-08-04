import pandas as pd

def most_genre(data:pd.DataFrame) -> pd.DataFrame:

    generos = data.groupby(['Primary Genre']).size().reset_index(name='counts')
    generos = generos.sort_values(by="counts", ascending=False)

    total = generos['counts'].sum()

    for i in generos.iterrows():
        generos['percent'] = generos['counts'] / total

    return generos

def most_country(data:pd.DataFrame) -> pd.DataFrame:

    country = data.groupby(['Country of Origin']).size().reset_index(name='counts')
    country = country.sort_values(by="counts", ascending=False)

    total = country['counts'].sum()

    for i in country.iterrows():
        country['percent'] = country['counts'] / total

    return country