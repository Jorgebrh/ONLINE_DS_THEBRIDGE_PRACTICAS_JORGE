import pandas as pd
import numpy as np
import yfinance as yf
import sys
sys.path.append('../utils')
import funciones
import importlib
importlib.reload(funciones)
from funciones import *


#Incluyo los tickers para sacar luego los dataframes
apple = yf.Ticker("AAPL") #Representa el 6.73% del índice
microsoft = yf.Ticker("MSFT") #Representa el 6.20% del índice
nvidia = yf.Ticker("NVDA") #Representa el 5.68% del indice
amazon = yf.Ticker("AMZN") #Representa el 3.78% del indice
meta = yf.Ticker("META") #Representa el 2.57% del indice
sp500 = yf.Ticker("^GSPC")

df_apple = apple.history(start = "2024-01-01", end = "2025-01-01", interval = "1d")
df_microsoft = microsoft.history(start = "2024-01-01", end = "2025-01-01", interval = "1d")
df_nvidia = nvidia.history(start = "2024-01-01", end = "2025-01-01", interval = "1d")
df_amazon = amazon.history(start = "2024-01-01", end = "2025-01-01", interval = "1d")
df_meta = meta.history(start = "2024-01-01", end = "2025-01-01", interval = "1d")
df_sp500 = sp500.history(start = "2024-01-01", end = "2025-01-01", interval = "1d")

for df in [df_apple, df_microsoft, df_nvidia, df_amazon, df_meta, df_sp500]:
    df.reset_index(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"]).dt.tz_localize(None) #Necesito eliminar la fecha con zona horaria para poder
    #exportarlo a excel

df_apple.to_excel("../data/historico_apple.xlsx", index=False)
df_microsoft.to_excel("../data/historico_microsoft.xlsx", index=False)
df_nvidia.to_excel("../data/historico_nvidia.xlsx", index=False)
df_amazon.to_excel("../data/historico_amazon.xlsx", index=False)
df_meta.to_excel("../data/historico_meta.xlsx", index=False)
df_sp500.to_excel("../data/historico_sp500.xlsx", index=False)

#Calculo de las rentabilidades diarias de las empresas con el precio de cierre
df_apple = rentabilidad_diaria(df_apple,"Close")
df_microsoft = rentabilidad_diaria(df_microsoft,"Close")
df_nvidia = rentabilidad_diaria(df_nvidia,"Close")
df_amazon = rentabilidad_diaria(df_amazon,"Close")
df_meta= rentabilidad_diaria(df_meta,"Close")
df_sp500 = rentabilidad_diaria(df_sp500,"Close")