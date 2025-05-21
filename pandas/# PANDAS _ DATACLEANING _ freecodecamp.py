# DATACLEANING freecodecamp


# 4 parti

# handling missing data

import numpy as np
import pandas as pd

''''
# identify  null values

pd.isnull(np.nan)

pd.isnull(None)

pd.isna(np.nan)

pd.isna(None)


# identify non-null values

pd.notnull(None)

pd.notnull(np.nan)

pd.notnull(3)


# lavorano con Serie e con dataframe

pd.isnull(pd.Series([1,2,3,np.nan]))
pd.notnull(pd.Series([1,2,3,np.nan]))

pd.isnull(pd.DataFrame([[1,2,3],[4,5,np.nan]]))
pd.notnull(pd.DataFrame([[1,2,3],[4,5,np.nan]]))



# pandas operations with missing values

pd.Series([1,2,3,np.nan]).sum()  # ci da 6.0
pd.Series([1,2,3,np.nan]).mean()  # ci da 2.0
pd.Series([1,2,3,np.nan]).count()  # ci da 3.0
pd.Series([1,2,3,np.nan]).min()  # ci da 1.0
pd.Series([1,2,3,np.nan]).max()  # ci da 3.0
pd.Series([1,2,3,np.nan]).median()  # ci da 2.0
pd.Series([1,2,3,np.nan]).std()  # ci da 1.0


# filtering missing data

s = pd.Series([1,2,3,np.nan])

pd.notnull(s)  # ci da una serie di booleani
pd.notnull(s).sum()  # ci da 3.0
pd.notnull(s).mean()  # ci da 0.75
pd.notnull(s).count()  # ci da 4.0

s[pd.notnull(s)]  # ci da una serie senza i valori nulli
s[s.notnull()]  # ci da una serie senza i valori nulli
s[s.notna()]  # ci da una serie senza i valori nulli

pd.isnull(s)  # ci da una serie di booleani
pd.isnull(s).sum()  # ci da 1.0
pd.isnull(s).mean()  # ci da 0.25
pd.isnull(s).count()  # ci da 4.0

s[pd.isnull(s)]  # ci da una serie con i valori nulli
s.isnull()  # ci da una serie con i valori nulli
s[s.isnull()]  # ci da una serie con i valori nulli
s[s.notnull()]  # ci da una serie senza i valori nulli # simile a dropna()
s[s.notna()]  # ci da una serie senza i valori nulli # simile a dropna()



# dropping null values

s.dropna()  # ci da una serie senza i valori nulli
s.dropna(inplace=True)  # ci da una serie senza i valori nulli e modifica la serie originale


df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, 5, 6],
    'C': [7, 8, np.nan, 9]
})

df.info()  # ci da informazioni sul dataframe

df.isnull()  # ci da un dataframe con i valori nulli

df.notnull()  # ci da un dataframe con i valori non nulli

df.notnull().sum()  # ci da il numero di valori non nulli per colonna

df.notnull().sum(axis=1)  # ci da il numero di valori non nulli per riga

df.notnull().sum(axis=0)  # ci da il numero di valori non nulli per colonna

df.dropna()  # ci da un dataframe senza i valori nulli, tutte le righe con almeno un valore nullo vengono eliminate, ci lascia solo la riga 1 = B


df2 = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, 5, 6],
    'C': [7, 8, np.nan, 9, np.nan],
    'D': [np.nan, 10, 11, 12]
})


df2.info()  # ci da informazioni sul dataframe

df2.isnull()  # ci da un dataframe con i valori nulli

df2.notnull()  # ci da un dataframe con i valori non nulli

df2.dropna(how='all')  # ci da un dataframe senza i valori nulli, tutte le righe con tutti i valori nulli vengono

df2.dropna(how='any')  # ci da un dataframe senza i valori nulli, tutte le righe con almeno un valore nullo vengono eliminate, ci lascia solo la riga 1 = B

df2.dropna(thresh=2)  # ci da un dataframe senza i valori nulli, tutte le righe con meno di 2 valori non nulli vengono eliminate, ci lascia solo la riga 1 = B e C

df.dropna(thresh=2, axis='columns')  # ci da un dataframe senza i valori nulli, tutte le colonne con meno di 2 valori non nulli vengono eliminate, ci lascia solo la colonna B e C

df.dropna(thresh=2, axis=1)  # ci da un dataframe senza i valori nulli, tutte le colonne con meno di 2 valori non nulli vengono eliminate, ci lascia solo la colonna B e C

df.dropna(thresh=2, axis=0)  # ci da un dataframe senza i valori nulli, tutte le righe con meno di 2 valori non nulli vengono eliminate, ci lascia solo la riga 1 = B e C

df.dropna(thresh=2, axis='index')  # ci da un dataframe senza i valori nulli, tutte le righe con meno di 2 valori non nulli vengono eliminate, ci lascia solo la riga 1 = B e C




## filling missing values

s = pd.Series([1, 2, 3, np.nan])

s.fillna(0)  # ci da una serie con i valori nulli sostituiti con 0

s.fillna(0, inplace=True)  # ci da una serie con i valori nulli sostituiti con 0 e modifica la serie originale

s.fillna(method='ffill')  # ci da una serie con i valori nulli sostituiti con il valore precedente

s.fillna(method='bfill')  # ci da una serie con i valori nulli sostituiti con il valore successivo

s.fillna(s.mean())  # ci da una serie con i valori nulli sostituiti con la media della serie

s.fillna(s.median())  # ci da una serie con i valori nulli sostituiti con la mediana della serie    


df = pd.DataFrame({
    'A': [1, 2, np.nan],
    'B': [4, 5, 6],
    'C': [7, 8, np.nan, 9]
})

df.fillna(0)  # ci da un dataframe con i valori nulli sostituiti con 0

df.fillna(0, inplace=True)  # ci da un dataframe con i valori nulli sostituiti con 0 e modifica il dataframe originale

df.fillna({'A': 0, 'B': 1, 'C': df['C'].mean()})  # ci da un dataframe con i valori nulli sostituiti con 0 per la colonna A, 1 per la colonna B e la media della colonna C per la colonna C

df.fillna(method='ffill')  # ci da un dataframe con i valori nulli sostituiti con il valore precedente

df.fillna(method='ffill', axis=0) # ci da un dataframe con i valori nulli sostituiti con il valore precedente per le colonne

df.fillna(method='ffill', axis=1) # ci da un dataframe con i valori nulli sostituiti con il valore precedente per le righe

df.fillna(method='bfill')  # ci da un dataframe con i valori nulli sostituiti con il valore successivo  

df.fillna(df.mean())  # ci da un dataframe con i valori nulli sostituiti con la media della colonna

df.fillna(df.median())  # ci da un dataframe con i valori nulli sostituiti con la mediana della colonna

df.fillna(df.median(axis=0))  # ci da un dataframe con i valori nulli sostituiti con la mediana della colonna

df.fillna(df.median(axis=1))  # ci da un dataframe con i valori nulli sostituiti con la mediana della riga  










### cleaning not-null values


df = pd.DataFrame({
    'Sex': ['M', 'F', 'D', 'M', 'F', '?'],
    'Age': [23, 45, 34, 231, 45],
    'Height': [1.80, 1.70, 1.75, 1.60, 1.65],
})


# non mancano valori, ma ci sono valori non validi

df['Sex'].unique()  # ci da i valori unici della col

df['Sex'].value_counts()  # ci da il numero di occorrenze di ogni valore della colonna


df['Sex'].replace('D', 'M')  # ci da un dataframe con i valori D sostituiti con M

df['Sex'].replace('D', 'M', inplace=True)  # ci da un dataframe con i valori D sostituiti con M e modifica il dataframe originale

df['Sex'].replace('?', np.nan)  # ci da un dataframe con i valori ? sostituiti con NaN

df['Sex'].replace({'D': 'M', '?': np.nan})  # ci da un dataframe con i valori D sostituiti con M e ? sostituiti con NaN


df.replace({
    'Sex': {'D': 'M', '?': np.nan},
    'Age': {231: 23}
})  # ci da un dataframe con i valori D sostituiti con M e ? sostituiti con NaN e 231 sostituiti con 23


### N.B. potremmo non sapere i valori di un dataframe
# in questo caso vediamo che i nostri anni devono essere sicuramente sotto i 100 anni, quindi possiamo fare un filtro per eliminare i valori sopra i 100 anni

df[df['Age'] < 100]  # ci da un dataframe con i valori sopra i 100 anni eliminati

df[df['Age'] < 100].copy()  # ci da un dataframe con i valori sopra i 100 anni eliminati e crea una copia del dataframe originale

df['Age'] = df['Age'].where(df['Age'] < 100)  # ci da un dataframe con i valori sopra i 100 anni sostituiti con NaN

df['Age'] = df['Age'].where(df['Age'] < 100, np.nan)  # ci da un dataframe con i valori sopra i 100 anni sostituiti con NaN

df['Age'] = df['Age'].where(df['Age'] < 100, 0)  # ci da un dataframe con i valori sopra i 100 anni sostituiti con 0

df['Age'] = df['Age'].where(df['Age'] < 100, df['Age'].mean())  # ci da un dataframe con i valori sopra i 100 anni sostituiti con la media della colonna








'''


### duplicate values

ambassador = pd.DataFrame([
    'France', 'Italy', 'Italy','Italy', 'Germany', 'Spain', 'France',
], index=[
    'Edoardo', 'Giovanni', 'Giuseppe', 'Francesco', 'Hans', 'Pedro', 'Edmundo'
])


ambassador  # ci da un dataframe con i valori duplicati
# cambiamo il nome della colonna
ambassador.columns = ['Country']  # ci da un dataframe con i valori duplicati e cambia il nome della colonna


ambassador.duplicated() # ci da un dataframe con i valori duplicati, ci da True per i valori duplicati e False per i valori unici, tiene in considerazione come true solo il secondo valore duplicato

ambassador.duplicated(keep='first')  # ci da un dataframe con i valori duplicati, ci da True per i valori duplicati e False per i valori unici, tiene in considerazione come true solo il secondo valore duplicato

ambassador.duplicated(keep='last')  # ci da un dataframe con i valori duplicati, ci da True per i valori duplicati e False per i valori unici, tiene in considerazione come true solo il primo valore duplicato

ambassador.duplicated(keep=False)  # ci da un dataframe con i valori duplicati, ci da True per i valori duplicati e False per i valori unici, tiene in considerazione come true tutti i valori duplicati



ambassador.drop_duplicates()  # ci da un dataframe senza i valori duplicati, ci lascia solo i valori unici

ambassador.drop_duplicates(keep='first')  # ci da un dataframe senza i valori duplicati, ci lascia solo il primo valore unico

ambassador.drop_duplicates(keep='last')  # ci da un dataframe senza i valori duplicati, ci lascia solo l'ultimo valore unico

ambassador.drop_duplicates(keep=False)  # ci da un dataframe senza i valori duplicati, ci lascia solo i valori unici




players = pd.DataFrame({
    'Nome': ['Del Piero', 'Totti', 'Nesta', 'Buffon', 'Pirlo', 'Totti', 'Del Piero',
], 'Posizione' :['Attaccante', 'Attaccante', 'Difensore', 'Portiere', 'Centrocampista', 'Centrocampista', 'Attaccante']})

players  # ci da un dataframe con i valori duplicati

players.duplicated()  # ci da un dataframe con i valori duplicati, ci da True per i valori duplicati e False per i valori unici, tiene in considerazione come true solo il secondo valore duplicato

players.duplicated(subset=['Nome'])  # ci da un dataframe con i valori duplicati, ci da True per i valori duplicati e False per i valori unici, tiene in considerazione come true solo il secondo valore duplicato, ma solo per la colonna Nome

players.duplicated(subset=['Nome', 'Posizione'])  # ci da un dataframe con i valori duplicati, ci da True per i valori duplicati e False per i valori unici, tiene in considerazione come true solo il secondo valore duplicato, ma solo per le colonne Nome e Posizione


# dobbiamo capire quali valori sono veramente duplicati, perchè totti e del piero sono duplicati, ma stiamo considerando magari stagioni diverse, quindi non sono duplicati
# in questo senso Totti potrebbe avere fatto 2 anni da attaccante e 2 da centrocampista, quindi non sono duplicati

# l'unico valore duplicato è Del Piero, che ha fatto 2 anni da attaccante, quindi possiamo considerarlo duplicato
# in questo caso possiamo considerare duplicati solo i valori che hanno lo stesso nome e la stessa posizione, quindi possiamo usare il metodo drop_duplicates() per eliminare i valori duplicati

players.drop_duplicates(subset=['Nome', 'Posizione'])  # ci da un dataframe senza i valori duplicati, ci lascia solo i valori unici












## string cleaning

'''

strangedf = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I   T_2',
    ]})

print(strangedf)  # ci da un dataframe con i valori duplicati
# ci da un dataframe con i valori duplicati

# sappiamo che ci sono 4 colonne, quindi possiamo usare il metodo str.split() per separare i valori in 4 colonne
# '' year, sex, country, number

strangedf['Data'].str.split('_')  # ci ridà il dataframe con i valori separati in 4 colonne, ma non sono puliti
strangedf['Data'].str.split('_', expand=True)  # ci da un dataframe con i valori separati in 4 colonne, ma non sono puliti

# Rimuovo spazi in eccesso
strangedf['Data'] = strangedf['Data'].str.replace(' ', '', regex=False)
strangedfdf = strangedf['Data'].str.split('_', expand=True)  # ci da un nuovo dataframe con i valori separati in 4 colonne, ma non sono puliti

print(strangedf)

strangedf.columns = ['Year', 'Sex', 'Country', 'Number']  # ci da un dataframe con i valori separati in 4 colonne e cambia il nome delle colonne

print(strangedf)


#  vediamo ora con contains, che ci da un booleano, se ci sono valori con ? o _

strangedf['Year'].str.contains('\?')  # ci da un dataframe con i valori booleani, se ci sono valori con ? o _
strangedf['Year'].str.contains('_')  # ci da un dataframe con i valori booleani, se ci sono valori con ? o _
strangedf['Year'].str.contains(' ')  # ci da un dataframe con i valori booleani, se ci sono valori con ? o _

# possiamo usare il metodo str.replace() per sostituire i valori con ? o _ con ''
# in questo caso possiamo usare il metodo str.replace() per sostituire i valori con ? o _ con ''

strangedf['Year'] = strangedf['Year'].str.replace('\?', '')  # ci da un dataframe con i valori sostituiti con ''
strangedf['Year'] = strangedf['Year'].str.replace('_', '')  # ci da un dataframe con i valori sostituiti con ''
strangedf['Year'] = strangedf['Year'].str.replace(' ', '')  # ci da un dataframe con i valori sostituiti con ''

'''



strangedf = pd.DataFrame({
    'Data': [
        '1987_M_US _1',
        '1990?_M_UK_1',
        '1992_F_US_2',
        '1970?_M_   IT_1',
        '1985_F_I   T_2',
    ]
})

# Rimuovo spazi in eccesso
strangedf['Data'] = strangedf['Data'].str.replace(' ', '', regex=False)

# Split in colonne
df = strangedf['Data'].str.split('_', expand=True)
df.columns = ['Year', 'Sex', 'Country', 'Number']

# Pulizia caratteri strani
df['Year'] = df['Year'].str.replace('?', '', regex=False)
df['Country'] = df['Country'].str.replace(' ', '', regex=False)

print(df)

# Optional: check contenuti anomali
print(df['Year'].str.contains('?', regex=False))




























#####################################################


import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from datetime import datetime, timedelta




# GLOBAL API
# 1. importare la libreria
# 2. creare una figura e un asse
# 3. creare i dati
# 4. creare il grafico
# 5. mostrare il grafico
# 6. salvare il grafico
# 7. chiudere il grafico

# 8. creare un grafico a dispersione
# 9. creare un grafico a dispersione con una linea di regressione
# 10. creare un grafico a dispersione con una linea di regressione e una curva di regressione
# 11. creare un grafico a dispersione con una linea di regressione e una curva di regressione e una retta di regressione
# 12. creare un grafico a dispersione con una linea di regressione e una curva di regressione e una retta di regressione e una retta di regressione
# 13. creare un grafico a dispersione con una linea di regressione e una curva di regressione e una retta di regressione e una retta di regressione e una retta di regressione

x = np.arange(-10, 11)
# y = np.random.randint(0, 10, size=21)

# iniziamo a creare un grafico a dispersione con i dati x
# non mi interessa il valore di y, ma voglio vedere i punti x

# devo assegnare una variabile a plt.scatter() per poterla modificare in seguito
plt.scatter(x, color='blue', label='Dati x')


plt.figure
plt.title('Grafico a dispersione')
plt.xlabel('Asse x')
plt.ylabel('Asse y')

plt.legend()
plt.grid()
plt.show()
plt.savefig('grafico_a_dispersione.png')
