from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Load and prep data
df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# Layout with styling
app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '20px', 'fontFamily': 'sans-serif'}, children=[
    html.H1(
        children='Pink Morsel Sales Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}
    ),

    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all', # Default value
            inline=True,
            style={'display': 'inline-block'}
        ),
    ]),

    dcc.Graph(id='sales-line-chart')
])

# Callback to update graph based on radio button
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Pink Morsel Sales: {selected_region.capitalize()}",
        line_shape="spline", # Makes the line look smoother
        render_mode="svg"
    )
    
    fig.update_layout(
        transition_duration=500,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#f9f9f9'
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)