import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('brani_musicali_dirty.csv')


# voglio forzare il DF per vedere tutte le colonne
pd.set_option('display.max_columns', None)  # mostra tutte le colonne

print(df.head())
print('\n')
print(df.info())
print('\n')
print(df.describe())
print('\n')
print(df.isnull().sum())  # valori nulli del DataFrame
# ce ne sono alcuni, ma non sono tanti
print('\n')
# vediamo le righe dove sono presenti i valori nulli
print(df[df.isnull().any(axis=1)])  # righe con valori nulli
print('\n')
# abbiamo solo 3 righe con valori nulli
# una riga p mancante di molti valori e la eliminiamo: la riga 10
df = df.drop(index=10)
print('\n')

# ora abbiamo 2 righe con valori nulli
# vediamo se abbiamo eliminato la riga coretta
print(df[df.isnull().any(axis=1)])  # righe con valori nulli
print('\n')



# ORA VEDIAMO COME RIEMPIRE I DATI MANCANTI


# la riga di wonderwall manca la durata, la cerchiamo su google
# la durata è 4:18, in secondi sono 258
df.loc[df['Titolo'] == 'Wonderwall', 'Durata'] = 258
# ora vediamo se abbiamo riempito la riga corretta
print(df[df['Titolo'] == 'Wonderwall'])  # righe con valori nulli
print('\n')

# la riga di Numb mancano i BPM, la cerchiamo su google 
# i BPM sono 110

df.loc[df['Titolo'] == 'Numb', 'BPM'] = 110
# ora vediamo se abbiamo riempito la riga corretta
print(df[df['Titolo'] == 'Numb'])  # righe con valori nulli
print('\n')


# vediamo se ci sono ancora righe con valori nulli
print(df.isnull().sum())  # righe con valori nulli
print('\n')


# ora non ci sono più righe con valori nulli


# ORA VEDIAMO SE CI SONO VALORI DUPLICATI
# vediamo se ci sono righe duplicate
print(df.duplicated().sum())  # righe duplicate
print('\n')
# non ci sono righe duplicate


# ORA VEDIAMO I VALORI UNICI DELLE COLONNE

# vediamo i valori unici della colonna 'ARTISTA'
# CONTROLLIAMO CHE NON CI SIANO VALORI STRANI
print(df['Artista'].unique())  # valori unici della colonna 'Artista'
print('\n')
# vediamo che Led Zeppelin è scritto in modo diverso, lo correggiamo
df.loc[df['Artista'] == 'Led Zeplin', 'Artista'] = 'Led Zeppelin'
# ora vediamo se abbiamo riempito la riga corretta
print(df[df['Artista'] == 'Led Zeppelin'])  # righe con valori nulli
print('\n')

# vediamo se ci sono TITOLI scritti in modo diverso
print(df['Titolo'].unique())  # valori unici della colonna 'Titolo'
print('\n')
# Smells Like Teen Spirit è scritto in modo diverso, lo correggiamo
df.loc[df['Titolo'] == 'Smels Like Teen Spirit', 'Titolo'] = 'Smells Like Teen Spirit'
# ora vediamo se abbiamo riempito la riga corretta
print(df[df['Titolo'] == 'Smells Like Teen Spirit'])  # righe con valori nulli
print('\n')


# vediamo se ci sono GENERI scritti in modo diverso
print(df['Genere'].unique())  # valori unici della colonna 'Genere'
print('\n')
# hanno tutti una formattazione differente, li correggiamo, mettendo la lettera maiuscola all'inizio 
df['Genere'] = df['Genere'].str.capitalize()
# ora vediamo se abbiamo riempito le righe correttamente
print(df['Genere'].unique())  # valori unici della colonna 'Genere'
print('\n')




# vediamo se ci sono DURATE scritte in modo diverso
print(df['Durata'].unique())  # valori unici della colonna 'Durata'
print('\n')
# ci sono due valori problematici: 3.15, che indica i minuti che vanno convertiti in secondi
# e 3.58, che non sappiamo se sono minuti o secondi

# intanto convertiamo i minuti in secondi dove c'è 3:15 mettiamo 195
df.loc[df['Durata'] == '3:15', 'Durata'] = 195
# ora vediamo se abbiamo riempito la riga corretta
print(df[df['Durata'] == 195])  
print('\n')

# il formato, essendoci i : era in string, lo convertiamo in float automaticamente, ma nella scrittura dobbiamo essere attenti perchè ci dà un errore se non capiamo che stiamo lavorando con una stringa, pensando sia un numero


# ora andiamo a prendere la riga con 3.58 e vediamo se dono i secondi o i minuti
print(df[df['Durata'] == '3.58'])  
print('\n')
# Creep dei Radiohead, cercata su google, dura 3.56 minuti, quindi 236 secondi
df.loc[df['Titolo'] == 'Creep', 'Durata'] = 236
# ora vediamo se abbiamo riempito la riga corretta
print(df[df['Titolo'] == 'Creep'])  # righe con valori nulli
print('\n')









# vediamo se i BPM sono scritti in modo diverso
print(df['BPM'].unique())  # valori unici della colonna 'BPM'
print('\n')
# c'è un 500 che non ha senso, lo andiamo a correggere. vediamo la riga dove c'è 500
print(df[df['BPM'] == 500])  # righe con valori nulli
print('\n')

# Believer degli imagine Dragons, cercata su google, ha 125 BPM

# df.loc[df['Titolo'] == 'Believer', 'BPM'] = 125
# ora vediamo se abbiamo riempito la riga corretta
#print(df[df['Titolo'] == 'Believer'])  # righe con valori nulli
print('\n')

# ho notato che anche Believer è scritto in modo sbagliato, lo correggo
df.loc[df['Titolo'] == 'Beliver', 'Titolo'] = 'Believer'
# ora vediamo se abbiamo riempito la riga corretta
print(df[df['Titolo'] == 'Believer'])  # righe con valori nulli
print('\n')

# cambiamo il BPM
df.loc[df['Titolo'] == 'Believer', 'BPM'] = 125
# ora vediamo se abbiamo riempito la riga corretta
print(df[df['Titolo'] == 'Believer'])  # righe con valori nulli
print('\n')


# vediamo se ci sono tonalità scritte in modo diverso
print(df['Tonalità'].unique())  # valori unici della colonna 'Tonalità'
print('\n')
# questa colonna va bene, non ci sono problemi





# vediamo infine la Data_Uscita
print(df['Data_Uscita'].unique())  # valori unici della colonna 'Data_Uscita'
print('\n')
# anche qui i valori non hanno segni evidenti di errore



# riprendiamo il nostro database completo, pulito

print(df)


# va bene tutto, ma ci siamo dimenticati di una cosa: la durata di Can't Stop è rimasta convertita male
# la durata è 4:29, in secondi sono 269
df.loc[df['Titolo'] == 'Can\'t Stop', 'Durata'] = 269
# ora vediamo se abbiamo riempito la riga corretta
print(df[df['Titolo'] == 'Can\'t Stop'])  # righe con valori nulli
print('\n')





# OK # ora abbiamo un database pulito, senza valori nulli, senza valori duplicati e senza valori strani
# ora possiamo salvare il nostro database pulito

# printiamo il nostro database pulito per sicurezza 
print(df)
# lo salviamo in un file csv
df.to_csv('brani_musicali_clean.csv', index=False) # index=False per non salvare l'indice del DataFrame









############################################################


# ora possiamo fare l'analisi del nostro database
# vogliamo fare un'analisi del nostro database




