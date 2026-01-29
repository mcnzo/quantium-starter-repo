from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# 1. Initialise Dash app
app = Dash(__name__)

# 2. Load and prep data
df = pd.read_csv('formatted_data.csv')
# Ensure date is in datetime format and sorted correctly
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# 3. Create line chart
fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Trends",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

# 4. Define visual layout
app.layout = html.Div(children=[
    html.H1(children='Soul Foods Pink Morsel Visualiser', style={'textAlign': 'center'}),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# 5. Run app
if __name__ == '__main__':
    app.run(debug=True)