


# Completa l'Arithmetic Arranger - Integra tutti gli esercizi precedenti per creare una calcolatrice completa che gestisce operazioni, errori e visualizza i risultati in modo formattato.



'''61. Funzione per Ordinare Numeri in una Lista

Scrivi una funzione che prende una lista di numeri e la ordina in ordine crescente.
62. Funzione per Calcolare la Media di una Lista di Numeri

Scrivi una funzione che calcola la media di una lista di numeri.
63. Funzione per Verificare Se un Numero è Primo

Crea una funzione che verifica se un numero è primo (uso di iterazione e condizioni booleane).
64. Creazione di una Lista con Numeri Pari da 1 a 100

Crea una lista contenente tutti i numeri pari tra 1 e 100, utilizzando un ciclo for.
65. Funzione per Sommare Numeri in una Lista di Numeri Positivi

Scrivi una funzione che somma solo i numeri positivi di una lista (usa un ciclo for).
66. Funzione che Stampa Operazioni Aritmetiche in Formato "Equazione"

Scrivi una funzione che prende due numeri e stampa l'operazione di somma, sottrazione, moltiplicazione e divisione in formato "numero1 operazione numero2 = risultato".
67. Creazione di una Lista con il Risultato delle Operazioni tra Due Numeri

Scrivi un programma che crea una lista contenente il risultato delle operazioni aritmetiche su due numeri (somma, sottrazione, moltiplicazione, divisione).
68. Creazione di un Dizionario con Operazioni Matematiche

Crea un dizionario in cui le chiavi sono le operazioni matematiche (somma, sottrazione, etc.) e i valori sono i risultati delle operazioni tra due numeri.
69. Funzione che Restituisce un Stringa con l'Equazione Formattata

Scrivi una funzione che prende due numeri e restituisce una stringa formattata in modo simile a una "equazione" (es. "5 + 3 = 8").
70. Funzione per Formattare i Risultati delle Operazioni in una Lista

Crea una funzione che prende una lista di numeri e restituisce una lista di stringhe formattate come equazioni. Per esempio, [5, 3, 2] restituisce ["5 + 3 = 8", "3 - 2 = 1", "2 * 5 = 10"].
'''





# 61. Funzione per Ordinare Numeri in una Lista

# Scrivi una funzione che prende una lista di numeri e la ordina in ordine crescente.

def ordinanumeri(numeri):
    # Ordina la lista in ordine crescente
    numeri.sort(reverse = True)  # sort() modifica direttamente la lista senza restituire nulla... Reverse modifica la lista in ordine decrescente, puoi usare anche uno slice [:]
    return numeri

listanumeri = [2, 54, 3, 89, 1]

# Chiamata della funzione per ordinare la lista
risultato = ordinanumeri(listanumeri)

print(risultato)  # Mostra la lista ordinata






# 62. 
# Funzione per Calcolare la Media di una Lista di Numeri
# Scrivi una funzione che calcola la media di una lista di numeri.



def calcolamedia(numeri):
    media = sum(numeri)/len(numeri)
    return media

listanumeri = [2, 54, 3, 89, 1]

# Chiamata della funzione per calcolare la media
risultato = calcolamedia(listanumeri)

print(risultato)  # Mostra la media








#63. Funzione per Verificare Se un Numero è Primo
#Crea una funzione che verifica se un numero è primo (uso di iterazione e condizioni booleane).


import math

def è_primo(n):
    if n <= 1:
        return False  # I numeri minori o uguali a 1 non sono primi
    for i in range(2, int(math.sqrt(n)) + 1):  # Controlla fino alla radice quadrata di n
        if n % i == 0:  # Se n è divisibile per i, non è primo
            return False
    return True  # Se non è divisibile da nessun numero, è primo

# Esempio di test
numero = 29
if è_primo(numero):
    print(f"{numero} è un numero primo")
else:
    print(f"{numero} non è un numero primo")





#64. 
# 
# Creazione di una Lista con Numeri Pari da 1 a 100
# Crea una lista contenente tutti i numeri pari tra 1 e 100, utilizzando un ciclo for.


lista = range(0,101)
for x in lista:
    if x % 2 == 0:
        numeropari = x
        print(numeropari)


# 64.
# così con list comprehension

numeri_pari = [x for x in range(0, 101) if x % 2 == 0]
print(numeri_pari)



# 64 plus
# 
# così mettiamo i numeri in una lista e non li stampiano in loop
elenco= list()
lista = range(0,101)
for x in lista:
    if x % 2 == 0:
        numeropari = x    # questo appesantisce il codice, ma lo sapevo, sono stato io a farlo così a posta
        elenco.append(numeropari)
        
print(elenco)


# 64 plus
# così con list comprehension

elenco = [x for x in range(0, 101) if x % 2 == 0]
print(elenco)






# 65. Funzione per Sommare Numeri in una Lista di Numeri Positivi
# Scrivi una funzione che somma solo i numeri positivi di una lista (usa un ciclo for). 
#

elencopositivi = list()
numeri = range(-23,23)
for x in numeri:
    if x > 0:
        elencopositivi.append(x)

print(elencopositivi)



# 65.
# con list comprehension

numeri = range(-23, 23)
somma_positivi = sum([x for x in numeri if x > 0])
print(somma_positivi)




# 65 plus
# funzione per trovare numeri positivi


def positivi(numeri):
    elencoposit = []
    for x in numeri:   
        if x > 0:
            elencoposit.append(x)
        
    return elencoposit

numbers = [1,45,-23,67,-47]
risultato = positivi(numbers)

print(risultato)




## 65.plus con list compehension   -> abbiamo bisgono di una nuova lista, gli facciamo fare ciò che vogliamo senza esplicitare il ciclo manualmente

numeri = [1, 45, -23, 67, -47]
positiv = [x for x in numeri if x > 0]
print(f"Lista dei numeri positivi: {positiv}")









#65 plus plus 
# 
# funzione che somma i numeri positivi di una lista

def somma_positivi(numeri):
    """
    Restituisce la somma dei numeri positivi in una lista.
    """
    somma = 0
    for x in numeri:
        if x > 0:
            somma += x
    return somma

# Test della funzione
numbers = [1, 45, -23, 67, -47]
risultato = somma_positivi(numbers)
print(f"La somma dei numeri positivi è: {risultato}")




# 65. plus plus 
# con list comprehension

def somma_positivi(numeri):
    """
    Restituisce la somma dei numeri positivi in una lista utilizzando una list comprehension.
    """
    return sum([x for x in numeri if x > 0])

# Test della funzione
numbers = [1, 45, -23, 67, -47]
risultato = somma_positivi(numbers)
print(f"La somma dei numeri positivi è: {risultato}")








# 66. Funzione che Stampa Operazioni Aritmetiche in Formato "Equazione"
# Scrivi una funzione che prende due numeri e stampa l'operazione di somma, sottrazione, moltiplicazione e divisione in formato "numero1 operazione numero2 = risultato".

def operatore(a,b):
    try:
        return a+b, a-b,a*b,a/b
    except ValueError:
        print('inserire solo numeri')
    except ZeroDivisionError:
        print('non si può dividere un numero per 0')

quattro_operazioni = operatore(35,2)
print(f'Quattro_operazioni: {quattro_operazioni}')





### esercizio 66.
def stampa_operazioni(num1, num2):
    """
    Stampa le operazioni di somma, sottrazione, moltiplicazione e divisione
    in formato 'numero1 operazione numero2 = risultato'.
    """
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print(f"{num1} / {num2} = Errore: Divisione per zero non consentita.")

# Esempio di utilizzo
stampa_operazioni(10, 5)
stampa_operazioni(8, 0)








# 67. Creazione di una Lista con il Risultato delle Operazioni tra Due Numeri
# Scrivi un programma che crea una lista contenente il risultato delle operazioni aritmetiche su due numeri (somma, sottrazione, moltiplicazione, divisione)


listarisultati = []

a = 5+4
b = 43-21
listarisultati.append(a)
listarisultati.append(b)

print(listarisultati)






# l'idea è questa:
listarisultati = []

# Numeri di input
num1 = 10
num2 = 5

# Operazioni
listarisultati.append(num1 + num2)  # Somma
listarisultati.append(num1 - num2)  # Sottrazione
listarisultati.append(num1 * num2)  # Moltiplicazione

if num2 != 0:
    listarisultati.append(num1 / num2)  # Divisione

print("Risultati:", listarisultati)


























# 67 plus
# scrivilo sotto forma di funzione

def appendrisultati(num1, num2):
    """
    Calcola le operazioni aritmetiche tra due numeri e restituisce una lista.
    """
    lista = []
    lista.append(num1 + num2)  # Somma
    lista.append(num1 - num2)  # Sottrazione
    lista.append(num1 * num2)  # Moltiplicazione

    if num2 != 0:
        lista.append(num1 / num2)  # Divisione
    else:
        lista.append("Errore: Divisione per zero")
    
    return lista

# Esempio di utilizzo
result = appendrisultati(10, 5)
print("Risultati delle operazioni:", result)

        

    







# 68. Creazione di un Dizionario con Operazioni Matematiche

# Crea un dizionario in cui le chiavi sono le operazioni matematiche (somma, sottrazione, etc.) e i valori sono i risultati delle operazioni tra due numeri.



# l'idea è questa:
dizio_operazioni_risultati = {}

# Numeri di input
num1 = 10
num2 = 5

# Operazioni
dizio_operazioni_risultati[f'{num1} + {num2}'] = num1 + num2 # Somma
dizio_operazioni_risultati[f'{num1} - {num2}'] = num1 - num2  # Sottrazione
dizio_operazioni_risultati[f'{num1} * {num2}'] = num1 * num2  # Moltiplicazione

if num2 != 0:
    dizio_operazioni_risultati[f'{num1} / {num2}'] = num1 / num2  # Divisione

print("Dizio_operazioni_risultati:", dizio_operazioni_risultati)








# una versione migliorata del codice:

def crea_dizionario_operazioni(num1, num2):
    # Dizionario vuoto per le operazioni
    dizio_operazioni_risultati = {}

    # Operazioni
    dizio_operazioni_risultati[f"{num1} + {num2}"] = num1 + num2
    dizio_operazioni_risultati[f"{num1} - {num2}"] = num1 - num2
    dizio_operazioni_risultati[f"{num1} * {num2}"] = num1 * num2

    # Divisione con controllo del divisore
    if num2 != 0:
        dizio_operazioni_risultati[f"{num1} / {num2}"] = num1 / num2
    else:
        dizio_operazioni_risultati[f"{num1} / {num2}"] = "Errore: Divisione per zero"

    return dizio_operazioni_risultati

# Numeri di input
num1 = 10
num2 = 5

# Chiamata alla funzione
risultati = crea_dizionario_operazioni(num1, num2)

# Stampa del dizionario
print("Dizionario delle operazioni:")
for operazione, risultato in risultati.items():
    print(f"{operazione} = {risultato}")
















#versione migliorata con list comprehension


def crea_dizionario_operazioni(num1, num2):
    """
    Crea un dizionario con operazioni matematiche tra due numeri.
    """
    operazioni = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
    }

    # Gestione della divisione per zero
    if num2 != 0:
        operazioni["/"] = num1 / num2
    else:
        operazioni["/"] = "Errore: Divisione per zero"

    # Creazione del dizionario con chiavi come "num1 operazione num2"
    dizio_operazioni_risultati = {f"{num1} {op} {num2}": risultato 
                                  for op, risultato in operazioni.items()}
    return dizio_operazioni_risultati

# Esempio di utilizzo
num1 = 10
num2 = 5
risultati = crea_dizionario_operazioni(num1, num2)

# Stampa formattata del dizionario
for operazione, risultato in risultati.items():
    print(f"{operazione} = {risultato}")



















# 69. Funzione che Restituisce un Stringa con l'Equazione Formattata

# Scrivi una funzione che prende due numeri e restituisce una stringa formattata in modo simile a una "equazione" (es. "5 + 3 = 8").



def stringaoperazioni(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print(f"{num1} / {num2} = Errore: Divisione per zero non consentita.")

# Esempio di utilizzo   / abbiamo saltato l'invoked della funzione su una variabile per velocizzare, nel caso avessimo necessità della stringa delle operazioni dobbiamo assegnare la funzione ad una variabile
### ma attento nella funzione noi non abbiamo dato un return, quindi se printiamo il valore ritorna NONE!
stringaoperazioni(10, 5)
stringaoperazioni(8, 0)











### primo miglioramento

def stringaoperazioni(num1, num2):
    # Creiamo una lista per raccogliere le operazioni
    equazioni = []
    
    # Aggiungiamo le operazioni formattate come stringhe
    equazioni.append(f"{num1} + {num2} = {num1 + num2}")
    equazioni.append(f"{num1} - {num2} = {num1 - num2}")
    equazioni.append(f"{num1} * {num2} = {num1 * num2}")
    
    if num2 != 0:
        equazioni.append(f"{num1} / {num2} = {num1 / num2}")
    else:
        equazioni.append(f"{num1} / {num2} = Errore: Divisione per zero non consentita.")
    
    # Combiniamo tutte le stringhe in una sola stringa, separata da \n
    return "\n".join(equazioni)

# Esempio di utilizzo
risultato = stringaoperazioni(10, 5)
risultato2 = stringaoperazioni(8, 0)

# Stampa dei risultati
print("Risultato 1:")
print(risultato)  # Output come stringa unica
print("\nRisultato 2:")
print(risultato2)

















## miglioramento con AI


def stringaoperazioni(num1, num2):
    # Lista per memorizzare le equazioni
    equazioni = []
    
    # Aggiungi le operazioni alla lista
    equazioni.append(f"{num1} + {num2} = {num1 + num2}")
    equazioni.append(f"{num1} - {num2} = {num1 - num2}")
    equazioni.append(f"{num1} * {num2} = {num1 * num2}")
    
    if num2 != 0:
        equazioni.append(f"{num1} / {num2} = {num1 / num2}")
    else:
        equazioni.append(f"{num1} / {num2} = Errore: Divisione per zero non consentita.")
    
    return equazioni

# Esempio di utilizzo
risultati1 = stringaoperazioni(10, 5)
risultati2 = stringaoperazioni(8, 0)

# Stampa dei risultati
print("\n".join(risultati1), type(risultati1))
print("\n".join(risultati2))










    











# 70. Funzione per Formattare i Risultati delle Operazioni in una Lista

# Crea una funzione che prende una lista di numeri e restituisce una lista di stringhe formattate come equazioni. Per esempio, [5, 3, 2] restituisce ["5 + 3 = 8", "3 - 2 = 1", "2 * 5 = 10"].

def operazioniinlista(listanumeri):
    """
    Prende una lista di numeri e restituisce una lista di stringhe formattate come equazioni
    eseguendo operazioni consecutive.
    """
    # Lista che conterrà le stringhe formattate
    stringheinlista = []
    
    # Ciclo sugli indici della lista, considerando coppie consecutive
    for i in range(len(listanumeri) - 1):
        num1 = listanumeri[i]
        num2 = listanumeri[i + 1]
        
        # Somma
        stringheinlista.append(f"{num1} + {num2} = {num1 + num2}")
        # Sottrazione
        stringheinlista.append(f"{num1} - {num2} = {num1 - num2}")
        # Moltiplicazione
        stringheinlista.append(f"{num1} * {num2} = {num1 * num2}")
        # Divisione (se il divisore non è zero)
        if num2 != 0:
            stringheinlista.append(f"{num1} / {num2} = {num1 / num2}")
        else:
            stringheinlista.append(f"{num1} / {num2} = Errore: Divisione per zero non consentita.")

    return stringheinlista

# Esempio di utilizzo
numeri = [2, 4, 6]
risultati = operazioniinlista(numeri)
print("\n".join(risultati))



    




"""
# Ciclo sugli indici della lista, considerando coppie consecutive
    for i in range(len(listanumeri) - 1):
        num1 = listanumeri[i]
        num2 = listanumeri[i + 1]
    



Questo blocco di codice è progettato per iterare su una lista di numeri e considerare coppie consecutive di numeri per eseguire operazioni tra di loro.

Come funziona
1. for i in range(len(listanumeri) - 1):
La funzione range(len(listanumeri) - 1) genera indici da 0 fino a len(listanumeri) - 2.
Questo accade perché vogliamo accedere sia all'elemento corrente che al successivo (listanumeri[i + 1]).
Se non sottraessimo 1, potremmo cercare di accedere a un indice che supera la lunghezza della lista, generando un errore di IndexError.
2. num1 = listanumeri[i]
listanumeri[i] è il numero corrente della lista.
Ad esempio, se la lista è [2, 4, 6]:
Quando i = 0, num1 = 2.
Quando i = 1, num1 = 4.
3. num2 = listanumeri[i + 1]
listanumeri[i + 1] è il numero immediatamente successivo al corrente.
Continuando con la lista [2, 4, 6]:
Quando i = 0, num2 = 4.
Quando i = 1, num2 = 6.
Cosa Succede nel Ciclo
Ogni iterazione considera una coppia consecutiva di numeri:

Alla prima iterazione (i = 0):

num1 = listanumeri[0] = 2
num2 = listanumeri[1] = 4
Alla seconda iterazione (i = 1):

num1 = listanumeri[1] = 4
num2 = listanumeri[2] = 6
Questo processo si interrompe prima dell'ultimo indice (i = len(listanumeri) - 1) perché non esiste un elemento successivo dopo l'ultimo.
Perché "Coppie Consecutive"
Considerare coppie consecutive è utile per eseguire operazioni solo tra due numeri adiacenti nella lista, invece di fare tutte le possibili combinazioni (che richiederebbero un ciclo annidato).
Esempio Passo-Passo
Supponiamo che la lista sia:

python
Copia codice
listanumeri = [2, 4, 6]
Iterazioni del ciclo:
Prima Iterazione (i = 0):

num1 = listanumeri[0] = 2
num2 = listanumeri[1] = 4
Operazioni eseguite: somma, sottrazione, ecc. tra 2 e 4.
Seconda Iterazione (i = 1):

num1 = listanumeri[1] = 4
num2 = listanumeri[2] = 6
Operazioni eseguite: somma, sottrazione, ecc. tra 4 e 6.
Fine del ciclo:

Non ci sono più numeri successivi, quindi il ciclo termina.
Vantaggi
Iterando con coppie consecutive, il codice rimane semplice ed evita combinazioni inutili o complesse.
Può essere utile per operazioni "in sequenza", ad esempio quando vogliamo calcolare differenze tra misurazioni consecutive, risultati intermedi, 
ecc.
"""





# es. 70
# calcola ogni numero a coppia 1,2 1,3 2,3, somma prodotto: per le altre operazioni, non essendo commutative, abbiamo bisogno di specificare meglio




# Lista di numeri da analizzare
numeri = [5, 8, 12, 3]

# Ciclo esterno per il primo numero
for i in range(len(numeri)):
    # Ciclo interno per il secondo numero
    # Parte da i+1 per evitare duplicati e confronti con se stesso
    for j in range(i + 1, len(numeri)):
        num1 = numeri[i]
        num2 = numeri[j]
        
        # Qui puoi fare le operazioni che vuoi con num1 e num2
        # Per esempio, stampare le coppie:
        print(f"Coppia: {num1} e {num2}")
        
        # Esempio di alcune operazioni:
        somma = num1 + num2
        prodotto = num1 * num2
        print(f"  Somma: {somma}")
        print(f"  Prodotto: {prodotto}")
        print("-----")





####
## es.70 plus plus
##
# aumenta la portata del codice precedente inserendo le ultime operazioni


# Lista di numeri da analizzare
numeri = [5, 8, 12]

# Ciclo esterno per il primo numero
for i in range(len(numeri)):
    # Ciclo interno per il secondo numero
    for j in range(i + 1, len(numeri)):
        num1 = numeri[i]
        num2 = numeri[j]
        
        # Calcolo di tutte le operazioni base
        somma = num1 + num2
        sottrazione = num1 - num2
        prodotto = num1 * num2
        
        # Per la divisione controlliamo che il divisore non sia zero
        if num2 != 0:
            divisione = num1 / num2
            # Formattiamo il risultato della divisione a 2 decimali
            divisione_formattata = round(divisione, 2)
        else:
            divisione_formattata = "Non possibile (divisione per zero)"
        
        # Stampa dei risultati
        print(f"Coppia: {num1} e {num2}")
        print(f"  Somma: {somma}")
        print(f"  Sottrazione: {sottrazione}")
        print(f"  Prodotto: {prodotto}")
        print(f"  Divisione: {divisione_formattata}")
        print("-----")





















### Ecco come modificare il codice per considerare anche le coppie al contrario (ad esempio, non solo 5,8 ma anche 8,5):
"""
Le principali modifiche sono:

Il ciclo interno ora parte da 0 invece che da i+1
Aggiungiamo un controllo if i != j per evitare di confrontare un numero con se stesso
Ora vediamo entrambe le direzioni (es. 5,8 e 8,5) - nota come la sottrazione e la divisione danno risultati diversi nelle due direzioni
"""
# Lista di numeri da analizzare
numeri = [5, 8, 12, 3]

# Ciclo esterno per il primo numero
for i in range(len(numeri)):
    # Ciclo interno per il secondo numero
    # Ora parte da 0 e include tutti i numeri tranne se stesso
    for j in range(len(numeri)):
        # Saltiamo quando i e j sono uguali (stesso numero)
        if i != j:
            num1 = numeri[i]
            num2 = numeri[j]
            
            # Calcolo di tutte le operazioni base
            somma = num1 + num2
            sottrazione = num1 - num2
            prodotto = num1 * num2
            
            # Per la divisione controlliamo che il divisore non sia zero
            if num2 != 0:
                divisione = num1 / num2
                divisione_formattata = round(divisione, 2)
            else:
                divisione_formattata = "Non possibile (divisione per zero)"
            
            # Stampa dei risultati
            print(f"Coppia: {num1} e {num2}")
            print(f"  Somma: {somma}")
            print(f"  Sottrazione: {sottrazione}")
            print(f"  Prodotto: {prodotto}")
            print(f"  Divisione: {divisione_formattata}")
            print("-----")













"""
organizzare questi risultati in una struttura dati più ordinata, come un dizionario o una lista di tuple
"""



# Lista di numeri da analizzare
numeri = [5, 8, 12, 3]

# Creiamo un dizionario per salvare i risultati
# La chiave sarà una tupla con la coppia di numeri
risultati_dict = {}

# Creiamo una lista di tuple per i risultati
risultati_lista = []

# Ciclo per generare tutte le coppie e i calcoli
for i in range(len(numeri)):
    for j in range(len(numeri)):
        if i != j:
            num1 = numeri[i]
            num2 = numeri[j]
            
            # Calcolo operazioni
            somma = num1 + num2
            sottrazione = num1 - num2
            prodotto = num1 * num2
            divisione = round(num1 / num2, 2) if num2 != 0 else "N/A"
            
            # Salvataggio nel dizionario
            # La chiave è una tupla (num1, num2)
            risultati_dict[(num1, num2)] = {
                'somma': somma,
                'sottrazione': sottrazione,
                'prodotto': prodotto,
                'divisione': divisione
            }
            
            # Salvataggio nella lista di tuple
            risultati_lista.append(
                (num1, num2, somma, sottrazione, prodotto, divisione)
            )

# Stampa dei risultati dal dizionario
print("RISULTATI DAL DIZIONARIO:")
for coppia, operazioni in risultati_dict.items():
    print(f"\nCoppia {coppia}:")
    for operazione, risultato in operazioni.items():
        print(f"  {operazione}: {risultato}")

print("\nRISULTATI DALLA LISTA DI TUPLE:")
for risultato in risultati_lista:
    print(f"\nCoppia {risultato[0]} e {risultato[1]}:")
    print(f"  somma: {risultato[2]}")
    print(f"  sottrazione: {risultato[3]}")
    print(f"  prodotto: {risultato[4]}")
    print(f"  divisione: {risultato[5]}")