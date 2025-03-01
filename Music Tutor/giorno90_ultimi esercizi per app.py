
'''
Convertire una scala in MIDI
Assegna un valore MIDI (numero da 0 a 127) alle note di una scala e stampa i valori.


Gestire una libreria di accordi
Permetti all’utente di aggiungere nuovi accordi e salvarli in un dizionario.
Mostra la libreria aggiornata.
Salvare e caricare progressioni di accordi
Chiedi all’utente di inserire una progressione di accordi.
Salvala in un file e permetti di ricaricarla successivamente.





def trova_accordo(note):
    """Identifica l'accordo dato un insieme di note"""
    # Implementazione complessa che richiederebbe la conoscenza di teoria musicale avanzata
    pass

def inverti_accordo(accordo, inversione=1):
    """Restituisce l'inversione specificata di un accordo"""
'''






#Convertire una scala in MIDI
#Assegna un valore MIDI (numero da 0 a 127) alle note di una scala e stampa i valori.


scale = {
    # Scale Maggiori
    "Do Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Do# Maggiore": ["Do#", "Re#", "Mi#", "Fa#", "Sol#", "La#", "Si#"],
    "Reb Maggiore": ["Reb", "Mib", "Fa", "Solb", "Lab", "Sib", "Do"],
    "Re Maggiore": ["Re", "Mi", "Fa#", "Sol", "La", "Si", "Do#"],
}


'''

valoremidi = {}


#assegnare i valori ogni 8 passi
for nota in scale.values():
    valoremidi[nota] = int(range(0,127)) % 8

print(valoremidi)


'''



# Dizionario delle scale
scale = {
    # Scale Maggiori
    "Do Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    
    "Reb Maggiore": ["Reb", "Mib", "Fa", "Solb", "Lab", "Sib", "Do"],
    "Re Maggiore": ["Re", "Mi", "Fa#", "Sol", "La", "Si", "Do#"],
}

# Mappa dei valori MIDI per le note musicali
mappa_midi = {
    "Do": 60, "Do#": 61, "Re": 62, "Re#": 63, "Mi": 64, "Fa": 65, "Fa#": 66,
    "Sol": 67, "Sol#": 68, "La": 69, "La#": 70, "Si": 71, "Do#": 72,
    "Reb": 59, "Mib": 63, "Solb": 66, "Lab": 68, "Sib": 70
}

# Creiamo un dizionario per i valori MIDI delle scale
valoremidi = {}

# Assegnamo i valori MIDI per ogni nota di ogni scala
for nome_scale, note in scale.items():
    valoremidi[nome_scale] = [mappa_midi[nota] for nota in note]

# Stampa il dizionario con i valori MIDI delle scale
for scale_name, midi_values in valoremidi.items():
    print(f"{scale_name}: {midi_values}")































accordi = {
    # Accordi Maggiori
    "Do Maggiore": ["Do", "Mi", "Sol"],
    "Do# Maggiore": ["Do#", "Fa", "Sol#"],
    "Reb Maggiore": ["Reb", "Fa", "Lab"],
    "Re Maggiore": ["Re", "Fa#", "La"],
    "Re# Maggiore": ["Re#", "Sol", "Si"],
    "Mib Maggiore": ["Mib", "Sol", "Sib"],
    "Mi Maggiore": ["Mi", "Sol#", "Si"],
    "Fa Maggiore": ["Fa", "La", "Do"],
    "Fa# Maggiore": ["Fa#", "La#", "Do#"],
    "Solb Maggiore": ["Solb", "Sib", "Reb"],
    "Sol Maggiore": ["Sol", "Si", "Re"],
    "Sol# Maggiore": ["Sol#", "Do", "Re#"],
    "Lab Maggiore": ["Lab", "Do", "Mib"],
    "La Maggiore": ["La", "Do#", "Mi"],
    "La# Maggiore": ["La#", "Re", "Fa"],
    "Sib Maggiore": ["Sib", "Re", "Fa"],
    "Si Maggiore": ["Si", "Re#", "Fa#"],
    
    # Accordi Minori
    "Do Minore": ["Do", "Mib", "Sol"],
    "Do# Minore": ["Do#", "Mi", "Sol#"],
    "Reb Minore": ["Reb", "Fab", "Lab"],
    "Re Minore": ["Re", "Fa", "La"],
    "Re# Minore": ["Re#", "Fa#", "La#"],
    "Mib Minore": ["Mib", "Solb", "Sib"],
    "Mi Minore": ["Mi", "Sol", "Si"],
    "Fa Minore": ["Fa", "Lab", "Do"],
    "Fa# Minore": ["Fa#", "La", "Do#"],
    "Solb Minore": ["Solb", "Sibb", "Reb"],
    "Sol Minore": ["Sol", "Sib", "Re"],
    "Sol# Minore": ["Sol#", "Si", "Re#"],
    "Lab Minore": ["Lab", "Dob", "Mib"],
    "La Minore": ["La", "Do", "Mi"],
    "La# Minore": ["La#", "Do#", "Fa"],
    "Sib Minore": ["Sib", "Reb", "Fa"],
    "Si Minore": ["Si", "Re", "Fa#"],

# Accordi Aumentati
    "Do Aumentato": ["Do", "Mi", "Sol#"],
    "Do# Aumentato": ["Do#", "Fa", "La"],
    "Reb Aumentato": ["Reb", "Fa", "La"],
    "Re Aumentato": ["Re", "Fa#", "La#"],
    "Re# Aumentato": ["Re#", "Sol", "Si"],
    "Mib Aumentato": ["Mib", "Sol", "Si"],
    "Mi Aumentato": ["Mi", "Sol#", "Do"],
    "Fa Aumentato": ["Fa", "La", "Do#"],
    "Fa# Aumentato": ["Fa#", "La#", "Re"],
    "Solb Aumentato": ["Solb", "Sib", "Re"],
    "Sol Aumentato": ["Sol", "Si", "Re#"],
    "Sol# Aumentato": ["Sol#", "Do", "Mi"],
    "Lab Aumentato": ["Lab", "Do", "Mi"],
    "La Aumentato": ["La", "Do#", "Fa"],
    "La# Aumentato": ["La#", "Re", "Fa#"],
    "Sib Aumentato": ["Sib", "Re", "Fa#"],
    "Si Aumentato": ["Si", "Re#", "Sol"],
    
    # Accordi Diminuiti
    "Do Diminuito": ["Do", "Mib", "Solb"],
    "Do# Diminuito": ["Do#", "Mi", "Sol"],
    "Reb Diminuito": ["Reb", "Fab", "Solb"],
    "Re Diminuito": ["Re", "Fa", "Lab"],
    "Re# Diminuito": ["Re#", "Fa#", "La"],
    "Mib Diminuito": ["Mib", "Solb", "Sibb"],
    "Mi Diminuito": ["Mi", "Sol", "Sib"],
    "Fa Diminuito": ["Fa", "Lab", "Si"],
    "Fa# Diminuito": ["Fa#", "La", "Do"],
    "Solb Diminuito": ["Solb", "Sibb", "Dob"],
    "Sol Diminuito": ["Sol", "Sib", "Reb"],
    "Sol# Diminuito": ["Sol#", "Si", "Re"],
    "Lab Diminuito": ["Lab", "Dob", "Rebb"],
    "La Diminuito": ["La", "Do", "Mib"],
    "La# Diminuito": ["La#", "Do#", "Mi"],
    "Sib Diminuito": ["Sib", "Reb", "Fab"],
    "Si Diminuito": ["Si", "Re", "Fa"]
}


def trova_accordo():
    print("\n\nIdentifica l'accordo dato un insieme di note\n\n")

    notedacercare = input('che note compongono il tuo accordo, dimmelo e ti troverò il nome adeguato:\n').title()

    notesconosciute = notedacercare.split(',')

    for nome, notes in accordi.items(): 
        if notes == notesconosciute:
            print(nome)

            return #esce dopo il primo accordo trovato
    
    
trova_accordo ()
    
###
# questo codice va bene, ma non tiene conto di pulire l'input e di poter cercare le note in ordine sparso: per questo ti serve un set!!!




'''
Ecco una versione migliorata del tuo codice con alcuni miglioramenti:

Miglioramenti Apportati
✅ Ignora l'ordine delle note → Confronto con set() invece di list()
✅ Rimuove spazi extra dall'input → Usa .strip() per pulire le note inserite
✅ Riconosce anche input parziali → Trova accordi contenenti le note inserite
✅ Gestione di più risultati → Mostra tutti gli accordi possibili
✅ Evita maiuscole/minuscole errate → Converte tutto in minuscolo per evitare errori
'''

def trova_accordo():
    print("\n\nIdentifica l'accordo dato un insieme di note\n\n")

    notedacercare = input('Che note compongono il tuo accordo? Separale con una virgola:\n')

    # Pulizia input: rimuove spazi e uniforma maiuscole/minuscole
    notesconosciute = set(n.strip().capitalize() for n in notedacercare.split(','))

    accordi_trovati = []

    for nome_accordo, notes in accordi.items():
        if set(notes) == notesconosciute:
            accordi_trovati.append(nome_accordo)

    if accordi_trovati:
        print("\nL'accordo corrispondente è:")
        for acc in accordi_trovati:
            print(f"- {acc}")
    else:
        print("❌ Nessun accordo trovato con queste note.")

trova_accordo()




def trova_accordo():
    print("\n\nIdentifica l'accordo dato un insieme di note\n\n")

    notedacercare = input('Che note compongono il tuo accordo? Separale con una virgola:\n')

    # Elaboriamo le note dell'input
    lista_note = notedacercare.split(',')
    note_pulite = []
    
    for n in lista_note:
        nota_formattata = n.strip().capitalize()
        note_pulite.append(nota_formattata)

    notesconosciute = set(note_pulite)  # Convertiamo in set per ignorare l'ordine

    accordi_trovati = []

    for nome_accordo, notes in accordi.items():
        if set(notes) == notesconosciute:
            accordi_trovati.append(nome_accordo)

    if accordi_trovati:
        print("\nL'accordo corrispondente è:")
        for acc in accordi_trovati:
            print(f"- {acc}")
    else:
        print("❌ Nessun accordo trovato con queste note.")

trova_accordo()




### con Ai   ### stesso codice di prima: in questo codice troviamo i rivolti perchè i set forniscono tutti gli accordi : keys per le note da noi inserite : values

def trova_accordo():
    print("\n\nIdentifica l'accordo dato un insieme di note\n\n")

    notedacercare = input('Che note compongono il tuo accordo? Separale con una virgola:\n')

    # Pulizia input: rimuove spazi e crea un set delle note
    notesconosciute = set(n.strip() for n in notedacercare.split(','))

    for nome_accordo, notes in accordi.items():
        if set(notes) == notesconosciute:
            print(f"L'accordo che hai inserito è: {nome_accordo}")
            return
    
    print("Nessun accordo trovato con queste note.")

trova_accordo()














def scala_dell_accordo():
    print('\n\nidentifica le scale di accordi\n\n')

    accordodacercare = ('dammi un accordo, ti dirò a che scal* appartiene')


    scale
    accordi






