
# ex. 6 Ciclo con Continue
# Usa un ciclo for con continue per stampare i numeri dispari.

print('inserisci numeri ti ridarò quelli pari')

## esercizio base
conto = list()
for x in range(1,43): # range(stop) -> range object range(start, stop[, step]) -> range object
                        #Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements. When step is given, it specifies the increment (or decrement).
    if x % 2 == 0:
        conto.append(x)
    else:
        continue
print(conto)




### esercizio con input

numeriinput = input('dammi dei numeri: ')

numeri = list(map(int, numeriinput.split()))  # Converte input in lista di interi
# input viene diviso in elementi con .split() e convertito in numeri interi usando map(int, ...).
for num in numeri:
    if num % 2 != 0:
        continue
    # else: puoi non metterlo
    print(num)


# ex. 6 Ciclo con Continue versione 2

# Usa un ciclo for con continue per stampare i numeri pari.
print('Inserisci numeri e ti restituirò quelli pari.')
numeriinput = input('Dammi dei numeri separati da uno spazio: ')

# Soluzione 1: Con list comprehension
# numeri = [int(num) for num in numeriinput.split()]

# Soluzione 2: Con 2 ciclo for : uno per la lista uno per l'operazione sulla lista
                        
numeriinput = numeriinput.replace(',', ' ')
numeri = []
for num in numeriinput.split(): #primo ciclo converte i numeri in interi
    numeri.append(int(num))

# Ciclo for per filtrare i numeri pari
for num in numeri:
    if num % 2 != 0:  # Salta i numeri dispari
        continue
    print(num)  # Stampa solo i numeri pari








#es.6

#Somma di Numeri Positivi
#Usa un ciclo while per sommare solo i numeri positivi fino a quando l'utente non inserisce 0.
##




## prima versione:


# Somma di Numeri Positivi
# Usa un ciclo while per sommare solo i numeri positivi fino a quando l'utente non inserisce 0.

# Variabile per tenere traccia della somma
somma = 0

# Ciclo while infinito (interrotto quando l'utente inserisce 0)
while True:
    # Richiede un numero dall'utente
    numero = input("Inserisci un numero positivo da sommare (0 per terminare): ")
    
    # Converte l'input in un intero e gestisce errori
    try:
        numero = int(numero)
    except ValueError:
        print("Per favore, inserisci un numero valido.")
        continue

    # Se l'utente inserisce 0, interrompe il ciclo
    if numero == 0:
        break

    # Aggiungi alla somma solo i numeri positivi
    if numero > 0:
        somma += numero
    else:
        print("Hai inserito un numero negativo, che non verrà sommato.")

# Stampa il risultato finale
print(f"La somma dei numeri positivi è: {somma}")


####
#### seconda versione
####

#prima convertiamo la stringa dell'utente in un numero intero
#con un ciclo for e la aggiungiamo alla lista
numeriin = input('Dammi numeri positivi che vuoi sommare, per chiudere la operazione inserisci 0: \n')

numeri = numeriin.replace(',', ' ').split()
listasomma = []
for x in numeri:
    listasomma.append(int(x))

print(f'Listasomma:{listasomma}')

for y in listasomma:
    while y > 0:
        print(sum(listasomma))

    else:
        if y == 0:
            break
print(listasomma)



##
## # Somma di Numeri Positivi
# Usa un ciclo while per sommare solo i numeri positivi finché l'utente non inserisce 0.

# Lista per contenere i numeri
listasomma = []

while True:
    # Richiede input dall'utente
    numeroinput = input('Inserisci un numero positivo da sommare (0 per terminare): ')
    
    # Converte l'input in un numero intero
    try:
        numero = int(numeroinput)
    except ValueError:
        print("Per favore, inserisci un numero valido.")
        continue

    # Se il numero è 0, esci dal ciclo
    if numero == 0:
        break

    # Aggiungi solo numeri positivi alla lista
    if numero > 0:
        listasomma.append(numero)
    else:
        print("Hai inserito un numero negativo, che non verrà sommato.")

# Calcola e stampa la somma
print(f'Lista dei numeri: {listasomma}')
print(f'Somma dei numeri positivi: {sum(listasomma)}')

        
#####

# c'è un errore


















