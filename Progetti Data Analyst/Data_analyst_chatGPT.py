'''

“Vogliamo stimare in modo realistico ed efficace quanto costa (in termini di energia, soldi e ambiente) 
mantenere un servizio come ChatGPT operativo ogni giorno”.



Domande che ci poniamo:
Quanta energia consuma una query su ChatGPT?

Quante query avvengono al giorno?

Quanto costa economicamente questa energia?

Quante emissioni di CO₂ produce questo uso?

Quanta acqua viene consumata per raffreddare i server?

Quali scenari futuri possiamo simulare (es. raddoppio utenti, maggiore efficienza)?








Per ogni domanda, individuiamo le variabili e unità di misura da raccogliere.

Variabile	Descrizione	Unità
energy_per_query_low	Consumo min per query	Wh
energy_per_query_high	Consumo max per query	Wh
num_queries_per_day	Numero medio di query	interi
cost_per_kWh	Prezzo energia elettrica	USD
co2_per_query_low	Emissioni CO₂ minime	g
co2_per_query_high	Emissioni CO₂ massime	g
water_per_session	Consumo acqua per sessione (media 20 query)	L

'''


# Dati stimati
energy_per_query_low = 0.3    # Wh
energy_per_query_high = 2.9   # Wh
num_queries_per_day = 1_000_000_000
cost_per_kWh = 0.10           # USD
co2_per_query_low = 0.3       # grammi
co2_per_query_high = 4.32     # grammi
water_per_session = 0.5       # litri per 20 query




'''

Giornalmente:
Energia totale consumata (Wh → kWh)

Costo totale giornaliero

Emissioni CO₂ totali (in kg e tonnellate)

Acqua totale consumata (in litri)

📅 Annualmente:
Tutto moltiplicato per 365





######################################à



 SIMULAZIONI (Scenario Analysis)
Questo è il bello da data analyst: testare scenari "what if".

🔼 Aumento utenti del 50%

🔽 Miglioramento dell’efficienza del 30%

💸 Cambiamento del costo per kWh (0,08 - 0,15 USD)

🌱 Obiettivo: abbattere emissioni CO₂ del 50% → quanta energia serve risparmiare?














STEP 6: VISUALIZZAZIONI
Faremo grafici per:

Consumo vs costo (low vs high)

Emissioni giornaliere e annuali

Risparmio simulato con tecnologie più efficienti

'''








'''

OBIETTIVO
Mettere a confronto le 5 AI generative più popolari (tipo ChatGPT, Claude, Gemini, Copilot, Mistral) in termini di:

Consumo energetico

Emissioni di CO₂

Consumo di acqua

Costo per query

Numero di utenti/adozione globale

🔎 STEP 1: LE 5 AI DA CONFRONTARE
Nome	Azienda	Modello	Tipo di accesso
ChatGPT	OpenAI	GPT-4-turbo	Web/app/API
Claude	Anthropic	Claude 3 Opus/Haiku	Web/API
Gemini	Google DeepMind	Gemini 1.5	Web/API
Copilot	Microsoft (OpenAI)	GPT-4 custom	IDEs/Web
Mistral	Mistral AI	Mistral Large/Mixtral	API/Open Source

📊 STEP 2: VARIABILI DA RACCOGLIERE
Variabile	Descrizione	Fonte attesa
energy_per_query	Consumo stimato per singola query (Wh)	Stime da paper/blog
co2_per_query	Emissioni CO₂ per query (g)	Come sopra
water_per_query	Acqua consumata (L)	Se disponibile
avg_cost_per_query	Costo stimato medio (USD)	API o analisi economiche
user_base	Utenti mensili (MAU)	Dati pubblici/stime

🧠 STEP 3: DOMANDE ANALITICHE
Quale AI è la più efficiente energeticamente?

Quale AI ha il miglior rapporto utenti/costo ambientale?

Chi inquina di più per query?

Quale modello ha il miglior bilancio tra costo e performance?

Cosa succederebbe se tutti usassero solo una AI?

📚 STEP 4: RACCOLTA DATI — iniziamo
Ora faccio una ricerca aggiornata sul web per raccogliere le stime disponibili su queste 5 AI. Cercherò:

dati su energia per query

emissioni CO₂

consumo acqua

numero utenti

prezzi API e consumer








##############################################à







Tabella Comparativa delle AI Generative
AI Model	Energia per Query (Wh)	CO₂ per Query (g)	Acqua per Query (ml)	Costo per Query (USD)	Utenti Attivi Mensili
ChatGPT	0.3 – 2.9	0.3 – 4.32	~1.5 (per 300 query)	~0.002 – 0.01	~400 milioni
Claude	~0.3 – 0.5	~0.3 – 1.0	ND	~0.002 – 0.005	ND
Gemini	~0.5 – 1.0	1.6	ND	~0.002 – 0.01	ND
Copilot	~0.3 – 0.5	ND	ND	Incluso in Microsoft 365	ND
Mistral	~0.2 – 0.4	Basso	ND	Open Source / API	ND

Note:

ND: Dato non disponibile.

I valori sono stime basate su fonti disponibili e possono variare in base all'uso specifico e all'infrastruttura sottostante.

🔍 Analisi dei Dati
⚡ Consumo Energetico
Mistral si distingue per l'efficienza energetica, con un consumo stimato tra 0.2 e 0.4 Wh per query.

ChatGPT mostra una variazione significativa, da 0.3 a 2.9 Wh per query, a seconda del modello e della complessità della richiesta.

🌍 Emissioni di CO₂
Gemini ha emissioni stimate di 1.6 g di CO₂ per query.

ChatGPT può arrivare fino a 4.32 g di CO₂ per query, secondo alcune stime.

💧 Consumo d'Acqua
ChatGPT consuma circa 1.5 ml di acqua per ogni 300 query, principalmente per il raffreddamento dei server.

💰 Costo per Query
Copilot è incluso nei pacchetti Microsoft 365, rendendo difficile stimare un costo per query.

Mistral offre modelli open source, potenzialmente riducendo i costi operativi.


'''











'''


La tabella seguente riepiloga i dati raccolti per ChatGPT, Claude, Google Gemini, Microsoft Copilot e Mistral AI sui parametri richiesti. I valori sono riportati con le fonti di riferimento.
Parametro	ChatGPT (OpenAI)	Claude (Anthropic)	Google Gemini	Microsoft Copilot	Mistral AI
Utenti attivi mensili (MAU)	~400 milioni (settimanali, Feb 2025)
techcrunch.com
18,9 milioni
backlinko.com
350 milioni
theverge.com
26–36 milioni
electroiq.com
N/D (nessun dato pubblico)
Energia/query (Wh)	~0,3 Wh
epoch.ai
–	–	–	–
CO₂/query (g)	~4,3 g
piktochart.com
–	–	–	–
Acqua/query (ml)	~5 ml (per conversazione tipo)
seangoedecke.com
–	–	–	–
Costo/query (USD)	~0,0036 $
manifold.markets
–	–	–	–
Tempo medio risposta	≈1 s di GPU per query
epoch.ai
–	–	–	–
Fonti energetiche (DC)	Azure: 100% rinnovabile entro il 2025
azure.microsoft.com
AWS: 100% energia rinnovabile (2023)
sustainability.aboutamazon.com
Google Cloud: 100% rinnovabile
cloud.google.com
Azure: 100% rinnovabile entro il 2025
azure.microsoft.com
AWS/Azure (100% rinnov.) e nuovo DC in FR completamente a energia nucleare
sifted.eu
Dimensione modello (parametri)	~1,8 trilioni
explodingtopics.com
(non pubblica, si parla di modelli fino ~2T)	~1,0 trilione (Gemini Ultra)
linkedin.com
(~1,8T se basato su GPT-4)	7,3 miliardi
mistral.ai

Note: “–” indica dati non disponibili pubblicamente. Per ChatGPT è riportato un consumo medio di 0,3 Wh per query (modello GPT-4o)
epoch.ai
, corrispondente a circa 4,3 g CO₂ (stima semplificata)
piktochart.com
 e ~5 ml di acqua per conversazione tipica
seangoedecke.com
. ChatGPT costa all’incirca 0,0036 USD per query
manifold.markets
. Le altre colonne (“Tempo medio risposta”, “Energia/query” etc.) non hanno stime pubbliche diffuse per gli altri modelli. Le fonti energetiche indicano le politiche dei cloud provider: Azure e AWS si stanno spingendo verso il 100% di elettricità rinnovabile
azure.microsoft.com
sustainability.aboutamazon.com
cloud.google.com
, mentre Mistral prevede un nuovo data center in Francia alimentato interamente da energia nucleare decarbonizzata
sifted.eu
. Fonti: I dati sono tratti da fonti ufficiali e analisi del settore
techcrunch.com
backlinko.com
theverge.com
electroiq.com
epoch.ai
piktochart.com
seangoedecke.com
manifold.markets
epoch.ai
azure.microsoft.com
sustainability.aboutamazon.com
cloud.google.com
sifted.eu
explodingtopics.com
linkedin.com
mistral.ai
.






Fonti





Hai detto:
come facciamo a fare una stima per tutti i dati che ci mancano, è impossibile


ChatGPT ha detto:
Hai perfettamente ragione: senza dati pubblici affidabili, alcune stime diventano difficilissime, se non impossibili. Tuttavia, possiamo ragionare da data analyst e costruire stime approssimative ma ragionate, usando:

⚙️ 1. Proxy e analogie con modelli noti
Ad esempio:

Se GPT-4o consuma ~0,3 Wh/query, possiamo supporre che Claude 3 Opus (simile per capacità) consumi valori vicini, soprattutto se gira su hardware simile (GPU A100/H100).

Se Gemini Ultra ha ~1 trilione di parametri, può essere paragonato per consumo a GPT-3.5 o GPT-4 base.

🧠 2. Supposizioni su base infrastrutturale
Claude usa AWS, che ha datacenter con ottimizzazione simile ad Azure.

Gemini gira su TPU v5e/v4, le cui performance energetiche sono documentate in studi di Google Cloud. Possiamo usare questi dati per stimare energia/query.

📊 3. Modelli matematici semplificati
Possiamo calcolare, ad esempio:

Stima energia/query = (tempo medio GPU) × (consumo energetico GPU)

Se 1 query richiede 1 secondo su una H100 da 700W → consumo = ~0,2 Wh/query

🌱 4. Conversioni standard
Conversione standard per CO₂:

1 kWh (USA mix energetico) ≈ 0,45 kg di CO₂

1 Wh ≈ 0,45 g CO₂

Conversione standard per acqua:

~1 litro evaporato per 5-10 kWh (stima Google + ricercatori)

quindi 0,3 Wh ≈ 5-6 ml per query

✅ Quindi: cosa possiamo fare
Ti propongo di costruire una seconda tabella che:

Indichi i dati reali dove esistono

Dove mancano, inserisca stime ragionate

Indichi il grado di affidabilità (Alta – Media – Bassa)

Sia pronta per l’esportazione in CSV

⚒️ Vuoi che lo faccia ora?
Posso:

Compilare la tabella con tutte le stime (indicate come tali)

Aggiungere una colonna "Fonte / Metodo"

Prepararla in formato CSV pronto da usare



'''




import numpy as np
import pandas as pd
import matplotlib as plt









df = pd.read_csv('ai_comparison_estimates.csv')

print(df.head())
print(df.info())

# forziamo il df a mostrarci tutte le righe e tabelle



# voglio forzare il DF per vedere tutte le colonne
pd.set_option('display.max_columns', None)  # mostra tutte le colonne

# voglio forzare il DF per vedere tutte le righe
pd.set_option('display.max_rows', None)  # mostra tutte le righe

print(df)




# 1 ripuliamo il CSV e rendiamolo numerico


import numpy as np

# Copia del DataFrame originale per la pulizia
df_clean = df.copy()

# Funzione per estrarre solo il numero dalla stringa (prima parte del campo)
def extract_number(value):
    try:
        return float(str(value).split()[0].replace("~", "").replace(",", "").replace("(", ""))
    except:
        return np.nan

# Applichiamo la funzione alle colonne numeriche
cols_to_clean = [
    "Energia per Query (Wh)",
    "CO2 per Query (g)",
    "Acqua per Query (ml)",
    "Costo per Query (USD)",
    "Utenti Attivi Mensili (MAU)"
]

# Per "Utenti Attivi Mensili", convertiamo milioni in numero intero
def clean_users(value):
    try:
        if "M" in value:
            return float(value.replace("M", "").replace("~", "").replace("(", "").replace(")", "")) * 1_000_000
        elif "B" in value:
            return float(value.replace("B", "").replace("~", "").replace("(", "").replace(")", "")) * 1_000_000_000
        else:
            return float(value)
    except:
        return np.nan

# Pulizia delle colonne
df_clean["Energia per Query (Wh)"] = df_clean["Energia per Query (Wh)"].apply(extract_number)
df_clean["CO2 per Query (g)"] = df_clean["CO2 per Query (g)"].apply(extract_number)
df_clean["Acqua per Query (ml)"] = df_clean["Acqua per Query (ml)"].apply(extract_number)
df_clean["Costo per Query (USD)"] = df_clean["Costo per Query (USD)"].apply(extract_number)
df_clean["Utenti Attivi Mensili (MAU)"] = df_clean["Utenti Attivi Mensili (MAU)"].apply(clean_users)

# Salvataggio della versione pulita
csv_clean_path = "ai_comparison_cleaned.csv"
df_clean.to_csv(csv_clean_path, index=False)

df_clean
