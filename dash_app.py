# Importing the important things!
import re  # For formatting the date values into ints

import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html, Input, Output


def datify(x):
    return re.sub("-", "", x)  # Formatting the date values into ints Credit: ChatGPT


# Take data from the CSV to display
df = pd.read_csv("Ozone_daily_44201_2024.csv",
                 dtype={'State Code': int, 'County Code': int, 'Site Num': int, 'Parameter Code': int, 'POC': int,
                        'Latitude': float, 'Longitude': float, 'Datum': str, 'Parameter Name': str,
                        'Sample Duration': str, 'Pollutant Standard': str, 'Date Local': str, 'Units of Measure': str,
                        'Event Type': str, 'Observation Count': int, 'Observation Percent': float,
                        'Arithmetic Mean': float, '1st Max Value': float, 'AQI': str, 'Method Code': str,
                        'Method Name': str, 'Local Site Name': str, 'Address': str, 'State Name': str,
                        'County Name': str, 'City Name': str, 'CBSA Name': str, 'Date of Last Change': str})
df["State Name"] = pd.Series(df["State Name"])
df["Date Local"] = df["Date Local"].apply(datify)
df["Date Local"] = df["Date Local"].astype(int)
print(df[["State Name", "Observation Percent"]].head())

min_date = df['Date Local'].min()
max_date = df['Date Local'].max()
dates = {int(val): str(val) for val in df['Date Local'].unique()}

# App Layout

stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div([
    html.H1(children="Ozone Levels By State and County, 2024", style={'textAlign': 'center'}),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {"label": x, "value": x}
            for x in sorted(df["State Name"].unique())
        ],
        value="Alabama",
        clearable=False,
    ),
    html.Div(dcc.Graph(id="bar-chart", figure={})),
    html.Div(
        dcc.Slider(
            id="slider",
            min=min_date,
            max=max_date,
            value=min_date,
            step=None,
            marks=dates,
            tooltip={"always_visible": True, "placement": "top", }
        )
    ),
    html.H3(children="Date", style={'textAlign': 'center'})
], className="row")


# Callback Time
# Change State With Dropdown
@app.callback(
    Output("bar-chart", "figure"),
    Input("dropdown", "value"), Input("slider", "drag_value"),
)
def update_bar_chart(state, date):
    print(f"Values chosen by user: {state, date}")

    selected_state = [state]
    selected_date = [date]
    df_filtered = df[df["State Name"].isin(selected_state)]
    df_filtered_twice = df_filtered[df_filtered["Date Local"].isin(selected_date)]
    df_filtered_thrice = (df_filtered_twice.groupby(['State Name', 'Date Local', 'County Name'], as_index=False)[
        'Observation Percent'].mean())
    # Allows me to grab the mean of each county for each day; there may be multiple values per county. Credit: ChatGPT
    chart = px.bar(
        data_frame=df_filtered_thrice,
        x="County Name",
        y="Observation Percent",
        log_y=False,
        labels={
            "Observation Percent": "Observed Percentage",
            "County Name": "County",
        },
    )
    chart.update_layout(yaxis=dict(range=[0, 1600]))  # Set Y-axis from 0 to 1600 Credit:ChatGPT
    return chart


if __name__ == "__main__":
    app.run_server(debug=True)
