import pandas as pd

df = pd.read_csv('top_1000_songs(guarda il file e elimina tutti gli errori).csv')
# df = pd.read_csv('top_1000_songs.csv', header=None) # se non voglio che la prima riga sia il nome delle colonne



# all'inizio il DataFrame è troppo grande e non riesco a vedere tutto, ma posso forzare il DF per vedere tutto
# voglio forzare il DF per vedere tutte le colonne
pd.set_option('display.max_columns', None)  # mostra tutte le colonne

# voglio forzare il DF per vedere tutte le righe
# pd.set_option('display.max_rows', None)  # mostra tutte le righe



# INIZIO DELL'ANALISI DEL DATAFRAME
# VEDIAMO COME È FATTO IL DATAFRAME


print(df.head())
print('\n')
print(df.tail())
print('\n')
print(df.shape)  # numero di righe e colonne
print('\n')
print(df.columns)  # nomi delle colonne
print('\n')
print(df.dtypes)  # tipi di dati delle colonne
print('\n')
print(df.info())  # informazioni sul DataFrame
print('\n')
print(df.describe())  # statistiche del DataFrame
print('\n')
print(df.isnull().sum())  # valori nulli del DataFrame
print('\n')
print(df.isnull().sum() / len(df) * 100)  # valori nulli del DataFrame in percentuale






# Se voglio vedere i valori unici di una colonna del DataFrame
# devo scrivere il nome della colonna tra parentesi quadre, esattamente quello!

#print(df['colonna1'].unique())  # valori unici di una colonna del DataFrame
#print(df['colonna1'].nunique())  # numero di valori unici di una colonna del DataFrame
#print(df['colonna1'].isnull().sum())  # valori nulli di una colonna del DataFrame
#print(df['colonna1'].isnull().sum() / len(df) * 100)  # valori nulli di una colonna del DataFrame in percentuale




# voglio vedere i vaLori unici della prima colonna, non so come si chiama, perciò utilizzo il comando
df.columns[0] # per vedere il nome della colonna

# Stampare i nomi delle colonne
print("Colonne disponibili:")
print(df.columns.tolist())

print(df[df.columns[0]].unique())  # valori unici della prima colonna del DataFrame

# OPPURE
# posso farlo anche con ILOC
# senza sapere il nome mi ridarà i valori unici della prima colonna
# gli dico che voglio vedere tutti i valori (:) e la prima colonna (0) del DataFrame
print(df.iloc[:, 0].unique())  # valori unici della prima colonna del DataFrame


# vediamo se ci sono valori non unici 
print(df[df.columns[0]].duplicated())  # valori duplicati della prima colonna del DataFrame, avrò una serie di booleani

# abbiamo visto che la prima colonna è il titolo della canzone, ora vediamo se ci sono titoli duplicati
# voglio vedere i titoli duplicati

print(df[df.columns[1]].duplicated())  # titoli duplicati della prima colonna del DataFrame

# notiamo che ci sono le prime 5 righe duplicate fino a mille, sia per il titolo che per l'artista

# vediamo allora se tutte le altre colonne sono duplicate
print(df[df.columns[2]].duplicated())  # titoli duplicati della prima colonna del DataFrame
# vediamo se ci sono valori duplicati in tutto il DataFrame



print('\n\n\n')


## PULIAMO IL DATAFRAME ELIMINANDO LE RIGHE DUPLICATE
# vogliamo eliminare le righe duplicate del DataFrame

df1 = df.drop_duplicates()  # elimina le righe duplicate del DataFrame
# vogliamo eliminare le righe duplicate del DataFrame e mantenere solo la prima occorrenza

# vediamo quante righe sono rimaste
print(df1.shape)  # numero di righe e colonne


print(df1.head(5))  # vediamo il DataFrame senza le righe duplicate

# sono rimaste 5 righe 



## VEDIAMO SE CI SONO VALORI NULLI

# vogliamo vedere se ci sono valori nulli nel DataFrame
print(df1.isnull().sum())  # valori nulli del DataFrame



# ABBIAMO COMPLETATO L'ANALISI DEL DATAFRAME
# ELIMINATO I DUPLICATI E I VALORI NULLI, CHE NON ERANO PRESENTI
# ORA POSSIAMO FARE L'ANALISI DEL DATAFRAME



# sapende i nomi delle colonne, vogliamo vedere i valori unici di una colonna del DataFrame

print(df1['Genere'].unique())  # valori unici della colonna Genere del DataFrame
print(df1['Anno'].value_counts()) # valori unici della colonna Anno del DataFrame
print(df1['Stream Spotify (M)'].mean()) # media degli stream su Spotify del DataFrame
print(df1['Stream Spotify (M)'].median()) # mediana degli stream su Spotify del DataFrame
print(df1['Stream Spotify (M)'].max()) # massimo degli stream su Spotify del DataFrame
print(df1['Stream Spotify (M)'].min()) # minimo degli stream su Spotify del DataFrame






# salviamo il nuovo DataFrame in un file csv
df1.to_csv('top_1000_songs_clean.csv', index=False)  # salva il DataFrame in un file csv senza l'indice

# andreamo quindi a fare un'analisi più approfondita del DataFrame
# con matplot lib vogliamo fare un istogramma per vedere la distribuzione degli stream su Spotify a seconda del genere 
# prendiamo il nuovo df 


import matplotlib.pyplot as plt
import seaborn as sns



