#77. Crea una Funzione che Restituisce la Somma di una Lista di Risultati

#Scrivi una funzione che restituisce la somma di tutti i risultati in una lista di operazioni.


listarisultati = []

def sommarisultati():
    for x in listarisultati:
        if x not in listarisultati:
            listarisultati.append(x)
    return sum(listarisultati)
    

while True:
    operazione = input("Inserisci un'operazione intera o esci con 'q': ")
    if operazione.lower() == 'q':
        print("Uscita dal programma. Arrivederci!")
        break
    try:
        risultato = eval(operazione)
        print(f'Il risultato è: {risultato}')
        listarisultati.append(risultato)

    except Exception as e:
        print(f'Errore: {e}')


risultato = sommarisultati()
print(risultato)




####
#questa la versione migliore
###



listarisultati = []

def sommarisultati(lista):
    return sum(lista)
    
while True:
    operazione = input("Inserisci un'operazione intera o esci con 'q': ")
    if operazione.lower() == 'q':
        print("Uscita dal programma. Arrivederci!")
        break
    try:
        risultato = eval(operazione)
        print(f'Il risultato è: {risultato}')
        listarisultati.append(risultato)

    except Exception as e:
        print(f'Errore: {e}')

risultato_totale = sommarisultati(listarisultati)
print(f'La somma totale dei risultati è: {risultato_totale}')
















#78. Verifica Se l'Operazione Scelta è Valida
#Scrivi una funzione che verifica se l'operazione scelta dall'utente è una delle operazioni matematiche valide (somma, sottrazione, etc.).





def calcolatore(num1,num2,oper):
    if oper == '+':
        return f'{num1} + {num2} = {num1+num2}'
    elif oper == '-':
        return f'{num1} - {num2} = {num1-num2}'
    else:
        return 'inseerisci termini validi'
    
while True: 
    try: 
        primo = float(input('Inserisci un numero o q per uscire:\n')) 
    except ValueError: 
        print('Errore: Inserisci un numero valido.') 
        continue 
    

    operatore = input('Inserisci + o - come operatore aritmetico:\n') 
    if operatore not in ['+', '-']: 
        print("Errore: Inserisci un operatore valido (+ o -).") 
        continue 

    try: 
        secondo = float(input('Inserisci un secondo numero:\n')) 
    except ValueError: 
        print('Errore: Inserisci un numero valido.') 
        continue
    
    risultato = calcolatore(primo,secondo,operatore)
    print(risultato)
    
  


### questo è un ciclo infinito che non si chiude

    
        












#79. Creazione di una Funzione che Genera Equazioni Casuali
#Scrivi una funzione che genera e stampa equazioni casuali con numeri tra 1 e 10, come ad esempio "2 + 3 = 5".


import random

def genera_equazione():
    numeri = range(1, 11)
    operatori = ['+', '-', '*', '/']

    num1 = random.choice(numeri)
    num2 = random.choice(numeri)
    operatore = random.choice(operatori)

    if operatore == '/' and num2 == 0:
        risultato = "Errore: divisione per zero"
    else:
        if operatore == '+':
            risultato = num1 + num2
        elif operatore == '-':
            risultato = num1 - num2
        elif operatore == '*':
            risultato = num1 * num2
        elif operatore == '/':
            risultato = round(num1 / num2, 2)  # Arrotondare il risultato a 2 decimali

        print(f"{num1} {operatore} {num2} = {risultato}")

# Genera e stampa 5 equazioni casuali come esempio
for _ in range(5):
    genera_equazione()








#80. Funzione per Gestire più Operazioni in Sequenza
#Scrivi una funzione che permette all'utente di inserire più operazioni in sequenza, restituisce i risultati e le equazioni in formato chiaro.

def esegui_operazioni_sequenza():
    risultati = []

    while True:
        operazione = input("Inserisci un'operazione intera (es. 2 + 3) o esci con 'q': ").lower()
        if operazione == 'q':
            print("Uscita dal programma. Arrivederci!")
            break

        try:
            risultato = eval(operazione)
            print(f'Il risultato è: {operazione} = {risultato}')
            risultati.append(f'{operazione} = {risultato}')
        except Exception as e:
            print(f'Errore: {e}')

    return risultati

# Esegui la funzione e stampa i risultati
risultati = esegui_operazioni_sequenza()
print("Equazioni e risultati:")
for r in risultati:
    print(r)




















### questo più complesso


def esegui_operazione(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        if num2 == 0:
            return "Errore: divisione per zero"
        else:
            return num1 / num2
    else:
        return "Operatore non valido. Usa +, -, *, /"

def gestisci_operazioni_sequenza():
    operazioni = []
    risultati = []

    while True:
        operazione = input("Inserisci un'operazione (es. 3 + 5) o 'q' per uscire: ")
        if operazione.lower() == 'q':
            break
        
        try:
            num1, oper, num2 = operazione.split()
            num1 = float(num1)
            num2 = float(num2)
            
            risultato = esegui_operazione(num1, oper, num2)
            if isinstance(risultato, str):
                print(risultato)
            else:
                operazioni.append(operazione)
                risultati.append(risultato)
                print(f"Il risultato di '{operazione}' è: {risultato}")

        except ValueError:
            print("Errore: Assicurati di inserire un'operazione valida nel formato corretto (es. 3 + 5).")
        except Exception as e:
            print(f"Errore: {e}")

    print("\nEcco le operazioni inserite e i loro risultati:")
    for operazione, risultato in zip(operazioni, risultati):
        print(f"{operazione} = {risultato}")

# Eseguire la funzione per permettere all'utente di inserire più operazioni
gestisci_operazioni_sequenza()






