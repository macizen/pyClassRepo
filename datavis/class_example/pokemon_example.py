import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("pokemon.csv")

top_fire_pokemon = df[df["Type 1"] == "Fire"].nlargest(10, "Attack")
top_water_pokemon = df[df["Type 1"] == "Water"].nlargest(10, "Attack")

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=[
        "top 10 fire pokemon by attack",
        "top 10 water pokemon by attack"
    ]
)

fig.add_trace(
    go.Bar(
        x=top_fire_pokemon["Name"],
        y=top_fire_pokemon["Attack"],
        marker_color='firebrick',
        text=top_fire_pokemon["Attack"],
        textposition='auto',
        hoverinfo='text',
        hovertext=[f"{name}<br>Attack: {attack}" for name, attack in zip(top_fire_pokemon["Name"], top_fire_pokemon["Attack"])]
    ),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
        x=top_water_pokemon["Name"],
        y=top_water_pokemon["Attack"],
        marker_color='royalblue',
        text=top_water_pokemon["Attack"],
        textposition='auto',
        hoverinfo='text',
        hovertext=[f"{name}<br>Attack: {attack}" for name, attack in zip(top_water_pokemon["Name"], top_water_pokemon["Attack"])]
    ),
    row=1, col=2
)

fig.update_layout(
    title_text="top 10 pokemon by attack for fire and water types",
    height=500,
    width=1000,
    showlegend=False
)

fig.update_xaxes(tickangle=45)

fig.show()