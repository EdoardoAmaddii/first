#es.7
# Trova il Massimo e il Minimo
# Trova il massimo e il minimo di una lista di numeri.

string = '1,2,3,4,65,9,0'
lista = string.replace(',',' ').split()
numeri = list(map(int,lista)) # converte ciascun elemento della lista in un numero
print(lista) #debug

            # avevi messo un ciclo for, ma non serviva

mass = max(numeri)
minim = min(numeri)
            # Non era necessario il ciclo for, poiché max() e min() lavorano già su tutta la lista.
            # Stavi calcolando il massimo e il minimo per ogni elemento, ma questo approccio non portava al risultato corretto.

print(mass, minim)


# Pensa globalmente, non localmente: Quando calcoli il massimo o il minimo, chiediti se hai bisogno di calcolare questo valore per l'intera lista (globale) o per ogni elemento (locale). Questo ti aiuta a scegliere se usare un ciclo o una funzione come max().

# Fai attenzione alla logica nei cicli: I cicli sono potenti, ma non sempre necessari. Cerca di identificare quando puoi evitare di iterare manualmente su una lista.









#es.8 tramite una funzione

# Somma degli Elementi di una Lista
# Somma tutti gli elementi di una lista numerica.

stringa = '1,25,3,2'
numeri = stringa.replace(',',' ').split()
listasomma = list(map(int, numeri))
somma = sum(listasomma)
print(somma)




#### esercizio 8 con funzione e try/except

def somma_elementi(stringa):
    try:
        # Sostituisci le virgole con spazi e dividi in numeri
        numeri = stringa.replace(',', ' ').split()
        
        # Converti ogni elemento in intero
        lista_numeri = list(map(int, numeri))
        
        # Calcola la somma
        somma = sum(lista_numeri)
        
        print(f'La somma degli elementi è: {somma}')
    except ValueError:
        print("Errore: La stringa deve contenere solo numeri separati da virgole o spazi.")

# Esempio d'uso
somma_elementi('1,25,3,2')






#es.9
# Unisci Due Liste
# Unisci due liste in una nuova lista.

stringslist = ['edd',1,'nu123']
string2 = 'edd'
lista = list(stringslist) # fare così
lista2 = [string2] # fare così e non list(), altrimenti non considera glie elementi della stringa

listacompleta = lista + lista2
print(listacompleta)


#Se vuoi unire liste senza duplicati (opzionale):
#Se desideri evitare duplicati tra le due liste:
stringslist = ['edd', 1, 'nu123']
string2 = 'edd'

lista2 = [string2]
listacompleta = list(set(stringslist + lista2))  # Usa set per rimuovere i duplicati
print(listacompleta)




### esercizio9 con funzione per nomi ###


def sommaliste (lista1, lista2):
    listacompleta = lista1 + lista2
    print(listacompleta)

lis1 = ['marco','giovanni']
lis2 = ['paola','francesca']
sommaliste(lis1,lis2)


### esercizio 9 plus:
# funzione per somma dei numeri all'interno di due liste ###


def sommanumeriliste(lista1, lista2):
    # Convertiamo le stringhe in liste di numeri
    numeri1 = lista1.split(',')
    numeri2 = lista2.split(',')
    
    somma_totale = 0
    # Ciclo per la prima lista
    for num in numeri1:
        somma_totale += int(num)
    
    # Ciclo per la seconda lista    
    for num in numeri2:
        somma_totale += int(num)
        
    print(somma_totale)

# Test della funzione
sommanumeriliste('2,3', '5,7')





#### così con list comprehension
### es.9

def sommanumeriliste(lista1, lista2):
    # Convertiamo le stringhe in liste di numeri
    numeri1 = [int(x) for x in lista1.split(',')]
    numeri2 = [int(x) for x in lista2.split(',')]
    
    # Sommiamo tutti i numeri delle due liste
    somma_totale = sum(numeri1) + sum(numeri2)
    print(somma_totale)

# Test della funzione
sommanumeriliste('2,3', '5,7')






### esercizio 9 
### con input

def sommanumeriinseriti (totale):
    numeridaoperare = []
    totale = 0
    numeri_inseriti = input('ti darò la somma dei numeri')

    for x in numeri_inseriti:
        numm = map(float,x)
        numeridaoperare.append(numm)

        totale = sum(numeridaoperare)
    
    print (totale)






def sommanumeriinseriti(): ## non serve mettere un argomento perchè stiamo inserendo noi cose, è una funzione vuota dove aggiungiamo noi argomenti per fare ciò che vogliamo
    numeridaoperare = []
    totale = 0

    while True:
        numeriinseriti = input('dacci numeri:\n')
        if numeriinseriti == 'done':  ### avevamo messo prima la conversione e questo sfanculava tutto, dobbiamo fare in modo che break non venga considerato come parametro calcolato
                                        ###Il più grave errore è nella riga con float(numeriinseriti): quando l'utente inserisce 'done', il programma proverà a convertire 'done' in float, causando un errore. Dovresti controllare prima se l'input è 'done' e poi fare la conversione.
            break
        numm = float(numeriinseriti)   
        numeridaoperare.append(numm)

    for x in numeridaoperare:
        totale = totale + x
    
    return  totale

daje = sommanumeriinseriti()
print('totale: ', daje)










#es.10
#Copia una Lista
#Copia una lista in un’altra lista.

# Metodo 1: usando il costruttore list()
lista_originale = [1, 2, 3, 4, 5]
nuova_lista = list(lista_originale)
print(nuova_lista)  # Output: [1, 2, 3, 4, 5]

# Metodo 2: usando la slice notation [:]
lista_originale = [1, 2, 3, 4, 5]
nuova_lista = lista_originale[:]
print(nuova_lista)  # Output: [1, 2, 3, 4, 5]

# Metodo 3: usando il metodo copy()
lista_originale = [1, 2, 3, 4, 5]
nuova_lista = lista_originale.copy()
print(nuova_lista)  # Output: [1, 2, 3, 4, 5]




# metodo profondo #
###Un punto importante da notare è la differenza tra "shallow copy" (copia superficiale) e "deep copy" (copia profonda):
# Per liste contenenti oggetti nidificati, potresti voler usare deepcopy
import copy

lista_originale = [[1, 2], [3, 4]]
# Deep copy - crea una copia completamente indipendente
nuova_lista = copy.deepcopy(lista_originale)

# Le modifiche alla lista nidificata non influenzano l'originale
nuova_lista[0][0] = 9
print(lista_originale)  # Output: [[1, 2], [3, 4]]
print(nuova_lista)      # Output: [[9, 2], [3, 4]]





#### esercizio 10 con funzione###

#il mio crea una lista con un singolo elemento, la stringa

def copialista(testo):
    lista = []
    lista.append(testo.replace(',',' '))
    return lista

esercizio = copialista('ndero, gnaro')
print(esercizio)

# La versione modificata copia tutti gli elementi da una lista esistente

# Versione modificata per copiare una lista
def copialista(lista_originale):
    lista_nuova = []
    for elemento in lista_originale:
        lista_nuova.append(elemento)
    return lista_nuova

# Test
lista_test = ['ndero', 'gnaro', 'piero']
esercizio = copialista(lista_test)
print(esercizio)  # Output: ['ndero', 'gnaro', 'piero']




###
# 
# 
# 
# Se vuoi mantenere l'idea di lavorare con una stringa ma creare una lista di parole, potresti fare così:
#
#
#
def copialista(testo):
    lista = testo.split(', ')
    return lista

esercizio = copialista('ndero, gnaro')
print(esercizio)  # Output: ['ndero', 'gnaro']
