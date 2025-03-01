#es. 7
# Visualizza Operazioni in Formato Tabella
#Crea una funzione che visualizza i risultati in una tabella ben formattata.


def tabella(a, b):
                        #Calcoli:

                        #Le quattro operazioni principali sono calcolate e memorizzate in variabili.
                        #La divisione è gestita con un controllo per evitare errori con divisore zero.
    somma = a + b
    sottrazione = a - b
    moltiplicazione = a * b
    divisione = "Errore: Divisione per zero" if b == 0 else a / b

    # Tabella ben formattata
    print(f"{'Operazione':<20}{'Risultato':>10}")
    print("-" * 30)
    print(f"{'Somma':<20}{somma:>10.2f}")
    print(f"{'Sottrazione':<20}{sottrazione:>10.2f}")
    print(f"{'Moltiplicazione':<20}{moltiplicazione:>10.2f}")
    print(f"{'Divisione':<20}{divisione:>10}")

                        #Tabella:

                        #Utilizzo di stringhe formattate con specificatori di larghezza (:<20 e :>10) per creare una struttura chiara e ben allineata.
                        #somma:>10.2f imposta due cifre decimali per i risultati numerici.


# Esempio di utilizzo
tabella(4, 7)
tabella(10, 0)











#es. 8
# Crea un Menu per il Calcolatore
#Crea un menu che permette all'utente di scegliere l’operazione (somma, sottrazione, ecc.).




def calcolatrice(a, b, oper):
    """
    Esegue l'operazione desiderata tra due numeri.
    """
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b != 0:
            return a / b
        else:
            return "Errore: Divisione per zero non consentita."
    else:
        return "Operatore non valido. Usa +, -, * o /."

while True:
    try:
        primoinput = input("iniziamo una nuova operazione premendo 'enter' o 'q' per uscire):\n ")
        if primoinput.lower() == 'q':
            print("Calcolatrice terminata. Arrivederci!")
            break
        
        num1 = float(input("Inserisci il primo numero:\n "))
        num2 = float(input("Inserisci il secondo numero:\n "))
        operazione = input("Inserisci un operatore (+, -, *, /):\n ").strip()

        risultato = calcolatrice(num1, num2, operazione)
        print(f"Risultato: {risultato}\n")
    except ValueError:
        print("Errore: Inserisci numeri validi.")
    except KeyboardInterrupt:
        print("\nCalcolatrice interrotta. Arrivederci!")
        break
    except Exception as e:
        print(f"Errore inaspettato: {e}")

    # Opzione per uscire dal ciclo ##  
    # 
    # così abbiamo un messaggio di uscita alla fine dell'operazione
    # 
    # ci può stare come no, comunque il ciclo si ferma quando gli viene ridato q all'inizio.
    #
    continua = input("Vuoi continuare? (sì per continuare, qualsiasi altro tasto per uscire):\n ").strip().lower()
    if continua not in ["sì", "si", "s"]:
        print("Calcolatrice terminata. Arrivederci!")
        break









#es. 9
# Aggiungi Supporto per Operazioni Complesse
# Aggiungi il supporto per esponenti e radici quadrate.





def calcolatrice(a, b, oper):
    """
    Esegue l'operazione desiderata tra due numeri.
    """
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b != 0:
            return a / b
        else:
            return "Errore: Divisione per zero non consentita."
        
    elif oper == '**':
        return a**b
    

    else:
        return "Operatore non valido. Usa +, -, * o /."

while True:
    try:
        primoinput = input("iniziamo una nuova operazione premendo 'enter' o 'q' per uscire):\n ")
        if primoinput.lower() == 'q':
            print("Calcolatrice terminata. Arrivederci!")
            break
        
            #
            # qui non c'è bisogno dell'else

        num1 = float(input("Inserisci il primo numero:\n "))
        operazione = input("Inserisci un operatore (+, -, *, /, ** per elevare a potenza, ** (b =0.5) per radice quadrata):\n ").strip()
        num2 = float(input("Inserisci il secondo numero:\n "))
        
        risultato = calcolatrice(num1, num2, operazione)
        print(f"Risultato: {risultato}\n")
    except ValueError:
        print("Errore: Inserisci numeri validi.")
    

    







#es. 10
# Gestisci Molteplici Operazioni
#Crea un loop che permette all'utente di eseguire più operazioni fino a quando non decide di uscire.
while True:
    try:
        primoinput = input("Premi 'Enter' per iniziare una nuova operazione o 'q' per uscire: ").strip().lower()
        if primoinput == 'q':
            print("Calcolatrice terminata. Arrivederci!")
            break

        # Chiedi l'input per l'operazione
        operazione = input("Inserisci un'espressione matematica (es. 2 + 3, 4 * 5, 2 ** 3): ").strip()

        # Controlla che l'operazione sia sicura ### opzionale
        if any(char not in "0123456789+-*/(). " for char in operazione):
            print("Errore: l'operazione contiene caratteri non validi.")
            continue

        # Usa eval solo dopo aver validato
        risultato = eval(operazione)
        print(f"Risultato: {risultato}\n")

    except ZeroDivisionError:
        print("Errore: Divisione per zero non consentita.\n")
    except Exception as e:
        print(f"Errore: {e}\n")





    






