import pandas as pd
import numpy as np

ds = {
    'Mesi': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Giorni': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
}

df = pd.DataFrame(ds)
print(df)

print('\n\n')

# vediamo le serie

# una serie è una colonna di un dataframe
# un dataframe è una tabella di dati

serie  =  [5,10,15,20,25,30,35,40,45,50]

panda_serie = pd.Series(serie)
print(panda_serie)

print('\n\n')
# ora vediamo come accedere agli elementi della serie
# differenza tra listsa e serie
# una lista è una sequenza di dati, una serie è una colonna di un dataframe
# in questo modo non semplicemente stampiamo i dati, ma li mettiamo in una colonna che è autonumerata


print(panda_serie[0]) # stampa il primo elemento della serie
print(panda_serie[1]) # stampa il secondo elemento della serie

print('\n\n')
# ora vediamo come creare una serie con un indice

# diamo a una serie un nome per ciascun elemento (etichette)
# in questo modo possiamo accedere agli elementi della serie in modo più semplice
# gli indici sono gli stessi che abbiamo usato per creare la serie
# gli indici sono le etichette delle righe del dataframe

serie_indici  = pd.Series(serie, index=['a','b','c','d','e','f','g','h','i','j'])
print(serie_indici)

print('\n\n')
# ora vediamo come accedere agli elementi della serie
print(serie_indici['a']) # stampa il primo elemento della serie
print(serie_indici['b']) # stampa il secondo elemento della serie


print('\n\n')
# ora vediamo come accedere agli elementi della serie in modo diverso, usando il metodo iloc
# iloc è un metodo che permette di accedere agli elementi della serie in base alla loro posizione

print(serie_indici.iloc[0]) # stampa il primo elemento della serie
print(serie_indici.iloc[1]) # stampa il secondo elemento della serie


print('\n\n')


# ora vediamo come accedere agli elementi della serie in modo diverso, usando il metodo loc

print(serie_indici.loc['a']) # stampa il primo elemento della serie
print(serie_indici.loc['b']) # stampa il secondo elemento della serie


print('\n\n')
# ora vediamo come accedere agli elementi della serie in modo diverso, usando il metodo at
# at è un metodo che permette di accedere agli elementi della serie in base alla loro etichetta
# at è più veloce di loc, ma non permette di accedere a più elementi contemporaneamente
print(serie_indici.at['a']) # stampa il primo elemento della serie
print(serie_indici.at['b']) # stampa il secondo elemento della serie


print('\n\n')

# ora vediamo come accedere agli elementi della serie in modo diverso, usando il metodo iat
# iat è un metodo che permette di accedere agli elementi della serie in base alla loro posizione    
# iat è più veloce di iloc, ma non permette di accedere a più elementi contemporaneamente
print(serie_indici.iat[0]) # stampa il primo elemento della serie   
print(serie_indici.iat[1]) # stampa il secondo elemento della serie


print('\n\n')


# ora vediamo come accedere agli elementi della serie in modo diverso, usando il metodo get
# get è un metodo che permette di accedere agli elementi della serie in base alla loro etichetta
# get è più veloce di loc, ma non permette di accedere a più elementi contemporaneamente
print(serie_indici.get('a')) # stampa il primo elemento della serie
print(serie_indici.get('b')) # stampa il secondo elemento della serie


print('\n\n')



# ora vediamo come accedere ad una serie in un dizionario
# un dizionario è una struttura dati che permette di memorizzare coppie chiave-valore
# in questo modo possiamo accedere agli elementi del dizionario in base alla loro chiave
# la chiave è l'etichetta della riga del dataframe
# il valore è il valore della riga del dataframe
# in questo modo possiamo accedere agli elementi del dizionario in base alla loro chiave

dizionario = {
    'a': 5,
    'b': 10,
    'c': 15,
    'd': 20,
    'e': 25,
    'f': 30,
    'g': 35,
    'h': 40,
    'i': 45,
    'j': 50
}


# iniziamo mandando a schermo la serie
serie = pd.Series(dizionario)
print(serie)
#ricorda che stamperà in fondo dtype: (int64) object, perchè non abbiamo specificato il tipo di dato


print('\n\n')
# ora vediamo come accedere agli elementi del dizionario rispetto ad un indice preciso

elementi_da_serie = pd.Series(dizionario, index=['b','c','d'])
print(elementi_da_serie) # stampa gli elementi del dizionario in base agli indici specificati





print('\n\n')

print(dizionario['a']) # stampa il primo elemento del dizionario
print(dizionario['b']) # stampa il secondo elemento del dizionario


print('\n\n')

# ora vediamo come accedere agli elementi del dizionario in modo diverso, usando il metodo get
# get è un metodo che permette di accedere agli elementi del dizionario in base alla loro chiave
# get è più veloce di loc, ma non permette di accedere a più elementi contemporaneamente








### creiamo un dataframe con i dati di un dizionario

import pandas as pd

pd.set_option('display.max_columns', None)  # mostra tutte le colonne del dataframe
pd.set_option('display.max_rows', None)  # mostra tutte le righe del dataframe
#pd.set_option('display.width', None)  # mostra tutte le righe del dataframe
#pd.set_option('display.max_colwidth', None)  # mostra tutte le righe del dataframe
#pd.set_option('display.max_seq_item', None)  # mostra tutte le righe del dataframe

data = {
    'mesi': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'giorni': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    'stagione': ['Inverno', 'Inverno', 'Primavera', 'Primavera', 'Primavera', 'Estate', 'Estate', 'Estate', 'Autunno', 'Autunno', 'Autunno', 'Inverno'],
    'festività': ['Capodanno', 'Carnevale', 'Pasqua', 'Festa della Liberazione', 'Festa dei Lavoratori', 'Festa della Repubblica', 'Ferragosto', 'Ognissanti', 'Immacolata Concezione', 'Natale', 'Santo Stefano', 'Capodanno'],
}

df = pd.DataFrame(data)
print(df.loc[0:5])  # stampa le prime 5 righe del dataframe  ## ricorda che serve loc per visualizzare le righe


df = pd.DataFrame(data, index=['riga1', 'riga2', 'riga3', 'riga4', 'riga5', 'riga6', 'riga7', 'riga8', 'riga9', 'riga10', 'riga11', 'riga12'])
print(df.loc['riga1':'riga5'])  # stampa le prime 5 righe del dataframe  ## non si può usare il metodo iloc perchè non abbiamo specificato gli indici numerici, ma le righe sono state create con le etichette
                                ## quindi non possiamo usare iloc, ma dobbiamo usare loc con il nome della riga

print('\n\n')
# ora vediamo come accedere agli elementi del dataframe in modo diverso, usando il metodo iloc
print(df.iloc[0:5])  # stampa le prime 5 righe del dataframe  ## si può usare il metodo iloc anche se abbiamo specificato gli indici numerici con altri nomi, quindi possiamo usare iloc con il numero della riga

