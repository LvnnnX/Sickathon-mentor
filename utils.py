# import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

movie_color = '#7a1214'
tvshow_color = '#012b78'

color_map:list[str] = ['#f5f5f1' for _ in range(10)]
color_map[0] = color_map[1] = color_map[2] = '#7a1214' 

def viz_typeblock(df:pd.DataFrame) -> plt.Figure:
    """Visualisasi type block dari dataframe netflix_titles"""
    fig, ax = plt.subplots()
    x = df.groupby(['type'])['type'].count()
    y = len(df)
    r = ((x/y)).round(2)
    mf_ratio = pd.DataFrame(r).T
    
    fig, ax = plt.subplots(1,1, figsize=(6.5, 2.5), facecolor='#0e1117')
    ax.set_facecolor('#0e1117')
    
    ax.barh(mf_ratio.index, mf_ratio['Movie'], color=movie_color, label='Movie')
    ax.barh(mf_ratio.index, mf_ratio['TV Show'], left=mf_ratio['Movie'], color=tvshow_color, label='TV Show')
    
    ax.set_xlim(0,1)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    
    for i in mf_ratio.index:
        ax.annotate(f"{int(mf_ratio['Movie'][i]*100)}%", xy=(mf_ratio['Movie'][i]/2, i), va='center', ha='center', color='white', fontweight='bold', fontsize=30)
        ax.annotate(f"Movies", xy=(mf_ratio['Movie'][i]/2, -0.15), va='center', ha='center', color='white', fontweight='bold', fontsize=10)
        
    for i in mf_ratio.index:
        ax.annotate(f"{int(mf_ratio['TV Show'][i]*100)}%", xy=(mf_ratio['Movie'][i]+mf_ratio['TV Show'][i]/2, i), va='center', ha='center', color='white', fontweight='bold')
        ax.annotate(f"TV Show", xy=(mf_ratio['Movie'][i]+mf_ratio['TV Show'][i]/2, -0.1), va='center', ha='center', color='white', fontweight='bold', fontsize=7)
        
        
    # fig.text(0.28, 0.9, 'Persebaran Tipe Netflix', fontsize=15, fontweight='bold')
    
    for s in ['top', 'left', 'right', 'bottom']:
        ax.spines[s].set_visible(False)
        
    ax.legend().set_visible(False)
    return fig

def fill_remove_top10(df: pd.DataFrame) -> pd.DataFrame:
    """Mengisi missing value dengan mode dan mencari top 10 negara"""
    df_now = df['country'].apply(lambda x: x.split(',')[0])
    
    df_now.replace({'': np.nan}, inplace=True)
    df_now = df_now.fillna(df_now.mode()[0])
    
    df_now = df_now.value_counts().sort_values(ascending=False).head(10)
    
    return df_now



def top_first_country(df: pd.DataFrame) -> plt.Figure:
    """Visualisasi top 10 negara dari dataframe netflix_titles"""
    df_tfc = fill_remove_top10(df)
    
    fig, ax = plt.subplots(1,1, figsize=(12,6))
    ax.bar(df_tfc.index, df_tfc, color=color_map, edgecolor='darkgray')
    
    for i in df_tfc.index:
        ax.annotate(f"{df_tfc[i]}", xy=(i, df_tfc[i]+50), va='center', ha='center', color='black')
        
    for s in ['top', 'left', 'right']:
        ax.spines[s].set_visible(False)
        
    fig.text(0.1, 0.95, 'Top 10 Negara', fontsize=15, fontweight='bold')
    fig.text(0.1, 0.9, 'Negara dengan jumlah konten netflix terbanyak', fontsize=12)
    ax.tick_params(axis='both', which='both', length=0)
    
    ax.grid(axis='y', linestyle='-', alpha=0.4)
    ax.set_axisbelow(True)
    grid_y_ticks= np.arange(0, 4500, 500)
    ax.set_yticks(grid_y_ticks)
    
    return fig

def top_first_country_stretched(df: pd.DataFrame, type:str | None = None) -> plt.Figure:
    """Visualisasi top 10 negara dari dataframe netflix_titles dengan tipe tertentu"""
    if type is None: type = 'Movie'
    elif type not in ['Movie', 'TV Show']: raise ValueError('type must be either "Movie" or "TV Show"')
    
    df10country: pd.DataFrame = df
    df10country['country'] = df['country'].apply(lambda x: x.split(',')[0])
    df10country.replace({'': np.nan}, inplace=True)
    df10country['country'] = df10country['country'].fillna(df10country['country'].mode()[0])
    
    df10country = df10country[df10country['type'] == f'{type}']
    df10country = df10country[['country', 'type']].value_counts().sort_values(ascending=False).head(10)
    
    xticks_label:list = df10country.index.unique().map(lambda x: x[0])
    
    fig, ax = plt.subplots(1,1, figsize=(12,6))

    df10country.plot(kind='barh', ax=ax, color=color_map, edgecolor='darkgray')
    plt.yticks(rotation=0, ticks=np.arange(0,10), labels=xticks_label)
    plt.ylabel('')
    plt.xticks(np.arange(0,3000,500))
    
    ax.invert_yaxis()
    
    fig.text(0.12, 0.9, f'Persebaran Tipe {type} pada 10 Negara Teratas', fontsize=15, fontweight='bold')
    
    for i in range(len(df10country.index)):
        ax.annotate(f"{df10country[i]}", xy=(df10country[i]+50, i), va='center', ha='center', color='black')
        
    return fig


def release_year(df: pd.DataFrame, start:int | None = None) -> plt.Figure:
    """Visualisasi rilis tahun dari dataframe netflix_titles"""
    if start is None: start = 2000
    elif start < 1925 or start > 2020: raise ValueError('start must be greater than 1925')
    
    df_ry = df[['release_year', 'type']].value_counts().sort_index()
    df_ry = df_ry[df_ry.index.get_level_values(0) >= start]
    df_ry = df_ry.unstack()
    
    fig, ax = plt.subplots(1,1, figsize=(12,6))
    
    ax.plot(df_ry.index, df_ry['Movie'], color=movie_color, label='Movie')
    ax.fill_between(df_ry.index, df_ry['Movie'], color=movie_color, alpha=1)
    
    ax.plot(df_ry.index, df_ry['TV Show'], color=tvshow_color, label='TV Show')
    ax.fill_between(df_ry.index, df_ry['TV Show'], color=tvshow_color, alpha=1)
    
    for s in ['top', 'left', 'right','bottom']:
        ax.spines[s].set_visible(False)
        
    ax.legend().set_visible(False)
    ax.set_xticks(np.arange(start, 2025, 5))
    ax.set_yticks(np.arange(0, 1000, 200))
    ax.set_yticklabels([f'{i}' for i in range(0,1000,200)])
    
    ax.grid(axis='y', linestyle='-', alpha=0.4)
    ax.set_axisbelow(True)
    ax.tick_params(axis='both', which='both', length=0)
    
    fig.text(0.1, 0.95, 'Persebaran Tipe Netflix', fontsize=15, fontweight='bold')
    fig.text(0.1, 0.9, 'Negara dengan jumlah konten netflix terbanyak', fontsize=12)
    fig.text(0.13,0.25,"Movie", fontweight="bold", fontfamily='serif', fontsize=15, color=movie_color)
    fig.text(0.19,0.25,"|", fontweight="bold", fontfamily='serif', fontsize=15, color='black')
    fig.text(0.2,0.25,"TV Show", fontweight="bold", fontfamily='serif', fontsize=15, color=tvshow_color)

    return fig

def popular_genre(df: pd.DataFrame) -> plt.Figure:
    """Visualisasi genre terpopuler dari dataframe netflix_titles"""
    df_pg = df
    df_pg['listed_in'] = df_pg['listed_in'].apply(lambda x: x.replace(' ,',',').replace(', ',',').split(','))
    Types = []
    for i in df_pg['listed_in']: Types += i
    Types = pd.Series(Types).value_counts().head(10)
    
    
    fig, ax = plt.subplots(1,1, figsize=(12,6))

    Types.plot(kind='barh', ax=ax, color=color_map, edgecolor='darkgray')
    plt.yticks(rotation=0, ticks=np.arange(0,10))
    plt.ylabel('')
    plt.xticks(np.arange(0,3000,500))
    
    ax.invert_yaxis()
    
    fig.text(0.12, 0.9, f'Persebaran Genre pada Netflix', fontsize=15, fontweight='bold')
    
    for i in range(len(Types.index)):
        ax.annotate(f"{Types[i]}", xy=(Types[i]+50, i), va='center', ha='center', color='black')
        
    return fig
