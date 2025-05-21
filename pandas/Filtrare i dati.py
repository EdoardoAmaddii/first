#Filtrare i dati

import pandas as pd
import os

df = pd.read_csv('pokemon_csv.csv')


# due opzioni per filtrare i dati
print(df[df.Name == 'Pikachu']) # filtriamo i dati in base al nome del pokemon

print('\n\n')


print(df[df['#'] == 25]) # filtriamo i dati in base al numero del pokemon

print('\n\n')
# filtriamo con str.contains
# str.contains() è un metodo di pandas che serve per filtrare i dati in base a una stringa
# in questo caso filtriamo i dati in base al nome del pokemon
print(df[df['Name'].str.contains('chu')]) # filtriamo i dati in base al nome del pokemon


print('\n\n')


# filtriamo con ISIN
# ISIN è un operatore di pandas che serve per filtrare i dati in base a una lista di valori

filtro = 'Grass' # in questo caso filtriamo i dati in base al tipo del pokemon

print(df[df['Type 1'].isin([filtro])]) # filtriamo i dati in base al tipo del pokemon


print('\n\n')
#
# filtriamo con >= e <
# >= e < sono operatori di pandas che servono per filtrare i dati in base a un valore numerico
# in questo caso filtriamo i dati in base al totale dei punti

print(df[df['Total'] > 700]) # filtriamo i dati in base al totale dei punti


print('\n\n')


# filtriamo con & e |
# & e | sono operatori di pandas che servono per filtrare i dati in base a più condizioni
print(df[(df['Total'] > 700) & (df['Attack'] > 70)]) # filtriamo i dati in base al totale dei punti

print('\n\n')


# filtriamo con loc()
# loc() è un metodo di pandas che serve per filtrare i dati in base a una lista di valori
# in questo caso filtriamo i dati in base al nome del pokemon

print(df.loc[df['Name'] == 'Pikachu']) # filtriamo i dati in base al nome del pokemon
print('\n\n')

# mettiamo di voler prendere solo le colonne 'Name' e 'Type 1'

print(df.loc[(df['Name'] == 'Pikachu'), ['Name', 'Type 1']]) # filtriamo i dati in base al nome del pokemon e prendiamo solo le colonne 'Name' e 'Type 1'
print('\n\n')


# mettiamo di voler usare contains() e prendere solo le colonne 'Name' e 'Type 1'

print(df.loc[df['Name'].str.contains('chu'), ['Name', 'Type 1']]) # filtriamo i dati in base al nome del pokemon e prendiamo solo le colonne 'Name' e 'Type 1'
print('\n\n')



##
## facciamo una condizione con query()
# query() è un metodo di pandas che serve per filtrare i dati in base a una stringa
# in questo caso filtriamo i dati in base al nome del pokemon

# dentro la query vogliamo una stringa
# non possiamo usare le virgolette singole, quindi usiamo le virgolette doppie
# non possiamo avere spazi nella nostra richiesta
# quindi usiamo il simbolo di underscore (_) al posto dello spazio
print(df.query('Name == "Bulbasaur"')) # filtriamo i dati in base al nome del pokemon
print('\n\n')


# facciamo un'altra query con più condizioni

print(df.query('Total > 700 & Speed >100')) # filtriamo i dati in base al tipo del pokemon

print('\n\n')

# facciamo un'altra query con più condizioni e prendiamo solo le colonne 'Name' e 'Type 1'
print(df.query('Total > 700 & Speed >100')[['Name', 'Type 1', 'Attack']]) # filtriamo i dati in base al tipo del pokemon e prendiamo solo le colonne 'Name' e 'Type 1'