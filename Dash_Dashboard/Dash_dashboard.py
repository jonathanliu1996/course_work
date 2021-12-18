# Creating local dashboard using dash and plotly express


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objs as go


data = pd.read_csv("avocado.csv")

data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = dash.Dash(__name__)

selected_region = 'Albany'


region_list = data.region.unique()
region_list.sort()

graph_1_data = data.query("type == 'conventional' and region == 'Albany'")

app.layout = html.Div(
    children=[
        html.H1(children="Total Volume and Average Price by Region"),
        html.P(
            children="See below for Total Volume over Time by Region, and Average Price over Time by Region",
        ),
        dcc.Dropdown(id='region',
                options=[
                    {'label': i, 'value': i} for i in region_list
                ],
                value='Albany'
        ),
        dcc.Graph(id = 'graph_1'),
        dcc.Graph(id = 'graph_2'),
        ]
)

@app.callback(
    Output('graph_1', 'figure'),
    Input('region', 'value'))

def update_figure_1(selected_region):
    fig_1 = px.line(data.query("type == 'conventional' and region == " + "'" + selected_region + "'"), x = "Date", y = 'Total Volume',
        title="Total Volume " + selected_region)

    return fig_1



@app.callback(
    Output('graph_2', 'figure'),
    Input('region', 'value'))

def update_figure_2(selected_region):
    fig_2 = px.line(data.query("type == 'conventional' and region == " + "'" + selected_region + "'"), x = "Date", y = 'AveragePrice',
        title="Average Price " + selected_region)

    return fig_2

app.run_server()
