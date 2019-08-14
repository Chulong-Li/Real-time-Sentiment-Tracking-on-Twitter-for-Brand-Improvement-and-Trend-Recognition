import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import settings

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('sample_data.csv')
df['created_at'] = pd.to_datetime(df['created_at'])
 # Clean and transform data to enable time series
result = df.groupby([pd.Grouper(key='created_at', freq='2s'), 'polarity']).count().unstack(fill_value=0).stack().reset_index()
result = result.rename(columns={"id_str": "Num of '{}' mentions".format(settings.TRACK_WORDS[0]), "created_at":"Time in UTC"})  
time_series = result["Time in UTC"][result['polarity']==0].reset_index(drop=True)

server = app.server

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Fertility rate, total (births per woman)'
            ),
            dcc.RadioItems(
                id='crossfilter-xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='crossfilter-yaxis-column',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Life expectancy at birth, total (years)'
            ),
            dcc.RadioItems(
                id='crossfilter-yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

    html.Div([
        html.Div([
            dcc.Graph(
                id='crossfilter-indicator-scatter',
                figure={
                    'data': [
                        go.Scatter(
                            x=time_series,
                            y=result["Num of '{}' mentions".format(settings.TRACK_WORDS[0])][result['polarity']==0].reset_index(drop=True),
                            name="Neural",
                            opacity=0.8
                        ),
                        go.Scatter(
                            x=time_series,
                            y=result["Num of '{}' mentions".format(settings.TRACK_WORDS[0])][result['polarity']==-1].reset_index(drop=True),
                            name="Negative",
                            opacity=0.8
                        ),
                        go.Scatter(
                            x=time_series,
                            y=result["Num of '{}' mentions".format(settings.TRACK_WORDS[0])][result['polarity']==1].reset_index(drop=True),
                            name="Positive",
                            opacity=0.8
                        )
                    ]
                }
            )

        ]),

        html.Div([
            dcc.Graph(id='x-time-series'),
            dcc.Graph(id='y-time-series'),
        ], style={'display': 'inline-block', 'width': '49%'})
    ]),
        
    html.Div([
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
            value=5
        )
    ])
])
#, style={'columnCount': 1}

if __name__ == '__main__':
    app.run_server(debug=True)