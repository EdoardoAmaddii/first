
# Esercizio 7: Iterazione su una Lista:
# Usa un ciclo for per iterare su una lista di nomi e stampare ciascuno.


inputnomi = input('due nomi che ti piacciono:\n')

nomi = inputnomi.replace(",", "")
listanomi = []
for x in nomi.split():
    listanomi.append(x.lower().capitalize())

print(f'Lista nomi: {listanomi}')

# così organizzi la stampa in un loop

for nome in listanomi:
    print(nome)










# Esercizio 7: Iterazione su una Lista: Uso di una list comprehension
# Usa un ciclo for per iterare su una lista di nomi e stampare ciascuno.

inputnomi = input("Inserisci nomi che ti piacciono separati da uno spazio o una virgola:\n")

# Rimuove eventuali virgole e crea una lista di nomi in maiuscolo
listanomi = [nome.strip().upper() for nome in inputnomi.replace(",", " ").split()]

# Stampa la lista dei nomi
print(f"Lista nomi: {listanomi}") 

# Itera sulla lista per stampare ogni nome
for nome in listanomi:
    print(nome)












#### esercizio 8 ####
print('\n\n\nESERCIZIO 8\n\n\n')



#  Raccogli i Numeri Positivi
## Usa un ciclo for per raccogliere tutti i numeri positivi da una lista e restituirli.

numeripos = input('dammi numeri, ti ridarò i positivi: ')
numeri = numeripos.split()

listanum = []
for x in numeri:
    listanum.append(float(x))

print(listanum) #debug

for x in listanum:
    if x > 0:
        print(x)


#Cosa migliorare:

#Il programma stampa listanum, che include tutti i numeri, positivi e negativi. Questo step è inutile, a meno che non ti serva per debug.
#Non c'è bisogno di creare due cicli for. Puoi combinare i due cicli in uno.
#Non restituisci i numeri positivi come lista. Se un utente volesse usarli, non potrebbe.


#esercizio 8 con AI : list comprehension
#Usato list comprehension per creare direttamente numeri e numeri_positivi.
#Eliminato cicli ridondanti e reso il codice più leggibile.

numeripos = input('Dammi numeri, ti restituirò i positivi: ')
numeri = [float(x) for x in numeripos.split()]  # List comprehension per convertire direttamente

numeri_positivi = [x for x in numeri if x > 0]  # Filtra i numeri positivi

print(f"Numeri positivi: {numeri_positivi}")




















###esercizio 9###

print('\n\n ESERCIZIO 9\n\n')

# Conta le lettere in una stringa
stringa = 'scalawais '
print(len(stringa)) #debug
sololettere = stringa.strip()
print(len(sololettere))


## Non è chiaro il tuo obiettivo: vuoi contare tutte le lettere escludendo spazi, o solo la lunghezza della stringa senza spazi vuoti?

##Ecco due approcci a seconda dell'obiettivo:

##Contare tutte le lettere escludendo gli spazi

###     no1  ## 
# Contare tutte le lettere escludendo gli spazi:

stringa = 'scalawais '
sololettere = stringa.replace(" ", "")  # Rimuovi tutti gli spazi
print(f"Numero di lettere: {len(sololettere)}")



#### no2 ###
# Contare la lunghezza della stringa senza spazi iniziali/finali

stringa = 'scalawais '
sololettere = stringa.strip()  # Rimuove solo spazi iniziali e finali
print(f"Lunghezza senza spazi iniziali/finali: {len(sololettere)}")











### esercizio 10###
print('\n\n\n ESRCIZIO 10')
# Contare Parole in una Stringa
# Usa un ciclo for per contare il numero di parole in una stringa.
string = 'La scala WAIS'
parole = string.split()  # Divide la stringa in una lista di parole
print(f"Numero di parole: {len(parole)}")

# Stampare anche ogni parola (se necessario):
for parola in parole:
    print(parola)



# così conto quante lettere ci sono in ciascuna parola
string = 'La scala WAIS'
for x in string.split():
     print(len(x)) #len di x ci dà il numero di lettere di ciascuna parola







