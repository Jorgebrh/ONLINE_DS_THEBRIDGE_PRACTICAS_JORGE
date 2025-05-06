import pandas as pd
import numpy as np
import yfinance as yf
import os

#funcion para obtener la rentabilidad diaria de cada accion tomando en cuenta el precio de cierre

def rentabilidad_diaria(df, columna_cierre = "Close"):
    df["rentabilidad_diaria"] = df[columna_cierre].pct_change()
    return df.dropna()

#Funcion para obtener la rentabilidad anual:
def rentabilidad_anual(df, columna_rentabilidad="rentabilidad_diaria"):
    numero_dias = len(df)
    rentabilidad_anualizada = ((1 + df[columna_rentabilidad]).prod() ** (252 / numero_dias) - 1)*100
    return round(rentabilidad_anualizada,2)

def volatilidad_accion_anualizada(df, columna_rentabilidad="rentabilidad_diaria"):
    volatilidad = df[columna_rentabilidad].std() * np.sqrt(252)
    return round(volatilidad,2)

def ratio_sharpe(df, columna_rentabilidad="rentabilidad_diaria", rf = 0.04): # La rf corresponde con la tasa libre de riesgo. Hemos tomado una tasa 
#de 4% que es aproximadamente la que ha habido durante este año.
    rent_anual = rentabilidad_anual(df, columna_rentabilidad) / 100
    volatilidad = volatilidad_accion_anualizada(df,columna_rentabilidad)
    sharpe =round((rent_anual-rf)/volatilidad,2)
    return sharpe

#funcion para obtener la covarianza, varianza y beta de la accion

def beta_accion(df_accion,df_indice,columna_rentabilidad="rentabilidad_diaria"):
    returns_accion = df_accion[columna_rentabilidad].pct_change().dropna()
    returns_indice = df_indice[columna_rentabilidad].pct_change().dropna()

    covarianza = returns_accion.cov(returns_indice)
    varianza_indice = returns_indice.var()
    beta = round(covarianza/varianza_indice, 2)
    return beta

#Dataframe resumiendo los datos obtenidos

def detalle_accion(df, columna_rentabilidad="rentabilidad_diaria", nombre_accion="Acción", df_indice=None, columna_cierre="Close", rf=0.04):
    rent_anual = rentabilidad_anual(df, columna_rentabilidad)
    volatilidad = volatilidad_accion_anualizada(df, columna_rentabilidad)
    sharpe = ratio_sharpe(df, columna_rentabilidad, rf)
    
    if df_indice is not None:
        beta = beta_accion(df, df_indice, columna_cierre)
    else:
        beta = None

    resumen = pd.DataFrame({
        "Acción": [nombre_accion],
        "Rentabilidad Anual (%)": [rent_anual],
        "Volatilidad Anual": [volatilidad],
        "Ratio de Sharpe": [sharpe],
        "Beta": [beta]
    })

    return resumen