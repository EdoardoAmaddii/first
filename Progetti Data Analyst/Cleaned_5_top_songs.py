import matplotlib.pyplot as plt
import numpy as np
import pandas as pd






'''

un piccolo recap di quello che abbiamo fatto finora e dei problemi che potrebbero sorgere:
1. abbiamo caricato il dataset
2. abbiamo visto che ci sono dei valori nulli
3. abbiamo visto che ci sono dei valori possono essere sbagliati
4. abbiamo visto che ci sono dei valori che non sono stati riempiti

# i valori nulli hanno vari metodi di riempimento, ma non sempre sono corretti
# N.B. a volte potrebbe mancare un header
o volerlo noi escludere


# i valori sbagliati possono essere corretti, ma non sempre sono corretti
# potremmo inoltre volere modificare alcuni valori che non ci piacciono
 ' ' lo spazio, '?' il punto interrogativo, 'NaN' il valore nullo, '0' lo zero, '-' il trattino, 'N/A' non applicabile, 'NULL' il valore nullo, 'NaT' il valore nullo per le date

basta scrivere il valore che vogliamo sostituire e il valore con cui vogliamo sostituirlo
es.
df = df.replace('?', '0')
o
df = df.replace('NaN', '0')
o
df = df.replace('0', 'NaN')
o
df = df.replace('N/A', '0')
o
na_values = [' ', '?', 'NaN', '0', '-', 'N/A', 'NULL', 'NaT'] 
così possiamo sostituire più valori contemporaneamente con un solo comando che ci ridà per tutti i valori strani un valore nullo

o
df = df.replace(na_values, np.nan)

#
possiamo farlo direttamente quando carichiamo il dataset

df = pd.read_csv('btc_prices.csv',
header = 0, # la prima riga è l'header,
na_values = [' ', '?', 'NaN', '0', '-', 'N/A', 'NULL', 'NaT'] # i valori nulli
)

oppure

df = pd.read_csv('btc_prices.csv',
header = None, # non c'è l'header
na_values = [' ', '?', 'NaN', '0', '-', 'N/A', 'NULL', 'NaT'] # i valori nulli
)



oppure
possiamo mettere noi l'header

df = pd.read_csv('btc_prices.csv',
header = None, # non c'è l'header
names = ['Data', 'Prezzo', 'Volume', 'Cap', 'Apertura', 'Chiusura'], # i nomi delle colonne
na_values = [' ', '?', 'NaN', '0', '-', 'N/A', 'NULL', 'NaT'] # i valori nulli
)




oppure



df = pd.read_csv('btc_prices.csv',
header = 0, # la prima riga è l'header,
names = ['Data', 'Prezzo', 'Volume', 'Cap', 'Apertura', 'Chiusura'], # i nomi delle colonne
na_values = [' ', '?', 'NaN', '0', '-', 'N/A', 'NULL', 'NaT'] # i valori nulli
)




'''






































df = pd.read_csv('top_1000_songs_clean.csv')

# sono rimaste 5 canzoni, le altre sono state eliminate



# voglio forzare il DF per vedere tutte le colonne
pd.set_option('display.max_columns', None)  # mostra tutte le colonne

# voglio forzare il DF per vedere tutte le righe
pd.set_option('display.max_rows', None)  # mostra tutte le righe



# vediamo la nostra tabella
print(df.head())




print('\n')
# COMPITO

# usando matplotlib per fare un grafico a barre
# voglio avere un istogramma che mi confronti gli stream su spotify e quelli su you tube, in base al titolo della canzone


# 1. vediamo il nome delle colonne
print(df.columns)



import matplotlib.pyplot as plt

# Seleziona i brani
top10 = df.head()

# Crea il grafico
plt.figure(figsize=(12, 6))

# Barre Spotify
plt.bar(top10['Titolo'], top10['Stream Spotify (M)'], label='Spotify', color='green')

# Barre YouTube (sovrapposte leggermente, oppure puoi usare plt.barh se preferisci orizzontale)
plt.bar(top10['Titolo'], top10['Visualizzazioni YouTube (M)'], label='YouTube', color='red', alpha=0.6)

# Etichette
plt.xticks(rotation=45, ha='right')
plt.ylabel('Numero di stream')
plt.title('Confronto Spotify vs YouTube')
plt.legend()

plt.tight_layout()
plt.show()








### codice con barre affiancate

import matplotlib.pyplot as plt
import numpy as np

# Seleziona i primi 10 brani
top10 = df.head()

# Assegna posizione base sull'asse X
x = np.arange(len(top10))

# Larghezza di ogni barra
bar_width = 0.4

# Crea il grafico
plt.figure(figsize=(12, 6))

# Barre Spotify (più a sinistra)
plt.bar(x - bar_width/2, top10['Stream Spotify (M)'], width=bar_width, label='Spotify', color='green')

# Barre YouTube (più a destra)
plt.bar(x + bar_width/2, top10['Visualizzazioni YouTube (M)'], width=bar_width, label='YouTube', color='red')

# Etichette X
plt.xticks(x, top10['Titolo'], rotation=45, ha='right')
plt.ylabel('Numero di stream')
plt.title('Confronto Spotify vs YouTube per i primi 5 brani')
plt.legend()

plt.tight_layout()
plt.show()
