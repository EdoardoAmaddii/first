
class Recupera:

    ###### funzioni recupera ########
    def chiediscala_ottieninota():
        print('Chiedi scala -> ottieni note')

        chiediscala = input('Le note di che scala vuoi sapere?\n').strip().title()

        if chiediscala in scale.keys():
            print(scale[chiediscala])
        
        else:
            print('La scala non è presente')


    chiediscala_ottieninota()



    def chiedinota_ottieniscala():
        print('Chiedi nota -> ottieni scale associate')

        chiedinota = input('Dimmi una nota, ti dirò le scale associate ad essa:\n').strip().capitalize()

        scaleassociateanota = []

        for scala, note in scale.items():
            if chiedinota in note:
                scaleassociateanota.append(scala)

        print(';'.join(scaleassociateanota))


    chiedinota_ottieniscala()





        #### questa va cambiata per prendere la possibilità di fare l'analisi di più accordi insieme
    def chiediaccordo_ottieninote():

        chiediaccordo = input('Dimmi un accordo, ti dirò le note che lo compongono\n(usa la notazione anglosassone per scrivere gli accordi. es: Cmaj7)').strip().capitalize()

        if chiediaccordo in accordi:
            print(f'{chiediaccordo} è composto da {accordi[chiediaccordo]}')


    chiediaccordo_ottieninote()


    def chiedinote_ottieniaccordo():

        chiedinotxacc = input('dammi tre o quattro note, ti troverò gli accordi composti da queste note:\n').split(',')

        if len(chiedinotxacc) > 4 or len(chiedinotxacc) < 2:
            print('errore')
            

        accordiperutente = []

        #setaccordiutente = set(chords)

        for x in accordi.values():
            if set(chiedinotxacc) == set(x):
                accordiperutente.append()

        print(accordiperutente)

    chiedinote_ottieniaccordo()


'''
    def chiedinote_ottieniaccordo():
        # Chiede le note all'utente e le normalizza (rimuove spazi e le rende maiuscole)
        chiedinotxacc = input('Dammi tre o quattro note, ti troverò gli accordi composti da queste note:\n')
        chiedinotxacc = [nota.strip().upper() for nota in chiedinotxacc.split(',')]  # Pulizia input
        
        # Controllo sul numero di note
        if len(chiedinotxacc) > 4 or len(chiedinotxacc) < 2:
            print('Errore: inserisci tra 2 e 4 note.')
            return
        
        # Convertiamo la lista in una tupla ordinata per confrontarla con le chiavi del dizionario
        chiedinotxacc = tuple(sorted(chiedinotxacc))  # Ordinata per evitare errori di ordine
        
        accordiperutente = []
        
        # Controlliamo se la combinazione di note è presente nel dizionario degli accordi
        for chiave, valore in accordi.items():
            if set(chiedinotxacc) == set(chiave):  # Confronto tra insiemi per ignorare l'ordine
                accordiperutente.append(valore)

        if accordiperutente:
            print(f"Gli accordi trovati per {chiedinotxacc} sono: {', '.join(accordiperutente)}")
        else:
            print("Nessun accordo trovato per queste note.")

    chiedinote_ottieniaccordo()

    '''




dammi quattro accordi e il loro grado, ti inserirò gli accordi funzionali connessi

























#funzioni suggerisce




#1
#Trasporre una scala
#Chiedi all’utente il nome di una scala e un intervallo (es. +2 per trasporre di un tono).
#Stampa la nuova scala trasposta.

class traspositore:
    def trasportatore(): #sposta la scala in base all'intervallo
        print('Traspositore scale')
        while True:
            scalascelta = input('Che scala vuoi trasporre? (Es. Do Maggiore, Si Minore Naturale)\n').strip().title()
            if scalascelta not in scale:
                print("Scala non trovata, riprova.")
                continue

            try:
                intervallo = int(input('Di che intervallo vuoi trasporre la scala che hai scelto? (Es. +2, -5)\n'))
            except ValueError:
                print("Inserisci un numero intero positivo o negativo.")
                continue


            # Determina se la scala usa diesis o bemolle in base alle sue note
            #Perché funziona?
            #set(scale[scalascelta]) & set(note_cromatiche_diesis)
            #→ Controlla se c'è almeno una nota in comune tra la scala scelta e la scala cromatica con diesis.
            #Se c'è una corrispondenza, significa che la scala usa diesis, quindi assegniamo note_cromatiche_diesis, altrimenti note_cromatiche_bemolle.
            
            
            
            ####note_cromatiche = note_cromatiche if set(scale[scalascelta]) & set(note_cromatiche_diesis) else note_cromatiche_bemolle

    # Determinare se la scala usa diesis o bemolli
        # usa_diesis = any('#' in nota for nota in scale[scalascelta])
        # note_cromatiche = note_cromatiche_diesis if usa_diesis else note_cromatiche_bemolle

    # Scegliere la scala cromatica basandosi sulla notazione della scala scelta
        # note_cromatiche = note_cromatiche_diesis if any('#' in nota for nota in scale[scalascelta]) else note_cromatiche_bemolle


            scala_originale = scale[scalascelta]
            scala_trasposta = []

            for nota in scala_originale:
                if nota in note_diesis:
                    indice_originale = note_diesis.index(nota)
                    nuovo_indice = (indice_originale + intervallo) % len(note_diesis)
                    scala_trasposta.append(note_diesis[nuovo_indice])
                
                elif nota in note_bemolle:
                    indice_originale = note_bemolle.index(nota)
                    nuovo_indice = (indice_originale + intervallo) % len(note_bemolle)
                    scala_trasposta.append(note_bemolle[nuovo_indice])
                
                
                
                else:
                    print(f"Nota '{nota}' non riconosciuta nella scala cromatica.")

            print(f"Scala '{scalascelta}' trasposta di {intervallo}: {scala_trasposta}")

            break  # Per ora esegue solo una trasposizione e termina



    trasportatore()




'''
# Funzioni utili

def trasponi_scala(scala, semitoni):
    """Traspone una scala di un dato numero di semitoni"""
    risultato = []
    
    # Per ogni nota nella scala
    for nota in scala:
        # Converti la nota nella rappresentazione cromatica
        # Questo richiede una funzione di supporto che non è implementata qui
        indice = trova_indice_nota(nota, note_cromatiche)
        
        # Calcola il nuovo indice dopo la trasposizione
        nuovo_indice = (indice + semitoni) % 12
        
        # Aggiungi la nuova nota al risultato
        risultato.append(note_cromatiche[nuovo_indice])
    
    return risultato
'''


















