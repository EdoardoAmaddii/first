# 21 Scrivi una Funzione Semplice
# Crea una funzione che stampa un messaggio.

def stampa(messaggio):
    print(messaggio)

stampa('fischia e canta')


# 22 Somma di Due Numeri
# Crea una funzione che restituisce la somma di due numeri.

def somma(x, y):
    numero1 = float(x)
    numero2 = float(y)
    print(numero1 + numero2)

somma (69584837392, 44646373625)

#Osservazioni:

# Non è necessario convertire esplicitamente i parametri a float all'interno della funzione se si assume che gli argomenti siano numerici. La conversione dovrebbe essere fatta solo se ci si aspetta input misti (es. stringhe).
# Attualmente la funzione stampa il risultato, ma non lo restituisce. Sarebbe meglio restituire la somma, così da poterla riutilizzare in altre parti del codice.

def somma(x, y):
    return float(x) + float(y)

risultato = somma(69584837392, 4.44646373625)
print(risultato)




#Funzione con Parametro
# Crea una funzione che prende un parametro e stampa il quadrato di un numero.
    
def quadrato(x):
    y = x**2
    print(y)

quadrato(5)


# Funzione con Valore di Default

# Crea una funzione con un parametro che ha un valore di default.

def stampa_quadrato_default(numero=2):
    # Calcola il quadrato del numero
    quadrato = numero ** 2
    print(f"Il quadrato di {numero} è {quadrato}")

# Esempio di utilizzo
stampa_quadrato_default()  # Usa il valore di default (2)
stampa_quadrato_default(7)  # Usa il valore passato (7)


# Funzione di Aritmetica
# Scrivi una funzione che calcola la somma, la sottrazione e la moltiplicazione di due numeri.

def calcolatore (numero1, numero2):
    print(numero1 * numero2)
    print(numero1 + numero2)
    print(numero1 - numero2)

risultato = calcolatore(5,4)
print(risultato)



#ex. Funzione con Risultato Condizionale
#Scrivi una funzione che restituisce un messaggio diverso a seconda di un parametro.

def unoodue(x):
    pari = (x % 2 == 0)
    if pari:
        return 'pari'
    else:
        return 'dispari'
    
inseriscinumero = input('Dammi un numero:\n')
numero = float(inseriscinumero)

unoodue(numero) 

risultato = unoodue(numero)
print(f'il tuo numero è: {risultato}')


#Perché il tuo codice originale mostra None?
#Funzione senza return: Quando una funzione non include un'istruzione return, Python restituisce implicitamente None.
#Uso di print nella funzione: print non restituisce alcun valore utilizzabile, serve solo a mostrare informazioni in console.
#Quando scrivi risultato = unoodue(numero), la funzione esegue print per mostrare "pari" o "dispari", ma poiché non restituisce niente, la variabile risultato riceve il valore None.

#Differenze tra print e return
#print: Mostra un messaggio sulla console, ma non restituisce un valore utilizzabile nel programma.
#return: Restituisce un valore che può essere assegnato a una variabile o utilizzato in altre parti del codice.
#Usare return è fondamentale quando vuoi che una funzione "comunichi" un risultato al resto del programma.






# Funzione con Lista di Numeri
# Crea una funzione che somma tutti gli elementi di una lista di numeri.

def sommanumeri(inputlista, inputlista2):
    lista = list()
    numero1 = float(inputlista)
    numero2 = float(inputlista2)
    lista.append(numero1)
    lista.append(numero2)
    return (sum(lista))

inputlista = input('dammi un numero\n')
inputlista2 = input('secondo numero\n')
risultato = sommanumeri(inputlista, inputlista2)
print(risultato)




#così è fatta meglio:

def somma_due_numeri(num1, num2):
    """Somma due numeri e restituisce il risultato."""
    return num1 + num2

# Input dell'utente
try:
    numero1 = float(input('Dammi un numero:\n'))
    numero2 = float(input('Secondo numero:\n'))

    # Chiamata alla funzione
    risultato = somma_due_numeri(numero1, numero2)
    print(f'La somma dei numeri è: {risultato}')
except ValueError:
    print("Errore: Inserisci solo numeri validi!")




# somma di una lista generica
def somma_lista(lista):
    """Somma tutti i numeri di una lista."""
    return sum(lista)

numeri = [1, 2, 3, 4, 5]
print(f'La somma è: {somma_lista(numeri)}')  # Output: 15




#somma con umeri illimitati (ARGS)
def somma_illimitata(*numeri):
    """Somma un numero arbitrario di valori. bisogna mettere l'asterisco sull'argomento della funzione, altrimenti abbiamo un errore"""
    return sum(numeri)

print(somma_illimitata(1, 2, 3))      # Output: 6
print(somma_illimitata(10, 20, 30))   # Output: 60








########
####  Per creare una funzione che accetta un solo input e genera una lista di numeri da sommare, puoi chiedere all'utente di fornire una stringa di numeri separati da uno spazio o da una virgola. Successivamente, puoi elaborare questa stringa per trasformarla in una lista di numeri e calcolare la somma.


def somma_lista_da_input():
    """Crea una lista di numeri da un input dell'utente e ne calcola la somma."""
    # Chiedi all'utente di inserire numeri separati da spazi o virgole
    input_numeri = input("Inserisci una lista di numeri separati da spazi o virgole:\n")
    
    # Sostituisci le virgole con spazi e dividi la stringa in una lista di numeri
    try:
        numeri = [float(num) for num in input_numeri.replace(",", " ").split()]
        # Calcola la somma
        return sum(numeri)
    except ValueError:
        return "Errore: assicurati di inserire solo numeri validi!"

# Chiamata della funzione
risultato = somma_lista_da_input()
print(f"La somma dei numeri è: {risultato}")


#Come Funziona il Codice
#Input Utente:
#L'utente inserisce una stringa con numeri separati da spazi o virgole, ad esempio:

#1 2 3 4
#1, 2, 3, 4
#Elaborazione della Stringa:

#Usa .replace(",", " ") per sostituire eventuali virgole con spazi.
#Usa .split() per dividere la stringa in una lista di sottostringhe.
#Trasforma ogni sottostringa in un numero con float(num).
#Gestione degli Errori:
#Se l'utente inserisce valori non numerici, il blocco try-except restituisce un messaggio di errore.

#Somma dei Numeri:
#La lista di numeri viene passata a sum() per calcolare la somma totale.






#############Consigli di Estensione
#Aggiungi la possibilità di interrompere l'input se l'utente digita qualcosa come "fine".
#Permetti all'utente di scegliere un delimitatore diverso (ad esempio, punto e virgola).
#Mostra anche il conteggio dei numeri oltre alla loro somma. 😊



def somma_lista_da_input():
    """
    Crea una lista di numeri da un input dell'utente e ne calcola la somma.
    L'utente può utilizzare diversi delimitatori e interrompere con 'fine'.
    """
    print("Inserisci una lista di numeri separati da spazi, virgole o punto e virgola.")
    print("Digita 'fine' per terminare.")

    while True:
        # Chiedi l'input all'utente
        input_numeri = input("\nInserisci i numeri:\n")
        
        # Controlla se l'utente vuole terminare
        if input_numeri.lower() == "fine":
            print("Operazione terminata. Grazie!")
            return

        # Sostituisci i delimitatori con spazi e dividi la stringa in numeri
        try:
            numeri = [
                float(num) for num in input_numeri.replace(",", " ").replace(";", " ").split()
            ]

            # Calcola la somma e conta i numeri
            somma = sum(numeri)
            conteggio = len(numeri)

            # Stampa il risultato
            print(f"\nHai inserito {conteggio} numeri.")
            print(f"La somma dei numeri è: {somma}\n")

        except ValueError:
            print("Errore: assicurati di inserire solo numeri validi!")


###
### Come Funziona il Codice Esteso
#Interruzione dell'Input:

#Se l'utente digita "fine", il programma termina con un messaggio di saluto.
#Supporto per Diversi Delimitatori:

#Il programma sostituisce automaticamente virgole (,), punto e virgola (;), e altri delimitatori con spazi per semplificare l'elaborazione.
#Conteggio dei Numeri:

#Usa len(numeri) per contare quanti numeri sono stati inseriti.
#Gestione degli Errori:

#Se l'utente inserisce qualcosa di non valido (ad esempio testo non numerico), viene mostrato un messaggio di errore.








# funzione ricorsiva
# Crea una funzione che calcola il fattoriale di un numero usando la ricorsione.
# l fattoriale di un numero intero non negativo indicato con 
# 𝑛! è il prodotto di tutti i numeri interi positivi da 1 fino a n.
#È una funzione matematica molto importante, utilizzata in diversi campi, come la combinatoria, la probabilità e l'analisi matematica.
## n!=n×(n−1)×(n−2)×…×1


def fattoriale(n):
    """
    Calcola il fattoriale di un numero n usando la ricorsione.
    """
    # Caso base: il fattoriale di 0 o 1 è 1
    if n == 0 or n == 1:
        return 1
    
    # Passo ricorsivo: n * fattoriale(n-1)   -->> ci sarà la moltiplicazione di tutti i numeri fino al caso base
    return n * fattoriale(n - 1)

# Input dell'utente
try:
    numero = int(input("Inserisci un numero intero non negativo:\n"))
    if numero < 0:
        print("Errore: il numero deve essere non negativo!")
    else:
        risultato = fattoriale(numero)
        print(f"Il fattoriale di {numero} è: {risultato}")
except ValueError:
    print("Errore: devi inserire un numero intero!")


#Come Funziona
#1. Caso Base:

#Il fattoriale di 0 o 1 è sempre 1.
#Questo serve a terminare la ricorsione, evitando chiamate infinite.

#2. Passo Ricorsivo:

#Se 𝑛>1, la funzione richiama sé stessa calcolando 
# 𝑛×fattoriale(𝑛−1)

#3. Gestione degli Input:

#Il programma verifica che l'utente inserisca un numero intero non negativo.
#Se l'input non è valido, viene mostrato un messaggio di errore.







# Funzione per Trovare il Massimo
# Scrivi una funzione che trova il massimo di tre numeri.

def massimo(x):
    return (max(x))
    
numeri = [1,3,5]
result = massimo(numeri)
print(f'il numero più grande della lista è: {result}')

# con input dell'utente

def maxx(y):
    return (max(y))

inputt = input('dammi dei numeri e troverò il più grande:\n')
# Converti l'input in una lista di numeri
numbers = [float(x) for x in inputt.split(',')]

risult = maxx(numbers)

print(risult)


