import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# mi genero l'intervallo di date utilizzando pandas.date_range
def genera_dati_visitatori(anno, giorni, media, deviazione_std, trend_max):
    # creo una serie di date che parte dal primo giorno dell'anno specificato e dura per il numero di giorni specificato
    intervallo_date = pd.date_range(start=f'{anno}-01-01', periods=giorni)
    #genero tutte le date dal 1 gennaio 2023 per 365 giorni.
    visitatori_giornalieri = np.random.normal(media, deviazione_std, size=len(intervallo_date))
    # creo un trend crescente che parte da 0 fino a trend_max con il numero di giorni come numero di punti nel trend
    trend_crescente = np.linspace(0, trend_max, len(intervallo_date))
    # sommo i dati dei visitatori giornalieri con il trend crescente,con incremento graduale nel tempo
    visitatori_con_trend = visitatori_giornalieri + trend_crescente
    return intervallo_date, visitatori_con_trend

# creo il dataframe contenente i dati giornalieri dei visitatori impostando l'intervallo_date come indice e la colonna numero di visitatori
def crea_dataframe(intervallo_date, visitatori_con_trend):
    df = pd.DataFrame(visitatori_con_trend, index=intervallo_date, columns=['Numero di visitatori'])
    df.index = pd.to_datetime(df.index)
    return df

# calcolo le statistiche mensili
def calcola_statistiche_mensili(df):
    media_mensile = df.resample('M').mean() #con il metodo resample aggrego dati temporali in mesi, invece con mean
    # calcolo la media di tutti i valori per ciascun mese
    deviazione_std_mensile = df.resample('M').std() #calcolo la deviazione standard dei valori per ciascun mese
    return media_mensile, deviazione_std_mensile

def visualizza_dati(df, media_mensile):
    plt.figure(figsize=(12, 6)) #configuro dimensione grafico avente larghezza 12 pollici e altezza 6
    plt.plot(df.index, df['Numero di visitatori'], label='Numero di visitatori giornalieri')
    #imposto lon stile della linea tratteggiata e il suo colore (rosso)
    plt.plot(media_mensile.index, media_mensile['Numero di visitatori'], label='Media mensile', linestyle='--', color='red')
    #etichetto asse x
    plt.xlabel('Data')
    #etichetto asse y
    plt.ylabel('Numero di visitatori')
    # do un nome al grafico con il metodo title della libreria matplotlib
    plt.title('Visitatori giornalieri e media mensile nel parco')
    # aggiungo un etichetta al grafico
    plt.legend()
    # fondamentale per mostrare il grafico in output
    plt.show()

# Utilizzo delle funzioni
intervallo_date, visitatori_con_trend = genera_dati_visitatori(2023, 365, 2000, 500, 500)
df = crea_dataframe(intervallo_date, visitatori_con_trend)
media_mensile, deviazione_std_mensile = calcola_statistiche_mensili(df)

# Visualizzazione delle statistiche mensili
print("Media mensile dei visitatori:")
print(media_mensile)
print("\nDeviazione standard mensile dei visitatori:")
print(deviazione_std_mensile)

# Visualizzazione dei dati
visualizza_dati(df, media_mensile)
 