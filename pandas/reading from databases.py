# reading from databases
'''
# reading direttamente da python senza usare pandas

import sqlite3

conn = sqlite3.connect('brani_musicali.db')  # connessione al database
cursor = conn.cursor()  # creazione del cursore
# creazione della tabella
cursor.execute('''
#CREATE TABLE IF NOT EXISTS brani_musicali (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    Titolo TEXT,
#    Artista TEXT,
#    Genere TEXT,
#    Durata INTEGER,
#    BPM INTEGER,
#    Data_Uscita TEXT,
#    Tonalità TEXT
#)''')
 
# il cursore esegue il comando

# a questo punto abbiamo creato la tabella, ora possiamo inserire i dati

# inserimento dei dati
#cursor.execute('''
#INSERT INTO brani_musicali (Titolo, Artista, Genere, Durata, BPM, Data_Uscita, Tonalità)
#VALUES
('Believer', 'Imagine Dragons', 'Rock', 204, 125, '2017-02-01', 'C#'),
('Can\'t Stop', 'Red Hot Chili Peppers', 'Rock', 269, 113, '2002-07-09', 'D'),
('Shape of You', 'Ed Sheeran', 'Pop', 235, 96, '2017-01-06', 'C#'),
('Despacito', 'Luis Fonsi ft. Daddy Yankee', 'Reggaeton', 229, 89, '2017-01-13', 'B'),
('Uptown Funk', 'Mark Ronson ft. Bruno Mars', 'Funk', 269, 115, '2014-11-10', 'D')
''')
# salviamo le modifiche
conn.commit()  # salvataggio delle modifiche

# ora possiamo leggere i dati
cursor.execute('SELECT * FROM brani_musicali')  # selezione di tutti i dati
rows = cursor.fetchall()  # recupero dei dati
for row in rows:  # stampa dei dati
    print(row)
# chiudiamo la connessione

conn.close()  # chiusura della connessione



# una volta che abbiamo i dati possiamo usare pandas per fare le nostre analisi

import pandas as pd

# creiamo un dataframe con i dati del database
df = pd.read_sql_query('SELECT * FROM brani_musicali', conn)  # creazione del dataframe
# chiudiamo la connessione
conn.close()  # chiusura della connessione
# ora possiamo usare il dataframe per
# fare le nostre analisi
# voglio forzare il DF per vedere tutte le colonne
pd.set_option('display.max_columns', None)  # mostra tutte le colonne
# voglio forzare il DF per vedere tutte le righe
pd.set_option('display.max_rows', None)  # mostra tutte le righe
# vediamo la nostra tabella
print(df.head())
print('\n')



# non ci stampa niente perchè il nostro dataaframe non esiste ancora








# leggiamo direttamente i file con pandas dal database

conn = sqlite3.connect('brani_musicali.db')  # connessione al database
# creiamo un dataframe con i dati del database
df = pd.read_sql('SELECT * FROM brani_musicali', conn)  # creazione del dataframe

# possiamo anche scrivere di leggere direttamente la query
df = pd.read_sql_query('SELECT * FROM brani_musicali', conn)  # creazione del dataframe

# ma possiamo anche leggere direttamente il file: la table deve essere già creata

df = pd.read_sql_table('brani_musicali', conn)  # creazione del dataframe


print(df.head())

# chiudiamo la connessione
conn.close()  # chiusura della connessione

# chiudere la connessione è importante per evitare problemi di memoria
# ma non è necessario farlo ogni volta che si legge un file











# possiamo anche leggere to_sql che ci permette di scrivere i dati in un database non esistente

df.to_sql('brani_musicali', conn, if_exists='replace', index=False)  # scrittura del dataframe nel database




'''























##############################################à##############################

# leggiamo file HTML

# pip install lxml
# pip install html5lib
# pip install beautifulsoup4
# pip install requests
# pip install pandas
# pip install openpyxl
# pip install xlrd
# pip install xlwt
# pip install openpyxl
# pip install html5lib

import numpy as np
import pandas as pd
from IPython.core.display import HTML

# attenzione alle pagine che non sono più disponibili, non ben strutturate o che non sono più aggiornate

df = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2023_totals.html')

# probabilmente avremo tabelle multiple
################################

# parsing with HTML

# possiamo leggere anche così

html_url = 'https://www.basketball-reference.com/leagues/NBA_2023_totals.html'

nba_tables = pd.read_html(html_url)


print(len(nba_tables)) # ci sono due tables

nba = nba_tables[0] # prendiamo il primo e leggiamolo

print(nba.head())





