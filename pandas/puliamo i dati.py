# puliamo i dati

import pandas as pd

df = pd.read_csv('calorie.csv')

print(df)


# notiamo che ci sono: valori nulli, duplicati, date mal formattate, durate mal formattate, ecc.
# ora andiamo a pulire i dati


#######################################

# iniziamo con i valori nulli

new_df = df.dropna() # dropna() è un metodo di pandas che serve per eliminare i valori nulli
# in questo caso eliminiamo tutte le righe che contengono valori nulli creando un nuovo dataframe
print(new_df) # stampiamo il dataframe senza valori nulli
print('\n\n')


#se non volessi creare un nuovo df, ma modificare il df originale, potrei usare il metodo inplace = True

df.dropna(inplace=True) # in questo caso eliminiamo tutte le righe che contengono valori nulli nel dataframe originale
print(df) # stampiamo il dataframe senza valori nulli



# riempiamo i valori nulli

df.fillna(0, inplace=True) # in questo caso riempiamo i valori nulli con 0 nel dataframe originale
print(df) # stampiamo il dataframe senza valori nulli


# riempiamo invece una specifica colonna

df['calories'].fillna(0, inplace=True) # in questo caso riempiamo i valori nulli con 0 nella colonna 'calories' del dataframe originale
print(df) # stampiamo il dataframe senza valori nulli

# riempiamo i valori nulli con la media della colonna

df['calories'].fillna(df['calories'].mean(), inplace=True) # in questo caso riempiamo i valori nulli con la media della colonna 'calories' del dataframe originale
print(df) # stampiamo il dataframe senza valori nulli

#riempiamo la data con quella che manca
df['date'].fillna('2020/12/22', inplace=True) # in questo caso riempiamo i valori nulli con la media della colonna 'calories' del dataframe originale
print(df) # stampiamo il dataframe senza valori nulli




###############################################
# occupiamoci del formato errato delle date


# in questo caso andiamo a convertire le date in un formato corretto
df['date'] = pd.to_datetime(df['date'])  ### non essenziale: ,format='%Y/%m/%d') # in questo caso convertiamo le date in un formato corretto
print(df)


print('\n\n')



################################################

# andiamo a modificare i minuti di allenamento scritti in modo sbagliato

df.loc[7, 'Duration'] = 45 # a riga 7, colomna 'Duration' mettiamo 45
print(df) # stampiamo il dataframe 


# se vogliamo fare la cosa su larga scala e ad esempio controllare che tutti i dati rispetti no il fatto di essere sotto i 60 min

for index in df.index:
    if df.loc[index, 'Duration'] > 60:
        df.loc[index, 'Duration'] = 60 

print(df) # stampiamo il dataframe



##################################################

# rimuoviamo i duplicati

# controlliamo se ne abbiamo
print(df.duplicated()) # stampiamo i duplicati --> VERO O FALSO
print('\n\n')

df.drop_duplicates(inplace=True) # in questo caso eliminiamo i duplicati nel dataframe originale
print(df) # stampiamo il dataframe senza duplicati

print('\n\n')

# è importante ricontrollare se ci sono duplicati
print(df.duplicated()) 
# stampiamo i duplicati --> VERO O FALSO

