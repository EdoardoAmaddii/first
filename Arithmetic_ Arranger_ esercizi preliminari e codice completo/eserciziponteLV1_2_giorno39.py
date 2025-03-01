#esercizi ponte LV1-2

# Crea un programma che:
# 1. Chiede all'utente di inserire 3 voti (da 0 a 10)
# 2. Calcola:
#    - La media dei voti
#    - Se tutti i voti sono sufficienti (>= 6)
#    - Se almeno un voto è insufficiente (< 6)
#    - Il voto più alto e più basso
# 3. Stampa un messaggio finale che indica se lo studente è promosso 
#    (media >= 6 e nessun voto sotto il 4)

#votistudente = input('Inserisci 3 voti tra 0 e 10:\n')

#for voto in votistudente:
#    voti = votistudente.split()
#    votidacalcolare=float(voti)


#    mediavoti = sum(voti)/3
#    print(mediavoti)


 #   votomassimo = max(voti)
 #   print(votomassimo)
 #   votominimo = min(voti)
 #   print(votominimo)



#    if voto >= 6:
#        print('Tutti sufficienti')
    
#    if voto < 6:
#        print(f'hai {len(voto<6)} insufficienza da recuperare')
#    if mediavoti >=6 and voto > 4:
#        print('SEI PROMOSSO! media >= 6 e nessun voto sotto il 4')

#else:
#    print('Spiaze, sei BOCCIATO')

#except ValueError:
#    print('Devi inserire voti tra 0 e 10 seguiti da uno spazio')







#hai provato a fare una cosa al di sopra delle tue competenze fin'ora, ci torniamo stasera per chiudere l'esercizio



#crea un sistema di voti:
print('dovrai inserire tre voti per calcolare la media e sapere se sei promosso\n')
try:
    voto1 = input('primo voto: ')
    voto2 = input('secondo voto: ')
    voto3 = input('terzo voto: ')

    # calcola
    primo = float(voto1)
    secondo = float(voto2)
    terzo = float(voto3)

    listavoti = [primo, secondo, terzo]

    mediavoti = sum(listavoti) / len(listavoti)
    print(mediavoti)

    votomassimo = max(listavoti)
    print(votomassimo)

    votominimo = min(listavoti)
    print(votominimo)

    if primo >= 6 and secondo >=6  and terzo >=6: 
        print('Tutti sufficienti')
    else: 
        print('hai materie da recuperare')

    # Verifica promozione
    if mediavoti >= 6 and min(listavoti) > 4:
        print('SEI PROMOSSO! media >= 6 e nessun voto sotto il 4')
    else:
        print('Spiaze, verrai BOCCIATO con un 4')

except ValueError:
    print('Devi inserire voti tra 0 e 10, fai per bene..')






#questa è la versione migliorata con AI

# Programma che analizza i voti di uno studente

# Input: Chiedi all'utente di inserire 3 voti (tra 0 e 10)
voto1 = float(input("Inserisci il primo voto (0-10): "))
voto2 = float(input("Inserisci il secondo voto (0-10): "))
voto3 = float(input("Inserisci il terzo voto (0-10): "))

# Crea una lista dei voti
voti = [voto1, voto2, voto3]

# Calcoli richiesti
media_voti = sum(voti) / len(voti)  # Media dei voti
voto_massimo = max(voti)           # Voto più alto
voto_minimo = min(voti)            # Voto più basso
tutti_sufficienti = all(v >= 6 for v in voti)  # Tutti sufficienti
almeno_un_insufficiente = any(v < 6 for v in voti)  # Almeno un insufficiente

# Output dei risultati
print(f"Media voti: {media_voti:.2f}")
print(f"Voto massimo: {voto_massimo}")
print(f"Voto minimo: {voto_minimo}")

if tutti_sufficienti:
    print("Tutti i voti sono sufficienti.")
else:
    print("Ci sono voti insufficienti.")

# Verifica promozione
if media_voti >= 6 and voto_minimo > 4:
    print("Sei PROMOSSO! Media >= 6 e nessun voto sotto il 4.")
else:
    print("Spiacente, sei BOCCIATO.")








#questa è la versione del tuo codice migliorata con AI

print('Dovrai inserire tre voti per calcolare la media e sapere se sei promosso\n')

try:
    # Input voti
    voto1 = input('Primo voto: ')
    voto2 = input('Secondo voto: ')
    voto3 = input('Terzo voto: ')

    # Conversione in float
    primo = float(voto1)
    secondo = float(voto2)
    terzo = float(voto3)

    # Controllo range voti
    if not (0 <= primo <= 10 and 0 <= secondo <= 10 and 0 <= terzo <= 10):
        print("I voti devono essere compresi tra 0 e 10.")
        exit()

    # Calcoli
    voti = [primo, secondo, terzo]
    mediavoti = sum(voti) / len(voti)
    votomassimo = max(voti)
    votominimo = min(voti)

    # Risultati intermedi
    print(f"La media dei voti è: {mediavoti:.2f}")
    print(f"Il voto più alto è: {votomassimo}")
    print(f"Il voto più basso è: {votominimo}")

    # Verifica sufficienza
    if all(v >= 6 for v in voti):
        print('Tutti i voti sono sufficienti.')
    else:
        print('Ci sono materie da recuperare.')

    # Verifica promozione
    if mediavoti >= 6 and votominimo > 4:
        print('SEI PROMOSSO! Media >= 6 e nessun voto sotto il 4.')
    else:
        print('Spiacente, sei BOCCIATO.')

except ValueError:
    print('Devi inserire voti validi (numeri da 0 a 10).')
