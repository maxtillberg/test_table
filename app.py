import dash
import dash_table
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df = pd.read_csv('2011_us_ag_exports.csv')
df1 = df[0:6]
app = dash.Dash(__name__)

server = app.server

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df1.columns],
    data=df1.to_dict("rows"),
)

if __name__ == '__main__':
    app.run_server(debug=True)
