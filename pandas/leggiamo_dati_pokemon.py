import pandas as pd
import os

pd.set_option('display.max_columns', None)  # mostra tutte le colonne del dataframe
pd.set_option('display.max_rows', None)  # mostra tutte le righe del dataframe


file_path = os.path.join(os.path.expanduser('~'), 'OneDrive', 'pandas', 'pokemon_csv.csv')
df = pd.read_csv(file_path)

# questo è un file ben formattato, con le intestazioni delle colonne e i dati separati da virgole
# prendiamo le righe con slicing, quindi prendiamo le righe da 0 a 8 e tutte le colonne, quindi le prime 9 righe
#ricorda che df[0] non esiste

df = df[0:9]
print(df)

print('\n\n')
# cancelliamo l'indice automaticamente generato da pandas
# per farlo dobbiamo usare il metodo reset_index() di pandas
# il metodo reset_index() di pandas restituisce un nuovo DataFrame con l'indice resettato
# quindi dobbiamo assegnarlo a una nuova variabile
# oppure possiamo usare il parametro drop=True per eliminare l'indice originale
# in questo modo pandas non restituirà un nuovo DataFrame, ma modificherà il DataFrame originale
df = df.reset_index(drop=True)

#rinominiamo l'indice invece che da 0 a 8, da 1 a 9
df.index = df.index + 1
print(df)
print('\n\n')




# ora prendiamo head, che ci mostra le prime 5 righe del dataframe
# head è un metodo di pandas che restituisce le prime n righe del DataFrame
# il metodo head() di pandas restituisce un nuovo DataFrame con le prime n righe
# quindi dobbiamo assegnarlo a una nuova variabile

df = df.head(5)
print(df)
print('\n\n')

# ora prendiamo tail, che ci mostra le ultime 5 righe del dataframe
# tail è un metodo di pandas che restituisce le ultime n righe del DataFrame
# il metodo tail() di pandas restituisce un nuovo DataFrame con le ultime n righe
# quindi dobbiamo assegnarlo a una nuova variabile

dc = df.tail(5)
print(dc)
print('\n\n')


# cosi abbiamo un errore perchè usiamo tail dopo head, quindi non ci sono più righe

# facciamo quindi una copia del dataframe originale
dc = pd.read_csv(file_path)
dc = dc.tail(5)
print(dc)
print('\n\n')


# ora prendiamo una colonna del dataframe
# per farlo dobbiamo usare il nome della colonna tra parentesi quadre
# e le prime 5 righe del dataframe
# in questo modo pandas restituirà un nuovo DataFrame con le prime 5 righe della colonna (possiamo usare sia lo slice che head)
# attenzione a maiuscole e minuscole, il nome della colonna è case sensitive
# quindi dobbiamo usare il nome della colonna esattamente come è scritto nel file csv

colonne = pd.read_csv(file_path)

print(colonne['Name'][0:6])

print('\n\n')

print(colonne['Type 1'].head())

print('\n\n')
# ora prendiamo una colonna del dataframe con il metodo loc
# per farlo dobbiamo usare il nome della colonna tra parentesi quadre
# e le prime 5 righe del dataframe
# in questo modo pandas restituirà un nuovo DataFrame con le prime 5 righe della colonna (possiamo usare sia lo slice che head)
print(colonne.loc[0:6, 'Speed'])

#ricorda che con loc avremo le righe da 0 a 6 e la colonna Speed
# quindi avremo 7 righe e una colonna
# mentre con le parentesi quadre avremo solo 6 righe e una colonna

# quindi con loc avremo 7 righe e una colonna, mentre con le parentesi quadre avremo solo 6 righe e una colonna
print('\n\n')




# prendiamo più colonne del dataframe
# per farlo dobbiamo usare il nome delle colonne tra parentesi quadre
# e le prime 5 righe del dataframe
# creiamo una lista con i nomi delle colonne
# e poi usiamo la lista tra parentesi quadre
# creiamo un arrey quindi con i nomi delle colonne


print(colonne [['Name', 'HP', 'Legendary']][10:20])

print('\n\n')




# vediamo ora i metodi loc e iloc
# loc è un metodo di pandas che permette di accedere agli elementi del DataFrame in base al loro nome
# iloc è un metodo di pandas che permette di accedere agli elementi del DataFrame in base alla loro posizione

print(colonne.loc[0:5, ['Name', 'HP', 'Legendary']])

print('\n\n')


# ora vediamo come accedere agli elementi del DataFrame in base alla loro posizione
# in questo caso dobbiamo usare il metodo iloc  
# il metodo iloc() di pandas restituisce un nuovo DataFrame con gli elementi selezionati
# quindi dobbiamo assegnarlo a una nuova variabile

# attenzione che come prima colonna è l'indice, quindi la prima colonna è 0 e non 1

print(colonne.iloc[0:5, [0, 1, 6]]) # stampa le prime 5 righe e le colonne 0, 1, 6 del dataframe, senza specificare il nome della colonna
print('\n\n')























##############################################################################################


# difefrenza tra loc e iloc
# loc = localization, permette di accedere agli elementi del DataFrame in base al loro nome
# iloc = integer(index) location, permette di accedere agli elementi del DataFrame in base alla loro posizione


# quindi loc è più veloce di iloc, perchè non deve convertire i nomi delle colonne in numeri
# e quindi non deve fare il mapping tra i nomi delle colonne e i numeri
# mentre iloc deve fare il mapping tra i nomi delle colonne e i numeri

# quindi con loc diremo: prendi la colonna con il nome 'Name' sulla riga di Bulbasaur
# mentre con iloc diremo: prendi la colonna 0 sulla riga 0 --> sono quindi delle coordinate



#vediamo allora come definire una colonna con il metodo loc
# riprendiamo il df originale e prendiamo la colonna 'Name' come base
# definisco index_col=1 per usare la colonna 'Name' come indice e non come colonna


df = pd.read_csv(file_path, index_col=1)
print(df.loc['Bulbasaur'])
print('\n\n')

# in questo modo mettiamo in colonna tutte le informazioni di Bulbasaur
# il nome che abbiamo dato alla colonna è 'Name' e il nome che abbiamo dato alla riga è 'Bulbasaur'
# quindi ora possiamo accedere agli elementi della colonna 'Name' in modo più semplice
# N.B. il Name è l'indice, quindi non lo vediamo, ma è presente in fondo alla tabella




# andiamo ad usare il metodo iloc per accedere agli elementi del DataFrame in base alla loro posizione
df = pd.read_csv(file_path, index_col=1)
print(df.iloc[23]) # stampa il primo elemento della riga 23 del dataframe


print('\n\n')



# Prendiamo ora una cella del DataFrame
# usiamo il metodo loc per accedere alla cella del DataFrame in base al nome della colonna e della riga

print(df.loc['Bulbasaur', 'HP']) # stampa il valore della cella della colonna 'HP' e della riga 'Bulbasaur'
print('\n\n')


# ora prendiamo una cella del DataFrame con il metodo iloc
# per farlo dobbiamo usare il numero della riga e il numero della colonna

print(df.iloc[0,4]) # stampa il valore della cella della riga 4, della colonna 1 del dataframe

print('\n\n')


# prendiamo più righe con lo slicing
# per farlo dobbiamo usare il numero della riga e il numero della colonna

print(df.loc['Bulbasaur':'Charmander', 'HP':'Speed'])  # non possiamo mettere 'name' nelle colonne perchè lo sto specificando come indice
print('\n\n')

# ora prendiamo più righe con il metodo iloc

print(df.iloc[0:2, 0:3]) # stampa le righe da 0 a 2 e le colonne da 0 a 3 del dataframe (ricorda che nello slicing l'ultimo numero non è incluso)
print('\n\n')






# andiamo ad usare il metodo iloc per accedere agli elementi del DataFrame in base alla loro posizione
# df = pd.read_csv(file_path, index_col=1)

# se eliminiamo il parametro index_col=1, il dataframe avrà come indice i numeri da 0 a 8
# quindi il primo elemento sarà 0 e non 'Bulbasaur'

# quindi ora possiamo accedere agli elementi della colonna 'Name' in modo più semplice

df = pd.read_csv(file_path)
print(df.loc[0, ['Name', 'HP', 'Legendary']]) # stampa la riga 0 e le colonne 'Name', 'HP', 'Legendary' del dataframe, non specificando il nome della colonna e quindi non usando bulbasaur

print('\n\n')

# con iloc invece dobbiamo specificare il numero della riga e il numero della colonna

print(df.iloc[0, [0, 1, 6]]) # stampa la riga 0 e le colonne 0, 1, 6 del dataframe, senza specificare il nome della colonna
print('\n\n')