import pandas as pd
import os

file_path = os.path.join(os.path.expanduser('~'), 'OneDrive', 'pandas', 'pokemon_csv.csv')
df = pd.read_csv(file_path)

# creiamo un sottodataframe

df2 = df[['Name', '#', 'Total']]

# ora salviamo il dataframe in diversi formati
# per farlo dobbiamo usare il metodo to_csv() di pandas
# il metodo to_csv() di pandas prende due parametri:
# il primo è il nome del file in cui vogliamo salvare il dataframe, il secondo è il separatore che vogliamo usare per salvare il dataframe
# il separatore di default è la virgola, quindi non dobbiamo specificarlo

df2.to_csv('mini_pokemon.csv', sep=',', index=False) # index = False per non salvare l'indice del dataframe





## in questo modo è più sicuro, salviamo il file in una cartella specifica
# in questo caso la cartella è OneDrive/pandas

import pandas as pd
import os

# Definiamo il percorso completo
base_dir = os.path.join(os.path.expanduser('~'), 'OneDrive', 'pandas')

# Controlliamo se la cartella esiste, se no la creiamo
os.makedirs(base_dir, exist_ok=True)

# Ora costruiamo il percorso completo del file da salvare
file_path = os.path.join(base_dir, 'mini_pokemon.csv')

# Leggiamo il file originale
original_file = os.path.join(base_dir, 'pokemon_csv.csv')
df = pd.read_csv(original_file)

# Creiamo un sottodataframe
df2 = df[['Name', '#', 'Total']]

# Salviamo il file nel percorso sicuro
df2.to_csv(file_path, sep=',', index=False)






######

# creiamo un csv compresso

compressed_df2 = dict(method='zip', archive_name='mini_pokemon.csv')
#
# questa parte del codice serve per comprimere il file in formato zip 
df2.to_csv('mini_pokemon.zip', sep=',', index=False, compression='zip') # index = False per non salvare l'indice del dataframe
# in questo caso il file sarà compresso in formato zip, quindi il file sarà più piccolo






### ora salviamo il dataframe in formato excel

# per farlo dobbiamo usare il metodo to_excel() di pandas
# il metodo to_excel() di pandas prende due parametri:
# il primo è il nome del file in cui vogliamo salvare il dataframe, il secondo è il nome del foglio in cui vogliamo salvare il dataframe
# il nome del foglio di default è 'Sheet1', quindi non dobbiamo specificarlo
# il file sarà salvato in formato xlsx, quindi il file sarà più grande



df2.to_excel('mini_pokemon.xlsx', sheet_name='Pokemon totali', index=False) # index = False per non salvare l'indice del dataframe

# creiamo più fogli in un file excel

df3 = df[['Name', '#', 'Total', 'HP']]
df4 = df[['Name', '#', 'Total', 'Attack']]


with pd.ExcelWriter('mini_pokemon_multiple_sheets.xlsx') as writer:
    df2.to_excel(writer, sheet_name='Pokemon totali', index=False) # index = False per non salvare l'indice del dataframe
    df3.to_excel(writer, sheet_name='Pokemon HP', index=False) # index = False per non salvare l'indice del dataframe
    df4.to_excel(writer, sheet_name='Pokemon Attack', index=False) # index = False per non salvare l'indice del dataframe




## creiamo un foglio con iloc

# iloc è un metodo di pandas che ci permette di selezionare le righe e le colonne del dataframe in base alla loro posizione
df5 = df.iloc[0:10, 0:4] # selezioniamo le prime 10 righe e le prime 3 colonne del dataframe

with pd.ExcelWriter('sezione_nuovi_pokemon.xlsx') as writer:
    df5.to_excel(writer, sheet_name='Foglio appeso', index=False) 
