from importlib import import_module
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import SelectDb
from datetime import date
import dash_table

plot_arr = SelectDb.getCurDay()
prog_name = plot_arr[0]
prog_id = plot_arr[2]
opt = []
i=0 # список работавших программ
while i<len(prog_name):
    opt.append({})
    opt[i]['label'] = prog_name[i]
    opt[i]['value'] = prog_id[i]
    i = i+1

app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Time Tracer:'),

    dash_table.DataTable(
    id='title_table',
    children="callback not executed",
    style_cell={'textAlign': 'left'},
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    },
    ),
    
dcc.RadioItems(
    id='cur_chart',
    options=[
        {'label': 'Chart', 'value': 'chart'},
        {'label': 'Pie', 'value': 'pie'}
    ],
    value='pie',
    labelStyle={'display': 'inline-block'}
),
dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2023, 9, 19),
        initial_visible_month=date(2017, 8, 5),
        end_date=date(2017, 8, 25)
    ),

dcc.Dropdown(
        id='select_prog',
        options = opt,
        value=''
    ),

dcc.Graph(  
    id='example-graph'
)
])

@app.callback(
        Output('example-graph', 'figure'),    
        Input('cur_chart', 'value')
    )
def check(input_value):
    if input_value == 'pie':
        plot = SelectDb.getCurDay()
        fig = go.Figure(data=[go.Pie(labels=plot[0], values=plot[1], hole=.8)]) #круговая диаграмма бублик
        return fig
    elif input_value == 'chart': # диограмма столбик
        plot = SelectDb.getCurDay()
        fig = go.Figure(
            data=[go.Bar(x=plot[0], y=plot[1])],
            layout=go.Layout(
                title=go.layout.Title(text="A Figure Specified By A Graph Object")
            )
        )
        return fig

@app.callback(
    Output('title_table', 'data'),
    Output('title_table', 'columns'),
    Input('select_prog', 'value')
    )
def createTable(prog_id):
    data = SelectDb.getTitleForProg(prog_id)
    columns=[{"name": 'Title', "id": 'title'},
             {"name": 'Time', "id": 'time'},
             {"name": 'Date', "id": 'date'}]
    return data, columns
 
app.run_server(debug=True)