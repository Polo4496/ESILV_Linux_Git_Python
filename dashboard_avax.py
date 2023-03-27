import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()
app.layout = html.Div([
    html.Div(children=[
        html.H1(children='Real-Time AVAX Crypto Tracker', 
            style={
                'color': '#e74c3c',
                'fontSize': 40,
                'fontFamily': 'Roboto, sans-serif',
                'fontWeight': 'bold',
                'textAlign': 'center',
                'textShadow': '1px 2px #CCCCCC'
            }
        ),
        html.Img(src='https://cryptologos.cc/logos/avalanche-avax-logo.png', style={'width': '50px', 'margin-left': '20px'}),
    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),

        html.Div(children='''
        AVAX is the native cryptocurrency of the Avalanche network. It can be used for transaction fees, staking, and governance on the network.
    ''', 
        style={
            'color': '#333333',
            'fontSize': 18,
            'fontFamily': 'Roboto, sans-serif',
            'fontStyle': 'italic',
            'textAlign': 'center',
            'textShadow': '1px 1px #f5f5f5',
            'marginTop': 20,
            'marginBottom': 20,
            'maxWidth': '80%',
            'marginLeft': 'auto',
            'marginRight': 'auto'
        }
    ),
    dcc.Graph(
        id='graph', 
        style={'height': '60vh', 'padding': '30px'}
    ),
    dcc.Interval(
        id='interval-component',
        interval=30000, # 30s
        n_intervals=0
    )
])

@app.callback(Output('graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def reload_data(n_intervals):
    df = pd.read_csv('avax_data.csv', names=["Date", "Price"])
    df['Date'] = pd.to_datetime(df['Date'])
    trace = go.Scatter(
        x=df['Date'],
        y=df['Price'],
        mode='lines',
        name='',
        line=dict(color='#e74c3c', width=2),
        hovertemplate="<b>AVAX Price:</b> %{y:.2f}<br>"
    )
    layout = go.Layout(
        xaxis=dict(
            showgrid=False,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label='15min', step='minute', stepmode='backward'),
                    dict(count=1, label='1h', step='hour', stepmode='backward'),
                    dict(count=3, label='3h', step='hour', stepmode='backward'),
                    dict(count=6, label='6h', step='hour', stepmode='backward'),
                    dict(count=1, label='1d', step='day', stepmode='backward'),
                    dict(count=7, label='1w', step='day', stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(visible=False),
            type='date'
        ),
        yaxis=dict(title='Price in $', showgrid=False),
        margin=dict(l=100, r=80, t=100, b=60),
        hovermode='x unified',
        plot_bgcolor='#f4f4fa',
        paper_bgcolor='#f4f4fa',
        font=dict(family='Roboto, sans-serif', size=12, color='#333333')
    )
    fig = go.Figure(data=[trace], layout=layout)
    fig.update_layout(
        hovermode="x",
        legend_orientation="h",
        legend=dict(
            y=-0.2,
            x=0.5,
            font=dict(size=10)
        ),
        title={
            'text': '<b>AVAX Price Trend over Time</b>',
            'font': {'size': 20},
            'x': 0.5,
            'y': 0.95,
            'xanchor': 'center',
            'yanchor': 'top',
            'pad': {'t': 20, 'b': 20, 'l': 20, 'r': 20}
        },
        images=[dict(
            source="https://cryptologos.cc/logos/avalanche-avax-logo.png",
            xref="paper", yref="paper",
            x=0.37, y=1.11,
            sizex=0.1, sizey=0.1,
            xanchor="right", yanchor="bottom"
          )]
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8000)