import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('brani_musicali_clean.csv')

# voglio forzare il DF per vedere tutte le colonne
pd.set_option('display.max_columns', None)  # mostra tutte le colonne
print(df.head())
print('\n')



# facciamo l'analisi esplorativa dei dati

# STATISTICHE DI BASE
print(df.info())
print('\n')
print(df.describe())
print('\n')



# STATISTICHE DESCRITTIVE
# BRANO PIU' LUNGO
print('BRANO PIU LUNGO')
print(df[df['Durata'] == df['Durata'].max()])  # brano più lungo
print('\n')

# BRANO PIU' CORTO
print('BRANO PIU CORTO')
print(df[df['Durata'] == df['Durata'].min()])  # brano più corto
print('\n')

# BRANO CON PIU' BPM
print('BPM MASSIMO')
print(df[df['BPM'] == df['BPM'].max()])  # brano con più BPM
print('\n')

# BRANO CON MENO BPM
print('BPM MINIMO')
print(df[df['BPM'] == df['BPM'].min()])  # brano con meno BPM
print('\n')


# CONTIAMO GENERI E ANNI PRESENTI NEL DATASET
# GENERI
print('GENERI')
print(df['Genere'].value_counts())  # generi
print('\n')

# ANNI
print('ANNI')
print(df['Data_Uscita'].value_counts())  # anni
print('\n')



# CONTIAMO I BPM MEDI PER ANNO
# BPM MEDI PER ANNO
bpm_medi_per_anno = df.groupby('Data_Uscita')['BPM'].mean()
print('BPM MEDI PER ANNO')  
print(bpm_medi_per_anno)  # BPM medi per anno
print('\n')


# CONTIAMO I BPM MEDI PER GENERE
# BPM MEDI PER GENERE
bpm_medi_per_genere = df.groupby('Genere')['BPM'].mean()
print('BPM MEDI PER GENERE')
print(bpm_medi_per_genere)  # BPM medi per genere
print('\n')

# CONTIAMO I BPM MEDI PER ANNO E GENERE
# BPM MEDI PER ANNO E GENERE
bpm_medi_per_anno_genere = df.groupby(['Data_Uscita', 'Genere'])['BPM'].mean()
print('BPM MEDI PER ANNO E GENERE')
print(bpm_medi_per_anno_genere)  # BPM medi per anno e genere
print('\n')


# CONTIAMO QUALI SONO LE TONALITA' PIU' PRESENTI
# TONALITA' PIU' PRESENTI
print('TONALITA PIU PRESENTI')
print(df["Tonalità"].value_counts())  # tonalità più presenti
print('\n')

# VEDIAMO LE TONALITà PIU' PRESENTI PER ANNO
# TONALITA' PIU' PRESENTI PER ANNO
tonalita_per_anno = df.groupby('Data_Uscita')['Tonalità'].value_counts()
print('TONALITA PIU PRESENTI PER ANNO')
print(tonalita_per_anno)  # tonalità più presenti per anno
print('\n')

# VEDIAMO LE TONALITà PIU' PRESENTI PER GENERE
# TONALITA' PIU' PRESENTI PER GENERE
tonalita_per_genere = df.groupby('Genere')['Tonalità'].value_counts()
print('TONALITA PIU PRESENTI PER GENERE')
print(tonalita_per_genere)  # tonalità più presenti per genere
print('\n')

# VEDIAMO LE TONALITà PIU' PRESENTI PER ANNO E GENERE
# TONALITA' PIU' PRESENTI PER ANNO E GENERE
tonalita_per_anno_genere = df.groupby(['Data_Uscita', 'Genere'])['Tonalità'].value_counts()
print('TONALITA PIU PRESENTI PER ANNO E GENERE')
print(tonalita_per_anno_genere)  # tonalità più presenti per anno e genere
print('\n')



# VEDIAMO LE DURATE MEDIE PER ANNO
# DURATE MEDIE PER ANNO
durate_per_anno = df.groupby('Data_Uscita')['Durata'].mean()
print('DURATE MEDIE PER ANNO')
print(durate_per_anno)  # durate medie per anno
print('\n')

# VEDIAMO LE DURATE MEDIE PER GENERE
# DURATE MEDIE PER GENERE
durate_per_genere = df.groupby('Genere')['Durata'].mean()
print('DURATE MEDIE PER GENERE')
print(durate_per_genere)  # durate medie per genere
print('\n')

# VEDIAMO LE DURATE MEDIE PER ANNO E GENERE
# DURATE MEDIE PER ANNO E GENERE
durate_per_anno_genere = df.groupby(['Data_Uscita', 'Genere'])['Durata'].mean()
print('DURATE MEDIE PER ANNO E GENERE')
print(durate_per_anno_genere)  # durate medie per anno e genere
print('\n')














# ABBIAMO TERMINATO L'ANALISI DEI DATI
# ORA VEDIAMO COME VISUALIZZARE I DATI






# 1. VEDIAMO I BPM MEDI PER ANNO
#  2. VEDIAMO LA DURATA MEDIA PER ANNO
#   3. VEDIAMO I BPM MEDI PER GENERE













# 1. VEDIAMO I BPM MEDI PER ANNO
bpm_medi_per_anno = df.groupby('Data_Uscita')['BPM'].mean()
plt.figure(figsize=(10, 5)) 
plt.plot(bpm_medi_per_anno.index, bpm_medi_per_anno.values, marker='o')
plt.title('BPM medi per anno')
plt.xlabel('Anno')
plt.ylabel('BPM')
plt.xticks(rotation=45)
plt.grid()
plt.show()





# 3. VEDIAMO I BPM MEDI PER GENERE
bpm_medi_per_genere = df.groupby('Genere')['BPM'].mean()
plt.figure(figsize=(10, 5)) 
plt.bar(bpm_medi_per_genere.index, bpm_medi_per_genere.values)
plt.title('BPM medi per genere')
plt.xlabel('Genere')
plt.ylabel('BPM')
plt.xticks(rotation=45)
plt.grid()
plt.show()






# 2. VEDIAMO LA DURATA MEDIA PER ANNO
durate_per_anno = df.groupby('Data_Uscita')['Durata'].mean()
plt.figure(figsize=(10, 5))
plt.plot(durate_per_anno.index, durate_per_anno.values, marker='o')
plt.title('Durata media per anno')
plt.xlabel('Anno')
plt.ylabel('Durata (in secondi)')
plt.xticks(rotation=45)
plt.grid()
plt.show()




# PLUS # 4. VEDIAMO LA DURATA MEDIA PER GENERE
durate_per_genere = df.groupby('Genere')['Durata'].mean()
plt.figure(figsize=(10, 5))
plt.bar(durate_per_genere.index, durate_per_genere.values)
plt.title('Durata media per genere')
plt.xlabel('Genere')
plt.ylabel('Durata (in secondi)')
plt.xticks(rotation=45)
plt.grid()
plt.show()








# CI INTERESSA, DATA L'ANALISI DI VEDERE COME I BPM MEDI AUMENTINO NEL TEMPO E LA DURATA MEDIA DIMINUISCA


'''
# VEDIAMO COME I BPM MEDI AUMENTINO NEL TEMPO E LA DURATA MEDIA DIMINUISCA
# BPM MEDI E DURATA MEDIA PER ANNO
bpm_medi_per_anno = df.groupby('Data_Uscita')['BPM'].mean()
durate_per_anno = df.groupby('Data_Uscita')['Durata'].mean()
plt.figure(figsize=(10, 5))
plt.plot(bpm_medi_per_anno.index, bpm_medi_per_anno.values, marker='o', label='BPM medi')
plt.plot(durate_per_anno.index, durate_per_anno.values, marker='o', label='Durata media')
plt.title('BPM medi e durata media per anno')
plt.xlabel('Anno')
plt.ylabel('BPM e durata (in secondi)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.show()

'''

# VEDIAMO COME I BPM MEDI AUMENTINO NEL TEMPO E LA DURATA MEDIA DIMINUISCA


import matplotlib.pyplot as plt
import seaborn as sns

fig, ax1 = plt.subplots(figsize=(12,6))

# Asse y sinistro per BPM
color_bpm = 'tab:blue'
ax1.set_xlabel('Anno')
ax1.set_ylabel('BPM medio', color=color_bpm)
ax1.plot(bpm_medi_per_anno.index, bpm_medi_per_anno.values, marker='o', color=color_bpm, label='BPM medio', linewidth=2)
ax1.tick_params(axis='y', labelcolor=color_bpm)
ax1.set_xticklabels(bpm_medi_per_anno.index, rotation=45)

# Asse y destro per durata
ax2 = ax1.twinx()
color_dur = 'tab:red'
ax2.set_ylabel('Durata media (s)', color=color_dur)
ax2.plot(durate_per_anno.index, durate_per_anno.values, marker='x', linestyle='--', color=color_dur, label='Durata media', linewidth=2)
ax2.tick_params(axis='y', labelcolor=color_dur)

# Aggiungo titolo esplicativo
plt.title('Evoluzione nel tempo: aumento BPM medio e diminuzione durata media')

# Aggiungo legenda combinata
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left')

# Aggiungo annotazioni
ax1.annotate('BPM in aumento', xy=(bpm_medi_per_anno.index[-1], bpm_medi_per_anno.values[-1]),
             xytext=(bpm_medi_per_anno.index[-3], bpm_medi_per_anno.values[-1]+5),
             arrowprops=dict(facecolor=color_bpm, shrink=0.05), color=color_bpm)

ax2.annotate('Durata in diminuzione', xy=(durate_per_anno.index[-1], durate_per_anno.values[-1]),
             xytext=(durate_per_anno.index[-3], durate_per_anno.values[-1]+40),
             arrowprops=dict(facecolor=color_dur, shrink=0.05), color=color_dur)

plt.grid(True)
plt.tight_layout()
plt.show()



# ABBIAMO TERMINATO LA VISUALIZZAZIONE DEI DATI

# DALL'ANALISI DEI DATI ABBIAMO VISTO CHE I BPM MEDI AUMENTANO NEL TEMPO E LA DURATA MEDIA DIMINUISCE

# I BPM MEDI PER IL POP SONO PIU' ALTI DELLA MEDIA
# I BPM MEDI PER IL ROCK SONO PIU' BASSI DELLA MEDIA






# LAVORO OTTENUTO ATTRAVERSO L'UTILIZZO DELLE MIE COMPETENZE COME DATA ANALYST UNITE ALLO STUDIO DEL PROMPT ENGENEERING DI CHATGPT

