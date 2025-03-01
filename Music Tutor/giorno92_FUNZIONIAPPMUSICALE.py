


note = ['' '' '' '' '' '' '' '' '' '' '' '' '']
note_anglo = ['' '' '' '' '' '' '' '' '' '' '' '' '']
note_diesis = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
note_bemolle = ["Do", "Do#", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib", "Si"]

scale = {
    # Scale Maggiori
    "Do Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Do# Maggiore": ["Do#", "Re#", "Mi#", "Fa#", "Sol#", "La#", "Si#"],
    "Reb Maggiore": ["Reb", "Mib", "Fa", "Solb", "Lab", "Sib", "Do"],
    "Re Maggiore": ["Re", "Mi", "Fa#", "Sol", "La", "Si", "Do#"]
}

accordi = {
    # Accordatura per C
    "C": ["Do", "Mi", "Sol"],
    "Cm": ["Do", "Mib", "Sol"],
    "C7": ["Do", "Mi", "Sol", "Sib"],
    "Cm7": ["Do", "Mib", "Sol", "Sib"],
    "Cmaj7": ["Do", "Mi", "Sol", "Si"],
    "Cdim": ["Do", "Mib", "Solb"]
}

accordi_triadi_tonalita = {
    # Scale maggiori
    "Do Maggiore": ["Do", "Re min", "Mi min", "Fa", "Sol", "La min", "Si dim"],
    "Sol Maggiore": ["Sol", "La min", "Si min", "Do", "Re", "Mi min", "Fa# dim"],
    "Re Maggiore": ["Re", "Mi min", "Fa# min", "Sol", "La", "Si min", "Do# dim"]
}

accordi_quadriadi_tonalita = {
    # Scale maggiori
    "Do Maggiore": [
        "Do maj7", "Re min7", "Mi min7", "Fa maj7", "Sol7", "La min7", "Si min7b5"
    ],
    "Sol Maggiore": [
        "Sol maj7", "La min7", "Si min7", "Do maj7", "Re7", "Mi min7", "Fa# min7b5"
        ]
}

progressioni_base = {
    "progressione_0": {"gradi": [0, 5, 1, 4], "descrizione": "Turn Around"},
    "progressione_1": {"gradi": [0, 4, 5, 0], "descrizione": "Cadenza perfetta, stabile e risolutiva. Tipica nel rock e pop."},
    "progressione_2": {"gradi": [0, 5, 6, 4], "descrizione": "Molto usata nel pop, emotiva e aperta."}
}

accordi_funzionali = {
    "Tonica_stasi": {
        "0": ["C"],
        "2": ["Em"],  # Terzo grado (minore) che aggiunge un senso di stabilità
        "5": ["Am"]  # Sesto grado (minore) che rafforza la sensazione di tonica
    },
    
    "Sottodominante_movimento": {
        "3": ['F'],
        "1": ["Dm"]
    },
    
    "Dominante_tensione": {
        "4": ["G"],
        "6": ["Bdim"]
    }
}

music_patterns = {
    "batteria": {
        "backbeat": ["D", "-", "D", "U", "-", "D", "-", "U"],
        "four_on_the_floor": ["D", "-", "D", "-", "D", "-", "D", "-"],
        "basic_rock_beat": ["D", "-", "D", "-", "U", "-", "D", "-", "U"],
        "shuffle": ["D", "-", "D", "U", "-", "D", "-", "U", "-", "D"],
        "funk_groove": ["D", "U", "-", "D", "U", "-", "D", "-", "U", "-"],
        "half_time_shuffle": ["D", "-", "U", "-", "D", "-", "U", "-", "D"],
        "jazz_swing": ["D", "-", "D", "-", "U", "-", "D", "-", "U", "-", "D", "-", "U"],
        "reggae_one_drop": ["D", "-", "-", "D", "-", "-", "U", "-", "D"],
        "linear_drumming": ["D", "-", "-", "-", "U", "-", "-", "-", "D"]
    }
}





class Mostra:

    #in questa classe le funzione hanno il semplice compito di mostrare i dati (liste, dizionari) a seconda degli input suggeriti all'utente.

    def mostranote():
        
        formatonote = input('come vuoi vedere le note: formato anglosassone o continentale?')
        
        if formatonote == 'anglosassone':
            print(note_anglo)
        if formatonote == 'continentale':
            print(note)

        else:
            print('forse hai scritto male qualcosa')

    mostranote()





def mostrascale():
    qualiscale = input('Che scale vuoi vedere:\n(0 : tutte le scale, 1 : maggiori , 2 : minori)\n')

    if qualiscale == '0':
        for nome, gradi in scale.items():
            print(f"{nome}: {', '.join(gradi)}")

    elif qualiscale == '1':  # Filtra solo le scale maggiori
        scale_maggiori = {}
        for k, v in scale.items():
            if 'Maggiore' in k:
                scale_maggiori[k] = v
        for nome, gradi in scale_maggiori.items():
            print(f"{nome}: {', '.join(gradi)}")

    elif qualiscale == '2':  # Filtra solo le scale minori
        scale_minori = {k: v for k, v in scale.items() if 'Minore' in k}
        for nome, gradi in scale_minori.items():
            print(f"{nome}: {', '.join(gradi)}")

    else:
        print('Forse hai scritto male qualcosa.')

mostrascale()




'''


Versione con AI

# Dizionario delle scale di esempio
scale = {
    'Do Maggiore': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'Sol Maggiore': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    'La Minore': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Mi Minore': ['E', 'F#', 'G', 'A', 'B', 'C', 'D']
}

def mostrascale():
    qualiscale = input('Che scale vuoi vedere:\n(0 : tutte, 1 : maggiori, 2 : minori)\n')

    if qualiscale == '0':
        da_mostrare = scale
    elif qualiscale == '1':
        da_mostrare = {k: v for k, v in scale.items() if 'Maggiore' in k}
    elif qualiscale == '2':
        da_mostrare = {k: v for k, v in scale.items() if 'Minore' in k}
    else:
        print('Errore: devi inserire 0, 1 o 2.')
        return

    if da_mostrare:
        for nome, gradi in da_mostrare.items():
            print(f"{nome}: {', '.join(gradi)}")
    else:
        print("Nessuna scala trovata.")

mostrascale()


'''










def mostraaccordi():

    accordidavedere = input('che accordi vuoi vedere:\n (0 : tutti gli accordi, altrimenti una parola di riferimento stamperà tutto ciò che è connesso)')
    
    if accordidavedere == '0':
        print(note_anglo)
    
    elif accordidavedere == accordidavedere:
        for k, v in accordi.items():
            if accordidavedere in k or v:
                print(f'{k}:{v}')

    else:
        print('forse hai scritto male qualcosa')


    #'''elif  == '1':  # Filtra solo le scale maggiori
    #    scale_maggiori = {}
    #    for k, v in scale.items():
    #        if 'Maggiore' in k:
    #            scale_maggiori[k] = v
    #    for nome, gradi in scale_maggiori.items():
    #        print(f"{nome}: {', '.join(gradi)}")'''
    
    
mostraaccordi()












# questo con AI



'''

# Dizionario di esempio degli accordi
accordi = {
    'Do Maggiore': ['C', 'E', 'G'],
    'Sol Maggiore': ['G', 'B', 'D'],
    'La Minore': ['A', 'C', 'E'],
    'Mi Minore': ['E', 'G', 'B']
}

def mostraaccordi():
    accordidavedere = input("Che accordi vuoi vedere?\n(0 : tutti gli accordi, oppure inserisci una parola chiave per filtrare)\n")

    if accordidavedere == '0':
        for nome, note in accordi.items():
            print(f"{nome}: {', '.join(note)}")

    else:
        trovati = {k: v for k, v in accordi.items() if accordidavedere.lower() in k.lower()}
        
        if trovati:
            for nome, note in trovati.items():
                print(f"{nome}: {', '.join(note)}")
        else:
            print("Nessun accordo trovato con questa chiave di ricerca.")

mostraaccordi()


'''






















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


















