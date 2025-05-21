# ///iter///items : iterare su colonne ci ritorna il nome della colonna e il valore della colonna: key, value
# iterrows : iterare su righe ci ritorna il nome della riga e il valore della riga: index, row
# itertuples: ci ritorna tutte le righe del dataframe come tuple, quindi ci ritorna il nome della riga e il valore della riga, come fosse una tupla

import pandas as pd
import os

file_path = os.path.join(os.path.expanduser('~'), 'OneDrive', 'pandas', 'pokemon_csv.csv')
df = pd.read_csv(file_path)


# questo è un file ben formattato, con le intestazioni delle colonne e i dati separati da virgole
# prendiamo solo la prima riga del dataframe
#ricorda che df[0] non esiste

df2 = df.head(1)
print(df2)
print('\n\n')


# iterando con items, ci ritorna il nome della colonna e il valore della colonna 

for k, v in df2.items():
    print(k)

print('\n\n')

for k, v in df2.items():
    print(v)

print('\n\n')


# iterando con iterrows, ci ritorna il nome della riga e il valore della riga


for index, row in df2.iterrows():
    print(row)


print('\n\n')


# iterando con itertuples, ci ritorna tutte le righe del dataframe come tuple, quindi ci ritorna il nome della riga e il valore della riga, come fosse una tupla
# in questo modo non semplicemente stampiamo i dati, ma li mettiamo in una colonna che è autonumerata

for row in df2.itertuples():
    print(row)

# se ci appaiono i nomi delle colonne come numeri, è perchè non abbiamo specificato correttamente il nome della colonna, quindi pandas ci restituisce i nomi delle colonne come numeri, con un underscore e un numero
# nel caso ci siano spazi o caratteri speciali nei nomi delle colonne, pandas ci restituirà i nomi delle colonne come "_0" e "_1"
print('\n\n')



#modifichiamo un po' il dataframe, per vedere come si comporta con i nomi delle colonne utilizzando un for loop

for index, row in df2.iterrows():
    if(index == 0):
        row['Name'] = 'sbublasaurus'
    print(row)

# così in realtà non stiamo modificando il dataframe, ma stiamo stampando i valori del dataframe cambiando un nome, quindi non stiamo modificando il dataframe originale
print('\n\n')

# se stampiamo il df dopo vediamo che non è cambiato nulla
print(df.head())

print('\n\n')










# ora ordiniamo il dataframe e ricordiamo che se ne creerà uno nuovo // ricorda che il dataframe originale non viene modificato, ma viene creato un nuovo dataframe con i dati ordinati

# il nuovo dataframe rispetta l'ordine alfabetico a seconda della colonna che scelgo come ordinamento
# quindi dobbiamo assegnarlo a una nuova variabile 

# possiamo usare il metodo sort_index per ordinare il dataframe in base all'indice
# in questo caso l'indice è la colonna 'Name', quindi il dataframe sarà ordinato in base alla colonna 'Name'

print('SORT INDEX')

sorted_df = df.sort_index()
print(sorted_df.head())

print('\n\n')


print('SORT INDEX ASCENDING')

sdf = df.sort_index(ascending=False)
print(sdf.head())

print('\n\n')




## ordianiamo in base a colonne diverse, quindi non in base all'indice
# ora ordiniamo il dataframe in base alla colonna 'Type 1'
# in questo caso il dataframe sarà ordinato in base alla colonna 'Type 1'
# quindi dobbiamo specificare il nome della colonna 'Type 1' come argomento del metodo sort_values


print('SORT VALUES')
typed_df = df.sort_values(by='Type 1')
print(typed_df.head())

print('\n\n')




# ora ordiniamo il dataframe in base alla colonna 'Type 1' e 'HP'

# in questo caso il dataframe sarà ordinato in base alla colonna 'Type 1' e 'HP'
# ci potrebbero essere stessi elementi di 'Type 1' che saranno ordinati in base alla colonna 'HP'
print('SORT VALUES PER PIU COLONNE')

mixed_df = df.sort_values(by=['Total', 'HP'], ascending = [False, False])
print(mixed_df[["Name", "Total", "HP"]].head())

