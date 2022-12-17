from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('data_merged.csv')

COLORS = {
    'font': '#33BBFF'
}

app.layout = html.Div([
    html.H1("Pink Morsel Sales", style={'color': COLORS['font']}),
    html.Div([
        dcc.RadioItems(
            ['North', 'East', 'South', 'West', 'All'],
            'All',
                id='radio-button-value',
                inline=True
            )
        ], style={'width': '48%', 'display': 'inline-block', 'textAlign': 'center'}),
    dcc.Graph(id='graph-with-radio-buttons'),
])

@app.callback(
    Output('graph-with-radio-buttons', 'figure'),
    Input('radio-button-value', 'value'))
    
def update_graph(radio_button_value):
    if radio_button_value == 'All':
        dff = df
    else:
        dff = df[df['region'] == radio_button_value.lower()]

    fig = px.line(dff, x="date", y="sales", title='Pink Morsel Sales Over Time')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
