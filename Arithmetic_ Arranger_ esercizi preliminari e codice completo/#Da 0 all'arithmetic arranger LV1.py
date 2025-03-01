#Da 0 all'arithmetic arranger


# 1 assegna e stampa variabile:
cinque = 5
print(cinque)

# 2 Crea variabili di tipo int, float, string e bool e stampale.

        #puoi convertire solo numeri, anche se in una stringa... NO LISTE!
cinque = float('56')
print(cinque)

        #Create a new string object from the given object. 
        # #If encoding or errors is specified, then the object must expose a data buffer that will be decoded using the given encoding and error handler. Otherwise, returns the result of object.__str__() (if defined) or repr(object). encoding defaults to 'utf-8'. errors defaults to 'strict'.
sette = str(7)
print(sette)
print(type(sette)) #<class 'str'>

        #Returns True when the argument is true, False otherwise. 
        # The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.
nove = False
print(nove)

        #utilizzo con variabili
x = 5
y = 7
per_davide = y < x
per_me = x == y
per_ali = y > x

print(f'\nPer Davide: {per_davide}\nPer Me: {per_me}\nPer Ali: {per_ali}')

        
        
        # Variabili booleani in base a espressioni logiche
x = 10
y = 20

is_x_less_than_y_and_even = (x < y) and (x % 2 == 0)  # True, perché x è minore di y e x è pari
print("\nx è minore di y e pari?", is_x_less_than_y_and_even)


##Le variabili bool possono essere costruite usando:
#Confronti tra valori (==, >, <, >=, <=, !=)
#Espressioni logiche (and, or, not)

#Le variabili bool sono spesso utilizzate in strutture di controllo come if
    
        #in formula condizionale

# Variabili booleane in una condizione

is_raining = False

if is_raining:
    print("\nPrendi l'ombrello!")
else:
    print("\nÈ una bella giornata!")



        #variabili booleane con input
is_raining = input('\nTrue or False?\n')

if is_raining == 'True':
    print("\nPrendi l'ombrello!")
elif is_raining == 'False':
    print("\nÈ una bella giornata!")
else:
    print('True or False, nothing else')
    #raise/return SyntaxError()


    # Variabili booleane con input
is_raining = input('\nTrue or False?\n').lower() == 'true'

if is_raining:
    print("\nPrendi l'ombrello!")
else:
    print("\nÈ una bella giornata!")




print('\n\n\n\n\n')

# 3 Somma due variabili numeriche e stampa il risultato.
x = 5+2
print(x)

# 4 Modifica una variabile e stampa il nuovo valore.
y = x + 5
print(y)

# 5 Concatenazione stringhe
saluto = 'ciao'
chi = 'studente'
print(f'\n{saluto + chi}')

# 6 Intercambia i valori di due variabili e stampa il risultato.

# Esempio con numeri
a = 5
b = 10
print(f"\n\nPrima dello scambio: a = {a}, b = {b}")

temp = a  # variabile temporanea
a = b
b = temp

print(f"\nDopo lo scambio: a = {a}, b = {b}")



# Esempio con stringhe \ metodo Pythonic (packing/unpacking)
nome = "Mario"
cognome = "Rossi"
print(f"\n\nPrima dello scambio: nome = {nome}, cognome = {cognome}")

nome, cognome = cognome, nome  # scambio diretto

print(f"\nDopo lo scambio: nome = {nome}, cognome = {cognome}")



#esempio solo con numeri
x = 15
y = 30
print(f"\n\nPrima dello scambio: x = {x}, y = {y}")

x = x + y  # x ora contiene la somma
y = x - y  # y ora contiene il valore originale di x
x = x - y  # x ora contiene il valore originale di y

print(f"Dopo lo scambio: x = {x}, y = {y}")



#esempio che chiede input all'utente

# Chiediamo due valori all'utente
valore1 = input("\n\nInserisci il primo valore: ")
valore2 = input("Inserisci il secondo valore: ")

print(f"\nValori originali:")
print(f"Primo valore: {valore1}")
print(f"Secondo valore: {valore2}")

# Scambio i valori
valore1, valore2 = valore2, valore1

print(f"\nValori dopo lo scambio:")
print(f"Primo valore: {valore1}")
print(f"Secondo valore: {valore2}")






print('\n\n\n\n\n')



# 7 Usa la funzione round() per arrotondare un numero.

virgola = 56.667
arrotondato = round(virgola)
print(f'\n{arrotondato}')



# 8 Converti una variabile in un altro tipo (ad esempio, da int a str).

delta = 3
stringa = str(delta)
print (stringa, type(stringa))

# Conversione da float a int (tronca i decimali)
prezzo = 23.95
prezzo_intero = int(prezzo)
print(f"Float convertito in intero: {prezzo_intero}, tipo: {type(prezzo_intero)}")


# Richiesta anno di nascita come stringa e conversione per calcoli
anno_nascita = input("In che anno sei nato? ")
anno_corrente = 2024

        # Convertiamo l'input in intero per fare il calcolo
eta = anno_corrente - int(anno_nascita)
print(f"La tua età è: {eta} anni")

        # Riconvertiamo in stringa per concatenare con altro testo
messaggio = "Hai " + str(eta) + " anni!"
print(messaggio)







#Alcuni punti importanti da ricordare:

#La conversione può generare errori se il valore non è convertibile nel tipo desiderato
#Quando si converte da float a int, i decimali vengono troncati (non arrotondati)
#La conversione in bool ha alcune particolarità: stringhe vuote, zero, e None diventano False, mentre quasi tutto il resto diventa True
#È sempre buona pratica gestire possibili errori di conversione con try/except#

# esempio Per gestire gli errori di conversione in modo sicuro:



def converti_sicuro(valore, tipo_destinazione):
    try:
        return tipo_destinazione(valore)
    except ValueError:
        print(f"Errore: Impossibile convertire '{valore}' in {tipo_destinazione.__name__}")
        return None

            # Esempio di utilizzo
input_utente = input("Inserisci un numero: ")
numero = converti_sicuro(input_utente, int)
if numero is not None:
    print(f"Conversione riuscita: {numero}")








#esercizio mio
# Scrivi un programma che chieda all'utente un numero come stringa
# e stampi il suo doppio come numero intero
# Esempio output: "Il doppio del tuo numero è: 10"

# La tua soluzione qui...

try: 
    numeroutente = input('Dammi un numero: \n')
    numeroconvert = int(numeroutente)
    risultato = numeroconvert * 2
    print(f'Questo è il doppio del tuo numero {risultato}')

except ValueError:
    print('Ti ho detto un numero, non delle lettere')




#CALCOLATORE DI SCONTI

# 1. Chiede il prezzo di un prodotto (può essere decimale)
# 2. Chiede la percentuale di sconto (numero intero)
# 3. Calcola e mostra:
#    - Il prezzo originale
#    - Lo sconto in euro
#    - Il prezzo finale
# 4. Deve gestire gli errori di input
# 5. I risultati devono essere formattati con due decimali

# Esempio di output atteso:
# Prezzo originale: €24.99
# Sconto (20%): €5.00
# Prezzo finale: €19.99


try:
    prezzoutente = input('quanto costa il prodotto?\n')
    scontoutente = input('quanto è la percentuale di sconto applicato?\n')

    prezzo = float(prezzoutente)
    sconto = int(scontoutente)
    euroscontati = (prezzo * sconto) / 100
    prezzo_finale = prezzo - euroscontati

    print(f'Prezzo_originale: {float(prezzo)}\nPrezzo_finale:{float(prezzo_finale)}\nEuro_scontati:{sconto}% {float(euroscontati)}')

except ValueError:
    print('perchè scrivi cose che non hanno senso?')

