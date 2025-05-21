import matplotlib as plt
import numpy as np
import pandas as pd


df = pd.read_csv('ai_comparison_cleaned.csv')

print(df.head())



# voglio forzare il DF per vedere tutte le colonne
pd.set_option('display.max_columns', None)  # mostra tutte le colonne

# voglio forzare il DF per vedere tutte le righe
pd.set_option('display.max_rows', None)  # mostra tutte le righe

print(df)




# abbiamo trovato i dati: utenti attivi mensili: inseriamoli


'''

📊 Utenti Attivi Mensili (MAU) – Maggio 2025
AI	MAU stimati (milioni)	Fonte
ChatGPT (GPT-4o)	600	Business Insider
Claude 3 Opus	18.9	Analyzify
Google Gemini Ultra	350	The Verge
Microsoft Copilot	26–36	Electro IQ
Mistral (Mixtral)	N/D	Nessun dato pubblico disponibile

'''


df.loc[df["AI"] == "ChatGPT (GPT-4o)", "Utenti Attivi Mensili (MAU)"] = 400000000

df.loc[df["AI"] == "Claude 3 Opus", "Utenti Attivi Mensili (MAU)"] = 20000000

df.loc[df["AI"] == "Google Gemini Ultra", "Utenti Attivi Mensili (MAU)"] = 350000000

df.loc[df["AI"] == "Microsoft Copilot", "Utenti Attivi Mensili (MAU)"] = 31000000


# per Mistral ci serve di inserire dati in modo diverso poichè non si trovano

# diciamo che essendo meno conosciuta hanno 10.000.000 di utenti al mese

df.loc[df["AI"] == "Mistral (Mixtral)", "Utenti Attivi Mensili (MAU)"] = 10000000


# vediamo se è tutto corretto
print(df)







# a questo punto inseriamo una nuova colonna per calcolare le query totali in un mese
# Aggiungo una colonna con un ipotesi di 20 query/giorno * 30 giorni

df["Query Totali Mese"] = df["Utenti Attivi Mensili (MAU)"] * 20 * 30



# vediamo se è tutto corretto
print(df)





# calcoliamo adesso il costo mensile

df["Costo Totale Mese (USD)"] = df["Query Totali Mese"] * df["Costo per Query (USD)"]

# check
print(df)




# Calcolo del consumo d'acqua mensile (in litri)
df["Acqua Totale Mese (litri)"] = (df["Query Totali Mese"] * df["Acqua per Query (ml)"]) / 1000
df["Acqua Totale Mese (litri)"] = df["Acqua Totale Mese (litri)"].round(0)


print(df)



# salviamo i nostri risultati
df.to_csv("nuova_versione_AI.csv", index=False)


















# creiamo grafici

import matplotlib.pyplot as plt


# Qui ti mostro il consumo acqua mensile (in litri) per ogni AI

plt.figure(figsize=(12,6))
plt.bar(df["AI"], df["Acqua per Query (ml)"] * df["Query Totali Mese"] / 1e6)  # Convertiamo ml a milioni di litri
plt.xticks(rotation=45, ha='right')
plt.ylabel("Acqua consumata mensilmente (milioni di litri)")
plt.title("Consumo mensile di acqua per AI")
plt.tight_layout()
plt.show()








########################


# Calcoliamo query totali mese e acqua totale mese (litri) come prima




df["Query Totali Mese"] = df["Utenti Attivi Mensili (MAU)"] * 20 * 30
df["Acqua Totale Mese (litri)"] = (df["Query Totali Mese"] * df["Acqua per Query (ml)"]) / 1000

# Usare la colonna "Costo Totale Mese (USD)" esistente senza ricalcolarla
# Conversioni per leggibilità
summary_df = df[["AI", "Utenti Attivi Mensili (MAU)", "Query Totali Mese", "Acqua Totale Mese (litri)", "Costo Totale Mese (USD)"]].copy()

summary_df["Query Totali Mese"] = summary_df["Query Totali Mese"] / 1e9  # miliardi
summary_df["Acqua Totale Mese (litri)"] = summary_df["Acqua Totale Mese (litri)"] / 1e6  # milioni litri
summary_df["Costo Totale Mese (USD)"] = summary_df["Costo Totale Mese (USD)"] / 1e6  # milioni USD

summary_df = summary_df.round({
    "Query Totali Mese": 2,
    "Acqua Totale Mese (litri)": 2,
    "Costo Totale Mese (USD)": 2
})

print(summary_df)

summary_df.to_csv("riepilogo_costi_acqua_utenza.csv", index=False)



# Grafico

labels = summary_df["AI"].values
x = np.arange(len(labels))
width = 0.25

fig, ax1 = plt.subplots(figsize=(14,7))

bar1 = ax1.bar(x - width, summary_df["Acqua Totale Mese (litri)"], width, label="Acqua (milioni litri)", color="tab:blue")
bar2 = ax1.bar(x, summary_df["Utenti Attivi Mensili (MAU)"] / 1e6, width, label="Utenti Attivi (milioni)", color="tab:orange")
bar3 = ax1.bar(x + width, summary_df["Costo Totale Mese (USD)"], width, label="Costo Totale (milioni USD)", color="tab:green")

ax1.set_ylabel("Valori")
ax1.set_title("Confronto mensile: Acqua, Utenti Attivi e Costo Totale")
ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45, ha='right')
ax1.legend()

def autolabel(bars, ax):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0,3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

autolabel(bar1, ax1)
autolabel(bar2, ax1)
autolabel(bar3, ax1)

plt.tight_layout()
plt.show()