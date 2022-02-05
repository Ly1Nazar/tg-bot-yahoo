import os

import pandas as pd


def read_data(name):
    direrctory = os.listdir("data")
    for i in direrctory:
        if i == str(name+".csv"):
            df = pd.read_csv(str('data/'+name+'.csv'))
            Date = df["Date"]
            Open = df["Open"]
            Close = df["Close"]
            Volume = df["Volume"]
            return Date, Open, Close, Volume
        else:
            return "no data", "no data", "no data", "no data"
