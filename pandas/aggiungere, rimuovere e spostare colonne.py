# aggiungere, rimuovere e spostare colonne

import pandas as pd
import os

file_path = os.path.join(os.path.expanduser('~'), 'OneDrive', 'pandas', 'pokemon_csv.csv')
df = pd.read_csv(file_path)


# agiungiamo una colonna al dataframe

df['nuova_colonna'] = 'ciao'
print(df[['Name','Total','nuova_colonna']].head())

print('\n\n')

# abbiamo aggiunto una colonna al dataframe, con il nome 'nuova_colonna' e il valore 'ciao' per tutte le righe

# ora possiamo aggiungere una colonna con i valori delle righe, quindi una colonna con i valori delle righe
# prendiamo il valore della colonna 'Total' e sommiamo 1 a tutti i valori della colonna 'Total'

df['nuova_colonna'] = df['Total'] + 1
print(df[['Name','Total','nuova_colonna']].head())

print('\n\n')


# aggiungiamo più colonne e dati all'interno di queste

df[['Wii', 'Switch', 'Gameboy']] = ['2nd', '7th', '1st']
print(df[['Name','Total','nuova_colonna','Wii', 'Switch', 'Gameboy']].head())

print('\n\n')




# aggiungiamo con insert una colonna in una posizione specifica, quindi non alla fine del dataframe
# per farlo dobbiamo usare il metodo insert() di pandas
# il metodo insert() di pandas prende tre parametri:
# il primo è la posizione in cui vogliamo inserire la colonna, il secondo è il nome della colonna e il terzo è i valori della colonna
# insert(indice, 'nome', valore)

df.insert(1, 'nuova_colonna2', 'aeiou')
print(df.head())

print('\n\n')



# aggiungiamo una colonna con loc
# per farlo dobbiamo usare il metodo loc[] di pandas
# il metodo loc[] di pandas prende due parametri:
# il primo è la riga a cui vogliamo assegnare il valore ( usando lo slicing (:) riempio tutta la colonna o solo parti), il secondo è il nome della nuova colonna che andrà in fondo
# loc[indice del valore, 'nome'] = valore

df.loc[2:5, 'nuova_colonna3'] = 'xyz'
print(df.head())

print('\n\n')


#utilizziamo assign per assegnare un valore a una colonna
# per farlo dobbiamo usare il metodo assign() di pandas 
# il metodo assign() di pandas prende due parametri:
# il primo è il nome della colonna e il secondo è i valori della colonna
# assign(nome, valore)  N.B. il nome della colonna non deve essere già presente nel dataframe, altrimenti lo sovrascrive, cancellando la precedente
                            ## se vogliamo aggiungere una colonna con lo stesso nome di una colonna già presente nel dataframe, dobbiamo usare il metodo assign() di pandas
                            # il nome della colonna non deve essere tra virgolette, altrimenti pandas lo interpreta come una stringa e non come il nome della colonna


df = df.assign(nuova_colonna4 = '123')
print(df.head())

print('\n\n')











## ora andiamo a rimuovere una colonna dal dataframe
# drop(), del(), pop()

# per rimuovere una colonna dal dataframe possiamo usare il metodo drop() di pandas

df.drop('nuova_colonna2', inplace=True, axis=1) # axis=1 per rimuovere una colonna, axis=0 per rimuovere una riga # inplace=True per modificare il dataframe originale, altrimenti crea un nuovo dataframe
print(df.head())


print('\n\n')


# ora andiamo a rimuovere più colonne dal dataframe
# per farlo possiamo ancora utilizzare il metodo drop() di pandas
# il metodo drop() di pandas prende due parametri:
# il primo è il nome della colonna e il secondo è l'asse su cui vogliamo rimuovere la colonna (0 per le righe, 1 per le colonne)
# drop(nome, axis=1) # axis=1 per rimuovere una colonna, axis=0 per rimuovere una riga # inplace=True per modificare il dataframe originale, altrimenti crea un nuovo dataframe
# df.drop(['nuova_colonna3', 'nuova_colonna4'], inplace=True, axis=1) # rimuove le colonne 'nuova_colonna3' e 'nuova_colonna4' dal dataframe
# print(df.head())




# usiamo il metodo DEL per rimuovere una colonna dal dataframe
# il metodo del df prende un parametro:
# il nome della colonna da rimuovere
# rimuove la colonna 'nuova_colonna3' dal dataframe

del df['nuova_colonna3'] # rimuove la colonna 'nuova_colonna3' dal dataframe
print(df.head())


print('\n\n')





# usiamo il metodo POP per rimuovere una colonna dal dataframe
# il metodo pop() di pandas prende un parametro:    
# il nome della colonna da rimuovere
# il metodo pop() di pandas restituisce la colonna rimossa come un oggetto Series
# quindi possiamo usarlo per rimuovere una colonna dal dataframe e assegnarla a una variabile

colpop = df.pop('nuova_colonna4') # rimuove la colonna 'nuova_colonna4' dal dataframe e la assegna alla variabile colpop
print(df.head())

print('\n\n')
#ora abbiamo rimosso la colonna 'nuova_colonna4' dal dataframe e l'abbiamo assegnata alla variabile colpop che stampiamo
print(colpop.head()) # stampa la colonna rimossa


print('\n\n')









# ora andiamo a spostare una colonna del dataframe
# possiamo farlo on print df[['colonna1', 'colonna2', 'colonna3']] per stampare il dataframe con le colonne in un ordine diverso senza modificare il dataframe originale
# oppure modificare tutto il dataframe


# usiamo loc per spostare una colonna del dataframe
# il metodo loc[] di pandas prende due parametri:
# il primo è la riga a cui vogliamo assegnare il valore ( usando lo slicing (:) riempio tutta la colonna o solo parti), il secondo è il nome della nuova colonna che andrà in fondo
# loc[indice del valore, 'nome'] = valore

print(df.loc[:, ['Type 1', 'Name', 'Type 2', 'Attack', 'Total']].head()) # stampa il dataframe con le colonne in un ordine diverso senza modificare il dataframe originale

print('\n\n')

# usiamo iloc per spostare colonne del dataframe
# il metodo iloc[] di pandas prende due parametri:
# il primo è la riga a cui vogliamo assegnare il valore ( usando lo slicing (:) riempio tutta la colonna o solo parti), il secondo è il nome della nuova colonna che andrà in fondo
# iloc[indice del valore, 'nome'] = valore

print(df.iloc[:, [1, 0, 2, 6, 4]].head()) # stampa il dataframe con le colonne in un ordine diverso senza modificare il dataframe originale


print('\n\n')


# posso non usare metodi e usare direttamente le colonne del dataframe
# per farlo dobbiamo usare il nome delle colonne tra parentesi quadre
# e le prime 5 righe del dataframe

print(df[['Type 1', 'Name', 'Type 2', 'Attack', 'Total']].head()) # stampa il dataframe con le colonne in un ordine diverso senza modificare il dataframe originale


print('\n\n')



## usiamo ora reverse per invertire l'ordine delle colonne del dataframe
# per farlo dobbiamo usare il metodo reverse() di pandas

columns = list(df.columns) # crea una lista con i nomi delle colonne del dataframe
# in questo modo possiamo usare il metodo reverse() di pandas per invertire l'ordine delle colonne del dataframe
columns.reverse() # inverte l'ordine delle colonne del dataframe
print(columns) # stampa la lista con i nomi delle colonne del dataframe in ordine inverso

print(df[columns].head()) # stampa il dataframe con le colonne in ordine inverso senza modificare il dataframe originale


print('\n\n')

# posso usare anche df.columns.tolist() per creare una lista con i nomi delle colonne del dataframe
# in questo modo possiamo usare il metodo reverse() di pandas per invertire l'ordine delle colonne del dataframe

colonne = df.columns.tolist() # crea una lista con i nomi delle colonne del dataframe
colonne.reverse() # inverte l'ordine delle colonne del dataframe
print(df[colonne]. head()) # stampa la lista con i nomi delle colonne del dataframe in ordine inverso

print('\n\n')




# modifichiamo il dataframe originale con le colonne in ordine inverso
# per farlo possiamo usare ad esempio il metodo reverse() di pandas

colonnemod = df.columns.tolist() # crea una lista con i nomi delle colonne del dataframe
colonnemod.reverse() # inverte l'ordine delle colonne del dataframe
df = df[colonnemod] # modifica il dataframe originale con le colonne in ordine inverso
print(df.head()) # stampa il dataframe con le colonne in ordine inverso 

print('\n\n')

