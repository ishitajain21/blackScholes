#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import requests
import pandas as pd

st.title("Black Scholes Options Pricing Formula")
STOCK = st.text_input("Enter Stock ticker", "IBM")
KEY = st.text_input("Enter key from alpha vantage", "DEMO")
# In[3]:


KEY = "F54F3D1VUSH0TQJF"
# can get your own at alpha vantage for free.


# In[2]:


options_url = (
    "https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol="
    + STOCK
    + "&apikey="
    + KEY
)
r = requests.get(options_url)
data = r.json()
data = data["data"]
pd.DataFrame(data).to_csv("options.csv", index=False)
options = pd.read_csv("options.csv")


# In[23]:


options.head()


# In[4]:


prices_url = (
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
    + STOCK
    + "&apikey=F54F3D1VUSH0TQJF"
)
r = requests.get(prices_url)
data = r.json()
data.keys()
data = data["Time Series (Daily)"]
pd.DataFrame(data).to_csv("prices.csv", index=False)
prices = pd.read_csv("prices.csv")
prices = prices.T


# In[12]:


prices.head()


#

# In[13]:


import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.stats import norm


# In[ ]:


""" Assuming these options are European, not American. (Can use the model made by Robert Merton in further iterations)"""


# In[14]:


TRANSACTION_COST = 1.001
R = 0.05


# In[32]:


def curr_price(date):
    return (prices.loc[date][0] + prices.loc[date][3]) / 2


# In[33]:


from datetime import date, datetime


def days_till(start, exp):
    start = datetime.strptime(start, "%Y-%m-%d").date()

    exp = datetime.strptime(exp, "%Y-%m-%d").date()
    return (exp - start).days


# In[38]:


def black_scholes(row):
    S, K, r, T, sigma, option_type = (
        curr_price(row["date"]),
        row["strike"],
        R,
        days_till(row["date"], row["expiration"]),
        row["implied_volatility"],
        row["type"],
    )
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return round(price, 2)


# In[39]:


options["ideal_val"] = options.apply(black_scholes, axis=1)


# In[1]:


options["ideal_val"] = options["ideal_val"] * TRANSACTION_COST
# In[40]:
to_display = options[
    [
        "contractID",
        "expiration",
        "strike",
        "type",
        "bid",
        "bid_size",
        "ask",
        "ask_size",
        "date",
        "implied_volatility",
        "ideal_val",
    ]
]
st.dataframe(data=to_display)
# In[ ]:


# In[5]:


# In[ ]:
