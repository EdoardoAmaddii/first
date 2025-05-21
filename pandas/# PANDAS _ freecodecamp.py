# PANDAS _ freecodecamp

import pandas as pd
from datetime import time as to_datetime



## SERIES

# ordered / indexing series of elements


serie = pd.Series([1,2,3,4,5])

print(serie)

print(serie[0])


# possiamo definire noi quale è l'indice da dare alla nostra serie

import pandas as pd

serie = pd.Series([1, 2, 3, 4, 5], index=[
    'Canada',
    'Francia',
    'Italia',
    'Russia',
    'U.S.A'
])

print(serie['Italia'])  # esempio di accesso tramite nuovo indice




# divisione del codice in blocchi    ---   così assomiglia ad un vocabolario, ma ordinato

valori = [1, 2, 3, 4, 5]
etichette = ['Canada', 'Francia', 'Italia', 'Russia', 'U.S.A']

seriedivisa = pd.Series(valori, index=etichette)


print(seriedivisa)             # stampa tutta la serie
print(seriedivisa['Italia'])   # accesso tramite etichetta
print(seriedivisa.iloc[2])          # accesso tramite posizione (possiamo usare direttamente lo slice, ma è meglio usare iloc)





# possiamo creare una serie come un vocabolario saltando un passaggio e inserendo anche un nome per la serie

seriedict = pd.Series({
    'Orbe': 100000,
    'Capalbio': 5000,
    'Porto Ercole': 3000
}, name='Population')

print(seriedict)



## altro modo

seriediv = pd.Series(
    [5,6,7,8],
    index=['Almati','Krakovia','Tahiti','Perugia'],
    name='City of the world'
)

print(seriediv)





print('\n\n')

# BOOLEAN SERIES


# possiamo fare operazioni sulle nostre serie
print(seriedict * 1000)

print('\n\n')

# possiamo prendere dti dalle nostre serie utilizando operatori booleani

print(seriedict > 7000)  # ci ridarà TRUE O FALSE

print('\n\n')

print(seriedict[seriedict>7000])


print('\n\n')
## dammi il valore media degli elementi e poi tutti gli elementi sotto la media

print(seriedict.mean())

print(seriedict[seriedict < seriedict.mean()])




print('\n\n')
# possiamo usare anche (not ~ (non hai la tilde sulla tastiera), or  |, and  &)



df = pd.DataFrame({
    'nome': ['Edoardo', 'Luca', 'Anna'],
    'attivo': [True, False, True]
})

# Filtra chi NON è attivo
non_attivi = df[~df['attivo']]
print(non_attivi)




print('\n\n\n')
######
# MODIFICA SERIE



seriedict = pd.Series({
    'Orbe': 100000,
    'Capalbio': 5000,
    'Porto Ercole': 3000
}, name='Population')

print(seriedict)



## ricorda che i cambiamenti sono permanenti

# by index

seriedict['Orbe'] = 400000

print(seriedict)


# by position

seriedict.iloc[-1] = 1000
print(seriedict)


# by boolean selection

# ricorda che l'operatore AND ha precedenze rispetto a min e mag, perciò senza parentesi ci ridà errore

seriedict[(seriedict>=1000) & (seriedict<6000)] = 70000

print(seriedict)

















print('\n\n\n\n')

###################
# DATAFRAME



import pandas as pd

data = {
    'Population': [35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.623],
    'GDP': [1785387, 2833687, 3874437, 2167744, 4602367, 2950039, 17348075],
    'Surface Area': [9984670, 640679, 357114, 301336, 377930, 242495, 9525067],
    'HDI': [0.913, 0.888, 0.916, 0.873, 0.891, 0.907, 0.915],
    'Continent': ['America', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe', 'America']
}

countries_index = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']

df = pd.DataFrame(data, index=countries_index)

#### 
# 
# OPERAZIONI COMUNI

print(df)

print('\n\n')

print(df.columns)

print('\n\n')

print(df.index)

print('\n\n')

print(df.info())

print('\n\n')

print(df.size)

print('\n\n')

print(df.shape)

print('\n\n')

print(df.describe())   # summary of statystics

print('\n\n')

print(df.dtypes)

print('\n\n')

print(df.dtypes.value_counts()) # che tipo di valori abbiamo e quanti





print('\n\n')
### selecting data from DF
# ci ridà una serie


# usando loc, ci ridà la riga

print(df.loc['Canada'])

print('\n\n')

# possiamo anche usare lo slice e criter*

print('\n')

print(df.loc['France':'Italy', 'Population'])

print('\n')
# usando iloc, per posizione la riga

print(df.iloc[-1])

print('\n\n')

# possiamo usare lo slice e criter*

print(df.iloc[1:3, 3])  # Germany and France HDI


print('\n')


# per nome la colonna

print(df['Population'])



print('\n\n\n')
#####
#####
#####
### CONDITIONAL SELECTION




data = {
    'Population': [35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.623],
    'GDP': [1785387, 2833687, 3874437, 2167744, 4602367, 2950039, 17348075],
    'Surface Area': [9984670, 640679, 357114, 301336, 377930, 242495, 9525067],
    'HDI': [0.913, 0.888, 0.916, 0.873, 0.891, 0.907, 0.915],
    'Continent': ['America', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe', 'America']
}

countries_index = ['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States']

df = pd.DataFrame(data, index=countries_index)



##
# 
#  restituisci determinati valori


print(df['Population']>70)   # true or false

print('\n')

print(df.loc[df['Population']>70]) # dati

print('\n')

print(df.loc[df['Population']>70, ['Population', 'HDI']])

print('\n')


## droppiamo

df1 = df.drop('Canada') # per indice nome
print(df1) #df, ma senza Canada   ['Canada','Japan']

print('\n\n')

df_nocol = df.drop(columns=['Population'])
print(df_nocol)

print('\n\n')



##### queste non sono raccomandate soprattutto ora

df_noaxis0 = df.drop(['Italy','Canada'], axis=0)
print(df_noaxis0)

print('\n\n')

df_noaxis1 = df.drop(['Population','HDI'], axis=1)
print(df_noaxis1)

#######

print('\n\n\n\n')




### operazioni tra le serie

# uniamo più serie

crisis = pd.Series([-1000000, -0.3], index = ['GDP','HDI'])
print(crisis)

print('\n')

unione_df = df [['GDP','HDI']] + crisis  # sottraiamo 1.000.000 dai GDP e 0.3 da HDI
print(unione_df)






print('\n\n')
####
# MODIFICHIAMO DATAFRAME

print(df.drop('Canada')) # notiamo che non è una modifica permanente
print(df)

print('\n\n')

## inseriamo una nuova colonna
langs = pd.Series(
    ['Franch', 'German', 'Italian'],
    index = ['France','Germany','Italy'],
    name = 'Language'
)

df['Language'] = langs
print(df)


print('\n\n')


###
# replacing values per column

df['Language'] = 'English'  # tutti i valori per la colonna diventano English

print(df)


print('\n\n')


# rename columns

newname = df.rename(
    columns={
        'HDI': 'Human Development Index',
        'Anual Popcorn consuption' : 'APC'  # non esiste, ma non crea problemi
    },
    index={
        'United States':'USA',
        'United Kingdom':'UK',
        'Argentina':'AR'  # non esiste, ma non crea problemi
    }
)

print(newname)


print('\n\n')




######
# 
#  create columns from other columns

# operazioni tra colonne su un altra colonna

df['GDP per population'] = df['GDP'] / df['Population']

print(df)







print('\n\n\n')

###########
# STATISTICAL INFORMATION

population = df['Population']

print(population.min(), population.max())
print('\n')
print(population.sum())
print('\n')
print(population.sum()/len(population))
print('\n')
print(population.mean())
print('\n')
print(population.std())
print('\n')
print(population.median())
print('\n')
print(population.describe())
print('\n')
print(population.quantile(.25))
print('\n')
print(population.quantile([.2,.4,.6,.8,1]))








'''
#####

# LEGGERE FILE ESTERNI

testo = pd.read_csv('')

# pandas assume di default che la prima riga del CSV are the name of the columns

testo = pd.read_csv('', header = None) # così non assume che la prima riga sia il nome delle colonne

testo.columns = ['','']

testo.shape

testo.head(), testo.tail()

testo.dtypes

testo.to_datetime(df['Timestamp']).head()  # turn this column in datetime column
testo['Timestamp'] = testo.to_datetime(df['Timestamp'])

# settiamo anche che l'indice del df sia il datetime

testo.set_index('Timestamp', inplace = True)

# es. prendiamo una riga particolare dicendo quale indice ci serve

testo.loc['2017-08-23']




#######
# mettiamo tutto insieme

df = pd.read_csv('ccsdev', header = None)

df.columns = ['Timestamp', 'Price']
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace = True)


### ancora più conciso

df = pd.read_csv(
    'vedvd.csv',
    header = None,
    names=['Timestamp','Price'],
    index_col=0,
    parse_dates=True
)

'''






















