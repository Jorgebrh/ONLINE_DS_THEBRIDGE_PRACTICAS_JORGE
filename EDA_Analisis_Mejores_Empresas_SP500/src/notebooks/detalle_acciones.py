import pandas as pd
import numpy as np
import yfinance as yf
import sys
sys.path.append('../utils')

import funciones
import extraccion_empresas_indice

import importlib
importlib.reload(funciones)
importlib.reload(extraccion_empresas_indice)

from funciones import *
from extraccion_empresas_indice import * 

detalle_apple = detalle_accion(df_apple, nombre_accion="Apple", df_indice=df_sp500)
detalle_microsoft = detalle_accion(df_microsoft, nombre_accion="Microsoft", df_indice=df_sp500)
detalle_nvidia = detalle_accion(df_nvidia, nombre_accion="Nvidia", df_indice=df_sp500)
detalle_amazon = detalle_accion(df_amazon, nombre_accion="Amazon", df_indice=df_sp500)
detalle_meta = detalle_accion(df_meta, nombre_accion="Meta", df_indice=df_sp500)
detalle_sp500 = detalle_accion(df_sp500, nombre_accion="S&P 500")

df_datos_detalle = pd.concat([
    detalle_apple,
    detalle_microsoft,
    detalle_nvidia,
    detalle_amazon,
    detalle_meta,
    detalle_sp500
], ignore_index=True)

df_datos_detalle.to_excel("../data/detalle_acciones_SP500.xlsx", index=True)
df_datos_detalle
