import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/news_aggregated.csv")

app = dash.Dash(__name__)
fig = px.bar(df, x='Theme', y='Title', title='News by Theme')

app.layout = html.Div([
    html.H1("News & Trends Monitor Dashboard"),
    dcc.Graph(figure=fig),
    html.H2("News Summaries"),
    html.Ul([html.Li(f"{row['Title']}: {row['Summary']}") for index, row in df.iterrows()])
])

if __name__ == '__main__':
    app.run_server(debug=True)
