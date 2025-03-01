#Sezione 5: Stringhe (Esercizi 41-50)

#es.1 
# Accedi a un Carattere in una Stringa
#Estrai il primo e l'ultimo carattere di una stringa.

stringa = 'phi ed edo.'
primo = stringa[0]
ultimo = stringa [-1]
if stringa.endswith('.'):
    ultimo = stringa [-2]
    print(f'quesa string aveva un punto in fondo: {primo, ultimo}')
else:
    print(primo, ultimo)

# es. 2
# Modifica una Stringa
# Usa il metodo replace() per sostituire una parola in una stringa.

string = 'phi ed edo'
coppia = string.replace('phi', 'Als')
print (coppia)


# es. 3
# Verifica la Lunghezza della Stringa
# Scrivi un programma che verifica se una stringa ha una lunghezza pari o dispari.

stringaa = 'phi ed edo'
if len(stringaa) % 2 == 0:
    print(f'la stringa è lunga {len(stringaa)}: pari')
else:
    print(f'la stringa è lunga {len(stringaa)}: dispari')


# possiamo avere un'output più chiaro così

stringaa = 'phi ed ed'
lunghezza = len(stringaa)
if lunghezza % 2 == 0:
    print(f"La stringa è lunga {lunghezza}: pari.")
else:
    print(f"La stringa è lunga {lunghezza}: dispari.")




# es.4 Trova una Parola in una Stringa
# Usa in per verificare se una parola è presente in una stringa.


string = 'phi ed edo'
if 'phi' in string:
    print('yabadoo')
else:
    print('nope')


print('\n\n')
# es. 5 
# Stringa in Maiuscolo
# Converte una stringa in maiuscolo.

stringa = 'phi ed edo'
maiuscola = stringa.upper()
print(maiuscola)




print('\n\n\n')








# es. 6
#Palindromi
#Scrivi una funzione che verifica se una stringa è un palindromo.


def verifica_palindromo(stringa):
    stringa_invertita = stringa[::-1]  # Usa slicing per invertire la stringa
    if stringa == stringa_invertita:
        return True  # È un palindromo
    else:
        return False  # Non è un palindromo
# Test
string = 'ottagatto'
if verifica_palindromo(string):
    print(f"'{string}' è un palindromo.")
else:
    print(f"'{string}' non è un palindromo.")



# così con una lista invertita
def verifica_palindromo(stringa):
    lista_caratteri = list(stringa)  # Trasforma la stringa in una lista di caratteri
    lista_caratteri_invertita = lista_caratteri[:]  # Copia la lista
    lista_caratteri_invertita.reverse()  # Usa il metodo reverse() per invertirla
    return lista_caratteri == lista_caratteri_invertita  # Confronta le due liste

# Test
string = 'radar'
if verifica_palindromo(string):
    print(f"'{string}' è un palindromo.")
else:
    print(f"'{string}' non è un palindromo.")







##
# così con una listcomprehension

def verifica_palindromo(stringa):
    # La funzione restituisce True se tutti i caratteri della prima metà della stringa
    # corrispondono ai caratteri della seconda metà (in ordine inverso).

    # `all()` è una funzione che verifica se tutti gli elementi di un iterabile (come una lista o un generatore) sono True.
    # Qui usiamo una comprehension per generare un confronto tra caratteri della stringa.

    # La comprehension genera una sequenza di confronti:
    # `stringa[i] == stringa[-i - 1]` controlla se il carattere nella posizione `i`
    # (dalla sinistra) è uguale al carattere nella posizione `-i - 1` (dalla destra).
    # Questo confronto avviene per tutti i caratteri della prima metà della stringa.

    # `range(len(stringa) // 2)` crea un intervallo che itera solo sui primi metà caratteri.
    # Non serve confrontare tutta la stringa perché il palindromo è simmetrico.

    return all(stringa[i] == stringa[-i - 1] for i in range(len(stringa) // 2))

    ##Spiegazione del codice passo passo:
        #all()

        #La funzione all() restituisce True solo se tutti gli elementi del generatore/comprensione che le passiamo sono True.
        #Qui ci aiuta a verificare in un colpo solo che tutti i caratteri a sinistra e a destra coincidano.

    
       # Questo è un generatore che confronta i caratteri della stringa:
       # stringa[i] è il carattere nella posizione i, partendo da sinistra.
       # stringa[-i - 1] è il carattere nella posizione corrispondente da destra.
       # Confrontiamo solo la prima metà della stringa, perché se la prima metà corrisponde alla seconda metà, sappiamo già che è un palindromo.
       # range(len(stringa) // 2)

       #[] La funzione range() produce un intervallo da 0 fino alla lunghezza della metà della stringa (len(stringa) // 2).
       # Ad esempio, se la stringa è lunga 6, range(6 // 2) diventa range(3) e genera 0, 1, 2.
       # Restituisce il risultato

       # Se tutti i confronti (stringa[i] == stringa[-i - 1]) sono veri, la funzione all() restituisce True, e la funzione conferma che la stringa è un palindromo.
       # Se anche uno solo dei confronti fallisce, all() restituisce False


# Test della funzione
string = 'anna'  # Proviamo con una stringa palindroma
if verifica_palindromo(string):
    print(f"'{string}' è un palindromo.")
else:
    print(f"'{string}' non è un palindromo.")


#Vantaggi:
#Compattezza e leggibilità per chi ha familiarità con Python.
#Non utilizza slicing o reverse direttamente, ma il confronto è altrettanto efficace.
#È efficiente perché confronta solo metà della stringa.








# es.7
# Estrazione Sottostringa
# Estrai una sottostringa da una stringa con un certo indice.

stringa = 'phi ed edo'
lettera = stringa[3]
if lettera == ' ':
    print('ti è andata male')
else:
    print(lettera)

# es.8
# Rimuovi Spazi dalla Stringa
# Rimuovi gli spazi all'inizio e alla fine di una stringa.

string = '  phi e edo  '
strippata = string.strip()
print(strippata)

# es.9
#Conta le Occorrenze di una Parola
#Conta quante volte una parola appare in una stringa.

stringaaa = 'phi ed ed'
count = 0
stringss = stringaaa.split()

for parola in stringss:
    if parola == parola:
        count += 1
        print(parola, count)
    
# non hai fatto ciò che richiede l'esercizio: così hai contato le parole una accanto all'altra, in ordine

# Conta le Occorrenze di una Parola
stringaaa = 'phi ed ed'
parola_da_cercare = 'ed'  # Definisci la parola da contare
count = 0

stringss = stringaaa.split()

for parola in stringss:
    if parola == parola_da_cercare:  # Confronta con la parola target
        count += 1

print(f"La parola '{parola_da_cercare}' appare {count} volte nella stringa.")



####
#### chiediamo all'utente quale parola vuole cercare
####

stringaaa = 'phi ed edo ed phi'
parola_da_cercare = input('quale parola vuoi contare?')  # l'utente definisce la parola da contare
count = 0

stringss = stringaaa.lower().split()

for parola in stringss:
    if parola == parola_da_cercare.lower():  # Confronta con la parola target, .lower per evitare problemi
        count += 1

print(f"La parola '{parola_da_cercare}' appare {count} volte nella stringa.")





#es.10
# Verifica Anagramma
# Crea una funzione che verifica se due stringhe sono anagrammi.

### questo è l'esercizio 10
print('\n\n ESERCIZIO 10\n\n')

def anagrammi(parola, parola2):
    # Controlla se le due parole hanno la stessa lunghezza
    if len(parola) != len(parola2):
        return print("Non sono anagrammi: lunghezza diversa")
    
    # Ordina i caratteri di entrambe le parole e confrontali
    if sorted(parola) == sorted(parola2):
        return print("Le parole sono anagrammi")
    else:
        return print("Non sono anagrammi")
        
# Test della funzione
anagrammi('lettera', 'lettear')  # Output: Le parole sono anagrammi
anagrammi('python', 'java')      # Output: Non sono anagrammi




####
# Se vuoi evitare di ordinare le stringhe, puoi utilizzare un contatore di caratteri con il modulo collections:


from collections import Counter

def anagrammi(parola, parola2):
    # Confronta i contatori di caratteri delle due stringhe
    if Counter(parola) == Counter(parola2):
        print("Le parole sono anagrammi")
    else:
        print("Non sono anagrammi")

# Test della funzione
anagrammi('lettera', 'lettear')  # Output: Le parole sono anagrammi
anagrammi('python', 'java')      # Output: Non sono anagrammi













#### ESERCIZIO FINALE
print('\n\n ESERCIZIO FINALE \n\n')
#Scrivi una funzione che riceve due stringhe e svolge le seguenti operazioni:

#Controlla se le due stringhe sono anagrammi.
#Verifica se ciascuna stringa è un palindromo.
#Restituisce un dizionario con queste informazioni:
#Se sono anagrammi.
#Se la prima stringa è un palindromo.
#Se la seconda stringa è un palindromo.

def anagrammipalindromi (parola1, parola2):
    if len(parola1) != len(parola2):
        print('le parole hanno lunghezza diversa e non sono perciò anagrammi')

    else:
        if sorted(parola1) == sorted(parola2):
            print('le parole sono anagrammi')

        else:
            print('le parole non sono anagrammi')

    stringa_invertita = parola1[::-1], parola2[::-1]  # Usa slicing per invertire la stringa
    if parola1 or parola2 == stringa_invertita:
        return print('è palindromo')  # È un palindromo
    else:
        return print('non è un palindromo') # Non è un palindromo
    
anagrammipalindromi ('anna', 'otto')






######
### questo il codice corretto e completo!

def anagrammipalindromi(parola1, parola2):
    risultato = {
        "anagrammi": False,
        "palindromo_parola1": False,
        "palindromo_parola2": False
    }
    
    # Controlla se sono anagrammi
    if len(parola1) == len(parola2) and sorted(parola1) == sorted(parola2):
        risultato["anagrammi"] = True

    # Controlla se parola1 è un palindromo
    if parola1 == parola1[::-1]:
        risultato["palindromo_parola1"] = True

    # Controlla se parola2 è un palindromo
    if parola2 == parola2[::-1]:
        risultato["palindromo_parola2"] = True

    return risultato

# Esempio di utilizzo
risultato = anagrammipalindromi('anna', 'otto')
print(risultato)









##
# domani reiniziamo da questo in cui c'è lo stesso criterio, ma viene chiesto all'utente di inserire una parolaz



