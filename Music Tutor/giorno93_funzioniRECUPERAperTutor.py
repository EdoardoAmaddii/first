

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




###### funzioni recupera ########
def chiediscala_ottieninota():
    print('Chiedi scala -> ottieni note')

    chiediscala = input('Le note di che scala vuoi sapere?\n').strip().title()

    if chiediscala in scale.keys():
        print(scale[chiediscala])
    
    else:
        print('La scala non è presente')

























def chiedinota_ottieniscala():
    print('Chiedi nota -> ottieni scale associate')

    chiedinota = input('Dimmi una nota, ti dirò le scale associate ad essa:\n').strip().capitalize()

    scaleassociateanota = []

    for scala, note in scale.items():
        if chiedinota in note:
            scaleassociateanota.append(scala)

    print(';'.join(scaleassociateanota))









#def chiedinote_ottieniscalecomplementari():
#    chiedinote = input('Dammi fino a 3 note, vediamo se hanno scale complementari:\n').strip().title()
#    noteutente = chiedinote.split()

#    if len(noteutente) > 3 or len(noteutente) == 0:
#        print("Errore: inserisci da 1 a 3 note.")
#        return

#    scalecomplementari = []

    # Controlla in quali scale sono contenute le note inserite dall'utente
#    for nome_scala, note_scala in scale.items():
#        if all(nota in note_scala for nota in noteutente):  # Verifica che tutte le note dell'utente siano presenti nella scala
#            scalecomplementari.append(nome_scala)

    # Stampa il risultato
#    if scalecomplementari:
#        print("\nScale complementari trovate:")
#        for scala in scalecomplementari:
#            print(f"- {scala}: {', '.join(scale[scala])}")
#    else:
#        print("Nessuna scala complementare trovata.")

# Esegui la funzione
#chiedinote_ottieniscalecomplementari()


   





def chiedinote_ottieniscalecomplementari():
    chiedinote = input('Dammi fino a 3 note, vediamo le scale corrispondenti e quelle complementari:\n').strip().title()
    noteutente = set(chiedinote.split())

    if len(noteutente) > 3 or len(noteutente) == 0:
        print("Errore: inserisci da 1 a 3 note.")
        return

    scale_corrispondenti = []
    scale_complementari = []

    for nome, note in scale.items():
        if noteutente.issubset(note):
            scale_corrispondenti.append(nome)
        elif noteutente & note:  # Verifica se c'è almeno un'intersezione
            scale_complementari.append(nome)

    # Stampa il risultato
    if scale_corrispondenti:
        print("\n Scale corrispondenti (contengono tutte le note richieste):")
        for scala in scale_corrispondenti:
            print(f"{scala}: {', '.join(scale[scala])}")
    else:
        print("\n Nessuna scala corrispondente trovata.")

    if scale_complementari:
        print("\nScale complementari (contengono almeno una delle note richieste):")
        for scala in scale_complementari:
            print(f"{scala}: {', '.join(scale[scala])}")
    else:
        print("\n Nessuna scala complementare trovata.")

# Esegui la funzione
chiedinote_ottieniscalecomplementari()






def chiediaccordi_ottieninote():

    chiediaccordo = input('Dimmi un accordo, ti dirò le note che lo compongono\n(usa la notazione anglosassone per scrivere gli accordi. es: Cmaj7)').strip().title()

    accordiutente = chiediaccordo.split()

    chords = {}

    for x, y in accordi.items():
        if accordiutente in accordi.keys():
                chords[x] = y

    else:
        print('Accordo non trovato.')
    
    print(chords)









def chiedinote_ottieniaccordi():

    chiedinotxacc = input('dammi tre o quattro note, ti troverò gli accordi composti da queste note:\n').strip().split(',')

    ##### chiedinotxacc = [nota.strip().upper() for nota in chiedinotxacc.split(',')]  # Pulizia input

    if len(chiedinotxacc) > 4 or len(chiedinotxacc) <= 2:
        print('Errore: controlla se hai rispettato la indicazione')
        return
        
    accordiperutente = []

    for x in accordi.values():
        if set(chiedinotxacc) == set(x):
            accordiperutente.append()

    if accordiperutente:
        for accordo in accordiperutente:
            print(f'{accordo} : {','.join(accordi[accordo])}')



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







def chiediaccordi_ottieniscaleassociate():
    pass

def chiediaccordi_ottieniscalecomplementari():
    pass








def accordiegrado_ottieniaccordifunzionalicorrispondenti():
    pass

def accordiegrado_ottienisesonoinunaprogressionecomune():
    pass
    








#dammi quattro accordi e il loro grado, ti inserirò gli accordi funzionali connessi

