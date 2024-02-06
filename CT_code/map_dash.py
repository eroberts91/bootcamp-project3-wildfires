import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load data
top_10_file_path = 'top_10_by_cause.csv'
top_10_df = pd.read_csv(top_10_file_path)

# Create Dash app
app = dash.Dash(__name__)

# Create scatter_geo figure
fig = px.scatter_geo(
    top_10_df,
    lat='LATITUDE',
    lon='LONGITUDE',
    text='FIRE_NAME',
    color='CAUSE',
    size='FIRE_SIZE',
    hover_name='CAUSE',
    title='Largest Fires By Cause',
    scope='usa',
    size_max=40,
    hover_data={'FIRE_NAME': True, 'FIRE_SIZE': True, 'CAUSE': True, 'LATITUDE': True, 'LONGITUDE': True},
)

# Adjust so no descriptive text showing over circles
fig.update_traces(text='')

# Dropdown options
individual_causes = top_10_df['CAUSE'].unique()
dropdown_options = [{'label': cause, 'value': cause} for cause in individual_causes]

# Layout
app.layout = html.Div([
    dcc.Graph(figure=fig, id='scatter-geo'),
    dcc.Dropdown(
        id='cause-dropdown',
        options=[{'label': 'All Causes', 'value': 'All Causes'}] + dropdown_options,
        value='All Causes',
        multi=False,
        style={'width': '50%'}
    ),
])

# Callback to update scatter_geo based on dropdown selection
@app.callback(
    Output('scatter-geo', 'figure'),
    [Input('cause-dropdown', 'value')]
)
def update_map(selected_cause):
    if selected_cause == 'All Causes':
        filtered_df = top_10_df
    else:
        filtered_df = top_10_df[top_10_df['CAUSE'] == selected_cause]

    updated_fig = px.scatter_geo(
        filtered_df,
        lat='LATITUDE',
        lon='LONGITUDE',
        text='FIRE_NAME',
        color='CAUSE',
        size='FIRE_SIZE',
        hover_name='CAUSE',
        title=f'Largest Fires By Cause - {selected_cause}',
        scope='usa',
        size_max=40,
        hover_data={'FIRE_NAME': True, 'FIRE_SIZE': True, 'CAUSE': True, 'LATITUDE': True, 'LONGITUDE': True},
    )

    updated_fig.update_traces(text='')

    return updated_fig

# Run the app in external mode
if __name__ == '__main__':
    app.run_server(port=8050)
