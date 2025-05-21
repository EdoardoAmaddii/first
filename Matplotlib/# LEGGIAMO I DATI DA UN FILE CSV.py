# LEGGIAMO I DATI DA UN FILE CSV
# E FACCIAMO LA COSA PIù COMUNE: LEGGIAMO I PRIMI 5 RECORD
# E LI STAMPIAMO
import csv
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Definisco il nome del file CSV
filename = 'dati.csv'
# Controllo se il file esiste
if not os.path.isfile(filename):
    print(f"Il file {filename} non esiste.")
    sys.exit(1)

# Apro il file CSV in lettura
with open(filename, mode='r', encoding='utf-8') as file:
    # Leggo il file CSV usando il modulo csv
    reader = csv.reader(file)
    # Salto la prima riga (intestazione)
    next(reader)
    # Leggo i primi 5 record
    for i, row in enumerate(reader):
        if i < 5:
            print(row)
        else:
            break






# Ora uso pandas per leggere il file CSV
# Apro il file CSV usando pandas
df = pd.read_csv(filename, encoding='utf-8')
# Mostro le prime 5 righe del DataFrame
print(df.head())
# Mostro le informazioni del DataFrame
print(df.info())
# Mostro le statistiche del DataFrame
print(df.describe())
# Mostro i nomi delle colonne del DataFrame
print(df.columns)
# Mostro il numero di righe e colonne del DataFrame
print(df.shape)
# Mostro i nomi delle righe del DataFrame
print(df.index)
# Mostro i tipi di dati delle colonne del DataFrame
print(df.dtypes)
# Mostro i valori unici di una colonna del DataFrame
print(df['colonna1'].unique())
# Mostro il numero di valori unici di una colonna del DataFrame
print(df['colonna1'].nunique())
# Mostro i valori nulli di una colonna del DataFrame
print(df['colonna1'].isnull().sum())
# Mostro i valori nulli del DataFrame
print(df.isnull().sum())
# Mostro i valori nulli del DataFrame in percentuale
print(df.isnull().sum() / len(df) * 100)
# Mostro i valori nulli del DataFrame in percentuale con 2 decimali
print(df.isnull().sum() / len(df) * 100).round(2)

# qui potrei fare altre operazioni con pandas, come ad esempio:
# - filtrare i dati
# - raggruppare i dati
# - unire i dati
# - fare statistiche sui dati
# - fare grafici sui dati



# iniziamo a filtrare i dati
# per esempio, vogliamo filtrare i dati in base a una colonna
# per esempio, vogliamo filtrare i dati in base alla colonna 'colonna1'

df_filtrato = df[df['colonna1'] == 'valore']
# mostriamo i dati filtrati 
print(df_filtrato)
