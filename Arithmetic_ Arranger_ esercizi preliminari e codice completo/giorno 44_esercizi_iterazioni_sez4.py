# Stampa da 1 a 10
# Usa un ciclo for per stampare i numeri da 1 a 10.

# base
for x in range(1,45):
    if x <= 10:
        print (x)

# Usando while
i = 1
while i <= 10:
    print(i)
    i += 1

# List comprehension
[print(x) for x in range(1,15)]



# Usando una lista diretta
numbers = list(range(1,7))
for num in numbers:
   print(num)


# Map e lambda
list(map(lambda x: print(x), range(1,9)))

        #map(lambda x: print(x), range(1,11)):
        #lambda x: print(x) è una funzione anonima che stampa un numero
        #map() applica questa funzione a ogni numero in range(1,11)
        #list() forza l'esecuzione del map

# Con sum e str.join
print('\n'.join(map(str, range(-3,2))))

        #'\n'.join(map(str, range(1,11))):
        #map(str, range(1,11)) converte ogni numero in stringa
        #join() unisce tutte le stringhe usando '\n' (newline) come separatore
        #print() mostra il risultato finale


print('\n\nesercizio 2\n\n')
# ex. 2 Somma da 1 a 10
## Usa un ciclo for per sommare i numeri da 1 a 10.

        # pensiero per risolverlo: per gli elementi in questo range, (che sono inseriti in una lista?)
        # sommiamo gli elementi, 
        # in particolare, il valore degli elementi indicizzati mi verrebbe da pensare. 

    # questo è il tuo esercizio sbagliato: 
numberi = list(range(1,7))
for x in numberi:    
    print(sum(numberi))

#Il tuo codice stampa ripetutamente la somma totale.
#  Ecco la correzione:


# Metodo veloce: usando sum() direttamente, senza ciclo for
print(sum(range(1,11)))



# Metodo 1: con variabile somma
somma = 0  # Inizializziamo la variabile
for x in range(1,11):  # Per ogni numero da 1 a 10
    somma += x  # Aggiungiamo il numero alla somma
print(somma)  # Stampiamo il risultato finale (55)



# altri esempi pratici:
# Somma numeri pari da 1 a 10
somma_pari = 0
for x in range(1,11):
    if x % 2 == 0:  # Se il numero è pari
        somma_pari += x
print(somma_pari)  # Risultato: 30

# Somma con condizione
somma_maggiore_5 = 0
for x in range(1,11):
    if x > 5:
        somma_maggiore_5 += x
print(somma_maggiore_5)  # Risultato: 40

# Somma con moltiplicazione
somma_prodotto = 0
for x in range(1,11):
    somma_prodotto += x * 2
print(somma_prodotto)  # Risultato: 110


# Somma con contatore
somma = 0
count = 0
for x in range(1,11):
   if x % 2 == 0:
       somma += x
       count += 1
print(f"Somma: {somma}, Numeri contati: {count}")

# Somma con lista comprensione
numeri = [x for x in range(1,11) if x % 3 == 0]
print(f"Numeri divisibili per 3: {sum(numeri)}")

# Somma con stringhe
somma_stringhe = ""
for x in range(1,11):
   somma_stringhe += str(x)
print(somma_stringhe)  # 12345678910





print('\n\nesercizio 3 \n\n')

#Ciclo con Condizione
#Usa un ciclo while per stampare i numeri fino a quando non raggiungi 10.

numero = 1 
while numero <= 10:
    print(numero)
    numero +=1



#somma dei numeri da 1 a 10 con while
numero = 1
somma = 0
while numero <= 10:
    somma += numero
    numero += 1
print("La somma dei numeri da 1 a 10 è:", somma)



### Contare fino a un numero specifico

numero = 1
limite = int(input("Inserisci un numero fino a cui contare: "))
while numero <= limite:
    print(numero)
    numero += 1


### stampa dei numeri dispari fino a 20

numero = 1
while numero <= 20:
    if numero % 2 != 0:  # Controlla se il numero è dispari
        print(numero)
    numero += 1


### fattoriale di un numero

numero = int(input("Inserisci un numero per calcolarne il fattoriale: "))
fattoriale = 1
counter = 1
while counter <= numero:
    fattoriale *= counter
    counter += 1
print(f"Il fattoriale di {numero} è: {fattoriale}")



#verifica di password

password_corretta = "python123"
tentativi = 0
max_tentativi = 3

while tentativi < max_tentativi:
    password_inserita = input("Inserisci la password: ")
    if password_inserita == password_corretta:
        print("Accesso consentito!")
        break
    else:
        print("Password errata. Riprova.")
        tentativi += 1

if tentativi == max_tentativi:
    print("Accesso negato. Troppi tentativi.")




print('\n esercizio 4 \n')
# esercizio 4 Verifica Pari nei Numeri
#Usa un ciclo for per stampare solo i numeri pari tra 1 e 20.

count = 1
for x in range(1,21):
    if count % 2 == 0:
        print(count)
    count +=1
    


# ex. 5 Ciclo con Break
#Usa un ciclo for con break per fermare il ciclo quando il numero raggiunge 5.

count = 1
for y in range(1,6):
    if y <= 5:
        print(y)


# ex. 6 Ciclo con Continue
#Usa un ciclo for con continue per saltare i numeri dispari.
