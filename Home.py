import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.connections import SQLConnection
from utils import viz_typeblock, top_first_country, top_first_country_stretched, release_year, popular_genre
from UI import clear_background,make_footer, make_header

clear_background()
make_footer()
make_header()
# st.write('hello world')
conn: SQLConnection = st.experimental_connection('sickathon-mentor',type='sql')
df: pd.DataFrame = conn.query('select * from netflix_titles')


st.markdown(f"<h1 style='text-align:center;'>Netflix Analysis for Movie Maker</h1>",unsafe_allow_html=True)
st.header(f'Raw Data from SQL Database (Neflix Titles)')
st.write('Data mentah dari SQL Database (Netflix Titles) yang diambil dari Kaggle.')
st.dataframe(df)
st.write(f'Data ini terdiri dari {len(df)} baris dan {len(df.columns)} kolom.')

st.divider()
st.header(f'Persebaran Tipe Netflix')
st.write('Persebaran tipe Netflix (Movie atau TV Show) dari data Netflix Titles.')
type_block: plt.Figure = viz_typeblock(df=df)
st.pyplot(type_block)
st.write('Dari data Netflix Titles, terdapat 70% Movie dan 30% TV Show. Lebih banyak perusahaan yang memproduksi Movie daripada TV Show.')

st.divider()
st.header(f'Persebaran Konten Netflix')
st.write('Persebaran konten Netflix (Movie atau TV Show) dari data Netflix Titles.')
top_10: plt.Figure = top_first_country(df=df)
st.pyplot(top_10)
st.write('Dari data di-atas, dapat dilihat bahwa Amerika Serikat merupakan negara yang paling banyak memproduksi konten Netflix dengan total ±4044 konten. Selain itu, dapat dilihat bahwa India merupakan negara yang paling banyak memproduksi konten Netflix kedua setelah Amerika Serikat.')

st.divider()
st.header(f'Persebaran Konten Netflix')
st.write('Persebaran konten Netflix (Movie atau TV Show) dari data Netflix Titles.')
selected_type = st.selectbox('Pilih Tipe', ['Movie', 'TV Show'], key='select-type', index=0, help='Pilih tipe konten yang ingin dilihat persebarannya.')
top_10_stretched: plt.Figure = top_first_country_stretched(df=df, type=selected_type)
st.pyplot(top_10_stretched)
if(selected_type == 'Movie'):
    st.write('Data di-atas menunjukkan bahwa USA merupakan negara yang paling banyak memproduksi Movie Netflix dengan total 2805 Movie. Disusul India dengan 927 Movie hasil produksinya.')
elif(selected_type == 'TV Show'):
    st.write('Data di-atas menunjukkan bahwa USA merupakan negara yang paling banyak memproduksi TV Show Netflix dengan total 1239 TV Show. Disusul United Kingdom dengan 246 TV Show hasil produksinya.')

st.divider()
st.header(f'Persebaran Tahun Rilis')
st.write('Persebaran tahun rilis dari data Netflix Titles.')
fig_release_year: plt.Figure = release_year(df=df, start=2000)
st.pyplot(fig_release_year)
st.write('Dari data di-atas, dapat dilihat bahwa tipe Movie pada Netflix terus mengalami kenaikan pada tiap tahunnya mengungguli TV Show. Pada tahun 2015 terjadi lonjakan besar pada kedua tipe konten Netflix. Hal ini menunjukkan bahwa pada tahun 2015, Netflix mulai populer di kalangan masyarakat.')

st.divider()
st.header(f'Persebaran Genre Populer')
st.write('Persebaran genre populer dari data Netflix Titles.')
fig_popular_genre: plt.Figure = popular_genre(df=df)
st.pyplot(fig_popular_genre)
st.write('Berdasarkan data di-atas, dapat dilihat bahwa genre populer pada Netflix adalah International Movies, Drama, dan Comedies. Hal ini menunjukkan bahwa pengguna Netflix menyukai International Movies, Dramas dan Comedy. Hal ini dapat menjadi acuan bagi pembuat konten untuk membuat konten yang sesuai dengan genre populer tersebut.')
