
scale = {
    # Scale Maggiori
    "Do Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Do# Maggiore": ["Do#", "Re#", "Mi#", "Fa#", "Sol#", "La#", "Si#"],
    "Reb Maggiore": ["Reb", "Mib", "Fa", "Solb", "Lab", "Sib", "Do"],
    "Re Maggiore": ["Re", "Mi", "Fa#", "Sol", "La", "Si", "Do#"],
    "Re# Maggiore": ["Re#", "Mi#", "Fa##", "Sol#", "La#", "Si#", "Do##"],
    "Mib Maggiore": ["Mib", "Fa", "Sol", "Lab", "Sib", "Do", "Re"],
    "Mi Maggiore": ["Mi", "Fa#", "Sol#", "La", "Si", "Do#", "Re#"],
    "Fa Maggiore": ["Fa", "Sol", "La", "Sib", "Do", "Re", "Mi"],
    "Fa# Maggiore": ["Fa#", "Sol#", "La#", "Si", "Do#", "Re#", "Mi#"],
    "Solb Maggiore": ["Solb", "Lab", "Sib", "Dob", "Reb", "Mib", "Fa"],
    "Sol Maggiore": ["Sol", "La", "Si", "Do", "Re", "Mi", "Fa#"],
    "Sol# Maggiore": ["Sol#", "La#", "Si#", "Do#", "Re#", "Mi#", "Fa##"],
    "Lab Maggiore": ["Lab", "Sib", "Do", "Reb", "Mib", "Fa", "Sol"],
    "La Maggiore": ["La", "Si", "Do#", "Re", "Mi", "Fa#", "Sol#"],
    "La# Maggiore": ["La#", "Si#", "Do##", "Re#", "Mi#", "Fa##", "Sol##"],
    "Sib Maggiore": ["Sib", "Do", "Re", "Mib", "Fa", "Sol", "La"],
    "Si Maggiore": ["Si", "Do#", "Re#", "Mi", "Fa#", "Sol#", "La#"]
}



#Conta le occorrenze di una nota in una sequenza
#Chiedi all’utente di inserire una sequenza di note. max 8
#conta quante volte compaiono le note


def conta_occorrenze():
    noteutente = input("Inserisci fino a 8 note separate da virgola (es. Do,Re,Mi,Fa):\n").strip()

    # Creiamo la lista delle note
    notesingole = [nota.strip().capitalize() for nota in noteutente.split(",")]

    # Controlliamo che non ci siano più di 8 note
    if len(notesingole) > 8:
        print("Hai inserito troppe note! Devi mettere al massimo 8.")
        return

    # Lista per tracciare le note già contate
    risultati = []

    # Contiamo manualmente le occorrenze
    for nota in notesingole:
        count = 0
        for n in notesingole:
            if n == nota:
                count += 1
        if (nota, count) not in risultati:  # Evitiamo duplicati
            risultati.append((nota, count))

    # Stampiamo il risultato
    print("\nEcco quante volte devi suonare ogni nota:")
    for nota, count in risultati:
        print(f"{nota}: {count} volte")

conta_occorrenze()




def conta_occorrenze_lista():
    noteutente = input("Inserisci fino a 8 note separate da virgola (es. Do,Re,Mi,Fa):\n").strip()

    # Creiamo la lista delle note
    notesingole = [nota.strip().capitalize() for nota in noteutente.split(",")]

    # Controlliamo che non ci siano più di 8 note
    if len(notesingole) > 8:
        print("Hai inserito troppe note! Devi mettere al massimo 8.")
        return

    # Creiamo una lista per raccogliere le note e le loro occorrenze
    risultati = []

    # Contiamo le occorrenze di ogni nota
    for nota in notesingole:
        #if nota:  # Evita stringhe vuote
            count = notesingole.count(nota)
            if (nota, count) not in risultati:  # Evita duplicati nella stampa
                risultati.append((nota, count))

    # Stampiamo il risultato
    print("\nEcco quante volte devi suonare ogni nota:")
    for nota, count in risultati:
        print(f"{nota}: {count} volte")

conta_occorrenze_lista()



def conta_occorrenze_dizionario():
    noteutente = input("Inserisci fino a 8 note separate da virgola (es. Do,Re,Mi,Fa):\n").strip()
    
    # Dividiamo la stringa in una lista di note
    notesingole = noteutente.split(',')

    # Verifichiamo che l'utente non abbia inserito più di 8 note
    if len(notesingole) > 8:
        print("Hai inserito troppe note! Devi mettere al massimo 8.")
        return

    # Creiamo un dizionario per contare le occorrenze
    conteggio = {}

    for nota in notesingole:
        nota = nota.strip().capitalize()  # Rimuove spazi e standardizza la maiuscola
        if nota:
            conteggio[nota] = conteggio.get(nota, 0) + 1  # Aggiunge al conteggio

    # Stampiamo i risultati
    print("\nEcco quante volte devi suonare ogni nota:")
    for nota, count in conteggio.items():
        print(f"{nota}: {count} volte")

conta_occorrenze()





#Conta e mostra quante volte compare una specifica nota nella scala maggiore delle varie tonalità.



def conta_occorrenze():
    noteutente = input("Inserisci fino a 8 note separate da virgola (es. Do,Re,Mi,Fa):\n").strip()

    # Creiamo la lista delle note
    notesingole = [nota.strip().capitalize() for nota in noteutente.split(",")]

    # Controlliamo che non ci siano più di 8 note
    if len(notesingole) > 8:
        print("Hai inserito troppe note! Devi mettere al massimo 8.")
        return

    # Lista per tracciare le note già contate
    risultati = {}
    

    # Contiamo manualmente le occorrenze
    # Contiamo le occorrenze nelle scale
    for nota in notesingole:
        count = 0  # Reset del contatore per ogni nota
        for scala in scale.values():
            if nota in scala:
                count += 1
        risultati[nota] = count  # Salviamo il risultato

    # Stampiamo il risultato
    print("\nEcco quante volte appare questa nota nelle scale maggiori:")
    for nota, count in risultati.items():
        print(f"{nota}: {count} volte")

conta_occorrenze()






#Ordinare le note alfabeticamente
#Chiedi all’utente una lista di strumenti musicali, ordinali alfabeticamente.
#Stampa la lista ordinata.


def strumentimusicali():
    print('\n\n strumenti musicali\n\n')

    
    strumenti = input('dammi tre strumenti, divisi da virgole, e li ordino:')
    
    listastrumenti = []
    for x in strumenti.split(','):
        
        listastrumenti.append(x.title())
        
    listastrumenti.sort()

    print(",".join(listastrumenti))
        
strumentimusicali()







# così con la comprehension

def strumentimusicali():
    print('\n\nStrumenti musicali\n\n')

    strumenti = input('Dammi tre strumenti, divisi da virgole, e li ordino: ')

    # Creiamo una lista vuota e aggiungiamo gli strumenti
    listastrumenti = [x.strip().capitalize() for x in strumenti.split(',')]

    # Ordiniamo la lista alfabeticamente
    listastrumenti.sort()

    # Stampiamo il risultato
    print("\nLista ordinata degli strumenti musicali:")
    print(", ".join(listastrumenti))

strumentimusicali()









#Generare una melodia casuale
#Fai scegliere all'utente la scala
#Usa la scala e genera una sequenza casuale di 8 note.
#Stampa la melodia generata.


import random


def generamelodia():

    print('\n\nGenera melodia\n\n')

    scalautente = input('dammi una scala e ti darò otto nota da suonare:')


    if scalautente in scale:
        notecasuali = random.choices(scale[scalautente], k=8)

        print(','.join(notecasuali))

    else:
        print('la scala scelta non è stata trovata')

generamelodia()



