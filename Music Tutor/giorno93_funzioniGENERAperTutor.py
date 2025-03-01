


#funzioni suggerisce




#1
#Trasporre una scala
#Chiedi all’utente il nome di una scala e un intervallo (es. +2 per trasporre di un tono).
#Stampa la nuova scala trasposta.


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













def accordiegrado_ottieniaccordifunzionalicorrispondenti():
    pass

def accordiegrado_ottienisesonoinunaprogressionecomune():
    pass
    







