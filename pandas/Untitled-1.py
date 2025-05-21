import pandas as pd

df = pd.read_csv('top_1000_songs.csv')
# df = pd.read_csv('top_1000_songs.csv', header=None) # se non voglio che la prima riga sia il nome delle colonne


print(df.head())
print(df.tail())
print(df.shape)  # numero di righe e colonne
print(df.columns)  # nomi delle colonne
print(df.dtypes)  # tipi di dati delle colonne
print(df.info())  # informazioni sul DataFrame
print(df.describe())  # statistiche del DataFrame
print(df.isnull().sum())  # valori nulli del DataFrame
print(df.isnull().sum() / len(df) * 100)  # valori nulli del DataFrame in percentuale
print(df['colonna1'].unique())  # valori unici di una colonna del DataFrame
print(df['colonna1'].nunique())  # numero di valori unici di una colonna del DataFrame
print(df['colonna1'].isnull().sum())  # valori nulli di una colonna del DataFrame
print(df['colonna1'].isnull().sum() / len(df) * 100)  # valori nulli di una colonna del DataFrame in percentuale

