import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import ta

app = dash.Dash()
# Main html page
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
    html.Div([
        html.P('Last Price:', 
            style={'display': 'inline-block', 
                'marginRight': '10px',
                'fontSize': '20px',
            }
        ),
        html.Span(id='last-price',
            style={'fontSize': '20px', 'color': '#e74c3c','textShadow': '1px 1px #CCCCCC'})
        ], 
        style={'display': 'flex', 
            'align-items': 'center', 
            'justify-content': 'center', 
            'marginBottom': '-15px',
            'fontFamily': 'Roboto, sans-serif',
            'textAlign': 'center',
            'textShadow': '1px 1px #f5f5f5',
            'fontWeight': 'bold',
        }
    ),
    dcc.Graph(
        id='graph', 
        style={'height': '70vh', 'padding': '30px'}
    ),
    html.Div([
        html.Div([
            html.Span('Report', 
                style={
                    'color': '#e74c3c',
                    'fontSize': 30,
                    'fontFamily': 'Roboto, sans-serif',
                    'fontWeight': 'bold',
                    'textAlign': 'center',
                    'textShadow': '1px 2px #CCCCCC'
                }
            ),
            html.Span(id='report-date',
                style={
                    'color': '#e74c3c',
                    'fontSize': 30,
                    'fontFamily': 'Roboto, sans-serif',
                    'fontWeight': 'bold',
                    'textAlign': 'center',
                    'textShadow': '1px 2px #CCCCCC',
                    'marginLeft': '10px'
                })
            ],
            style={'display': 'flex', 
                    'align-items': 'center', 
                    'justify-content': 'center', 
                    'marginBottom': '10px'}
        ),
        html.Div([
            html.P('Return:', 
                style={'display': 'inline-block', 
                    'marginRight': '10px', 
                    'fontWeight': 'bold', 
                    'fontSize': '18px'}),
            html.Span(id='returns-last-day',
                style={'fontSize': '18px'})
            ], 
            style={'display': 'flex', 
                'align-items': 'center', 
                'justify-content': 'center', 
                'marginBottom': '-15px'}
        ),
        html.Div([
            html.P('Volatility:', 
                style={'display': 'inline-block', 
                    'marginRight': '10px', 
                    'fontWeight': 'bold', 
                    'fontSize': '18px'}),
            html.Span(id='volatility-last-day', 
                style={'fontSize': '18px'})
            ], 
            style={'display': 'flex', 
                'align-items': 'center', 
                'justify-content': 'center', 
                'marginBottom': '-15px'}
        ),
        html.Div([
            html.P('Max Price:', 
                style={'display': 'inline-block', 
                    'marginRight': '10px', 
                    'fontWeight': 'bold', 
                    'fontSize': '18px'}),
            html.Span(id='max-last-day', 
                style={'fontSize': '18px', "color": "#2ecc71"})
            ], 
            style={'display': 'flex', 
                'align-items': 'center', 
                'justify-content': 'center', 
                'marginBottom': '-15px'}
        ),
        html.Div([
            html.P('Mean Price:', 
                style={'display': 'inline-block', 
                    'marginRight': '10px', 
                    'fontWeight': 'bold', 
                    'fontSize': '18px'}),
            html.Span(id='mean-last-day', 
                style={'fontSize': '18px'})
            ], 
            style={'display': 'flex', 
                'align-items': 'center', 
                'justify-content': 'center', 
                'marginBottom': '-15px'}
        ),
        html.Div([
            html.P('Min Price:', 
                style={'display': 'inline-block', 
                    'marginRight': '10px', 
                    'fontWeight': 'bold', 
                    'fontSize': '18px'}),
            html.Span(id='min-last-day', 
                style={'fontSize': '18px', "color": "#e74c3c"})
            ], 
            style={'display': 'flex', 
                'align-items': 'center', 
                'justify-content': 'center', 
                'marginBottom': '-15px'}
        ),
        html.Div([
            html.P('Open Price:', 
                style={'display': 'inline-block', 
                    'marginRight': '10px', 
                    'fontWeight': 'bold', 
                    'fontSize': '18px'}),
            html.Span(id='open-last-day', 
                style={'fontSize': '18px'})
            ], 
            style={'display': 'flex', 
                'align-items': 'center', 
                'justify-content': 'center', 
                'marginBottom': '-15px'}
        ),
        html.Div([
            html.P('Close Price:', 
                style={'display': 'inline-block', 
                    'marginRight': '10px', 
                    'fontWeight': 'bold', 
                    'fontSize': '18px'}),
            html.Span(id='close-last-day', 
                style={'fontSize': '18px'})
            ], 
            style={'display': 'flex', 
                'align-items': 'center', 
                'justify-content': 'center', 
                'marginBottom': '-15px'}
        )
    ], style={
        'textAlign': 'center',
        'fontFamily': 'Roboto, sans-serif',
        'backgroundColor': '#f4f4f9',
        'paddingTop': '5px'
    }),
    dcc.Interval(
        id='interval-price',
        interval=10000, # 10s
        n_intervals=0
    ),
    dcc.Interval(
        id='interval-report',
        interval=600000, # 10min
        n_intervals=0
    )
])

# Get live data
@app.callback([Output('graph', 'figure'),
               Output('last-price', 'children')],
            [Input('interval-price', 'n_intervals')])
def reload_data(n_intervals):
    df = pd.read_csv('avax_data.csv', names=["Date", "Price"])
    df['Date'] = pd.to_datetime(df['Date'])
    df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
    last_price = np.array(df["Price"])[-1]
    rsi = ta.momentum.RSIIndicator(df['Price'], window=14).rsi()
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1, row_heights=[0.7, 0.3])
    trace = go.Scatter(
        x=df['Date'],
        y=df['Price'],
        mode='lines',
        name='AVAX',
        line=dict(color='#e74c3c', width=2),
        hovertemplate="<b>Price:</b> %{y:.2f}<br>"
    )
    rsi_trace = go.Scatter(
        x=df['Date'],
        y=rsi,
        mode='lines',
        name='RSI',
        line=dict(color='#3498db', width=1),
        hovertemplate="<b>Value:</b> %{y:.2f}<br>"
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
        yaxis=dict(title='Price', showgrid=True, dtick=0.2, tickprefix='$'),
        yaxis2=dict(title='RSI', tickvals=[30, 70]),
        margin=dict(l=100, r=80, t=100, b=60),
        hovermode='x',
        plot_bgcolor='#f4f4f9',
        paper_bgcolor='#f4f4f9',
        font=dict(family='Roboto, sans-serif', size=12, color='#333333'),
        legend_orientation="h",
        legend=dict(
            y=-0.3,
            x=0.43,
            font=dict(size=12)
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
            x=0.37, y=1.09,
            sizex=0.1, sizey=0.1,
            xanchor="right", yanchor="bottom"
          )]
    )
    fig.add_trace(trace, row=1, col=1)
    fig.add_trace(rsi_trace, row=2, col=1)
    fig.add_hline(y=70, line_width=1, line_color='#e74c3c', row=2, col=1, line_dash='dot')
    fig.add_hline(y=30, line_width=1, line_color='#2ecc71', row=2, col=1, line_dash='dot')
    fig.update_layout(layout)
    return fig, "$"+str(last_price)

# Get report data
@app.callback([Output('report-date', 'children'),
               Output('returns-last-day', 'children'),
               Output('volatility-last-day', 'children'),
               Output('max-last-day', 'children'),
               Output('mean-last-day', 'children'),
               Output('min-last-day', 'children'),
               Output('open-last-day', 'children'),
               Output('close-last-day', 'children')],
            [Input('interval-report', 'n_intervals')])
def reload_report(n_intervals):
    report = pd.read_csv("report.csv").tail(1).iloc[0]
    last_date = pd.to_datetime(report["Date"]).strftime('%B %d, %Y')
    return_last_day = report["Return"]
    volatility_last_day = report["Vol"]
    max_last_day = report["Max"]
    mean_last_day = report["Mean"]
    min_last_day = report["Min"]
    open_last_day = report["Open"]
    close_last_day = report["Close"]

    return last_date, html.Div(f'{return_last_day:.2%}', style={"color": "#2ecc71" if return_last_day > 0 else "#e74c3c"}), f'{volatility_last_day:.2%}', \
    f'${max_last_day}', f'${round(mean_last_day,2)}', f'${min_last_day}', f'${open_last_day}', f'${close_last_day}'


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=8000)