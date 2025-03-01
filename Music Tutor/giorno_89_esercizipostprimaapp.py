
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





note_cromatiche_diesis = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
note_cromatiche_bemolle = ["Do", "Reb", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib", "Si"]



# Intervalli musicali
intervalli = {
    "unisono": 0,
    "seconda minore": 1,
    "seconda maggiore": 2,
    "terza minore": 3,
    "terza maggiore": 4,
    "quarta giusta": 5,
    "quarta aumentata / quinta diminuita": 6,
    "quinta giusta": 7,
    "sesta minore": 8,
    "sesta maggiore": 9,
    "settima minore": 10,
    "settima maggiore": 11,
    "ottava": 12
}


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
    "Si Maggiore": ["Si", "Do#", "Re#", "Mi", "Fa#", "Sol#", "La#"],

    # Scale Minori Naturali
    "Do Minore Naturale": ["Do", "Re", "Mib", "Fa", "Sol", "Lab", "Sib"],
    "Do# Minore Naturale": ["Do#", "Re#", "Mi", "Fa#", "Sol#", "La", "Si"],
    "Reb Minore Naturale": ["Reb", "Mib", "Fb", "Solb", "Lab", "Sibb", "Dob"],
    "Re Minore Naturale": ["Re", "Mi", "Fa", "Sol", "La", "Sib", "Do"],
    "Re# Minore Naturale": ["Re#", "Mi#", "Fa#", "Sol#", "La#", "Si", "Do#"],
    "Mib Minore Naturale": ["Mib", "Fa", "Solb", "Lab", "Sib", "Dob", "Reb"],
    "Mi Minore Naturale": ["Mi", "Fa#", "Sol", "La", "Si", "Do", "Re"],
    "Fa Minore Naturale": ["Fa", "Sol", "Lab", "Sib", "Do", "Reb", "Mib"],
    "Fa# Minore Naturale": ["Fa#", "Sol#", "La", "Si", "Do#", "Re", "Mi"],
    "Solb Minore Naturale": ["Solb", "Lab", "Sibb", "Dob", "Reb", "Febb", "Geb"],
    "Sol Minore Naturale": ["Sol", "La", "Sib", "Do", "Re", "Mib", "Fa"],
    "Sol# Minore Naturale": ["Sol#", "La#", "Si", "Do#", "Re#", "Mi", "Fa#"],
    "Lab Minore Naturale": ["Lab", "Sib", "Dob", "Reb", "Mib", "Fb", "Solb"],
    "La Minore Naturale": ["La", "Si", "Do", "Re", "Mi", "Fa", "Sol"],
    "La# Minore Naturale": ["La#", "Si#", "Do#", "Re#", "Mi#", "Fa#", "Sol#"],
    "Sib Minore Naturale": ["Sib", "Do", "Reb", "Mib", "Fa", "Solb", "Lab"],
    "Si Minore Naturale": ["Si", "Do#", "Re", "Mi", "Fa#", "Sol", "La"],

    # Scale Pentatoniche Maggiori
    "Do Pentatonica Maggiore": ["Do", "Re", "Mi", "Sol", "La"],
    "Do# Pentatonica Maggiore": ["Do#", "Re#", "Mi#", "Sol#", "La#"],
    "Reb Pentatonica Maggiore": ["Reb", "Mib", "Fa", "Lab", "Sib"],
    "Re Pentatonica Maggiore": ["Re", "Mi", "Fa#", "La", "Si"],
    "Re# Pentatonica Maggiore": ["Re#", "Mi#", "Fa##", "La#", "Si#"],
    "Mib Pentatonica Maggiore": ["Mib", "Fa", "Sol", "Sib", "Do"],
    "Mi Pentatonica Maggiore": ["Mi", "Fa#", "Sol#", "Si", "Do#"],
    "Fa Pentatonica Maggiore": ["Fa", "Sol", "La", "Do", "Re"],
    "Fa# Pentatonica Maggiore": ["Fa#", "Sol#", "La#", "Do#", "Re#"],
    "Solb Pentatonica Maggiore": ["Solb", "Lab", "Sib", "Reb", "Mib"],
    "Sol Pentatonica Maggiore": ["Sol", "La", "Si", "Re", "Mi"],
    "Sol# Pentatonica Maggiore": ["Sol#", "La#", "Si#", "Re#", "Mi#"],
    "Lab Pentatonica Maggiore": ["Lab", "Sib", "Do", "Mib", "Fa"],
    "La Pentatonica Maggiore": ["La", "Si", "Do#", "Mi", "Fa#"],
    "La# Pentatonica Maggiore": ["La#", "Si#", "Do##", "Mi#", "Fa##"],
    "Sib Pentatonica Maggiore": ["Sib", "Do", "Re", "Fa", "Sol"],
    "Si Pentatonica Maggiore": ["Si", "Do#", "Re#", "Fa#", "Sol#"],

    # Scale Pentatoniche Minori
    "Do Pentatonica Minore": ["Do", "Mib", "Fa", "Sol", "Sib"],
    "Do# Pentatonica Minore": ["Do#", "Mi", "Fa#", "Sol#", "Si"],
    "Reb Pentatonica Minore": ["Reb", "Fb", "Solb", "Lab", "Dob"],
    "Re Pentatonica Minore": ["Re", "Fa", "Sol", "La", "Do"],
    "Re# Pentatonica Minore": ["Re#", "Fa#", "Sol#", "La#", "Do#"],
    "Mib Pentatonica Minore": ["Mib", "Solb", "Lab", "Sib", "Reb"],
    "Mi Pentatonica Minore": ["Mi", "Sol", "La", "Si", "Re"],
    "Fa Pentatonica Minore": ["Fa", "Lab", "Sib", "Do", "Mib"],
    "Fa# Pentatonica Minore": ["Fa#", "La", "Si", "Do#", "Mi"],
    "Solb Pentatonica Minore": ["Solb", "Sibb", "Dob", "Reb", "Fb"],
    "Sol Pentatonica Minore": ["Sol", "Sib", "Do", "Re", "Fa"],
    "Sol# Pentatonica Minore": ["Sol#", "Si", "Do#", "Re#", "Fa#"],
    "Lab Pentatonica Minore": ["Lab", "Dob", "Reb", "Mib", "Solb"],
    "La Pentatonica Minore": ["La", "Do", "Re", "Mi", "Sol"],
    "La# Pentatonica Minore": ["La#", "Do#", "Re#", "Mi#", "Sol#"],
    "Sib Pentatonica Minore": ["Sib", "Reb", "Mib", "Fa", "Lab"],
    "Si Pentatonica Minore": ["Si", "Re", "Mi", "Fa#", "La"],

    # Scale Blues
    "Do Blues": ["Do", "Mib", "Fa", "Fa#", "Sol", "Sib"],
    "Do# Blues": ["Do#", "Mi", "Fa#", "Sol", "Sol#", "Si"],
    "Reb Blues": ["Reb", "Fb", "Solb", "Sol", "Lab", "Dob"],
    "Re Blues": ["Re", "Fa", "Sol", "Sol#", "La", "Do"],
    "Re# Blues": ["Re#", "Fa#", "Sol#", "La", "La#", "Do#"],
    "Mib Blues": ["Mib", "Solb", "Lab", "La", "Sib", "Reb"],
    "Mi Blues": ["Mi", "Sol", "La", "La#", "Si", "Re"],
    "Fa Blues": ["Fa", "Lab", "Sib", "Si", "Do", "Mib"],
    "Fa# Blues": ["Fa#", "La", "Si", "Do", "Do#", "Mi"],
    "Solb Blues": ["Solb", "Sibb", "Dob", "Dob#", "Reb", "Fb"],
    "Sol Blues": ["Sol", "Sib", "Do", "Do#", "Re", "Fa"],
    "Sol# Blues": ["Sol#", "Si", "Do#", "Re", "Re#", "Fa#"],
    "Lab Blues": ["Lab", "Dob", "Reb", "Re", "Mib", "Solb"],
    "La Blues": ["La", "Do", "Re", "Re#", "Mi", "Sol"],
    "La# Blues": ["La#", "Do#", "Re#", "Mi", "Mi#", "Sol#"],
    "Sib Blues": ["Sib", "Reb", "Mib", "Mi", "Fa", "Lab"],
    "Si Blues": ["Si", "Re", "Mi", "Fa", "Fa#", "La"]
}



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
    
    # Accordi di Settima
    "Do Settima": ["Do", "Mi", "Sol", "Sib"],
    "Do# Settima": ["Do#", "Fa", "Sol#", "Si"],
    "Reb Settima": ["Reb", "Fa", "Lab", "Dob"],
    "Re Settima": ["Re", "Fa#", "La", "Do"],
    "Re# Settima": ["Re#", "Sol", "Si", "Do#"],
    "Mib Settima": ["Mib", "Sol", "Sib", "Reb"],
    "Mi Settima": ["Mi", "Sol#", "Si", "Re"],
    "Fa Settima": ["Fa", "La", "Do", "Mib"],
    "Fa# Settima": ["Fa#", "La#", "Do#", "Mi"],
    "Solb Settima": ["Solb", "Sib", "Reb", "Fab"],
    "Sol Settima": ["Sol", "Si", "Re", "Fa"],
    "Sol# Settima": ["Sol#", "Do", "Re#", "Fa#"],
    "Lab Settima": ["Lab", "Do", "Mib", "Solb"],
    "La Settima": ["La", "Do#", "Mi", "Sol"],
    "La# Settima": ["La#", "Re", "Fa", "Sol#"],
    "Sib Settima": ["Sib", "Re", "Fa", "Lab"],
    "Si Settima": ["Si", "Re#", "Fa#", "La"],
    
    # Accordi di Settima Minore
    "Do Settima Minore": ["Do", "Mib", "Sol", "Sib"],
    "Do# Settima Minore": ["Do#", "Mi", "Sol#", "Si"],
    "Reb Settima Minore": ["Reb", "Fab", "Lab", "Dob"],
    "Re Settima Minore": ["Re", "Fa", "La", "Do"],
    "Re# Settima Minore": ["Re#", "Fa#", "La#", "Do#"],
    "Mib Settima Minore": ["Mib", "Solb", "Sib", "Reb"],
    "Mi Settima Minore": ["Mi", "Sol", "Si", "Re"],
    "Fa Settima Minore": ["Fa", "Lab", "Do", "Mib"],
    "Fa# Settima Minore": ["Fa#", "La", "Do#", "Mi"],
    "Solb Settima Minore": ["Solb", "Sibb", "Reb", "Fab"],
    "Sol Settima Minore": ["Sol", "Sib", "Re", "Fa"],
    "Sol# Settima Minore": ["Sol#", "Si", "Re#", "Fa#"],
    "Lab Settima Minore": ["Lab", "Dob", "Mib", "Solb"],
    "La Settima Minore": ["La", "Do", "Mi", "Sol"],
    "La# Settima Minore": ["La#", "Do#", "Fa", "Sol#"],
    "Sib Settima Minore": ["Sib", "Reb", "Fa", "Lab"],
    "Si Settima Minore": ["Si", "Re", "Fa#", "La"],
    
    # Accordi di Sesta
    "Do Sesta": ["Do", "Mi", "Sol", "La"],
    "Do# Sesta": ["Do#", "Fa", "Sol#", "La#"],
    "Reb Sesta": ["Reb", "Fa", "Lab", "Sib"],
    "Re Sesta": ["Re", "Fa#", "La", "Si"],
    "Re# Sesta": ["Re#", "Sol", "Si", "Do"],
    "Mib Sesta": ["Mib", "Sol", "Sib", "Do"],
    "Mi Sesta": ["Mi", "Sol#", "Si", "Do#"],
    "Fa Sesta": ["Fa", "La", "Do", "Re"],
    "Fa# Sesta": ["Fa#", "La#", "Do#", "Re#"],
    "Solb Sesta": ["Solb", "Sib", "Reb", "Mib"],
    "Sol Sesta": ["Sol", "Si", "Re", "Mi"],
    "Sol# Sesta": ["Sol#", "Do", "Re#", "Fa"],
    "Lab Sesta": ["Lab", "Do", "Mib", "Fa"],
    "La Sesta": ["La", "Do#", "Mi", "Fa#"],
    "La# Sesta": ["La#", "Re", "Fa", "Sol"],
    "Sib Sesta": ["Sib", "Re", "Fa", "Sol"],
    "Si Sesta": ["Si", "Re#", "Fa#", "Sol#"],
    
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


accordi_tonalita = {
    # Scale maggiori
    "Do Maggiore": ["Do", "Re min", "Mi min", "Fa", "Sol", "La min", "Si dim"],
    "Sol Maggiore": ["Sol", "La min", "Si min", "Do", "Re", "Mi min", "Fa# dim"],
    "Re Maggiore": ["Re", "Mi min", "Fa# min", "Sol", "La", "Si min", "Do# dim"],
    "La Maggiore": ["La", "Si min", "Do# min", "Re", "Mi", "Fa# min", "Sol# dim"],
    "Mi Maggiore": ["Mi", "Fa# min", "Sol# min", "La", "Si", "Do# min", "Re# dim"],
    "Si Maggiore": ["Si", "Do# min", "Re# min", "Mi", "Fa#", "Sol# min", "La# dim"],
    "Fa# Maggiore": ["Fa#", "Sol# min", "La# min", "Si", "Do#", "Re# min", "Mi# dim"],
    "Do# Maggiore": ["Do#", "Re# min", "Mi# min", "Fa#", "Sol#", "La# min", "Si# dim"],
    
    "Fa Maggiore": ["Fa", "Sol min", "La min", "Sib", "Do", "Re min", "Mi dim"],
    "Sib Maggiore": ["Sib", "Do min", "Re min", "Mib", "Fa", "Sol min", "La dim"],
    "Mib Maggiore": ["Mib", "Fa min", "Sol min", "Lab", "Sib", "Do min", "Re dim"],
    "Lab Maggiore": ["Lab", "Sib min", "Do min", "Reb", "Mib", "Fa min", "Sol dim"],
    "Reb Maggiore": ["Reb", "Mib min", "Fa min", "Solb", "Lab", "Sib min", "Do dim"],
    "Solb Maggiore": ["Solb", "Lab min", "Sib min", "Dob", "Reb", "Mib min", "Fa dim"],
    "Dob Maggiore": ["Dob", "Reb min", "Mib min", "Fab", "Solb", "Lab min", "Sib dim"],
    
    # Scale minori naturali
    "La Minore": ["La min", "Si dim", "Do", "Re min", "Mi min", "Fa", "Sol"],
    "Mi Minore": ["Mi min", "Fa# dim", "Sol", "La min", "Si min", "Do", "Re"],
    "Si Minore": ["Si min", "Do# dim", "Re", "Mi min", "Fa# min", "Sol", "La"],
    "Fa# Minore": ["Fa# min", "Sol# dim", "La", "Si min", "Do# min", "Re", "Mi"],
    "Do# Minore": ["Do# min", "Re# dim", "Mi", "Fa# min", "Sol# min", "La", "Si"],
    "Sol# Minore": ["Sol# min", "La# dim", "Si", "Do# min", "Re# min", "Mi", "Fa#"],
    "Re# Minore": ["Re# min", "Mi# dim", "Fa#", "Sol# min", "La# min", "Si", "Do#"],
    "La# Minore": ["La# min", "Si# dim", "Do#", "Re# min", "Mi# min", "Fa#", "Sol#"],
    
    "Re Minore": ["Re min", "Mi dim", "Fa", "Sol min", "La min", "Sib", "Do"],
    "Sol Minore": ["Sol min", "La dim", "Sib", "Do min", "Re min", "Mib", "Fa"],
    "Do Minore": ["Do min", "Re dim", "Mib", "Fa min", "Sol min", "Lab", "Sib"],
    "Fa Minore": ["Fa min", "Sol dim", "Lab", "Sib min", "Do min", "Reb", "Mib"],
    "Sib Minore": ["Sib min", "Do dim", "Reb", "Mib min", "Fa min", "Solb", "Lab"],
    "Mib Minore": ["Mib min", "Fa dim", "Solb", "Lab min", "Sib min", "Dob", "Reb"],
    "Lab Minore": ["Lab min", "Sib dim", "Dob", "Reb min", "Mib min", "Fab", "Solb"]
}



accordi_quadriadi_tonalita = {
    # Scale maggiori
    "Do Maggiore": [
        "Do maj7", "Re min7", "Mi min7", "Fa maj7", "Sol7", "La min7", "Si min7b5"
    ],
    "Sol Maggiore": [
        "Sol maj7", "La min7", "Si min7", "Do maj7", "Re7", "Mi min7", "Fa# min7b5"
    ],
    "Re Maggiore": [
        "Re maj7", "Mi min7", "Fa# min7", "Sol maj7", "La7", "Si min7", "Do# min7b5"
    ],
    "La Maggiore": [
        "La maj7", "Si min7", "Do# min7", "Re maj7", "Mi7", "Fa# min7", "Sol# min7b5"
    ],
    "Mi Maggiore": [
        "Mi maj7", "Fa# min7", "Sol# min7", "La maj7", "Si7", "Do# min7", "Re# min7b5"
    ],
    "Si Maggiore": [
        "Si maj7", "Do# min7", "Re# min7", "Mi maj7", "Fa#7", "Sol# min7", "La# min7b5"
    ],
    "Fa# Maggiore": [
        "Fa# maj7", "Sol# min7", "La# min7", "Si maj7", "Do#7", "Re# min7", "Mi# min7b5"
    ],
    "Do# Maggiore": [
        "Do# maj7", "Re# min7", "Mi# min7", "Fa# maj7", "Sol#7", "La# min7", "Si# min7b5"
    ],
    
    "Fa Maggiore": [
        "Fa maj7", "Sol min7", "La min7", "Sib maj7", "Do7", "Re min7", "Mi min7b5"
    ],
    "Sib Maggiore": [
        "Sib maj7", "Do min7", "Re min7", "Mib maj7", "Fa7", "Sol min7", "La min7b5"
    ],
    "Mib Maggiore": [
        "Mib maj7", "Fa min7", "Sol min7", "Lab maj7", "Sib7", "Do min7", "Re min7b5"
    ],
    "Lab Maggiore": [
        "Lab maj7", "Sib min7", "Do min7", "Reb maj7", "Mib7", "Fa min7", "Sol min7b5"
    ],
    "Reb Maggiore": [
        "Reb maj7", "Mib min7", "Fa min7", "Solb maj7", "Lab7", "Sib min7", "Do min7b5"
    ],
    "Solb Maggiore": [
        "Solb maj7", "Lab min7", "Sib min7", "Dob maj7", "Reb7", "Mib min7", "Fa min7b5"
    ],
    "Dob Maggiore": [
        "Dob maj7", "Reb min7", "Mib min7", "Fab maj7", "Solb7", "Lab min7", "Sib min7b5"
    ],
    
    # Scale minori naturali
    "La Minore": [
        "La min7", "Si min7b5", "Do maj7", "Re min7", "Mi min7", "Fa maj7", "Sol7"
    ],
    "Mi Minore": [
        "Mi min7", "Fa# min7b5", "Sol maj7", "La min7", "Si min7", "Do maj7", "Re7"
    ],
    "Si Minore": [
        "Si min7", "Do# min7b5", "Re maj7", "Mi min7", "Fa# min7", "Sol maj7", "La7"
    ],
    "Fa# Minore": [
        "Fa# min7", "Sol# min7b5", "La maj7", "Si min7", "Do# min7", "Re maj7", "Mi7"
    ],
    "Do# Minore": [
        "Do# min7", "Re# min7b5", "Mi maj7", "Fa# min7", "Sol# min7", "La maj7", "Si7"
    ],
    "Sol# Minore": [
        "Sol# min7", "La# min7b5", "Si maj7", "Do# min7", "Re# min7", "Mi maj7", "Fa#7"
    ],
    "Re# Minore": [
        "Re# min7", "Mi# min7b5", "Fa# maj7", "Sol# min7", "La# min7", "Si maj7", "Do#7"
    ],
    "La# Minore": [
        "La# min7", "Si# min7b5", "Do# maj7", "Re# min7", "Mi# min7", "Fa# maj7", "Sol#7"
    ],
    
    "Re Minore": [
        "Re min7", "Mi min7b5", "Fa maj7", "Sol min7", "La min7", "Sib maj7", "Do7"
    ],
    "Sol Minore": [
        "Sol min7", "La min7b5", "Sib maj7", "Do min7", "Re min7", "Mib maj7", "Fa7"
    ],
    "Do Minore": [
        "Do min7", "Re min7b5", "Mib maj7", "Fa min7", "Sol min7", "Lab maj7", "Sib7"
    ],
    "Fa Minore": [
        "Fa min7", "Sol min7b5", "Lab maj7", "Sib min7", "Do min7", "Reb maj7", "Mib7"
    ],
    "Sib Minore": [
        "Sib min7", "Do min7b5", "Reb maj7", "Mib min7", "Fa min7", "Solb maj7", "Lab7"
    ],
    "Mib Minore": [
        "Mib min7", "Fa min7b5", "Solb maj7", "Lab min7", "Sib min7", "Dob maj7", "Reb7"
    ],
    "Lab Minore": [
        "Lab min7", "Sib min7b5", "Dob maj7", "Reb min7", "Mib min7", "Fab maj7", "Solb7"
    ]
}
'''
Lista di 20 progressioni armoniche
[0, 3, 4, 0] → I - vi - V - I (Classico Pop)
[0, 4, 3, 5] → I - V - vi - IV (Pop moderno, usata in migliaia di hit)
[0, 3, 5, 4] → I - vi - IV - V (Molto comune nel rock e pop)
[0, 5, 3, 4] → I - IV - vi - V (Usata in ballate e power ballads)
[0, 3, 4, 5] → I - vi - V - IV (Variante molto orecchiabile)
[0, 5, 4, 3] → I - IV - V - vi (Molto usata nel soul e gospel)
[0, 4, 5, 3] → I - V - IV - vi (Pop e rock alternative)
[0, 3, 5, 1, 4] → I - vi - IV - ii - V (Jazz e R&B)
[0, 2, 5, 4] → I - iii - IV - V (Molto dolce e aperta)
[0, 3, 5, 6, 4] → I - vi - IV - vii° - V (Progressione con tensione tipica del jazz)
[0, 5, 1, 4, 3, 4] → I - IV - ii - V - vi - V (Tipica jazz standard)
[0, 3, 6, 4, 5] → I - vi - vii° - V - IV (Soul/R&B, molto usata da artisti come Stevie Wonder)
[0, 5, 4, 3, 2] → I - IV - V - vi - iii (Progressione con maggiore movimento)
[0, 4, 2, 5, 3] → I - V - iii - IV - vi (Alternative rock)
[0, 5, 3, 4, 6] → I - IV - vi - V - vii° (Più tensione, usata in jazz e musica orchestrale)
[0, 4, 3, 5, 4] → I - V - vi - IV - V (Molto pop-punk)
[0, 5, 4, 6, 2, 3] → I - IV - V - vii° - iii - vi (Progressione sofisticata)
[0, 2, 5, 4, 6] → I - iii - IV - V - vii° (Buona per armonie più dolci)
[0, 3, 5, 4, 2, 5] → I - vi - IV - V - iii - IV (Tipico del soft rock)
[0, 6, 4, 5, 3, 2] → I - vii° - IV - V - vi - iii (Più tensione e risoluzione)
'''

progressioni_classiche = [
    [0, 3, 4, 0], [0, 4, 3, 5], [0, 3, 5, 4], [0, 5, 3, 4], 
    [0, 3, 4, 5], [0, 5, 4, 3], [0, 4, 5, 3], [0, 3, 5, 1, 4], 
    [0, 2, 5, 4], [0, 3, 5, 6, 4], [0, 5, 1, 4, 3, 4], [0, 3, 6, 4, 5], 
    [0, 5, 4, 3, 2], [0, 4, 2, 5, 3], [0, 5, 3, 4, 6], [0, 4, 3, 5, 4], 
    [0, 5, 4, 6, 2, 3], [0, 2, 5, 4, 6], [0, 3, 5, 4, 2, 5], [0, 6, 4, 5, 3, 2]
]




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
        note_cromatiche = note_cromatiche_diesis if set(scale[scalascelta]) & set(note_cromatiche_diesis) else note_cromatiche_bemolle

# Determinare se la scala usa diesis o bemolli
       # usa_diesis = any('#' in nota for nota in scale[scalascelta])
       # note_cromatiche = note_cromatiche_diesis if usa_diesis else note_cromatiche_bemolle

 # Scegliere la scala cromatica basandosi sulla notazione della scala scelta
       # note_cromatiche = note_cromatiche_diesis if any('#' in nota for nota in scale[scalascelta]) else note_cromatiche_bemolle


        scala_originale = scale[scalascelta]
        scala_trasposta = []

        for nota in scala_originale:
            if nota in note_cromatiche:
                indice_originale = note_cromatiche.index(nota)
                nuovo_indice = (indice_originale + intervallo) % len(note_cromatiche)
                scala_trasposta.append(note_cromatiche[nuovo_indice])
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







#2
# Generare una progressione di accordi
#Chiedi all’utente una tonalità e genera una progressione armonica di quattro accordi basata sulla tonalità scelta.

import random




def progressore_accordi():
    print('\n\nprogressore di accordi\n\n')
    while True:
        # Chiedi la tonalità all'utente
        scelta_tonalita = input("Scegli la tonalità (es. Do Maggiore, La Minore):\n").strip().title()
        
        # Verifica se la tonalità è nel dizionario
        if scelta_tonalita in accordi_tonalita:
            # Recupera gli accordi per quella tonalità
            accordi_disponibili = accordi_tonalita[scelta_tonalita]
            
            # Scegli un pattern di progressione casuale
            pattern = random.choice(progressioni_classiche)
            
            # Genera la progressione di accordi
            progressione = [accordi_disponibili[i] for i in pattern]
            
            # Stampa il risultato
            print(f"\nProgressione di accordi in {scelta_tonalita}:")
            print(" - ".join(progressione))
            
            # Chiedi se vuole un'altra progressione
            continua = input("Vuoi un'altra progressione? (sì/no): ").strip().lower()
            if continua not in ["si", "sì"]:
                print('ciao ciao')
                break
        else:
            print(f"Tonalità '{scelta_tonalita}' non trovata. Prova con una delle seguenti:")
            print(", ".join(accordi_tonalita.keys()))

# Avvia il generatore di progressioni
progressore_accordi()






#3
#Filtrare note da una lista
#Chiedi all’utente una nota e rimuovila da una lista di note musicali.
#Stampa la lista aggiornata.


def listaaggiornata():
    print('\n\n Lista con note rimosse \n\n')

    scaladaoperare = input('che scala vuoi vedere?').strip().title()
    if scaladaoperare not in scale:
        print(f"Scala '{scaladaoperare}' non trovata.")
        return
    if scaladaoperare in scale:
        print(scale[scaladaoperare])

    notadalevare = input(f'che nota vuoi levare da questa scala: {scaladaoperare}?').strip().capitalize()

    if notadalevare in scale[scaladaoperare]:
        scale[scaladaoperare].remove(notadalevare)
        print(scale[scaladaoperare])


listaaggiornata ()

'''
Come risolverlo?
Modifica la lista direttamente, poi stampala:


scale[scaladaoperare].remove(notadalevare)
print(scale[scaladaoperare])
Qui, .remove() rimuove l'elemento e poi stampiamo direttamente la lista aggiornata.

Oppure crea una nuova lista senza la nota eliminata (senza .remove()):


nuovascala = [nota for nota in scale[scaladaoperare] if nota != notadalevare]
print(nuovascala)
Questo metodo non modifica la lista originale, ma ne crea una nuova con la nota rimossa.
'''



def lista_aggiornata():
    print("\n\nLista con note rimosse\n\n")

    scaladaoperare = input("Che scala vuoi vedere? ").strip().title()

    if scaladaoperare not in scale:
        print(f"Scala '{scaladaoperare}' non trovata.")
        return

    print(f"Scala originale: {scale[scaladaoperare]}")

    notadalevare = input(f"Quale nota vuoi rimuovere da {scaladaoperare}? ").strip().capitalize()

    if notadalevare in scale[scaladaoperare]:
        nuova_scala = [nota for nota in scale[scaladaoperare] if nota != notadalevare]
        print(f"Scala aggiornata senza '{notadalevare}': {nuova_scala}")
    else:
        print(f"La nota '{notadalevare}' non è presente nella scala {scaladaoperare}.")

lista_aggiornata()






#Conta le occorrenze di una nota in una sequenza
#Chiedi all’utente di inserire una sequenza di note. max 8
#conta quante volte compaiono le note


#Conta e mostra quante volte compare una specifica nota nella scala maggiore delle varie tonalità.


noteutente = input('dammi fino ad 8 note, ti dirò quante volte devi suonare ogni nota')

count = 0
notesingole = [noteutente.split()]
notesingole.count()

#for xnote in notesingole:
 #   if note == note:
  #      count














#Generare una melodia casuale
#Usa una lista di note e genera una sequenza casuale di 8 note.
#Stampa la melodia generata.


#Ordinare le note alfabeticamente
#Chiedi all’utente una lista di note e ordinala in ordine alfabetico.
#Stampa la lista ordinata.