from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('data_merged.csv')

fig = px.line(df, x="date", y="sales", title='Pink Morsel Sales Over Time')
fig.show()

app.layout = html.Div([
    dcc.Graph(
        id='pink-morsel-sales',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
