


note = ['' 'do' '' '' '' '' '' '' '' '' '' '' '']
note_anglo = ['' '' '' '' '' '' 'C' '' '' '' '' '' '']
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

pattern_ritmici_base = {
    "batteria": {
        "backbeat": ["D", "-", "D", "U", "-", "D", "-", "U"],
        "four_on_the_floor": ["D", "-", "D", "-", "D", "-", "D", "-"],
        "basic_rock_beat": ["D", "-", "D", "-", "U", "-", "D", "-", "U"],
        "shuffle": ["D", "-", "D", "U", "-", "D", "-", "U", "-", "D"],
        "funk_groove": ["D", "U", "-", "D", "U", "-", "D", "-", "U", "-"],
        
    }
}


pattern_ritmici_avanzati = {
    "half_time_shuffle": ["D", "-", "U", "-", "D", "-", "U", "-", "D"],
        "jazz_swing": ["D", "-", "D", "-", "U", "-", "D", "-", "U", "-", "D", "-", "U"],
        "reggae_one_drop": ["D", "-", "-", "D", "-", "-", "U", "-", "D"],
        "linear_drumming": ["D", "-", "-", "-", "U", "-", "-", "-", "D"]
}





    

    #in questa classe le funzione hanno il semplice compito di mostrare i dati (liste, dizionari) a seconda degli input suggeriti all'utente.

def mostranote():
    
    formatonote = input('come vuoi vedere le note: formato anglosassone o continentale?\n[1 o 2]:')
    
    if formatonote == '1':
        print(note_anglo)
    if formatonote == '2':
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







def mostraprogressioni():

    chiediprog = input('vuoi vedere le progressioni base o quelle avanzate?')

    if chiediprog == 'base':
        print(progressioni_base)

    elif chiediprog == 'avanzate':
        sceglilivello = input('che difficoltà vuoi vedere?\n(Lv.1-2-3)')

        if sceglilivello == '1':
            #mostra le progressioni che mostrano nella chiave del dizionario livello 1
            progressionilv1 = {}
            for k, x in progressioni_base.items():
                if sceglilivello in k:
                    progressionilv1[k] = x

            print(progressionilv1)


        elif sceglilivello == '2':
            #mostra le progressioni che mostrano nella chiave del dizionario livello 1
            progressionilv2 = {}
            for k, x in progressioni_base.items():
                if sceglilivello in k:
                    progressionilv2[k] = x

            print(progressionilv2)

        elif sceglilivello == '3':
            #mostra le progressioni che mostrano nella chiave del dizionario livello 1
            progressionilv3 = {}
            for k, x in progressioni_base.items():
                if sceglilivello in k:
                    progressionilv3[k] = x

            print(progressionilv3)
    else:
        print('Probabilmente hai scritto male')






def mostrapatternritmici():
    
    chiedipattern = input('vuoi vedere i pattern ritmici base o quelle avanzate?')

    if chiedipattern == 'base':
        print(pattern_ritmici_base)

    elif chiedipattern == 'avanzate':
        sceglilivello = input('che difficoltà vuoi vedere?\n(Lv.1-2)')

        if sceglilivello == '1':
            #mostra le progressioni che mostrano nella chiave del dizionario livello 1
            patternlv1 = {}
            for k, x in pattern_ritmici_avanzati.items():
                if sceglilivello in k:
                    patternlv1[k] = x

            print(patternlv1)


        elif sceglilivello == '2':
            #mostra le progressioni che mostrano nella chiave del dizionario livello 1
            patternlv2 = {}
            for k, x in progressioni_base.items():
                if sceglilivello in k:
                    patternlv2[k] = x

            print(patternlv2)


mostrapatternritmici()













