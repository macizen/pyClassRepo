import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# dataset im using from https://www.kaggle.com/code/varunsaikanuri/spotify-data-visualization/input
df = pd.read_csv('spotify_data/songs_normalize.csv')

# some entries had multiple genres so i had to split them for re-organization
genres = df['genre'].str.split(', ').explode('genre')
unique_genres = genres.unique()
df_exploded_by_genres = df.assign(genre=genres)
# now re grouping each new with individual genre to loudness
loudness_by_genre = df_exploded_by_genres.groupby('genre')['loudness'].apply(list).reset_index()

# the keys in the dataset are written as integers so I need a list to turn the integers to the key names
keys = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
df['key_name'] = df['key'].map({i: keys[i] for i in range(12)})

# subplots so i can have three types on the same screen
fig = make_subplots(rows=2, cols=2, specs=[[{"colspan": 2}, None], [{}, {}]])


# box plots showing loudness by genre
for i, row in loudness_by_genre.iterrows():
    fig.add_trace(go.Box(
        y=row['loudness'],
        name=row['genre'],
        boxpoints='all',
        jitter=0.3
        ),row=1, col=1)

# bar chart that has each song in the 12 keys, with the song name and artist on hover
fig.add_trace(go.Bar(
    x = df['key_name'],
    y = df['song'],
    customdata=np.array([df['song'], df['artist']]).T,
    hovertemplate="Song Name: %{customdata[0]}<br>Artist: %{customdata[1]}"),
    row=2, col=1)

# simple scatter plot that shows relationship between tempo and 'energy'
fig.add_trace(go.Scatter(
    x = df['tempo'],
    y = df['energy'],
    mode = 'markers'
    ),row=2, col=2)

# remove yaxes labels for bar graph
fig.update_yaxes(showticklabels=False, row=2, col=1)

# update layout to make the charts/graphs more readable
fig.update_layout(
    showlegend=False,
    title_text="spotify music data",
    yaxis_title="loudness (dB)",
    xaxis_title="genre",
    xaxis2=dict(
        title=dict(
            text="song key signatures"
        )
    ),
    xaxis3=dict(
        title=dict(
            text="tempo (bpm)"
        )
    ),
    yaxis3=dict(
        title=dict(
            text="energy (0-1)"
        )
    )
)

fig.show()