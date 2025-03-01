
91-100

#es.1 
# Calcolatrice con Storico

#Memorizza il risultato di ogni operazione in una lista e mostra lo storico.
listaoperazioni = []

while True:
    try:
        primoinput = input("Premi 'Enter' per iniziare una nuova operazione o 'q' per uscire: ").strip().lower()
        if primoinput == 'q':
            print("Calcolatrice terminata. Arrivederci!")
            break

        # Chiedi l'input per l'operazione
        operazione = input("Inserisci un'espressione matematica (es. 2 + 3, 4 * 5, 2 ** 3): ").strip()
        
        # Append su una lista
        listaoperazioni.append(operazione)
        # Usa eval
        risultato = eval(operazione)
        print(f"Risultato: {risultato}\n")

        print(listaoperazioni)

    except ZeroDivisionError:
        print("Errore: Divisione per zero non consentita.\n")
    except Exception as e:
        print(f"Errore: {e}\n")









# Metodo 2


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
    

listaoper = []

while True:
    try:
        primoinput = input("iniziamo una nuova operazione premendo 'enter' o 'q' per uscire:\n ")
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


        operazione_completa = f"{num1} {operazione} {num2} = {risultato}"
        
        listaoper.append(operazione_completa)
        print(f"listaoperazioni: {listaoper}")


    except ValueError:
        print("Errore: Inserisci numeri validi.")
    

print(listaoper)








#es.2
# Visualizza Risultati con la Formattazione

#Usa f-string per formattare i risultati in modo chiaro.


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
        primoinput = input("iniziamo una nuova operazione premendo 'enter' o 'q' per uscire:\n ")
        if primoinput.lower() == 'q':
            print("Calcolatrice terminata. Arrivederci!")
            break

        num1 = float(input("Inserisci il primo numero:\n "))
        operazione = input("Inserisci un operatore (+, -, *, /, ** per elevare a potenza, ** (b =0.5) per radice quadrata):\n ").strip()
        num2 = float(input("Inserisci il secondo numero:\n "))

        
        risultato = calcolatrice(num1, num2, operazione)
        print(f"Risultato: {risultato}\n")

        lunghezza_max = max(len(f"{num1}"), len(f"{num2}"), len(f"{risultato}"))

        print("\nOperazione:")
        print(f"{num1:>{lunghezza_max}}")
        print(f"{operazione:>{lunghezza_max}}")
        print(f"{num2:>{lunghezza_max}}")
        print("_" * lunghezza_max)
        print(f"{risultato:>{lunghezza_max}}\n")


    except ValueError:
        print("Errore: Inserisci numeri validi.")
    









# es.3
# Esportazione Risultati in un File

#Esporta i risultati delle operazioni in un file di testo.


# Funzione principale per calcolare il risultato di un'operazione
def calcolatrice(a, b, oper):
    """
    Esegue l'operazione desiderata tra due numeri.
    """
    if oper == '+':  # Somma
        return a + b
    elif oper == '-':  # Sottrazione
        return a - b
    elif oper == '*':  # Moltiplicazione
        return a * b
    elif oper == '/':  # Divisione (con controllo per divisione per zero)
        if b != 0:
            return a / b
        else:
            return "Errore: Divisione per zero non consentita."
    elif oper == '**':  # Potenza
        return a ** b
    else:  # Operatore non riconosciuto
        return "Operatore non valido. Usa +, -, *, / o **."


# Apertura del file per salvare i risultati
# 'a' significa "append", per aggiungere nuovi risultati senza sovrascrivere il file

#La modalità 'a' è necessaria per il comportamento specifico di aggiungere dati al file senza cancellarne il contenuto precedente. Ecco cosa fanno le principali modalità di apertura dei file in Python:

#'a' (append): Aggiunge dati al file senza sovrascrivere il contenuto esistente. Se il file non esiste, lo crea.
#'w' (write): Sovrascrive completamente il contenuto esistente del file. Se il file non esiste, lo crea.
#'r' (read): Apre il file in sola lettura. Solleva un errore se il file non esiste.
#Nella tua applicazione, usi 'a' per consentire la scrittura incrementale di più operazioni nello stesso file, senza cancellare quelle precedenti.

#Se vuoi eliminare il contenuto precedente ogni volta che avvii il programma, puoi usare la modalità 'w'. Ad esempio:

with open("risultati_operazioni.txt", "a") as file:

    while True:  # Ciclo infinito, termina solo se l'utente sceglie di uscire
        try:
            # Input per iniziare o terminare il programma
            primoinput = input("Premi 'Enter' per iniziare una nuova operazione o 'q' per uscire:\n ").strip().lower()
            if primoinput == 'q':  # Se l'utente inserisce 'q', termina il programma
                print("Calcolatrice terminata. Arrivederci!")
                break

            # Richiesta del primo numero
            num1 = float(input("Inserisci il primo numero:\n "))

            # Richiesta dell'operatore matematico
            operazione = input("Inserisci un operatore (+, -, *, /, ** per elevare a potenza):\n ").strip()

            # Richiesta del secondo numero
            num2 = float(input("Inserisci il secondo numero:\n "))

            # Chiamata alla funzione per calcolare il risultato
            risultato = calcolatrice(num1, num2, operazione)

            # Determina la lunghezza massima tra i numeri e il risultato per l'allineamento in colonna
            lunghezza_max = max(len(f"{num1:.2f}"), len(f"{num2:.2f}"), len(f"{risultato:.2f}" if isinstance(risultato, (int, float)) else "Errore"))

            # Stampa l'operazione in formato colonna
            print("\nOperazione:")
            print(f"{num1:>{lunghezza_max}.2f}")  # Primo numero allineato a destra
            print(f"{operazione:>{lunghezza_max}}")  # Operatore allineato a destra
            print(f"{num2:>{lunghezza_max}.2f}")  # Secondo numero allineato a destra
            print("_" * lunghezza_max)  # Linea di separazione
            print(f"{risultato:>{lunghezza_max}}\n")  # Risultato allineato a destra

            # Salvataggio dell'operazione nel file
            if isinstance(risultato, (int, float)):  # Salva solo se il risultato è valido
                file.write(f"{num1} {operazione} {num2} = {risultato}\n")

        except ValueError:  # Errore quando l'utente inserisce dati non validi
            print("Errore: Inserisci numeri validi.\n")

# Alla fine del programma, il messaggio viene visualizzato
print("I risultati sono stati salvati in 'risultati_operazioni.txt'.")








#es.4 

# Sistema di Log per Errori
#Implementa un sistema di log per memorizzare gli errori in un file.


import logging

# Configura il sistema di logging
logging.basicConfig(
    filename='errore_log.txt',  # Il file dove registrare gli errori
    level=logging.ERROR,         # Registra solo errori (puoi anche usare INFO, DEBUG per log più dettagliati)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log #opzionale
)

def calcolatrice(a, b, oper):
    """
    Esegue l'operazione desiderata tra due numeri.
    """
    try:
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
                raise ZeroDivisionError("Errore: Divisione per zero non consentita.")
        elif oper == '**':
            return a ** b
        else:
            raise ValueError("Errore: Operatore non valido.")
    except Exception as e:
        # Registra l'errore nel file di log
        logging.error(f"Errore nell'operazione {a} {oper} {b}: {e}")
        return str(e)

while True:
    try:
        primoinput = input("Premi 'Enter' per una nuova operazione o 'q' per uscire: ")
        if primoinput.lower() == 'q':
            print("Calcolatrice terminata. Arrivederci!")
            break
        
        num1 = float(input("Inserisci il primo numero:\n "))
        operazione = input("Inserisci un operatore (+, -, *, /, ** per elevare a potenza):\n ").strip()
        num2 = float(input("Inserisci il secondo numero:\n "))

        risultato = calcolatrice(num1, num2, operazione)
        print(f"Risultato: {risultato}\n")
        
    except ValueError:
        print("Errore: Inserisci numeri validi.")










# es.5

# Ottimizzazione delle Funzioni
# Ottimizza le funzioni di calcolo per gestire input più grandi e operazioni multiple.


import logging

# Configurazione di logging per salvare gli errori in un file
logging.basicConfig(
    filename='errore_log.txt',
    level=logging.ERROR,  # Salva solo gli errori
)

def calcolatrice(operazioni):
    """
    Esegue una sequenza di operazioni sui numeri.
    """
    risultato = operazioni[0][0]  # Inizializza con il primo numero
    try:
        for i in range(1, len(operazioni)):
            num, oper = operazioni[i]
            if oper == '+':
                risultato += num
            elif oper == '-':
                risultato -= num
            elif oper == '*':
                risultato *= num
            elif oper == '/':
                if num != 0:
                    risultato /= num
                else:
                    raise ZeroDivisionError("Errore: Divisione per zero non consentita.")
            elif oper == '**':
                risultato = risultato ** num
            else:
                raise ValueError(f"Errore: Operatore {oper} non valido.")
        return risultato
    except Exception as e:
        # Registra l'errore nel file di log
        logging.error(f"Errore nelle operazioni: {e}")
        return str(e)

while True:
    try:
        primoinput = input("Premi 'Enter' per una nuova operazione o 'q' per uscire: ")
        if primoinput.lower() == 'q':
            print("Calcolatrice terminata. Arrivederci!")
            break

        # Input numeri e operatori
        operazioni = []
        num1 = float(input("Inserisci il primo numero:\n "))
        operazione = input("Inserisci un operatore (+, -, *, /, ** per elevare a potenza):\n ").strip()
        operazioni.append((num1, operazione))
        
        while True:
            try:
                num2 = float(input("Inserisci il prossimo numero (o premi 'enter' per calcolare il risultato finale):\n "))
                operazione2 = input("Inserisci un operatore (+, -, *, /, ** per elevare a potenza):\n ").strip()
                operazioni.append((num2, operazione2))
            except ValueError:
                break  # Se l'input non è un numero, calcola il risultato

        # Calcola il risultato
        risultato = calcolatrice(operazioni)
        print(f"Risultato: {risultato}\n")
        
    except ValueError:
        print("Errore: Inserisci numeri validi.")













print('\n\n\n calcolatrice \n\n\n')



#Interfaccia Grafica del Calcolatore

#Aggiungi una semplice interfaccia grafica per il calcolatore usando tkinter.


import tkinter as tk

# Funzione per eseguire i calcoli
def calcola():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        oper = operatore.get()

        if oper == '+':
            risultato = num1 + num2
        elif oper == '-':
            risultato = num1 - num2
        elif oper == '*':
            risultato = num1 * num2
        elif oper == '/':
            if num2 != 0:
                risultato = num1 / num2
            else:
                risultato = "Errore: Divisione per zero"
        elif oper == '**':
            risultato = num1 ** num2
        else:
            risultato = "Operatore non valido"
        
        # Mostra il risultato
        label_risultato.config(text=f"Risultato: {risultato}")
    except ValueError:
        label_risultato.config(text="Errore: Inserisci numeri validi.")

# Funzione per cancellare il contenuto
def reset():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_risultato.config(text="")

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolatrice")

# Layout
root.geometry("400x300")

# Etichetta e campo di input per il primo numero
label_num1 = tk.Label(root, text="Inserisci il primo numero:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

# Etichetta e campo di input per il secondo numero
label_num2 = tk.Label(root, text="Inserisci il secondo numero:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Selezione dell'operatore
operatore = tk.StringVar()
operatore.set("+")  # Valore di default
label_oper = tk.Label(root, text="Scegli l'operatore:")
label_oper.pack()

# Creazione dei pulsanti per gli operatori
frame_operatori = tk.Frame(root)
frame_operatori.pack()

# Pulsanti per gli operatori
button_plus = tk.Radiobutton(frame_operatori, text="+", variable=operatore, value="+")
button_plus.grid(row=0, column=0)

button_minus = tk.Radiobutton(frame_operatori, text="-", variable=operatore, value="-")
button_minus.grid(row=0, column=1)

button_multiply = tk.Radiobutton(frame_operatori, text="*", variable=operatore, value="*")
button_multiply.grid(row=0, column=2)

button_divide = tk.Radiobutton(frame_operatori, text="/", variable=operatore, value="/")
button_divide.grid(row=1, column=0)

button_power = tk.Radiobutton(frame_operatori, text="**", variable=operatore, value="**")
button_power.grid(row=1, column=1)

# Pulsante per calcolare
button_calcola = tk.Button(root, text="Calcola", command=calcola)
button_calcola.pack()

# Etichetta per il risultato
label_risultato = tk.Label(root, text="Risultato:")
label_risultato.pack()

# Pulsante per resettare
button_reset = tk.Button(root, text="Reset", command=reset)
button_reset.pack()

# Avvio dell'interfaccia grafica
root.mainloop()







#Semplificazione del Codice
#Rendi il codice più leggibile e modulare suddividendolo in funzioni.













#Completa l'Arithmetic Arranger - Integra tutti gli esercizi precedenti per creare una calcolatrice completa che gestisce operazioni, errori e visualizza i risultati in modo formattato.






