#es.1 
# Crea un Dizionario
#Crea un dizionario con almeno tre coppie chiave-valore.

mary = 1
luca = 'ciao'
gio = 3

dizio = dict()               # puoi inserrire qualsiasi tipo di item, 
                                #lui lo salverà come una coppia chiave-valore
dizio [gio] = 1              #questo è il metodo di add al dizionario
dizio [luca] = 2
dizio [mary] = 3

print(dizio)                 #l'ordine di print degli elementi del dizionario è imprevedibile


##es.1
# Inizializza il dizionario direttamente, senza aggiungere elementi uno per uno:

dizio = {3: 1, 'ciao': 2, 1: 3}
print(dizio)



# es .2 
# Accedi agli Elementi di un Dizionario
#Accedi al valore associato a una chiave di un dizionario.

print(dizio[gio]) #così lo printi, ma se la chiave non esiste genererà errore

                  #così vedi se i valori sono presenti .values()
                  #così vedi se le chiavi sono presenti .keys()  ''''potresti averle salvate in un altro modo

valori = list(dizio.keys())
if 'ciao' in valori:
    print('yess')
else:
    print('nope')


###
## es.2
if 'ciao' in dizio:  # Non serve list(). if key in dizio.keys() è anche valido
    print('yess')
else:
    print('nope')

###
## suggerimento: es.2 plus:
# Usa un controllo con get() per evitare errori se la chiave non è presente




#es. 3 
# Aggiungi una Coppia Chiave-Valore
#Aggiungi una nuova coppia chiave-valore al dizionario.

jonny = dizio['edd'] = 9   
print(dizio)

#Suggerimento:
#Aggiungi semplicemente la chiave-valore senza assegnare il risultato a una variabile:

dizio['edd'] = 9
print(dizio)








#es. 4
# Rimuovi una Coppia Chiave-Valore
#Rimuovi una coppia chiave-valore dal dizionario usando del.

if 1 in dizio:
    del dizio['edd'] 

print(dizio)

# versione con list comprhension
chiavi_da_rimuovere = [k for k, v in dizio.items() if v == 1]  # Trova chiavi con valore 1
for k in chiavi_da_rimuovere:
    del dizio[k]
print(dizio)


#es.4 plus
# 
#creare un nuovo dizionario, contenente tutte le parole meno quella che ho rimosso

#
chiave_da_rimuovere = 'ciao'
# Creazione del nuovo dizionario senza la chiave da rimuovere
nuovodizio = {}

if chiave_da_rimuovere in dizio:
    for chiave, valore in dizio.items():
        if chiave != chiave_da_rimuovere:  # Esclude la chiave da rimuovere
            nuovodizio[chiave] = valore
    print("Nuovo dizionario senza 'ciao':", nuovodizio)
else:
    print(f"La chiave '{chiave_da_rimuovere}' non è presente nel dizionario.")

# Stampa del dizionario originale (immutato)
print("Dizionario originale:", dizio)





#con list comprehension

# Dizionario originale
dizio = {3: 1, 'ciao': 2, 1: 3, 'edd': 9}

# Chiave da rimuovere
chiave_da_rimuovere = 3

# Creazione di un nuovo dizionario senza la chiave da rimuovere
nuovo_dizio = {k: v for k, v in dizio.items() if k != chiave_da_rimuovere}

print("Dizionario originale:", dizio)
print("Nuovo dizionario:", nuovo_dizio)

#Spiegazione
#Comprensione del Dizionario ({k: v for k, v in dizio.items() if k != chiave_da_rimuovere}):

#dizio.items() restituisce tutte le coppie chiave-valore del dizionario.
#Il costrutto {k: v for k, v in ...} crea un nuovo dizionario.
#La condizione if k != chiave_da_rimuovere esclude la chiave specificata.
#Inalterabilità del Dizionario Originale:

#Questo metodo non modifica il dizionario originale (dizio), ma ne crea uno nuovo con gli elementi desiderati.



#es. 5
# Verifica la Presenza di una Chiave
#Verifica se una chiave esiste in un dizionario usando in.


if 1 in dizio:
    print('yeppa')

else: 
    print('non è presente la chiave 1' )

#Suggerimento aggiuntivo: Puoi estendere il codice per verificare non solo se esiste, ma anche qual è il valore associato, se necessario.
#Esempio esteso:


if 1 in dizio:
    print(f'La chiave 1 è presente e ha il valore: {dizio[1]}')
else:
    print('La chiave 1 non è presente nel dizionario.')



#es. 6
# Modifica il Valore di una Chiave
#Modifica il valore associato a una chiave nel dizionario.

if 1 in dizio:
    dizio[1] = 'primo'
print(dizio)

# N.B.!
# in python non è permesso cambiare direttamente il nome di una key in un vocabolario

#puoi simulare il cambio di una chiave:
# 
# .pop('ciao'):         Rimuove la chiave 'ciao' dal dizionario e restituisce il suo valore.
# dizio['saluto'] =:   Aggiunge una nuova chiave 'saluto' con lo stesso valore della chiave rimossa.

# Cambia il nome della chiave 'ciao' in 'saluto'
if 'ciao' in dizio:
    dizio['saluto'] = dizio.pop('ciao')  # Sposta il valore dalla vecchia chiave alla nuova

print(dizio)





#es.6 plus
# Se vuoi farlo in modo dinamico (cambiare qualsiasi chiave in un'altra)
#  puoi creare una funzione:


def cambia_chiave(dizionario, chiave_vecchia, chiave_nuova):
    if chiave_vecchia in dizionario:
        dizionario[chiave_nuova] = dizionario.pop(chiave_vecchia)
    else:
        print(f"La chiave '{chiave_vecchia}' non esiste nel dizionario.")

# Esempio di utilizzo
dizio = {3: 1, 'ciao': 2, 1: 'primo', 'edd': 9}
cambia_chiave(dizio, 'ciao', 'saluto')
print(dizio)








#es.7 
# Itera su un Dizionario
#Itera su un dizionario e stampa le chiavi e i valori.

for keys, values in dizio.items():
    print(keys, values)

# Creiamo un dizionario di esempio
dizionario = {
    'nome': 'Mario',
    'età': 25,
    'città': 'Roma'
}

# Metodo 1: iterare su chiavi e valori insieme usando .items()
for chiave, valore in dizio.items():
    print(f'Chiave: {chiave}, Valore: {valore}')

# Metodo 2: iterare solo sulle chiavi
for chiave in dizio:  # oppure dizionario.keys()
    print(f'Chiave: {chiave}, Valore: {dizio[chiave]}')

# Metodo 3: iterare solo sui valori
for valore in dizio.values():
    print(f'Valore: {valore}')






def itera_dizionario(diz):
    for chiave, valore in diz.items():
        print(f'Chiave: {chiave}, Valore: {valore}')

# Test della funzione
studente = {
    'nome': 'Laura',
    'materia': 'Matematica',
    'voto': 28
}

itera_dizionario(studente)





#########

# questo nel giro di un mese

#########

def esplora_dizionario(dizionario, livello=0):
    # Il parametro livello ci aiuta a gestire l'indentazione per una visualizzazione chiara
    spazio = "  " * livello  # Creiamo l'indentazione basata sul livello di profondità
    
    for chiave, valore in dizionario.items():
        # Verifichiamo se il valore è un altro dizionario
        if isinstance(valore, dict):
            print(f"{spazio}► {chiave}:")
            # Chiamata ricorsiva per esplorare il dizionario annidato
            esplora_dizionario(valore, livello + 1)
        # Verifichiamo se il valore è una lista
        elif isinstance(valore, list):
            print(f"{spazio}► {chiave}:")
            # Iteriamo sulla lista con indentazione
            for elemento in valore:
                if isinstance(elemento, dict):
                    # Se l'elemento della lista è un dizionario, esploriamolo
                    esplora_dizionario(elemento, livello + 1)
                else:
                    print(f"{spazio}  - {elemento}")
        else:
            # Caso base: stampa chiave e valore semplice
            print(f"{spazio}• {chiave}: {valore}")

# Creiamo un dizionario complesso di esempio
scuola = {
    "nome": "Liceo Einstein",
    "indirizzo": {
        "via": "Via Roma 123",
        "città": "Milano",
        "cap": "20100"
    },
    "classi": [
        {
            "nome": "3A",
            "studenti": 25,
            "materie": ["Matematica", "Italiano", "Storia"]
        },
        {
            "nome": "4B",
            "studenti": 22,
            "materie": ["Fisica", "Latino", "Inglese"]
        }
    ],
    "personale": {
        "docenti": 30,
        "amministrativi": 5,
        "collaboratori": 8
    }
}

# Testiamo la funzione
print("Struttura della scuola:")
esplora_dizionario(scuola)


#Analizziamo come funziona questo codice:

#La Funzione Principale:

#esplora_dizionario accetta due parametri: il dizionario da esplorare e il livello di profondità attuale
#Il parametro livello viene usato per creare l'indentazione visiva che mostra la struttura gerarchica


#Gestione dei Tipi di Dati:

#Il codice gestisce tre casi principali:

#Dizionari annidati (usando ricorsione)
#Liste (che potrebbero contenere dizionari o valori semplici)
#Valori semplici (stringhe, numeri, ecc.)




#Visualizzazione Strutturata:

#Usiamo simboli diversi per una migliore leggibilità:

#► per indicare sottosezioni (dizionari o liste)
#• per valori semplici
#- per elementi di liste
















''''Ti aiuterò a comprendere meglio il codice spiegandolo passo per passo, usando analogie e esempi pratici.
Immagina il dizionario come una grande biblioteca. La nostra funzione esplora_dizionario è come un bibliotecario che esplora sistematicamente ogni sezione, scaffale e libro.
pythonCopydef esplora_dizionario(dizionario, livello=0):
    # Come il bibliotecario che tiene traccia di quanto è sceso nei sottolivelli
    spazio = "  " * livello
Il parametro livello è come il piano della biblioteca in cui ci troviamo. Più scendiamo in profondità (nei dizionari annidati), più spazi aggiungiamo per mostrare questa "profondità".
pythonCopy    for chiave, valore in dizionario.items():
        # Il bibliotecario controlla ogni elemento (chiave-valore)
        if isinstance(valore, dict):
            # Ha trovato una nuova stanza (un altro dizionario)
            print(f"{spazio}► {chiave}:")
            esplora_dizionario(valore, livello + 1)  # Entra nella stanza
Quando troviamo un dizionario dentro il dizionario (come indirizzo nel nostro esempio della scuola), è come trovare una nuova stanza da esplorare. La funzione si chiama ricorsivamente, come se il bibliotecario aprisse la porta e entrasse in questa nuova stanza.
pythonCopy        elif isinstance(valore, list):
            # Ha trovato uno scaffale con più libri (una lista)
            print(f"{spazio}► {chiave}:")
            for elemento in valore:
                if isinstance(elemento, dict):
                    # Ogni libro è un piccolo dizionario
                    esplora_dizionario(elemento, livello + 1)
                else:
                    # Ogni libro è un semplice valore
                    print(f"{spazio}  - {elemento}")
Le liste sono come scaffali con più elementi. Ogni elemento potrebbe essere un semplice libro (un valore) o un'altra collezione (un dizionario).
Vediamo un esempio pratico più semplice:
pythonCopy# Un dizionario più semplice per iniziare
studente = {
    "nome": "Marco",
    "dettagli": {                    # Un dizionario annidato
        "età": 16,
        "classe": "4B"
    },
    "materie": ["Italiano", "Matematica"]  # Una lista
}

esplora_dizionario(studente)
Questo produrrà:
Copy- nome: Marco
► dettagli:
  • età: 16
  • classe: 4B
► materie:
  - Italiano
  - Matematica
La funzione segue questo processo mentale:

Trova "nome" → è un valore semplice → lo stampa
Trova "dettagli" → è un dizionario → entra dentro e aumenta l'indentazione
Trova "materie" → è una lista → stampa ogni elemento con un trattino

Gli elementi speciali di formattazione aiutano a capire la struttura:

► indica che stiamo "entrando" in qualcosa (un dizionario o una lista)
• indica un elemento semplice chiave-valore
- indica un elemento di una lista'''''