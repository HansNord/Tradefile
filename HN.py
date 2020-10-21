#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
def tradefile():
    columns = ['TimeStamp', 'Symbol', 'Price', 'Volume']
    df = pd.read_csv('input.csv', header = None, names = columns)
    df["Crossprod"] = df["Price"] * df["Volume"]
    Totalcross = df.groupby('Symbol').agg({'Crossprod':sum}).round(0)
    df['diff'] = df.groupby('Symbol')['TimeStamp'].diff().fillna(0)
    Totalvol = df.groupby('Symbol').agg({'Volume':sum})
    Totalvol = Totalvol.round(0).astype('int')
    Maxprice = df.groupby('Symbol').agg({'Price':max})
    Maxprice = Maxprice.round(0).astype('int')
    Maxdiff = df.groupby('Symbol').agg({'diff':max})
    Maxdiff = Maxdiff.round(0).astype('int')
    VWAP = Totalcross.div(Totalvol.values)
    VWAP = VWAP.round(0).astype('int')
    array = (Maxdiff, Totalvol, VWAP, Maxprice)
    array_concat = pd.concat(array, axis=1)
    csvoutput = array_concat.to_csv('output.csv', header=None)
tradefile()

