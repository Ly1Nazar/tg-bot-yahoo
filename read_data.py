import pandas as pd


def read_data(name):
    df = pd.read_csv(str('data/'+name+'.csv'))
    Date = df["Date"]
    Open = df["Open"]
    Close = df["Close"]
    Volume = df["Volume"]
    return Date, Open, Close, Volume