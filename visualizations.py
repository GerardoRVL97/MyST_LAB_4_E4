
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import plotly.express as px
import pandas as pd

def orderbook_barchart(ob_data, levels):
    k = list(ob_data.keys())
    max_volume = 0
    max_timestamp = k[-1]
    for i in k:
        volume = ob_data[i].bid_size.sum() + ob_data[i].ask_size.sum()
        if volume > max_volume:
            max_volume = volume
            max_timestamp = i

    bids = ob_data[max_timestamp][["bid_size", "bid"]].rename(columns={"bid_size": "Size", "bid": "Value"})
    bids["label"] = "Bid"
    asks = ob_data[max_timestamp][["ask_size", "ask"]].rename(columns={"ask_size": "Size", "ask": "Value"})
    asks["label"] = "Ask"
    bids = bids.sort_values(by=['Value'], ascending=False)
    asks = asks.sort_values(by=['Value'], ascending=True)
    long_df = pd.concat([bids.head(levels), asks.head(levels)])
    fig = px.bar(long_df, x="Value", y="Size", color="label", title="OrderBook TimeStamp: " + max_timestamp)
    fig.update_xaxes(type='category')
    fig.show()