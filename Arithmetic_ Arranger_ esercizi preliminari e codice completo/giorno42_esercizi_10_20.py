# Crea un’espressione booleana per verificare se un numero è maggiore di 10.
#Usa anche and per combinare due condizioni.
x = 3 
y = 7
if x < 10 and y > 5 :
    print('yessa')
else: 
    print('nope')

# Verifica se un numero è pari usando un’espressione booleana.

x = 4003
if x % 2 == 0:
    print('pari')
else:
    print('dispari')

# Verifica Anagrammi
# Confronta due stringhe per determinare se sono anagrammi.     
           # La funzione sorted() restituisce una lista ordinata delle lettere di una stringa.
edo = 'hello'
ode = 'world'

if sorted(edo) == sorted(ode):
    print('yep')
else:
    print('gnao')


# Usa or per controllare se un numero è pari o dispari.

x = 8
if x%2 == 0 or x%2 != 0:
    print('il numero è pari o dispari')
else:
    raise ValueError

# 16 Condizione Inversa
#Usa l’operatore not per invertire una condizione booleana.

#16.1
x = True
print(not x) 

#16.2
numero = 10
if not numero > 5:
    print("Il numero non è maggiore di 5.")
else:
    print("Il numero è maggiore di 5.")  # Output

#16.3
stringa = ""
if not stringa:
    print("La stringa è vuota.")  # Output
else:
    print("La stringa non è vuota.")

    ##In Python, una stringa vuota è valutata come False. not stringa diventa True se la stringa è vuota.


#16.4
lista = []
if not lista:
    print("La lista è vuota.")  # Output
else:
    print("La lista contiene elementi.")



#16.5
x = 10
y = 5
if not (x > 5 and y < 3):
    print("La condizione combinata non è vera.")  # Output
else:
    print("La condizione combinata è vera.")

# Spiegazione: L'operatore not inverte l'intera espressione (x > 5 and y < 3).




#16.6
#negara l'appartenenza ad un inseme
parola = "ciao"
vocali = "aeiou"
if not parola[0] in vocali:
    print(f"La prima lettera di '{parola}' non è una vocale.")  # Output
else:
    print(f"La prima lettera di '{parola}' è una vocale.")


#16.7
#applicazione complessa: validazione di input

utente = input("Inserisci il tuo nome (almeno 3 caratteri): ")
if not utente or len(utente) < 3:
    print("Nome non valido!")
else:
    print(f"Benvenuto, {utente}!")


#16.8
#invertire condizioni in funzioni

def è_pari(numero):
    return numero % 2 == 0

numero = 7
if not è_pari(numero):
    print(f"{numero} è dispari.")  # Output
else:
    print(f"{numero} è pari.")

##Spiegazione: La funzione è_pari restituisce True per numeri pari. not è_pari(numero) verifica se un numero non è pari.





#16.9
#negare un'espressione con generatori

numeri = [1, 2, 3, 4, 5]
if not all(n > 0 for n in numeri):
    print("Non tutti i numeri sono positivi.")
else:
    print("Tutti i numeri sono positivi.")  # Output

##Spiegazione: all restituisce True se tutti gli elementi della lista soddisfano la condizione. not all(...) verifica se almeno uno non la soddisfa.


#16.10
#caso avanzato, controllo su dizionari

utenti = {"utente1": "attivo", "utente2": "disattivo"}
if not any(stato == "attivo" for stato in utenti.values()):
    print("Nessun utente è attivo.")
else:
    print("Almeno un utente è attivo.")  # Output

#Spiegazione: any restituisce True se almeno uno degli utenti è attivo. not any(...) inverte questa condizione.




#17 
# Scrivi un'espressione booleana per verificare se un numero è positivo o negativo.

x = -4
if x > 0:
    print('positivo')

else:
    print('negativo')




#18
# Usa l'operatore modulo (%) per verificare se un numero è divisibile per 3.

x = 6
if x % 3 == 0:
    print('siu')
else:
    print('nonee')




#19
# Controllo di Voto Sufficiente
# Usa una condizione booleana per verificare se un voto è sufficiente (>= 6).

try:
        
    inputvoto = input('che voto hai preso?\n')
    voto = float(inputvoto)
    if voto >= 6:
        print('te la sei scampata')
    else:
        print('che dici, studiamo?')

except ValueError:
    print('inserisci un voto, non una stringa.. se non sai cosa è una stringa, vallo a riguardare')



#20 
# Verifica Parole con la stessa Lunghezza
# Usa una condizione booleana per verificare se due stringhe hanno la stessa lunghezza.

x = 'ciao'
y = 'mare'
if len(x) == len(y):
    print('si')
else:
    print('no')