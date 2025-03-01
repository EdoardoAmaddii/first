"""
Sezione 9: Progetto Finale: Arithmetic Arranger (Esercizi 81-90)

81. Costruzione della Funzione per l'Arithmetic Arranger

Scrivi la funzione principale che raccoglie tutte le operazioni aritmetiche e le formatta in una lista.
82. Gestione dell'Input Utente per Inserire Più Operazioni

Scrivi il codice per raccogliere più operazioni aritmetiche dall'utente e visualizzare le equazioni formattate.
83. Creazione di un Sistema che Separa le Operazioni in Due Gruppi

Organizza le operazioni in due gruppi separati, uno per le operazioni completate correttamente e l'altro per quelle non valide o incompletate.


88. Calcolo della Media dei Risultati delle Operazioni

Scrivi una funzione che calcola la media dei risultati delle operazioni eseguite.
89. Funzione per Rimuovere Operazioni Non Corrette

Crea una funzione che rimuove dalle operazioni quelle che non sono valide o che contengono errori.
"""




#  81. Costruzione della Funzione per l'Arithmetic Arranger

#  Scrivi la funzione principale che raccoglie tutte le operazioni aritmetiche e le formatta in una lista.

#  82. Gestione dell'Input Utente per Inserire Più Operazioni

#  Scrivi il codice per raccogliere più operazioni aritmetiche dall'utente e visualizzare le equazioni formattate.


def operazioni (num1,oper,num2):
    listaoperazioni = []

    if oper == '+':
        listaoperazioni.append(f'{num1} + {num2} = {num1+num2}')
        return listaoperazioni
    elif oper == '-':
        listaoperazioni.append(f'{num1} - {num2} = {num1-num2}')
        return listaoperazioni
    elif oper == '*':
        listaoperazioni.append(f'{num1} * {num2} = {num1*num2}')
        return listaoperazioni
    elif oper == '/':
        if num2 == 0:
            return "Errore: divisione per zero"
        else:
            listaoperazioni.append(f'{num1} / {num2} = {num1/num2}')
        return listaoperazioni
    
    else:
        listaoperazioni.append(operazioni)
        return "Operatore non valido. Usa +, -, *, /"
    

listacompleta = []

while True:
    intro = input('inizia premendo enter, o q per uscire')
    if intro == 'q': 
        break

    numero1 = float(input('inserisci un numero:\n'))
    operatore = input('inserisci un operatore:\n')
    numero2 = float(input('inserisci il secondo numero:\n'))

    risultato = operazioni(numero1,operatore,numero2)
    print(risultato)

    for r in risultato:
        listacompleta.append(risultato)
        
print(listacompleta)



    



### questo il codice che dovrebbe essere 



# Definiamo la funzione 'operazioni' che accetta un numero variabile di operazioni come input
def operazioni(*operazioni):
    # Inizializziamo una lista vuota per memorizzare i risultati delle operazioni
    listaoperazioni = []

    # Iteriamo su tutte le operazioni fornite come input
    for operazione in operazioni:
        # Destrutturiamo la tupla 'operazione' nei suoi componenti: num1, oper e num2
        num1, oper, num2 = operazione
        
        # Verifichiamo quale operatore è stato fornito e calcoliamo il risultato di conseguenza
        if oper == '+':
            # Aggiungiamo il risultato dell'operazione alla lista delle operazioni formattata come stringa
            listaoperazioni.append(f'{num1} + {num2} = {num1 + num2}')
        elif oper == '-':
            listaoperazioni.append(f'{num1} - {num2} = {num1 - num2}')
        elif oper == '*':
            listaoperazioni.append(f'{num1} * {num2} = {num1 * num2}')
        elif oper == '/':
            # Gestione della divisione per zero
            if num2 == 0:
                listaoperazioni.append("Errore: divisione per zero")
            else:
                listaoperazioni.append(f'{num1} / {num2} = {num1 / num2}')
        else:
            # Se l'operatore non è valido, aggiungiamo un messaggio di errore alla lista delle operazioni
            listaoperazioni.append("Operatore non valido. Usa +, -, *, /")

    # Restituiamo la lista delle operazioni completate
    return listaoperazioni

# Esempi di utilizzo della funzione 'operazioni'
# Passiamo diverse operazioni alla funzione sotto forma di tuple
risultato = operazioni((1, '+', 5), (43, '*', 3), (10, '/', 0), (20, '-', 4))

# Iteriamo sui risultati e stampiamo ciascuna operazione e il suo risultato
for r in risultato:
    print(r)

    






#  83. Creazione di un Sistema che Separa le Operazioni in Due Gruppi
#  Organizza le operazioni in due gruppi separati, uno per le operazioni completate correttamente e l'altro per quelle non valide o incompletate.

def operazioni(num1, oper, num2):
    listaoperazioni = []
    errore = False

    if oper == '+':
        listaoperazioni.append(f'{num1} + {num2} = {num1 + num2}')
    elif oper == '-':
        listaoperazioni.append(f'{num1} - {num2} = {num1 - num2}')
    elif oper == '*':
        listaoperazioni.append(f'{num1} * {num2} = {num1 * num2}')
    elif oper == '/':
        if num2 == 0:
            listaoperazioni.append("Errore: divisione per zero")
            errore = True
        else:
            listaoperazioni.append(f'{num1} / {num2} = {num1 / num2}')
    else:
        listaoperazioni.append("Operatore non valido. Usa +, -, *, /")
        errore = True
    
    return listaoperazioni, errore

# Liste separate per operazioni valide e non valide

operazioni_valide = []
operazioni_non_valide = []

while True:
    intro = input('Premi Enter per iniziare, o "q" per uscire: ').lower()
    if intro == 'q':
        break

    try:
        numero1 = float(input('Inserisci un numero:\n'))
        operatore = input('Inserisci un operatore (+, -, *, /):\n')
        numero2 = float(input('Inserisci un secondo numero:\n'))

        risultato, errore = operazioni(numero1, operatore, numero2)
        print(risultato)

        if errore:
            for r in risultato:
                operazioni_non_valide.append(r)
        else:
            for r in risultato:
                operazioni_valide.append(r)

    except ValueError:
        print('Errore: Inserisci numeri validi.')
        operazioni_non_valide.append("Errore: Input non valido")

print("Operazioni valide:")
for operazione in operazioni_valide:
    print(operazione)

print("\nOperazioni non valide:")
for operazione in operazioni_non_valide:
    print(operazione)


"""
Spiegazione delle Modifiche
Ritorno della Funzione:

La funzione operazioni ora restituisce una tupla contenente la lista delle operazioni e una variabile errore che indica se c'è stato un errore nell'operazione.

Liste Separate:

Aggiunte due liste separate operazioni_valide e operazioni_non_valide per memorizzare rispettivamente le operazioni valide e non valide.

Verifica degli Errori:

Verifichiamo la variabile errore per determinare se aggiungere l'operazione alla lista delle operazioni valide o non valide.

Gestione degli Errori di Input:

Gli errori di input vengono aggiunti alla lista delle operazioni non valide.

Stampa dei Risultati:

Alla fine, stampiamo separatamente le operazioni valide e non valide.

"""






# 88. Calcolo della Media dei Risultati delle Operazioni

# Scrivi una funzione che calcola la media dei risultati delle operazioni eseguite.


# Funzione che esegue un'operazione aritmetica su due numeri
def operazioni(num1, oper, num2):
    operazione_descrizione = ""  # Stringa per descrivere l'operazione
    risultato = None  # Variabile per memorizzare il risultato dell'operazione

    # Verifica dell'operatore e calcolo del risultato corrispondente
    if oper == '+':
        operazione_descrizione = f'{num1} + {num2} = {num1 + num2}'
        risultato = num1 + num2
    elif oper == '-':
        operazione_descrizione = f'{num1} - {num2} = {num1 - num2}'
        risultato = num1 - num2
    elif oper == '*':
        operazione_descrizione = f'{num1} * {num2} = {num1 * num2}'
        risultato = num1 * num2
    elif oper == '/':
        if num2 == 0:
            # Gestione della divisione per zero
            return "Errore: divisione per zero", None
        else:
            operazione_descrizione = f'{num1} / {num2} = {num1 / num2}'
            risultato = num1 / num2
    else:
        # Operatore non valido
        return "Operatore non valido. Usa +, -, *, /", None

    # Restituisce la descrizione dell'operazione e il risultato
    return operazione_descrizione, risultato

# Liste per memorizzare le operazioni e i risultati numerici
listacompleta = []
risultati_numerici = []

# Ciclo principale per inserire operazioni
while True:
    # Chiede all'utente di premere Enter per iniziare o 'q' per uscire
    intro = input('Premi Enter per iniziare, o "q" per uscire: ').lower()
    if intro == 'q':
        break

    try:
        # Richiede l'inserimento del primo numero
        numero1 = float(input('Inserisci un numero:\n'))
        # Richiede l'inserimento dell'operatore
        operatore = input('Inserisci un operatore (+, -, *, /):\n')
        # Richiede l'inserimento del secondo numero
        numero2 = float(input('Inserisci il secondo numero:\n'))

        # Esegue l'operazione e ottiene la descrizione e il risultato
        descrizione, risultato = operazioni(numero1, operatore, numero2)
        print(descrizione)

        if risultato is not None:
            # Aggiunge la descrizione dell'operazione alla lista completa
            listacompleta.append(descrizione)
            # Aggiunge il risultato numerico alla lista dei risultati numerici
            risultati_numerici.append(risultato)

    except ValueError:
        # Gestione dell'errore di input non valido
        print('Errore: Inserisci numeri validi.')

# Calcolo della media dei risultati numerici
if risultati_numerici:
    media = sum(risultati_numerici) / len(risultati_numerici)
else:
    media = None

# Stampa della lista completa delle operazioni
print("\nLista completa delle operazioni:")
for operazione in listacompleta:
    print(operazione)

# Stampa della media dei risultati delle operazioni
print(f"\nMedia dei risultati delle operazioni: {media}")














# 89. Funzione per Rimuovere Operazioni Non Corrette
# Crea una funzione che rimuove dalle operazioni quelle che non sono valide o che contengono errori.


# Funzione che esegue un'operazione aritmetica su due numeri
def operazioni(num1, oper, num2):
    operazione_descrizione = ""  # Stringa per descrivere l'operazione
    risultato = None  # Variabile per memorizzare il risultato dell'operazione

    # Verifica dell'operatore e calcolo del risultato corrispondente
    if oper == '+':
        operazione_descrizione = f'{num1} + {num2} = {num1 + num2}'
        risultato = num1 + num2
    elif oper == '-':
        operazione_descrizione = f'{num1} - {num2} = {num1 - num2}'
        risultato = num1 - num2
    elif oper == '*':
        operazione_descrizione = f'{num1} * {num2} = {num1 * num2}'
        risultato = num1 * num2
    elif oper == '/':
        if num2 == 0:
            # Gestione della divisione per zero
            return "Errore: divisione per zero", None
        else:
            operazione_descrizione = f'{num1} / {num2} = {num1 / num2}'
            risultato = num1 / num2
    else:
        # Operatore non valido
        return "Operatore non valido. Usa +, -, *, /", None

    # Restituisce la descrizione dell'operazione e il risultato
    return operazione_descrizione, risultato

# Funzione per rimuovere le operazioni non valide o che contengono errori
def rimuovi_operazioni_non_valide(lista_operazioni):
    operazioni_valide = []  # Lista per memorizzare le operazioni valide

    # Itera su tutte le operazioni nella lista
    for descrizione, risultato in lista_operazioni:
        # Aggiungi l'operazione alla lista delle operazioni valide solo se il risultato non è None
        if risultato is not None:
            operazioni_valide.append((descrizione, risultato))

    return operazioni_valide

# Liste per memorizzare le operazioni e i risultati numerici
listacompleta = []

# Ciclo principale per inserire operazioni
while True:
    # Chiede all'utente di premere Enter per iniziare o 'q' per uscire
    intro = input('Premi Enter per iniziare, o "q" per uscire: ').lower()
    if intro == 'q':
        break

    try:
        # Richiede l'inserimento del primo numero
        numero1 = float(input('Inserisci un numero:\n'))
        # Richiede l'inserimento dell'operatore
        operatore = input('Inserisci un operatore (+, -, *, /):\n')
        # Richiede l'inserimento del secondo numero
        numero2 = float(input('Inserisci il secondo numero:\n'))

        # Esegue l'operazione e ottiene la descrizione e il risultato
        descrizione, risultato = operazioni(numero1, operatore, numero2)
        print(descrizione)

        # Aggiunge l'operazione e il risultato alla lista completa
        listacompleta.append((descrizione, risultato))

    except ValueError:
        # Gestione dell'errore di input non valido
        print('Errore: Inserisci numeri validi.')
        listacompleta.append(("Errore: Input non valido", None))

# Rimuove le operazioni non valide
listacompleta_valide = rimuovi_operazioni_non_valide(listacompleta)

# Stampa della lista completa delle operazioni valide
print("\nLista completa delle operazioni valide:")
for descrizione, risultato in listacompleta_valide:
    print(descrizione)









