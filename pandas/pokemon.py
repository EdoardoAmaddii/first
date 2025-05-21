
import pandas as pd
import os
file_path = os.path.join(os.path.expanduser('~'), 'OneDrive', 'pandas', 'pokemon_csv.csv')
df = pd.read_csv(file_path)
print(df.head())

# questo è un file ben formattato, con le intestazioni delle colonne e i dati separati da virgole

# SEPARATORE

# ora mettiamo che ci siano dei tab a caso in mezzo ai dati e non la virgola
# per esempio, il file potrebbe essere formattato in questo modo:
# Nome\tTipo\tAttacco\tDifesa
# Pikachu\tElettrico\t55\t40    
# Charmander\tFuoco\t52\t43
# Bulbasaur\tErba\t49\t49
# ora proviamo a leggere il file con pandas, ma senza specificare il separatore
# in questo caso pandas non riuscirà a interpretare correttamente i dati
# df = pd.read_csv(file_path)  # Questo darà errore
# ora proviamo a leggere il file specificando il separatore come tab
# in questo modo pandas riuscirà a interpretare correttamente i dati

        #df = pd.read_csv(file_path, sep='\t')


# DELIMITER

# ci potrebbero essere tutti dati attaccati in una sola colonna, quindi dobbiamo specificare il delimiter
# in questo caso pandas non riuscirà a interpretare correttamente i dati
# df = pd.read_csv(file_path, delimiter='\t')  
# ora proviamo a leggere il file specificando il delimitatore come tab  
# in questo modo pandas riuscirà a interpretare correttamente i dati

print('\n\n')
#i file potrebbero essere delimitati da tab o da virgole o da a capo, quindi dobbiamo specificare il delimitatore
# in questo caso pandas non riuscirà a interpretare correttamente i dati
#proviamo a inserire come delimitatore il tab e a capo
    # df = pd.read_csv(file_path, delimiter='\n')
    # print(df.head())






#proviamo ora a leggere un file json
# il file json è un file di testo che contiene dati in formato json


file_json = os.path.join(os.path.expanduser('~'), 'OneDrive', 'pandas', 'pokemon_json.json')
df_json = pd.read_json(file_json)
print(df_json.head())

# la differenza si può vedere nel trattamento dei dati quando sono nulli
# in questo caso pandas userà NaN per i dati nulli, mentre in un file csv pandas userà " " per i dati nulli

# mandiamolo a schermo come fosse una stringa
print(df_json.head(10).to_string)




