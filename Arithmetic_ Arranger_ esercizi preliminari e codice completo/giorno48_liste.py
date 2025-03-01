# es.1
# Crea una Lista di Numeri
#Crea una lista contenente i numeri da 1 a 5.

numeri = range(1,6)

primalista = list(numeri)
print(primalista)



#es.2
# Accedi agli Elementi della Lista
#Accedi al primo e all’ultimo elemento di una lista.

stringa = 'phi ed edo'
nomi = stringa.split()
lista = list(nomi)

print (lista[0],lista[-1])



#es.3
# Modifica una Lista
#Modifica il secondo elemento di una lista.

# lo devo replicare, ho provato così


string = 'PhI ed edo '
nomi = string.lower().strip().split()
nomi[1] = 'ora'
print(nomi)



#es.4 
# Aggiungi Elementi alla Lista
#Aggiungi un nuovo elemento alla lista usando append().


stringa = 'phi ed edo'

lista = list(stringa.split())

nuovaparola = lista.append('daje')

#Il metodo append() modifica la lista direttamente e restituisce None. Non è necessario assegnare il risultato di append() a una variabile. Puoi semplificare così:
lista.append('daje')
#Se provi a fare qualcosa come nuovaparola = lista.append('daje'), la variabile nuovaparola sarà uguale a None, mentre la lista sarà comunque aggiornata.
lista.insert(0, 'nas')
#con insert riesci ad inserire il nuovo elemento dove vuoi


print(lista)
print(nuovaparola) # printa NONE!






#es.5
# Rimuovi un Elemento dalla Lista
#Rimuovi il terzo elemento di una lista usando remove().


stringa = '+39 389 4425185'
lista = stringa.split()
lista.remove(lista[2]) # Remove first occurrence of value. # Raises ValueError if the value is not present
                       #Il metodo remove() rimuove l'elemento specificato dal valore, non in base alla sua posizione. Quindi, la riga:
                        # funziona, ma solo perché stai prima accedendo al valore del terzo elemento (lista[2]) e poi passando quel valore a remove()
# di solito usiamo .remove('4425185')
print(lista)


#ricorda:
# Se vuoi rimuovere un elemento in base alla posizione, dovresti usare del o il metodo .pop().
# Esempio corretto con del:

stringa = '+39 389 4425185'
lista = stringa.split()
del lista[2]  # Rimuove l'elemento alla posizione 2
print(lista)

# Esempio con .pop()
stringa = '+39 389 4425185'
lista = stringa.split()
lista.pop(2)  # Rimuove l'elemento alla posizione 2 e lo restituisce
print(lista)



# es.5 completo, considerando il possibile errore di .len()
# Rimuovi un Elemento dalla Lista
# Rimuovi il terzo elemento di una lista usando del.

stringa = '+39 389 4425185'
lista = stringa.split()

# Verifica che la lista abbia almeno 3 elementi
if len(lista) >= 3:
    del lista[2]  # Rimuove l'elemento all'indice 2
    print("Lista dopo la rimozione:", lista)
else:
    print("La lista non ha abbastanza elementi per rimuovere il terzo.")


# es.5 : così attuato attraverso la creazione di una funzione precisa
# Rimuovi un Elemento dalla Lista
# Rimuovi il terzo elemento di una lista usando pop().

def rimuovi_terzo_elemento(stringa):
    lista = stringa.split()
    print("Lista originale:", lista)
    
    try:
        elemento_rimosso = lista.pop(2)  # Rimuove l'elemento all'indice 2
        print(f"Elemento rimosso: {elemento_rimosso}")
        print("Lista dopo la rimozione:", lista)
    except IndexError:
        print("Errore: La lista non ha abbastanza elementi per rimuovere il terzo.")

# Test della funzione
stringa = '+39 389 4425185'
rimuovi_terzo_elemento(stringa)





#es.6
#   Ordina una Lista di Numeri
#   Ordina una lista di numeri in ordine crescente.

numericasuali = 1,5,2,7,8,43,22
lista = list(numericasuali)

listacrescente = sorted(lista)
# per mettere un'altra lista in reverse devi riprendere la lista principale, non quella aggiornata come parametro da modificare
listadecrescente = sorted(lista, reverse=True)

print (lista, listacrescente, listadecrescente)



### invece che con sorted possiamo agire con .sort()

# Differenze tra sorted() e sort()
#sorted(): Ritorna una nuova lista ordinata, lasciando intatta la lista originale.
#sort(): Modifica direttamente la lista originale e non restituisce nulla (None).
#Usa sorted() se vuoi mantenere la lista originale invariata.

# Ordina e stampa le liste usando reverse()
lista = list(numericasuali)

# Ordina in ordine crescente
lista.sort()
print("Lista in ordine crescente:", lista)

# Ordina in ordine decrescente
lista.reverse()
print("Lista in ordine decrescente:", lista)






#eseercizio 6 plus: 
# conta il numero di occorrenze di una lettera in una stringa, 
# fai una lista ordinata in senso decrescente di quante volte appaiono le lettere.

stringa = 'phi ed edo'
lista = sorted(stringa.replace(' ',''))
print(lista)
count = 0

for lettera in lista:
    if lettera == lettera:
        count += 1
        print(lettera, count)

## hai fatto bene l'inizio, ma l'esercizio è sbagliato!
## sotto trovi fatto con elenchi e dizionari




# Esercizio 6 Plus - 
stringa = 'phi ed edo'

# Rimuovi gli spazi dalla stringa
stringa = stringa.replace(' ', '')

# Crea due liste: una per le lettere e una per i conteggi
lettere = []
conteggi = []

# Conta le occorrenze delle lettere
for lettera in stringa:
    if lettera not in lettere:
        lettere.append(lettera)       # Aggiungi la lettera se non è già nella lista
        conteggi.append(stringa.count(lettera))  # Conta quante volte appare la lettera

print(lettere)
print(conteggi)








# Esercizio 6 Plus
# Conta il numero di occorrenze di ogni lettera in una stringa
# Crea una lista ordinata in senso decrescente basata sulle occorrenze

stringa = 'phi ed edo'

# Rimuovi gli spazi dalla stringa
stringa = stringa.replace(' ', '')

# Crea un dizionario per contare le occorrenze delle lettere
conteggio_lettere = {}

for lettera in stringa:
    if lettera in conteggio_lettere:
        conteggio_lettere[lettera] += 1
    else:
        conteggio_lettere[lettera] = 1

# Ordina le lettere in base al conteggio (decrescente)
lettere_ordinate = sorted(conteggio_lettere.items(), key=lambda x: x[1], reverse=True)

# Stampa i risultati
print("Occorrenze delle lettere in ordine decrescente:")
for lettera, count in lettere_ordinate:
    print(f"'{lettera}': {count} volte")



#Spiegazione del Codice
#Rimozione degli Spazi:

#stringa.replace(' ', '') elimina tutti gli spazi per considerare solo le lettere.
#Conteggio delle Occorrenze:

#Viene usato un dizionario (conteggio_lettere) dove ogni chiave è una lettera e il valore è il numero di volte che appare nella stringa.
#Se una lettera già esiste come chiave, incrementiamo il valore.
#Se è la prima volta che la vediamo, la aggiungiamo con valore iniziale 1.
#Ordinamento:

#sorted(conteggio_lettere.items(), key=lambda x: x[1], reverse=True) ordina gli elementi del dizionario (come coppie chiave-valore) in base al valore (conteggio delle lettere), in ordine decrescente.
#Stampa:

#Iteriamo sulle coppie ordinate e stampiamo ciascuna lettera con il rispettivo conteggio.


