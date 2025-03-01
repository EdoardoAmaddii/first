

#9️⃣ Creare un menu interattivo (Espansa)
#📌 Cosa fare:
#
#Crea un menu con più opzioni per gestire scale e accordi.



def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Mostra una scala")
        print("2. Mostra un accordo")
        print("3. Verifica una nota in una scala")
        print("4. Esci")

        scelta = input("Scegli un'opzione: ")    #qui ci vorrebbe try per accettare solo stringhe, o per essere più sicuri utilizzare proprio dei numeri convertendo il primo input in int

        if scelta == '1':
            chescala = input('quale scala vuoi vedere?\n(Maggiore, Minore Naturale)').strip().title()
            if chescala in scale:
                print(scale[chescala]) # mostra questa scala del dizionario

            else: #try-except anche qui
                print('la scala non è presente')
                

        elif scelta == '2':
            cheaccordo = input('che accordo vuoi vedere?').strip().title()
            if cheaccordo in accordi:
                print(accordi[cheaccordo])

            else:          #qui un try-xcept per vedere se l'accordo è scritto correttamente
                print('non è ancora presente questo accordo')
                

        elif scelta == '3':
            print('scopriamo se la nota appartiene ad una determinata scala')
            nota = input('inserisci una nota:\n').strip().capitalize()         #ci vorrebbe un try except per vedere se la nota inserita è corretta
            scalapernota = input('inserisci la scala su cui cercare la nota:\n')    # un try-except anche per la scala

            if scalapernota in scale:
                if nota in scale[scalapernota]:
                    print(f'la nota {nota} è nella scala {scalapernota}')
                else:
                    print('la nota non è presente in questa scala')

            else:
                print('non abbiamo questa scala')


        elif scelta == '4':
            print('Arrivederci')
            break
    
        

scale = {
    "Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Minore Naturale": ["Do", "Re", "Mib", "Fa", "Sol", "Lab", "Sib"],
    "Pentatonica Maggiore": ["Do", "Re", "Mi", "Sol", "La"],
    "Pentatonica Minore": ["Do", "Mib", "Fa", "Sol", "Sib"],
    "Blues": ["Do", "Mib", "Fa", "Fa#", "Sol", "Sib"]
}



accordi = {
    "Do Maggiore": ["Do", "Mi", "Sol"],
    "Do Minore": ["Do", "Mib", "Sol"],
    "Sol Settima": ["Sol", "Si", "Re", "Fa"],
    "La Minore": ["La", "Do", "Mi"],
    "Re Maggiore": ["Re", "Fa#", "La"]
}

menu()









#####
# Codice corretto e migliorato

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Mostra una scala")
        print("2. Mostra un accordo")
        print("3. Verifica una nota in una scala")
        print("4. Esci")

        scelta = input("Scegli un'opzione (1-4): ").strip()

        # Verifica che l'input sia un numero valido
        if not scelta.isdigit() or int(scelta) not in range(1, 5):
            print("⚠️ Errore: Inserisci un numero valido tra 1 e 4.")
            continue  # Fa ripartire il ciclo senza interrompere il programma

        scelta = int(scelta)

        if scelta == 1:
            chescala = input('Quale scala vuoi vedere?\n(Maggiore, Minore Naturale, ecc.): ').strip().title()
            if chescala in scale:
                print(f"\nScala {chescala}: {', '.join(scale[chescala])}")
            else:
                print(f"⚠️ Errore: La scala '{chescala}' non è presente.")

        elif scelta == 2:
            cheaccordo = input('Quale accordo vuoi vedere? ').strip().title()
            if cheaccordo in accordi:
                print(f"\nAccordo {cheaccordo}: {', '.join(accordi[cheaccordo])}")
            else:
                print(f"⚠️ Errore: L'accordo '{cheaccordo}' non è presente.")

        elif scelta == 3:
            print('\nScopriamo se una nota appartiene a una scala!')

            nota = input('Inserisci una nota (es. Do, Re, Fa#):\n').strip().capitalize()
            scalapernota = input('Inserisci la scala su cui cercare la nota:\n').strip().title()

            if scalapernota in scale:
                if nota in scale[scalapernota]:
                    grado = scale[scalapernota].index(nota) + 1  # Indice parte da 0, aggiungiamo 1
                    print(f"\n✅ La nota {nota} è nella scala {scalapernota}, al grado {grado}°.")
                else:
                    print(f"❌ La nota {nota} NON è nella scala {scalapernota}.")
            else:
                print(f"⚠️ Errore: La scala '{scalapernota}' non è presente.")

        elif scelta == 4:
            print("👋 Arrivederci!")
            break  # Esce dal loop

# Dizionari delle scale e degli accordi
scale = {
    "Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Minore Naturale": ["Do", "Re", "Mib", "Fa", "Sol", "Lab", "Sib"],
    "Pentatonica Maggiore": ["Do", "Re", "Mi", "Sol", "La"],
    "Pentatonica Minore": ["Do", "Mib", "Fa", "Sol", "Sib"],
    "Blues": ["Do", "Mib", "Fa", "Fa#", "Sol", "Sib"]
}

accordi = {
    "Do Maggiore": ["Do", "Mi", "Sol"],
    "Do Minore": ["Do", "Mib", "Sol"],
    "Sol Settima": ["Sol", "Si", "Re", "Fa"],
    "La Minore": ["La", "Do", "Mi"],
    "Re Maggiore": ["Re", "Fa#", "La"]
}

# Avvia il menu
menu()








'''
Cosa ho migliorato?
✅ Controllo dell’input nel menu

Se l’utente inserisce qualcosa di diverso da un numero tra 1 e 4, il programma non crasha e lo avvisa con un messaggio di errore.
✅ Miglior gestione degli input utente

capitalize() per le note (evita errori con lettere maiuscole/minuscole).
title() per le scale e gli accordi, ma potrebbe essere perfezionato con una gestione più avanzata per nomi complessi.
strip() per rimuovere eventuali spazi vuoti.
✅ Gestione degli errori migliorata

Se la scala o l’accordo non sono presenti, ora viene mostrato un messaggio chiaro con il nome dell’elemento errato.
✅ Grado corretto della nota nella scala

Invece di index(nota, 1), che è errato (il secondo parametro è un punto di partenza per la ricerca), ora index(nota) + 1 dà il numero del grado corretto partendo da 1.
Cosa potresti aggiungere?
🔹 Un loop per chiedere nuovamente l’input quando l’utente sbaglia.
Ad esempio, se scrive una scala inesistente, potresti dargli una seconda possibilità senza dover rilanciare il menu.

🔹 Gestione degli errori avanzata con try-except
In questo caso try-except non è strettamente necessario perché abbiamo già isdigit() per verificare l’input numerico, ma se volessi accettare solo nomi di scale valide senza errori, potresti usare un try-except per evitare crash in caso di input errati.

🔹 Espansione del dizionario
Potresti aggiungere altre scale e accordi, magari anche quelli alterati (es. Dominanti, Diminuiti).
'''










'''

🔹 BLOCCO 1: Fondamenti (Esercizi 11-20)
💡 Obiettivo: Rafforzare la gestione di liste, dizionari e input utente, introducendo manipolazione dati e operazioni più strutturate.

Trasporre una scala
Chiedi all’utente il nome di una scala e un intervallo (es. +2 per trasporre di un tono).
Stampa la nuova scala trasposta.
Generare una progressione di accordi
Chiedi all’utente una tonalità e genera una progressione armonica di quattro accordi basata sulla tonalità scelta.
Filtrare note da una lista
Chiedi all’utente una nota e rimuovila da una lista di note musicali.
Stampa la lista aggiornata.
Conta le occorrenze di una nota in una sequenza
Chiedi all’utente di inserire una sequenza di note.
Conta e mostra quante volte compare una specifica nota.
Generare una melodia casuale
Usa una lista di note e genera una sequenza casuale di 8 note.
Stampa la melodia generata.
Ordinare le note alfabeticamente
Chiedi all’utente una lista di note e ordinala in ordine alfabetico.
Stampa la lista ordinata.
Costruire un arpeggio da un accordo
Chiedi all’utente il nome di un accordo e stampa le note in ordine arpeggiato.
Convertire una scala in MIDI
Assegna un valore MIDI (numero da 0 a 127) alle note di una scala e stampa i valori.
Gestire una libreria di accordi
Permetti all’utente di aggiungere nuovi accordi e salvarli in un dizionario.
Mostra la libreria aggiornata.
Salvare e caricare progressioni di accordi
Chiedi all’utente di inserire una progressione di accordi.
Salvala in un file e permetti di ricaricarla successivamente.

'''










