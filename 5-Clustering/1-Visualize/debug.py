# %pip install seaborn
import matplotlib.pyplot as plt
import pandas as pd

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filepath = '/home/kalebkei/AIResearch/ML-For-Beginners/5-Clustering/data/nigerian-songs.csv'
if not os.path.exists(filepath):
    raise FileNotFoundError(f"{filepath} does not exist")

df = pd.read_csv(filepath)
df.head()

df.info()

df.isnull().sum()

df.describe()

top = df['artist_top_genre'].value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=top[:5].index,y=top[:5].values)
plt.xticks(rotation=45)
plt.title('Top genres',color = 'blue')

df = df[df['artist_top_genre'] != 'Missing']
top = df['artist_top_genre'].value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=top.index,y=top.values)
plt.xticks(rotation=45)
plt.title('Top genres',color = 'blue')

df = df[(df['artist_top_genre'] == 'afro dancehall') | (df['artist_top_genre'] == 'afropop') | (df['artist_top_genre'] == 'nigerian pop')]
df = df[(df['popularity'] > 0)]
df = df.dropna(subset=['danceability'])
df = df[pd.to_numeric(df['popularity'], errors='coerce').notnull()]
top = df['artist_top_genre'].value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=top.index,y=top.values)
plt.xticks(rotation=45)
plt.title('Top genres',color = 'blue')

df = df[df['popularity'].apply(lambda x: str(x).isdigit())]
corrmat = df.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)