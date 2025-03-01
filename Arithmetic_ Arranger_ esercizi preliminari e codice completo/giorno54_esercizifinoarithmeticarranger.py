"""
Sezione 8: Funzionalità Preparatorie per l'Arithmetic Arranger (Esercizi 71-80)
71. Costruisci una Funzione che Aggiunge Numeri alla Lista

Scrivi una funzione che aggiunge un numero alla fine di una lista e restituisce la lista aggiornata.
72. Creazione di una Funzione che Calcola l'Operazione Selezionata

Scrivi una funzione che esegue l'operazione aritmetica selezionata (somma, sottrazione, etc.) tra due numeri.
73. Costruzione di un'Interfaccia Utente per Inserire Numeri

Scrivi un programma che chiede all'utente di inserire due numeri e l'operazione aritmetica che desidera eseguire, poi visualizza il risultato.
74. Crea una Funzione che Aggiunge e Restituisce il Risultato

Crea una funzione che esegue l'operazione scelta su due numeri, aggiunge il risultato a una lista e restituisce la lista.
75. Calcolare il Risultato e Visualizzare un Messaggio con l'Operazione

Scrivi una funzione che calcola il risultato di un'operazione e visualizza un messaggio che mostra il calcolo, come ad esempio "5 + 3 = 8".
76. Aggiungi un Ciclo che Continua Finché l'Utente Non Decida di Fermarsi

Implementa un ciclo che continua a chiedere operazioni all'utente (somma, sottrazione, etc.) finché non inserisce un comando per fermarsi.
77. Crea una Funzione che Restituisce la Somma di una Lista di Risultati

Scrivi una funzione che restituisce la somma di tutti i risultati in una lista di operazioni.
78. Verifica Se l'Operazione Scelta è Valida

Scrivi una funzione che verifica se l'operazione scelta dall'utente è una delle operazioni matematiche valide (somma, sottrazione, etc.).
79. Creazione di una Funzione che Genera Equazioni Casuali

Scrivi una funzione che genera e stampa equazioni casuali con numeri tra 1 e 10, come ad esempio "2 + 3 = 5".
80. Funzione per Gestire più Operazioni in Sequenza

Scrivi una funzione che permette all'utente di inserire più operazioni in sequenza, restituisce i risultati e le equazioni in formato chiaro.
"""









#71. Costruisci una Funzione che Aggiunge Numeri alla Lista
#Scrivi una funzione che aggiunge un numero alla fine di una lista e restituisce la lista aggiornata.

listanumeri = [1,3,4,7]

def aggiunginumero(numero, lista):

    """
    # Validazione input :: possiamo controllare gli errori
    if not isinstance(lista, list):
        raise TypeError("Il secondo argomento deve essere una lista")
    if not isinstance(numero, (int, float)):
        raise TypeError("Il primo argomento deve essere un numero")
    """

    if numero not in lista:
        lista.append(numero)

    return lista

risultato = aggiunginumero(54, listanumeri)
print(risultato)




## una versione migliorata, eliminato il suerfluo:
listanumeri = [1, 3, 4, 7]

def aggiunginumero(numero, lista):
    # Controlla una sola volta se il numero è già presente
    if numero not in lista:
        lista.append(numero)
    return lista

risultato = aggiunginumero(54, listanumeri)
print(risultato)





#Versione che non modifica la lista originale:

def aggiunginumero(numero, lista):
    nuova_lista = lista.copy()  # Crea una copia della lista
    if numero not in nuova_lista:
        nuova_lista.append(numero)
    return nuova_lista



# Versione che accetta più numeri:

def aggiunginumeri(numeri, lista):
    nuova_lista = lista.copy()
    for numero in numeri:
        if numero not in nuova_lista:
            nuova_lista.append(numero)
    return nuova_lista

# Uso:
risultato = aggiunginumeri([54, 55, 56], listanumeri)




    








# 72. Creazione di una Funzione che Calcola l'Operazione Selezionata
# Scrivi una funzione che esegue l'operazione aritmetica selezionata (somma, sottrazione, etc.) tra due numeri.

def operatore(a,b, operatore):
    if operatore == '+':
        return f'{a} + {b} = {a+b}'
    
    elif operatore == '-':
        return f'{a} - {b} = {a-b}'
    
    elif operatore == '*':
        return f'{a} * {b} = {a*b}'
    
    elif operatore == '/' and b != 0:
        return f'{a} / {b} = {a/b}'

        
operazione = operatore(3,5,'+')
print(f'Operazione:\n{operazione}')
                    
"""
# problemi del codice:
Non c'è gestione del caso in cui l'operatore non è valido
Non c'è messaggio di errore per la divisione per zero

"""


def operatore(a, b, operatore):
    if operatore == '+':
        return f'{a} + {b} = {a+b}'
    
    elif operatore == '-':
        return f'{a} - {b} = {a-b}'
    
    elif operatore == '*':
        return f'{a} * {b} = {a*b}'
    
    elif operatore == '/':
        if b == 0:
            return "Errore: divisione per zero"
        return f'{a} / {b} = {round(a/b, 2)}'  # round() arrotonda a 2 decimali
    
    elif operatore == '**':
        return f'{a} ** {b} = {round(a**b, 2)}' 
    
    else:
        return "Operatore non valido. Usa +, -, *, /"

# Test
print(operatore(3, 5, '+'))    # Somma normale
print(operatore(10, 0, '/'))   # Test divisione per zero
print(operatore(4, 2, '%'))    # Test operatore non valido
print(operatore(2, -1, '**'))   # potenza
















# 73. Costruzione di un'Interfaccia Utente per Inserire Numeri
# Scrivi un programma che chiede all'utente di inserire due numeri e l'operazione aritmetica che desidera eseguire, poi visualizza il risultato.


def operator(a, b, operatore):
    if operatore == '+':
        return f'{a} + {b} = {a+b}'
    
    elif operatore == '-':
        return f'{a} - {b} = {a-b}'
    
    elif operatore == '*':
        return f'{a} * {b} = {a*b}'
    
    elif operatore == '/':
        if b == 0:
            return "Errore: divisione per zero"
        return f'{a} / {b} = {round(a/b, 2)}'  # round() arrotonda a 2 decimali
    
    elif operatore == '**':
        return f'{a} ** {b} = {round(a**b, 2)}' 
    
    else:
        return "Operatore non valido. Usa +, -, *, /"

numero1 = float(input('inserisci un numero:\n'))
unoperatore = input('inserisci operatore (+,-,*,/,**:\n')
numero2 = float(input('inserisci il secondo numero:\n'))

risultato = operator(numero1, numero2, unoperatore)

print(risultato)





# 74. Crea una Funzione che Aggiunge e Restituisce il Risultato
# Crea una funzione che esegue l'operazione scelta su due numeri, aggiunge il risultato a una lista e restituisce la lista.


listarisultati = list()

def risultat (a,oper,b):
    
    if oper == '+':
        listarisultati.append(a+b)
    
    elif oper == '-':
        listarisultati.append(a-b)
    
    elif oper == '*':
        listarisultati.append(a*b)
    
    elif oper == '/':
        if b == 0:
            return "Errore: divisione per zero"
        else:
            listarisultati.append(a/b)
    
    elif oper == '**':
        listarisultati.append(a**b)
    
    else:
        return "Operatore non valido. Usa +, -, *, /"
    
    return listarisultati
    

while True:
    try:
        enter_exit = input("premi 'enter' per continuare, 'q' per uscire:\n")
        if enter_exit == 'q'.lower():
            break
        numero1 = float(input('inserisci un numero:\n'))
        unoperatore = input('inserisci operatore (+,-,*,/,**):\n')
        if unoperatore not in ['+','-','*,','/','**']:
            print("operatore non valido, usa l'operatore corretto")
            continue
        numero2 = float(input('inserisci il secondo numero:\n'))
    
    except ValueError:
        print('inserisci numeri e rispetta gli operatori')
        continue

    #print della lista aggiornata ad ogni passaggio
    risultatolista = risultat(numero1,unoperatore,numero2)
    print(f'risultati fino ad ora: {risultatolista},{type(risultatolista)}')







# 75. Calcolare il Risultato e Visualizzare un Messaggio con l'Operazione
# Scrivi una funzione che calcola il risultato di un'operazione e visualizza un messaggio che mostra il calcolo, come ad esempio "5 + 3 = 8".


def calcolatore(num1,num2,oper):
    if oper == '+':
        return f'{num1} + {num2} = {num1+num2}'
    else:
        return 'inserisci termini validi'
    

risultato = calcolatore(32,21,'+')
print(risultato)











# 76. Aggiungi un Ciclo che Continua Finché l'Utente Non Decida di Fermarsi
# Implementa un ciclo che continua a chiedere operazioni all'utente (somma, sottrazione, etc.) finché non inserisce un comando per fermarsi.
"""
def calcolatrice ():
    pass

while True:
    primoinp = input("inserisci un operazione o esci con 'q': ")
    if primoinp == 'q':
        break
"""

####### l'abbiamo già fatto più volte questo esercizio, c'è un modo alternativo, non devi scrivere necessariamente tutto il codice della calcolatrice
    

while True:
    operazione = input("Inserisci un'operazione intera o esci con 'q': ")
    if operazione.lower() == 'q':
        print("Uscita dal programma. Arrivederci!")
        break

    try:
        risultato = eval(operazione)
        print(f'Il risultato è: {risultato}')
    except Exception as e:
        print(f'Errore: {e}')

"""
Spiegazione del Codice
Ciclo while True: Il ciclo continua a chiedere input all'utente finché non viene inserito 'q' per uscire.

Input dell'Operazione: Viene chiesta un'operazione matematica completa come input (es. "3 + 5 * 2").

Valutazione dell'Operazione: Utilizziamo la funzione eval() per valutare l'espressione matematica inserita. La funzione eval() esegue la stringa come codice Python.

Gestione degli Errori: Utilizziamo un blocco try-except per catturare e gestire eventuali errori che potrebbero verificarsi durante la valutazione dell'espressione.

Sicurezza
È importante notare che l'uso della funzione eval() può essere rischioso se l'input non è controllato, in quanto permette l'esecuzione di qualsiasi codice Python. In un'applicazione reale, dovresti aggiungere ulteriori controlli per assicurarti che l'input sia sicuro. Un'alternativa più sicura potrebbe essere l'uso di una libreria come sympy per valutare espressioni matematiche in modo sicuro.

"""









