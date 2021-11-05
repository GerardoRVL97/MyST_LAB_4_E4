
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: functions.py : python script with general functions                                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/Itzy17/MyST_LAB_4_E4                                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
from datetime import timedelta,datetime
import pandas as pd

def f_compare_ts(ts_list_o, ts_list_d):
    ts_list_o_dt = [datetime.strptime(i, "%Y-%m-%dT%H:%M:%S.%fZ") for i in ts_list_o]
    ts_list_d_dt = [datetime.strptime(i, "%Y-%m-%dT%H:%M:%S.%fZ") for i in ts_list_d]
    f_compare_ts = {}
    f_compare_ts['first_o'] = min(ts_list_o_dt).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    f_compare_ts['last_o'] = max(ts_list_o_dt).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    f_compare_ts['qty_o'] = len(ts_list_o_dt)
    f_compare_ts['first_d'] = min(ts_list_d_dt).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    f_compare_ts['last_d'] = max(ts_list_d_dt).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    f_compare_ts['qty_d'] = len(ts_list_d_dt)
    unique_dates = list(dict.fromkeys(ts_list_o_dt + ts_list_d_dt))
    exact_matches = [i for i in unique_dates if (i in (ts_list_o_dt) and i in (ts_list_d_dt))]
    f_compare_ts['exact_match'] = {"qty":len(exact_matches), "values":exact_matches}
    return f_compare_ts

def historical_spread(ob_data):
    k = list(ob_data.keys())
    lowest_asks = []
    highest_bids = []
    spreads = []
    for i in k:
        lowest_asks.append(ob_data[i].ask.min())
        highest_bids.append(ob_data[i].bid.max())
        spreads.append(abs(ob_data[i].ask.min() - ob_data[i].bid.max()))

    df_ts_tob = pd.DataFrame()
    df_ts_tob["timestamp"] = k
    df_ts_tob["bid"] = highest_bids
    df_ts_tob["ask"] = lowest_asks
    df_ts_tob["spread"] = spreads
    return df_ts_tob

