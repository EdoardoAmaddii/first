import pandas as pd

df = pd.read_csv('pokemon_csv.csv')

# modifichiamo il nome di un pokemon
df.loc[df['Name'] == 'Bulbasaur', 'Name'] = 'Bulbasaur 2.0' # modifichiamo il nome di un pokemon

print(df[df['Name'] == 'Bulbasaur 2.0']) # stampiamo il pokemon modificato
print('\n\n')

print(df.head())


# modifichiamo più colonne
# Assegnazione di valori diversi a colonne diverse
df.loc[df['Name'] == 'Bulbasaur 2.0', ['Type 1', 'Type 2']] = ['Erba', 'Veleno']
print(df[df['Name'] == 'Bulbasaur 2.0']) # stampiamo il pokemon modificato
print('\n\n')


# Modifica ogni colonna separatamente    # N.B.  i numeri devono rimanere tali, non stringhe nella modifica
df.loc[df['Name'] == 'Bulbasaur 2.0', 'Sp. Atk'] = 100 # modifichiamo il valore di una colonna
df.loc[df['Name'] == 'Bulbasaur 2.0', 'Sp. Def'] = 1000 # modifichiamo il valore di un'altra colonna

print(df[df['Name'] == 'Bulbasaur 2.0']) # stampiamo il pokemon modificato
print('\n\n')



# condiioni multiple
# Modifica di più colonne in base a più condizioni

df.loc[(df['Name'].str.contains('saur')) & (df['Total'] > 500), ['Type 1', 'Type 2']] = ['Erba Malefica', 'Veleno supremo'] 

print(df.head())














#####################################################################################################

#aggregazione dei dati


# raggiungiamo i dati in base a una colonna

types = df.groupby('Type 1')

print(types.groups) # stampiamo i gruppi creati
print('\n\n')


for name, group in types:
    print(name) # stampiamo il nome del gruppo
    print(group) # stampiamo il gruppo
    print('\n\n')




# raggruppiamo per multiple colonne


types = df.groupby(['Type 1', 'Type 2'])
print(types.groups) # stampiamo i gruppi creati
print('\n\n')

for name, group in types:
    print(name) # stampiamo il nome del gruppo
    print(group) # stampiamo il gruppo
    print('\n\n')




# raggruppiamo per più colonne e facciamo un'aggregazione
# in questo caso facciamo la somma dei punti di attacco e difesa
# e facciamo la media dei punti di attacco e difesa
# printiamo anche il conto dei pokemon per ogni tipo

print(df.groupby(['Type 1', 'Type 2'])[['Attack', 'Defense']].agg(['sum', 'mean', 'count'])) # stampiamo il risultato
print('\n\n')







# possiamo quindi vedere sum, min, max, count, mean, std, median, quantile, first, last, all, any, nunique, unique

types = df.groupby(['Type 1'])[['HP', 'Attack', 'Defense']].mean() # calcoliamo la media dei punti di attacco e difesa per ogni tipo
print(types) # stampiamo il risultato

print('\n\n')


# così per maggior flessibilità possiamo usare agg() per calcolare più aggregazioni
# Opzione 2
types = df.groupby(['Type 1']).agg({'HP': 'sum', 'Attack': 'mean', 'Defense': 'std', 'Speed': 'max'}) # calcoliamo la somma dei punti di attacco e difesa per ogni tipo
print(types)

print('\n\n')


# Opzione 3
# dopo aver fattto i calcoli possiamo anche sortare i risultati
# in questo caso facciamo la somma dei punti di attacco e difesa per ogni tipo
# e facciamo la media dei punti di attacco e difesa
# e ordiniamoli dal più basso al più alto
# e stampiamo anche il conto dei pokemon per ogni tipo

types = df.groupby(['Type 1'])[['HP', 'Attack', 'Defense']].agg(['sum', 'mean', 'count']).sort_values(by=[('HP', 'sum')], ascending=True) # calcoliamo la somma dei punti di attacco e difesa per ogni tipo / ordinati dal più piccolo al più grande
print(types) # stampiamo il risultato

# potremmo mettere il sort nel print invece di farlo prima
# types = df.groupby(['Type 1'])[['HP', 'Attack', 'Defense']].agg(['sum', 'mean', 'count'])
# print(types.sort_values(by=[('HP', 'sum')], ascending=False)) # calcoliamo la somma dei punti di attacco e difesa per ogni tipo
# stampiamo il risultato


print('\n\n')




# prendiamo, per type 1, i valori massimi di HP, Attack, Defense e Speed

# e stampiamo il risultato

types = df.groupby(['Type 1'])[['HP', 'Attack', 'Defense', 'Speed']].max().sort_values(by='HP',ascending=False) # calcoliamo la somma dei punti di attacco e difesa per ogni tipo

print(types) # stampiamo il risultato
print('\n\n')




## troviamo il nome corrispondente ai pokemon
# e stampiamo il risultato

# Supponiamo che df sia già il tuo DataFrame con le colonne 'Name', 'Type 1', 'HP', 'Attack', 'Defense', 'Speed'

# Troviamo i valori massimi per ogni statistica, per ogni 'Type 1'
max_stats = df.groupby('Type 1')[['HP', 'Attack', 'Defense', 'Speed']].max()

# Ora per ogni tipo e ogni statistica massima, troviamo il/i Pokémon corrispondente/i
for poke_type in max_stats.index:
    print(f"=== {poke_type} ===")
    max_values = max_stats.loc[poke_type]
    for stat in ['HP', 'Attack', 'Defense', 'Speed']:
        value = max_values[stat]
        matching_pokemon = df[(df['Type 1'] == poke_type) & (df[stat] == value)]
        for _, row in matching_pokemon.iterrows():
            print(f"{stat}: {row['Name']} ({value})")
    print("\n")





## salviamo il dataframe in un file csv

import pandas as pd

# Supponiamo che df sia già il tuo DataFrame con le colonne 'Name', 'Type 1', 'HP', 'Attack', 'Defense', 'Speed'

# Troviamo i valori massimi per ogni statistica, per ogni 'Type 1'
max_stats = df.groupby('Type 1')[['HP', 'Attack', 'Defense', 'Speed']].max()

# Lista per salvare i risultati
results = []

# Per ogni tipo e statistica, troviamo i Pokémon corrispondenti
for poke_type in max_stats.index:
    max_values = max_stats.loc[poke_type]
    for stat in ['HP', 'Attack', 'Defense', 'Speed']:
        value = max_values[stat]
        matching_pokemon = df[(df['Type 1'] == poke_type) & (df[stat] == value)]
        for _, row in matching_pokemon.iterrows():
            results.append({
                'Type': poke_type,
                'Stat': stat,
                'Name': row['Name'],
                'Value': value
            })

# Convertiamo in DataFrame
result_df = pd.DataFrame(results)

# Salviamo in CSV
result_df.to_csv('pokemon_top_stats_by_type.csv', index=False)

print("CSV salvato come 'pokemon_top_stats_by_type.csv'")







## concludiamo in modo più semplice e vediamo il count per i pokemon per ogni tipo
# e stampiamo il risultato

types = df.groupby(['Type 1']).count() 
print(types) # stampiamo il risultato


print('\n\n')


# vediamo anche le combinazioni e facciamo solo una colonna
# e stampiamo il risultato

df['count'] = 1 # creiamo una colonna con il valore 1 per ogni pokemon
types = df.groupby(['Type 1', 'Type 2']).count() # calcoliamo la somma dei punti di attacco e difesa per ogni tipo
print(types) # stampiamo il risultato