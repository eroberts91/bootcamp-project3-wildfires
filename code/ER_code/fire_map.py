# save this as app.py
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import dash
from dash import dcc
from dash import html

#app data wrangling
##########################

#import cleaned csv file from data folder
large_fires_df = pd.read_csv('data/cleaned_largefires.csv')

#create list of unique years for building drop down menu
years_list = large_fires_df.FIRE_YEAR.unique().tolist()

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[{'label': k, 'value': k} for k in years_list],
        value=years_list[0]
    ),

    html.Hr(),
    dcc.Graph(id='display-selected-values'),

])

@app.callback(
    dash.dependencies.Output('display-selected-values', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    
    #update df by selected year
    select_df = large_fires_df[large_fires_df['FIRE_YEAR'] == value]
    
    
    fig = go.Figure(data=go.Scattergeo(
        locationmode = 'USA-states',
        lon = select_df['LONGITUDE'],
        lat = select_df['LATITUDE'],
        text = select_df['FIRE_NAME'],
        mode = 'markers',
        marker = dict(
            size = 0.1*np.sqrt(select_df['FIRE_SIZE']/3.1415),
            opacity = 1,
            reversescale = True,
            autocolorscale = False,
            symbol = 'circle',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = 'YlOrRd_r',
            cmin = 0,
            color = select_df['FIRE_SIZE'],
            cmax = select_df['FIRE_SIZE'].max(),
            colorbar_title=f"Wild Fires<br>{value}"
        )))

    fig.update_layout(
        title = f'Wild Fires during {value}<br>(Hover for Specific Fire Names)',
        margin=dict(l=20, r=20, t=20, b=20),
        height=800,
        geo = dict(
            scope='usa',
            projection_type='albers usa',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )
    return fig

if __name__ == '__main__':
    app.run_server()