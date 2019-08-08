import plotly as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

tips = px.data.tips()
col_options = [dict(label=x, value=x) for x in tips.columns]
dimensions = ["x", "y", "color", "facet_col", "facet_row"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Demo: Plotly Express in Dash with Tips Dataset"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)


@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y, color, facet_col, facet_row):
    return px.scatter(
        tips,
        x=x,
        y=y,
        color=color,
        facet_col=facet_col,
        facet_row=facet_row,
        height=700,
    )


app.run_server(debug=True)

#import dash
#import dash_table
#import pandas as pd

#df = pd.read_csv('2011_us_ag_exports.csv')
#df1 = df[0:6]
#app = dash.Dash(__name__)

#server = app.server

#app.layout = dash_table.DataTable(
#    id='table',
#    columns=[{"name": i, "id": i} for i in df1.columns],
#    data=df1.to_dict("rows"),
#)

#if __name__ == '__main__':
#    app.run_server(debug=True)
