#es.8 
# Unisci Due Dizionari
#Unisci due dizionari in uno nuovo.

# Metodo 1: usando l'operatore |= (Python 3.9+) o l'operatore di update |
dizio1 = {1: 'ciao', 2: 'amore'}
dizio2 = {3: 'macchè', 4: 'ahah'}
# Creiamo un nuovo dizionario che contiene tutto
diziocompleto = dizio1 | dizio2
print(diziocompleto)  # Output: {1: 'ciao', 2: 'amore', 3: 'macchè', 4: 'ahah'}

    

# Metodo 2: usando update()
dizio1 = {1: 'ciao', 2: 'amore'}
dizio2 = {3: 'macchè', 4: 'ahah'}

diziocompleto = dizio1.copy()  # Facciamo una copia per non modificare l'originale
diziocompleto.update(dizio2)   # Aggiungiamo gli elementi del secondo dizionario
print(diziocompleto)



### facciamo una funzione che fa questa operazione:
def unisci_dizionari(diz1, diz2):
    # Creiamo un nuovo dizionario combinando i due
    dizionario_unito = diz1.copy()  # Partiamo con una copia del primo
    dizionario_unito.update(diz2)   # Aggiungiamo il secondo
    return dizionario_unito

    # Proviamo la funzione
dizio1 = {1: 'ciao', 2: 'amore'}
dizio2 = {3: 'macchè', 4: 'ahah'}

risultato = unisci_dizionari(dizio1, dizio2)
print(risultato)




###
# ATTENZIONE!!
# se ci fossero chiavi duplicate?
# Un aspetto importante da considerare è cosa succede se ci sono chiavi duplicate. Per esempio:


dizio1 = {1: 'ciao', 2: 'amore'}
dizio2 = {2: 'tesoro', 3: 'macchè'}  # Nota che '2' è presente in entrambi

# Il valore del secondo dizionario sovrascriverà quello del primo
diziocompleto = dizio1 | dizio2
print(diziocompleto)  # {1: 'ciao', 2: 'tesoro', 3: 'macchè'}







#Se vuoi gestire le chiavi duplicate in modo diverso, potresti creare una funzione personalizzata


def unisci_dizionari_sicuro(diz1, diz2):
    risultato = {}
    # Aggiungiamo tutti gli elementi del primo dizionario
    for chiave, valore in diz1.items():
        risultato[chiave] = valore
    
    # Aggiungiamo gli elementi del secondo dizionario
    # controllando se la chiave esiste già
    for chiave, valore in diz2.items():
        if chiave in risultato:
            print(f"Attenzione: la chiave {chiave} esiste già!")
            # Qui puoi decidere cosa fare in caso di duplicati
        risultato[chiave] = valore
    
    return risultato




def unisci_dizionari_smart(diz1, diz2, gestione_duplicati='mantieni_primo'):
    """
    Unisce due dizionari gestendo i duplicati in modi diversi.
    
    Parametri:
    - diz1, diz2: i dizionari da unire
    - gestione_duplicati: come gestire le chiavi duplicate
        'mantieni_primo': mantiene il valore del primo dizionario
        'mantieni_secondo': mantiene il valore del secondo dizionario
        'combina': crea una lista con entrambi i valori
    """
    risultato = diz1.copy()  # Partiamo con una copia del primo dizionario
    
    for chiave, valore in diz2.items():
        if chiave in risultato:
            # Abbiamo trovato una chiave duplicata
            if gestione_duplicati == 'mantieni_primo':
                print(f"Chiave duplicata '{chiave}': mantengo il valore '{risultato[chiave]}'")
                continue
            elif gestione_duplicati == 'mantieni_secondo':
                print(f"Chiave duplicata '{chiave}': sostituisco con '{valore}'")
                risultato[chiave] = valore
            elif gestione_duplicati == 'combina':
                print(f"Chiave duplicata '{chiave}': combino i valori")
                # Se non è già una lista, creiamo una lista con il valore esistente
                if not isinstance(risultato[chiave], list):
                    risultato[chiave] = [risultato[chiave]]
                # Aggiungiamo il nuovo valore
                risultato[chiave].append(valore)
        else:
            # Chiave nuova, la aggiungiamo semplicemente
            risultato[chiave] = valore
    
    return risultato

# Proviamo con alcuni esempi
prodotti1 = {'mela': 1.0, 'pera': 1.5, 'banana': 0.8}
prodotti2 = {'mela': 1.2, 'arancia': 1.3, 'banana': 0.9}

print("Esempio 1: Manteniamo i prezzi del primo negozio")
risultato1 = unisci_dizionari_smart(prodotti1, prodotti2, 'mantieni_primo')
print(risultato1)

print("\nEsempio 2: Prendiamo i prezzi più recenti (secondo negozio)")
risultato2 = unisci_dizionari_smart(prodotti1, prodotti2, 'mantieni_secondo')
print(risultato2)

print("\nEsempio 3: Manteniamo tutti i prezzi in una lista")
risultato3 = unisci_dizionari_smart(prodotti1, prodotti2, 'combina')
print(risultato3)



#Questo codice mostra tre strategie diverse per gestire i duplicati:

#Mantenere il primo valore incontrato (utile quando vogliamo dare priorità ai dati originali)
#Usare il secondo valore (utile quando vogliamo i dati più recenti)
#Combinare i valori in una lista (utile quando vogliamo mantenere tutta l'informazione)

#Per valori duplicati invece delle chiavi, potremmo creare una funzione che cerca per valore:



def trova_per_valore(dizionario, valore_cercato):
    """
    Trova tutte le chiavi che hanno un certo valore
    """
    risultato = []
    for chiave, valore in dizionario.items():
        if valore == valore_cercato:
            risultato.append(chiave)
    return risultato

# Esempio di uso
prezzi = {'mela': 1.0, 'pera': 1.0, 'banana': 0.8, 'arancia': 1.0}
prezzo_comune = 1.0
prodotti_stesso_prezzo = trova_per_valore(prezzi, prezzo_comune)
print(f"Prodotti che costano {prezzo_comune}:", prodotti_stesso_prezzo)










#es. 9
# Crea un Dizionario con i Voti
#Crea un dizionario che memorizza i voti di diversi studenti.

# Dizionario con voti di studenti
voti = {
    "Alice": 28,
    "Bob": 25,
    "Carla": 30,
    "Dario": 27
}

print(voti)







#es.10
# Ordina un Dizionario
#Ordina un dizionario per chiave.


# Dizionario da ordinare
dizionario = {
    "banana": 2,
    "mela": 5,
    "arancia": 3
}

# Ordina il dizionario per chiave
dizionario_ordinato = dict(sorted(dizionario.items()))

print(dizionario_ordinato)



#esercizio 10 plus:
#fai una funzione del dizionario ordinato per chiave
def dizionario_ordinato(dizionario):
    return dict(sorted(dizionario.items()))

# Esempio di utilizzo
dizionario = {
    "banana": 2,
    "mela": 5,
    "arancia": 3
}

dizionario_ordinato = dizionario_ordinato(dizionario)
print(dizionario_ordinato)



###
# dizionario che ordina le chiavi in senso decrescente

def dizionario_ordinato_reverse(dizionario):
    return dict(sorted(dizionario.items(), reverse=True))

# Esempio di utilizzo
dizionario = {
    "banana": 2,
    "mela": 5,
    "arancia": 3
}

dizionario_ordinato = dizionario_ordinato_reverse(dizionario)
print(dizionario_ordinato)









####Ordinare un Dizionario per Valori
##
# Per ordinare un dizionario in base ai valori, puoi usare una lambda function come chiave di ordinamento.
###
def dizionario_ordinato_per_valori(dizionario):
    return dict(sorted(dizionario.items(), key=lambda item: item[1]))

# Esempio di utilizzo
dizionario = {
    "banana": 2,
    "mela": 5,
    "arancia": 3
}

dizionario_ordinato = dizionario_ordinato_per_valori(dizionario)
print(dizionario_ordinato)



###Ordinare un Dizionario per Chiavi in Ordine Decrescente (Reverse)
##Per ordinare un dizionario per chiavi in ordine decrescente, puoi utilizzare il parametro reverse=True nella funzione sorted(). Ecco come fare:


def dizionario_ordinato_reverse(dizionario):
    return dict(sorted(dizionario.items(), reverse=True))

# Esempio di utilizzo
dizionario = {
    "banana": 2,
    "mela": 5,
    "arancia": 3
}

dizionario_ordinato = dizionario_ordinato_reverse(dizionario)
print(dizionario_ordinato)




##Ordinare un Dizionario per Valori
##Per ordinare un dizionario in base ai valori, puoi usare una lambda function come chiave di ordinamento. Ecco un esempio:


def dizionario_ordinato_per_valori(dizionario):
    return dict(sorted(dizionario.items(), key=lambda item: item[1]))

# Esempio di utilizzo
dizionario = {
    "banana": 2,
    "mela": 5,
    "arancia": 3
}

dizionario_ordinato = dizionario_ordinato_per_valori(dizionario)
print(dizionario_ordinato)




####
####Ordinare un Dizionario per Valori in Ordine Decrescente
####Se vuoi ordinare un dizionario per valori in ordine decrescente, puoi combinare la lambda function con reverse=True
###

def dizionario_ordinato_per_valori_reverse(dizionario):
    return dict(sorted(dizionario.items(), key=lambda item: item[1], reverse=True))

# Esempio di utilizzo
dizionario = {
    "banana": 2,
    "mela": 5,
    "arancia": 3
}

dizionario_ordinato = dizionario_ordinato_per_valori_reverse(dizionario)
print(dizionario_ordinato)






####
###
### più semplice:

# Funzione che restituisce il valore di un elemento del dizionario
def get_value(item):
    return item[1]

# Funzione che ordina un dizionario per valori
def dizionario_ordinato_per_valori(dizionario):
    return dict(sorted(dizionario.items(), key=get_value))

# Esempio di utilizzo
dizionario = {
    "banana": 2,
    "mela": 5,
    "arancia": 3
}

dizionario_ordinato = dizionario_ordinato_per_valori(dizionario)
print(dizionario_ordinato)







#Passaggio 1: Definire una Funzione di Ordinamento
#La funzione get_value prende un elemento del dizionario (una coppia chiave-valore) e restituisce il valore.

#Passaggio 2: Creare la Funzione che Ordina il Dizionario
#La funzione dizionario_ordinato_per_valori ordina il dizionario in base ai valori utilizzando get_value.