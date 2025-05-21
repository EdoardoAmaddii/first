import os
import pandas as pd

# Configura pandas per mostrare tutte le colonne e più righe
pd.set_option('display.max_columns', None)  # Mostra tutte le colonne
pd.set_option('display.width', None)  # Usa tutta la larghezza disponibile
pd.set_option('display.max_rows', None)  # Mostra tutte le righe
pd.set_option('display.float_format', '{:.2f}'.format)  # Formatta i numeri decimali

# Il percorso del file excel
file_excel = os.path.join(os.path.expanduser('~'), 'OneDrive', 'pandas', 'cryptos.xlsx')

# Leggi il file Excel, specificando il foglio "Bitcoin"
df = pd.read_excel(file_excel, sheet_name="Bitcoin")

# Mostra il DataFrame completo
print(df)
print('\n\n')

# Se il DataFrame è troppo grande, puoi usare df.head() per mostrare solo le prime righe
# Visualizza le prime 5 righe del dataframe con tutte le colonne

print(df.head())
print('\n\n')

# Mostra le informazioni sul DataFrame
print(df.info())
print('\n\n')


# se vogliamo modificare gli indici che sono diversi da 0,1,2,3,4,5,6,7,8,9
# possiamo usare index_col=0 per usare la prima colonna come indice, senza che sia un numero
# Leggi il file Excel, specificando il foglio "Bitcoin" e usando la prima colonna come indice
df = pd.read_excel(file_excel, sheet_name="Bitcoin", index_col=0)

# Mostra il primo elemento del DataFrame
print(df.iloc[0])
# me lo mostrerà in colonna come un dizionario, con le chiavi come i nomi delle colonne e i valori come i valori della riga
print('\n\n')

# se lo vogliamo prendere con loc, dobbiamo specificare il nome della colonna
# Mostra il primo elemento del DataFrame usando loc
print(df.loc['2019-03-20 14:00:00'])
print('\n\n')



