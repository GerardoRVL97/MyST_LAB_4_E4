
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/Itzy17/MyST_LAB_4_E4                                                 -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import timedelta, datetime


def plot_orderbook(ob_data, levels):
    k = list(ob_data.keys())
    max_volume = 0
    max_timestamp = k[-1]
    for i in k:
        volume = ob_data[i].bid_size.sum() + ob_data[i].ask_size.sum()
        if volume >= max_volume:
            max_volume = volume
            max_timestamp = i

    bids = ob_data[max_timestamp][["bid_size", "bid"]].rename(columns={"bid_size": "Size", "bid": "Value"})
    bids["label"] = "Bid"
    asks = ob_data[max_timestamp][["ask_size", "ask"]].rename(columns={"ask_size": "Size", "ask": "Value"})
    asks["label"] = "Ask"
    bids = bids.sort_values(by=['Value'], ascending=True)
    asks = asks.sort_values(by=['Value'], ascending=True)
    long_df = pd.concat([bids.tail(levels), asks.head(levels)])
    fig = px.bar(long_df, x="Value", y="Size", color="label", title="OrderBook TimeStamp: " + max_timestamp)
    fig.update_xaxes(type='category')
    fig.show()


def spread_graph(df_ts_tob):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_ts_tob['timestamp'], y=df_ts_tob['bid'], name='Bid', mode='lines'))
    fig.add_trace(go.Scatter(x=df_ts_tob['timestamp'], y=df_ts_tob['ask'], name='Ask', mode='lines'))
    fig.update_layout(title='SPREAD GRAPH')
    fig.show()


def spread_boxplot(df_ts_tob):
    df_ts_tob['timestamp'] = df_ts_tob['timestamp'].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%fZ"))
    df_ts_tob['hour'] = df_ts_tob['timestamp'].dt.hour
    fig = px.box(df_ts_tob, x="hour", y="spread")
    return fig, df_ts_tob


def detect_outliers(spread_data):
    fig = px.box(spread_data.query("Outlier == False"), x="hour", y="spread", color="hour")
    fig.update_layout(title='SPREAD WITHOUT OUTLIERS BOXPLOT')
    return fig.show()

#%% Edgar

def martingala_hist(pdataframe: 'Martingala DataFrame'):
    fig = px.histogram(pdataframe, x='Type', y='Zeros vs Non Zeros', color='Type')
    fig.show()