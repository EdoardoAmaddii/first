note_ = ["Do", "Do#/Reb", "Re", "Re#/Mib", "Mi", "Fa", "Fa#/Solb", "Sol", "Sol#/Lab", "La", "La#/Sib", "Si"]




# Note cromatiche con diesis e bemolle
note_cromatiche = {
    "diesis": [
        "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"
    ],
    "bemolle": [
        "Do", "c", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib", "Si"
    ]
}

# Note in notazione anglosassone
note_anglosassoni = {
    "C": "Do",     "C#": "Do#",    "D": "Re",     "D#": "Re#",    "E": "Mi",
    "F": "Fa",     "F#": "Fa#",    "G": "Sol",    "G#": "Sol#",   "A": "La",
    "A#": "La#",   "B": "Si",     "Cb": "Do",    "B#": "Do#",    "Db": "Re",
    "Eb": "Mib",   "Fb": "Mi",    "Gb": "Fa",    "Ab": "Sol",    "Bb": "Lab"
}
# Intervalli musicali (in semitoni)
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


'''
# Un dizionario per i nomi degli intervalli con i loro valori di semitoni (potresti usarlo per trovare un intervallo tra due note)
def intervallo_tra_noti(nota1, nota2):
    # Troviamo gli indici delle due note nelle note cromatiche
    note_cromatiche_diesis = note_cromatiche["diesis"]
    
    try:
        index1 = note_cromatiche_diesis.index(nota1)
        index2 = note_cromatiche_diesis.index(nota2)
    except ValueError:
        return "Nota non valida"
    
    # Calcoliamo la differenza tra gli indici per trovare l'intervallo
    intervallo = (index2 - index1) % 12  # Ci assicuriamo che l'intervallo sia positivo e compreso tra 0 e 12
    
    # Ritorniamo l'intervallo in base ai semitoni
    for nome, semitoni in intervalli.items():
        if intervallo == semitoni:
            return nome
    return "Intervallo non trovato"

# Esempio di utilizzo
print(intervallo_tra_noti("Do", "Mi"))  # Output: "terza maggiore"
'''




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
    "Si Blues": ["Si", "Re", "Mi", "Fa", "Fa#", "La"],

    "Do Minore Armonica": ["Do", "Re", "Mib", "Fa", "Sol", "Lab", "Si"],
    "Do# Minore Armonica": ["Do#", "Re#", "Mi", "Fa#", "Sol#", "La", "Si#"],
    "Reb Minore Armonica": ["Reb", "Mib", "Fb", "Solb", "Lab", "Sibb", "Do"],
    "Re Minore Armonica": ["Re", "Mi", "Fa", "Sol", "La", "Sib", "Do#"],
    "Re# Minore Armonica": ["Re#", "Mi#", "Fa#", "Sol#", "La#", "Si", "Do##"],
    "Mib Minore Armonica": ["Mib", "Fa", "Solb", "Lab", "Sib", "Dob", "Re"],
    "Mi Minore Armonica": ["Mi", "Fa#", "Sol", "La", "Si", "Do", "Re#"],
    "Fa Minore Armonica": ["Fa", "Sol", "Lab", "Sib", "Do", "Reb", "Mi"],
    "Fa# Minore Armonica": ["Fa#", "Sol#", "La", "Si", "Do#", "Re", "Mi#"],
    "Sol Minore Armonica": ["Sol", "La", "Sib", "Do", "Re", "Mib", "Fa#"],
    "Sol# Minore Armonica": ["Sol#", "La#", "Si", "Do#", "Re#", "Mi", "Fa##"],
    "Lab Minore Armonica": ["Lab", "Sib", "Dob", "Reb", "Mib", "Fb", "Sol"],
    "La Minore Armonica": ["La", "Si", "Do", "Re", "Mi", "Fa", "Sol#"],
    "La# Minore Armonica": ["La#", "Si#", "Do#", "Re#", "Mi#", "Fa#", "Sol##"],
    "Sib Minore Armonica": ["Sib", "Do", "Reb", "Mib", "Fa", "Solb", "La"],
    "Si Minore Armonica": ["Si", "Do#", "Re", "Mi", "Fa#", "Sol", "La#"],

    "Do Minore Melodica": ["Do", "Re", "Mib", "Fa", "Sol", "La", "Si"],
    "Do# Minore Melodica": ["Do#", "Re#", "Mi", "Fa#", "Sol#", "La#", "Si#"],
    "Reb Minore Melodica": ["Reb", "Mib", "Fb", "Solb", "Lab", "Sib", "Do"],
    "Re Minore Melodica": ["Re", "Mi", "Fa", "Sol", "La", "Si", "Do#"],
    "Re# Minore Melodica": ["Re#", "Mi#", "Fa#", "Sol#", "La#", "Si#", "Do##"],
    "Mib Minore Melodica": ["Mib", "Fa", "Solb", "Lab", "Sib", "Do", "Re"],
    "Mi Minore Melodica": ["Mi", "Fa#", "Sol", "La", "Si", "Do#", "Re#"],
    "Fa Minore Melodica": ["Fa", "Sol", "Lab", "Sib", "Do", "Re", "Mi"],
    "Fa# Minore Melodica": ["Fa#", "Sol#", "La", "Si", "Do#", "Re#", "Mi#"],
    "Sol Minore Melodica": ["Sol", "La", "Sib", "Do", "Re", "Mi", "Fa#"],
    "Sol# Minore Melodica": ["Sol#", "La#", "Si", "Do#", "Re#", "Mi#", "Fa##"],
    "Lab Minore Melodica": ["Lab", "Sib", "Dob", "Reb", "Mib", "Fa", "Sol"],
    "La Minore Melodica": ["La", "Si", "Do", "Re", "Mi", "Fa#", "Sol#"],
    "La# Minore Melodica": ["La#", "Si#", "Do#", "Re#", "Mi#", "Fa##", "Sol##"],
    "Sib Minore Melodica": ["Sib", "Do", "Reb", "Mib", "Fa", "Sol", "La"],
    "Si Minore Melodica": ["Si", "Do#", "Re", "Mi", "Fa#", "Sol#", "La#"]
}


# Aggiungiamo le scale modali principali
scale_modali = {
    # Scale Doriche (secondo modo)
    "Do Dorica": ["Do", "Re", "Mib", "Fa", "Sol", "La", "Sib"],
    "Do# Dorica": ["Do#", "Re#", "Mi", "Fa#", "Sol#", "La#", "Si"],
    "Re Dorica": ["Re", "Mi", "Fa", "Sol", "La", "Si", "Do"],
    "Mib Dorica": ["Mib", "Fa", "Solb", "Lab", "Sib", "Do", "Reb"],
    "Mi Dorica": ["Mi", "Fa#", "Sol", "La", "Si", "Do#", "Re"],
    "Fa Dorica": ["Fa", "Sol", "Lab", "Sib", "Do", "Re", "Mib"],
    "Fa# Dorica": ["Fa#", "Sol#", "La", "Si", "Do#", "Re#", "Mi"],
    "Sol Dorica": ["Sol", "La", "Sib", "Do", "Re", "Mi", "Fa"],
    "Lab Dorica": ["Lab", "Sib", "Dob", "Reb", "Mib", "Fa", "Solb"],
    "La Dorica": ["La", "Si", "Do", "Re", "Mi", "Fa#", "Sol"],
    "Sib Dorica": ["Sib", "Do", "Reb", "Mib", "Fa", "Sol", "Lab"],
    "Si Dorica": ["Si", "Do#", "Re", "Mi", "Fa#", "Sol#", "La"],

    # Scale Frigie (terzo modo)
    "Do Frigia": ["Do", "Reb", "Mib", "Fa", "Sol", "Lab", "Sib"],
    "Do# Frigia": ["Do#", "Re", "Mi", "Fa#", "Sol#", "La", "Si"],
    "Re Frigia": ["Re", "Mib", "Fa", "Sol", "La", "Sib", "Do"],
    "Mib Frigia": ["Mib", "Fb", "Solb", "Lab", "Sib", "Dob", "Reb"],
    "Mi Frigia": ["Mi", "Fa", "Sol", "La", "Si", "Do", "Re"],
    "Fa Frigia": ["Fa", "Solb", "Lab", "Sib", "Do", "Reb", "Mib"],
    "Fa# Frigia": ["Fa#", "Sol", "La", "Si", "Do#", "Re", "Mi"],
    "Sol Frigia": ["Sol", "Lab", "Sib", "Do", "Re", "Mib", "Fa"],
    "Lab Frigia": ["Lab", "Sibb", "Dob", "Reb", "Mib", "Fb", "Solb"],
    "La Frigia": ["La", "Sib", "Do", "Re", "Mi", "Fa", "Sol"],
    "Sib Frigia": ["Sib", "Dob", "Reb", "Mib", "Fa", "Solb", "Lab"],
    "Si Frigia": ["Si", "Do", "Re", "Mi", "Fa#", "Sol", "La"],

    # Scale Lidie (quarto modo)
    "Do Lidia": ["Do", "Re", "Mi", "Fa#", "Sol", "La", "Si"],
    "Do# Lidia": ["Do#", "Re#", "Mi#", "Sol", "Sol#", "La#", "Si#"],
    "Re Lidia": ["Re", "Mi", "Fa#", "Sol#", "La", "Si", "Do#"],
    "Mib Lidia": ["Mib", "Fa", "Sol", "La", "Sib", "Do", "Re"],
    "Mi Lidia": ["Mi", "Fa#", "Sol#", "La#", "Si", "Do#", "Re#"],
    "Fa Lidia": ["Fa", "Sol", "La", "Si", "Do", "Re", "Mi"],
    "Fa# Lidia": ["Fa#", "Sol#", "La#", "Do", "Do#", "Re#", "Mi#"],
    "Sol Lidia": ["Sol", "La", "Si", "Do#", "Re", "Mi", "Fa#"],
    "Lab Lidia": ["Lab", "Sib", "Do", "Re", "Mib", "Fa", "Sol"],
    "La Lidia": ["La", "Si", "Do#", "Re#", "Mi", "Fa#", "Sol#"],
    "Sib Lidia": ["Sib", "Do", "Re", "Mi", "Fa", "Sol", "La"],
    "Si Lidia": ["Si", "Do#", "Re#", "Mi#", "Fa#", "Sol#", "La#"],

    # Scale Misolidie (quinto modo)
    "Do Misolidia": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Sib"],
    "Do# Misolidia": ["Do#", "Re#", "Mi#", "Fa#", "Sol#", "La#", "Si"],
    "Re Misolidia": ["Re", "Mi", "Fa#", "Sol", "La", "Si", "Do"],
    "Mib Misolidia": ["Mib", "Fa", "Sol", "Lab", "Sib", "Do", "Reb"],
    "Mi Misolidia": ["Mi", "Fa#", "Sol#", "La", "Si", "Do#", "Re"],
    "Fa Misolidia": ["Fa", "Sol", "La", "Sib", "Do", "Re", "Mib"],
    "Fa# Misolidia": ["Fa#", "Sol#", "La#", "Si", "Do#", "Re#", "Mi"],
    "Sol Misolidia": ["Sol", "La", "Si", "Do", "Re", "Mi", "Fa"],
    "Lab Misolidia": ["Lab", "Sib", "Do", "Reb", "Mib", "Fa", "Solb"],
    "La Misolidia": ["La", "Si", "Do#", "Re", "Mi", "Fa#", "Sol"],
    "Sib Misolidia": ["Sib", "Do", "Re", "Mib", "Fa", "Sol", "Lab"],
    "Si Misolidia": ["Si", "Do#", "Re#", "Mi", "Fa#", "Sol#", "La"],

    # Scale Locrie (settimo modo)
    "Do Locria": ["Do", "Reb", "Mib", "Fa", "Solb", "Lab", "Sib"],
    "Do# Locria": ["Do#", "Re", "Mi", "Fa#", "Sol", "La", "Si"],
    "Re Locria": ["Re", "Mib", "Fa", "Sol", "Lab", "Sib", "Do"],
    "Mib Locria": ["Mib", "Fb", "Solb", "Lab", "Sibb", "Dob", "Reb"],
    "Mi Locria": ["Mi", "Fa", "Sol", "La", "Sib", "Do", "Re"],
    "Fa Locria": ["Fa", "Solb", "Lab", "Sib", "Dob", "Reb", "Mib"],
    "Fa# Locria": ["Fa#", "Sol", "La", "Si", "Do", "Re", "Mi"],
    "Sol Locria": ["Sol", "Lab", "Sib", "Do", "Reb", "Mib", "Fa"],
    "Lab Locria": ["Lab", "Sibb", "Dob", "Reb", "Fbb", "Fb", "Solb"],
    "La Locria": ["La", "Sib", "Do", "Re", "Mib", "Fa", "Sol"],
    "Sib Locria": ["Sib", "Dob", "Reb", "Mib", "Fb", "Solb", "Lab"],
    "Si Locria": ["Si", "Do", "Re", "Mi", "Fa", "Sol", "La"]
}
'''
# Aggiungiamo le scale diminuite (ottafoniche)
# Esistono solo due scale diminuite per via della loro simmetria
scale_diminuite = {
    # Scala diminuita dominante (Semitono-Tono)
    "Do Diminuita": ["Do", "Reb", "Mib", "Mi", "Fa#", "Sol", "La", "Sib"],
    "Do# Diminuita": ["Do#", "Re", "Mi", "Fa", "Sol", "Lab", "La#", "Si"],
    "Re Diminuita": ["Re", "Mib", "Fa", "Fa#", "Sol#", "La", "Si", "Do"],
    "Mib Diminuita": ["Mib", "Fb", "Solb", "Sol", "La", "Sib", "Do", "Reb"],
    "Mi Diminuita": ["Mi", "Fa", "Sol", "Lab", "Sib", "Si", "Do#", "Re"],
    "Fa Diminuita": ["Fa", "Solb", "Lab", "La", "Si", "Do", "Re", "Mib"],
    "Fa# Diminuita": ["Fa#", "Sol", "La", "Sib", "Do", "Do#", "Re#", "Mi"],
    "Sol Diminuita": ["Sol", "Lab", "Sib", "Si", "Do#", "Re", "Mi", "Fa"],
    "Lab Diminuita": ["Lab", "La", "Si", "Do", "Re", "Mib", "Fa", "Solb"],
    "La Diminuita": ["La", "Sib", "Do", "Do#", "Re#", "Mi", "Fa#", "Sol"],
    "Sib Diminuita": ["Sib", "Si", "Do#", "Re", "Mi", "Fa", "Sol", "Lab"],
    "Si Diminuita": ["Si", "Do", "Re", "Mib", "Fa", "Fa#", "Sol#", "La"],

    # Scala diminuita semidiminuita (Tono-Semitono)
    "Do Semidiminuita": ["Do", "Re", "Mib", "Fa", "Solb", "Lab", "La", "Si"],
    "Do# Semidiminuita": ["Do#", "Re#", "Mi", "Fa#", "Sol", "La", "La#", "Do"],
    "Re Semidiminuita": ["Re", "Mi", "Fa", "Sol", "Lab", "Sib", "Si", "Do#"],
    "Mib Semidiminuita": ["Mib", "Fa", "Solb", "Lab", "La", "Si", "Do", "Re"],
    "Mi Semidiminuita": ["Mi", "Fa#", "Sol", "La", "Sib", "Do", "Do#", "Re#"],
    "Fa Semidiminuita": ["Fa", "Sol", "Lab", "Sib", "Si", "Do#", "Re", "Mi"],
    "Fa# Semidiminuita": ["Fa#", "Sol#", "La", "Si", "Do", "Re", "Re#", "Fa"],
    "Sol Semidiminuita": ["Sol", "La", "Sib", "Do", "Do#", "Re#", "Mi", "Fa#"],
    "Lab Semidiminuita": ["Lab", "Sib", "Si", "Do#", "Re", "Mi", "Fa", "Sol"],
    "La Semidiminuita": ["La", "Si", "Do", "Re", "Re#", "Fa", "Fa#", "Sol#"],
    "Sib Semidiminuita": ["Sib", "Do", "Do#", "Re#", "Mi", "Fa#", "Sol", "La"],
    "Si Semidiminuita": ["Si", "Do#", "Re", "Mi", "Fa", "Sol", "Sol#", "La#"]
}

# Aggiungiamo le scale esatonali (per toni interi)
# Esistono solo due scale esatonali possibili per via della loro simmetria
scale_esatonali = {
    "Do Esatonale": ["Do", "Re", "Mi", "Fa#", "Sol#", "La#"],
    "Do# Esatonale": ["Do#", "Re#", "Fa", "Sol", "La", "Si"],
    "Re Esatonale": ["Re", "Mi", "Fa#", "Sol#", "La#", "Do"],
    "Mib Esatonale": ["Mib", "Fa", "Sol", "La", "Si", "Do#"],
    "Mi Esatonale": ["Mi", "Fa#", "Sol#", "La#", "Do", "Re"],
    "Fa Esatonale": ["Fa", "Sol", "La", "Si", "Do#", "Re#"],
    "Fa# Esatonale": ["Fa#", "Sol#", "La#", "Do", "Re", "Mi"],
    "Sol Esatonale": ["Sol", "La", "Si", "Do#", "Re#", "Fa"],
    "Lab Esatonale": ["Lab", "Sib", "Do", "Re", "Mi", "Fa#"],
    "La Esatonale": ["La", "Si", "Do#", "Re#", "Fa", "Sol"],
    "Sib Esatonale": ["Sib", "Do", "Re", "Mi", "Fa#", "Sol#"],
    "Si Esatonale": ["Si", "Do#", "Re#", "Fa", "Sol", "La"]
}





# Scale Alterate per il Jazz Moderno

scale_jazz_moderne = {
    # Scala Alterata (Superlocria)
    "Do Alterata": ["Do", "Reb", "Mib", "Fb", "Solb", "Lab", "Sib"],
    "Do# Alterata": ["Do#", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Re Alterata": ["Re", "Mib", "Fa", "Solb", "Lab", "Sib", "Do"],
    "Mib Alterata": ["Mib", "Fb", "Solb", "Sob", "Sibb", "Dob", "Reb"],
    "Mi Alterata": ["Mi", "Fa", "Sol", "Lab", "Sib", "Do", "Re"],
    "Fa Alterata": ["Fa", "Solb", "Lab", "Sibb", "Dob", "Reb", "Mib"],
    "Fa# Alterata": ["Fa#", "Sol", "La", "Sib", "Do", "Re", "Mi"],
    "Sol Alterata": ["Sol", "Lab", "Sib", "Dob", "Reb", "Mib", "Fa"],
    "Lab Alterata": ["Lab", "Sibb", "Dob", "Rebb", "Mibb", "Fb", "Solb"],
    "La Alterata": ["La", "Sib", "Do", "Reb", "Mib", "Fa", "Sol"],
    "Sib Alterata": ["Sib", "Dob", "Reb", "Fbb", "Solb", "Lab", "Sib"],
    "Si Alterata": ["Si", "Do", "Re", "Mib", "Fa", "Sol", "La"],

    # Scala Lidia Dominante (Lidia b7)
    "Do Lidia Dominante": ["Do", "Re", "Mi", "Fa#", "Sol", "La", "Sib"],
    "Do# Lidia Dominante": ["Do#", "Re#", "Mi#", "Sol", "Sol#", "La#", "Si"],
    "Re Lidia Dominante": ["Re", "Mi", "Fa#", "Sol#", "La", "Si", "Do"],
    "Mib Lidia Dominante": ["Mib", "Fa", "Sol", "La", "Sib", "Do", "Reb"],
    "Mi Lidia Dominante": ["Mi", "Fa#", "Sol#", "La#", "Si", "Do#", "Re"],
    "Fa Lidia Dominante": ["Fa", "Sol", "La", "Si", "Do", "Re", "Mib"],
    "Fa# Lidia Dominante": ["Fa#", "Sol#", "La#", "Do", "Do#", "Re#", "Mi"],
    "Sol Lidia Dominante": ["Sol", "La", "Si", "Do#", "Re", "Mi", "Fa"],
    "Lab Lidia Dominante": ["Lab", "Sib", "Do", "Re", "Mib", "Fa", "Solb"],
    "La Lidia Dominante": ["La", "Si", "Do#", "Re#", "Mi", "Fa#", "Sol"],
    "Sib Lidia Dominante": ["Sib", "Do", "Re", "Mi", "Fa", "Sol", "Lab"],
    "Si Lidia Dominante": ["Si", "Do#", "Re#", "Mi#", "Fa#", "Sol#", "La"],

    # Scala Lidia Aumentata
    "Do Lidia Aumentata": ["Do", "Re", "Mi", "Fa#", "Sol#", "La", "Si"],
    "Do# Lidia Aumentata": ["Do#", "Re#", "Mi#", "Sol", "Sol##", "La#", "Si#"],
    "Re Lidia Aumentata": ["Re", "Mi", "Fa#", "Sol#", "La#", "Si", "Do#"],
    "Mib Lidia Aumentata": ["Mib", "Fa", "Sol", "La", "Si", "Do", "Re"],
    "Mi Lidia Aumentata": ["Mi", "Fa#", "Sol#", "La#", "Si#", "Do#", "Re#"],
    "Fa Lidia Aumentata": ["Fa", "Sol", "La", "Si", "Do#", "Re", "Mi"],
    "Fa# Lidia Aumentata": ["Fa#", "Sol#", "La#", "Do", "Re", "Re#", "Mi#"],
    "Sol Lidia Aumentata": ["Sol", "La", "Si", "Do#", "Re#", "Mi", "Fa#"],
    "Lab Lidia Aumentata": ["Lab", "Sib", "Do", "Re", "Mi", "Fa", "Sol"],
    "La Lidia Aumentata": ["La", "Si", "Do#", "Re#", "Mi#", "Fa#", "Sol#"],
    "Sib Lidia Aumentata": ["Sib", "Do", "Re", "Mi", "Fa#", "Sol", "La"],
    "Si Lidia Aumentata": ["Si", "Do#", "Re#", "Mi#", "Fa##", "Sol#", "La#"]
}


# Scale Jazz Moderne Addizionali

scale_jazz_avanzate = {
    # Scala Simmetrica Aumentata
    "Do Simmetrica Aumentata": ["Do", "Do#", "Mi", "Fa", "Sol#", "La", "Do"],
    "Do# Simmetrica Aumentata": ["Do#", "Re", "Fa", "Fa#", "La", "La#", "Do#"],
    "Re Simmetrica Aumentata": ["Re", "Re#", "Fa#", "Sol", "La#", "Si", "Re"],
    "Mib Simmetrica Aumentata": ["Mib", "Mi", "Sol", "Lab", "Si", "Do", "Mib"],
    "Mi Simmetrica Aumentata": ["Mi", "Fa", "Lab", "La", "Do", "Do#", "Mi"],
    "Fa Simmetrica Aumentata": ["Fa", "Fa#", "La", "La#", "Do#", "Re", "Fa"],
    "Fa# Simmetrica Aumentata": ["Fa#", "Sol", "La#", "Si", "Re", "Re#", "Fa#"],
    "Sol Simmetrica Aumentata": ["Sol", "Lab", "Si", "Do", "Re#", "Mi", "Sol"],
    "Lab Simmetrica Aumentata": ["Lab", "La", "Do", "Do#", "Mi", "Fa", "Lab"],
    "La Simmetrica Aumentata": ["La", "La#", "Do#", "Re", "Fa", "Fa#", "La"],
    "Sib Simmetrica Aumentata": ["Sib", "Si", "Re", "Re#", "Fa#", "Sol", "Sib"],
    "Si Simmetrica Aumentata": ["Si", "Do", "Re#", "Mi", "Sol", "Lab", "Si"],

    # Scala Bebop Dominante
    "Do Bebop Dominante": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Sib", "Si"],
    "Do# Bebop Dominante": ["Do#", "Re#", "Mi#", "Fa#", "Sol#", "La#", "Si", "Do"],
    "Re Bebop Dominante": ["Re", "Mi", "Fa#", "Sol", "La", "Si", "Do", "Do#"],
    "Mib Bebop Dominante": ["Mib", "Fa", "Sol", "Lab", "Sib", "Do", "Reb", "Re"],
    "Mi Bebop Dominante": ["Mi", "Fa#", "Sol#", "La", "Si", "Do#", "Re", "Re#"],
    "Fa Bebop Dominante": ["Fa", "Sol", "La", "Sib", "Do", "Re", "Mib", "Mi"],
    "Fa# Bebop Dominante": ["Fa#", "Sol#", "La#", "Si", "Do#", "Re#", "Mi", "Fa"],
    "Sol Bebop Dominante": ["Sol", "La", "Si", "Do", "Re", "Mi", "Fa", "Fa#"],
    "Lab Bebop Dominante": ["Lab", "Sib", "Do", "Reb", "Mib", "Fa", "Solb", "Sol"],
    "La Bebop Dominante": ["La", "Si", "Do#", "Re", "Mi", "Fa#", "Sol", "Sol#"],
    "Sib Bebop Dominante": ["Sib", "Do", "Re", "Mib", "Fa", "Sol", "Lab", "La"],
    "Si Bebop Dominante": ["Si", "Do#", "Re#", "Mi", "Fa#", "Sol#", "La", "La#"],

    # Scala Bebop Maggiore
    "Do Bebop Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "Lab", "La", "Si"],
    "Do# Bebop Maggiore": ["Do#", "Re#", "Mi#", "Fa#", "Sol#", "La", "La#", "Do"],
    "Re Bebop Maggiore": ["Re", "Mi", "Fa#", "Sol", "La", "Sib", "Si", "Do#"],
    "Mib Bebop Maggiore": ["Mib", "Fa", "Sol", "Lab", "Sib", "Si", "Do", "Re"],
    "Mi Bebop Maggiore": ["Mi", "Fa#", "Sol#", "La", "Si", "Do", "Do#", "Re#"],
    "Fa Bebop Maggiore": ["Fa", "Sol", "La", "Sib", "Do", "Reb", "Re", "Mi"],
    "Fa# Bebop Maggiore": ["Fa#", "Sol#", "La#", "Si", "Do#", "Re", "Re#", "Fa"],
    "Sol Bebop Maggiore": ["Sol", "La", "Si", "Do", "Re", "Mib", "Mi", "Fa#"],
    "Lab Bebop Maggiore": ["Lab", "Sib", "Do", "Reb", "Mib", "Mi", "Fa", "Sol"],
    "La Bebop Maggiore": ["La", "Si", "Do#", "Re", "Mi", "Fa", "Fa#", "Sol#"],
    "Sib Bebop Maggiore": ["Sib", "Do", "Re", "Mib", "Fa", "Solb", "Sol", "La"],
    "Si Bebop Maggiore": ["Si", "Do#", "Re#", "Mi", "Fa#", "Sol", "Sol#", "La#"],

    # Scala Maggiore Armonica
    "Do Maggiore Armonica": ["Do", "Re", "Mi", "Fa", "Sol", "Lab", "Si"],
    "Do# Maggiore Armonica": ["Do#", "Re#", "Mi#", "Fa#", "Sol#", "La", "Si#"],
    "Re Maggiore Armonica": ["Re", "Mi", "Fa#", "Sol", "La", "Sib", "Do#"],
    "Mib Maggiore Armonica": ["Mib", "Fa", "Sol", "Lab", "Sib", "Dob", "Re"],
    "Mi Maggiore Armonica": ["Mi", "Fa#", "Sol#", "La", "Si", "Do", "Re#"],
    "Fa Maggiore Armonica": ["Fa", "Sol", "La", "Sib", "Do", "Reb", "Mi"],
    "Fa# Maggiore Armonica": ["Fa#", "Sol#", "La#", "Si", "Do#", "Re", "Mi#"],
    "Sol Maggiore Armonica": ["Sol", "La", "Si", "Do", "Re", "Mib", "Fa#"],
    "Lab Maggiore Armonica": ["Lab", "Sib", "Do", "Reb", "Mib", "Fb", "Sol"],
    "La Maggiore Armonica": ["La", "Si", "Do#", "Re", "Mi", "Fa", "Sol#"],
    "Sib Maggiore Armonica": ["Sib", "Do", "Re", "Mib", "Fa", "Solb", "La"],
    "Si Maggiore Armonica": ["Si", "Do#", "Re#", "Mi", "Fa#", "Sol", "La#"],

    # Scala Minore Melodica Ascendente Dominante (4° modo della melodica)
    "Do Melodica Dominante": ["Do", "Re", "Mi", "Fa#", "Sol", "La", "Sib"],
    "Do# Melodica Dominante": ["Do#", "Re#", "Mi#", "Sol", "Sol#", "La#", "Si"],
    "Re Melodica Dominante": ["Re", "Mi", "Fa#", "Sol#", "La", "Si", "Do"],
    "Mib Melodica Dominante": ["Mib", "Fa", "Sol", "La", "Sib", "Do", "Reb"],
    "Mi Melodica Dominante": ["Mi", "Fa#", "Sol#", "La#", "Si", "Do#", "Re"],
    "Fa Melodica Dominante": ["Fa", "Sol", "La", "Si", "Do", "Re", "Mib"],
    "Fa# Melodica Dominante": ["Fa#", "Sol#", "La#", "Do", "Do#", "Re#", "Mi"],
    "Sol Melodica Dominante": ["Sol", "La", "Si", "Do#", "Re", "Mi", "Fa"],
    "Lab Melodica Dominante": ["Lab", "Sib", "Do", "Re", "Mib", "Fa", "Solb"],
    "La Melodica Dominante": ["La", "Si", "Do#", "Re#", "Mi", "Fa#", "Sol"],
    "Sib Melodica Dominante": ["Sib", "Do", "Re", "Mi", "Fa", "Sol", "Lab"],
    "Si Melodica Dominante": ["Si", "Do#", "Re#", "Mi#", "Fa#", "Sol#", "La"]
}

scale_orientali_struttura = {
    "Scala Minore Ungherese": {
        "Struttura": "T - S - T+S - S - S - T+S - S",
        "Caratteristica": "Introduce un intervallo aumentato tra il secondo e il terzo grado, offrendo un sound distintivo e drammatico."
    },
    "Scala Giapponese (In Sen)": {
        "Struttura": "T - T - T+S - T - T+S",
        "Caratteristica": "Scala pentatonica utilizzata nella musica tradizionale giapponese, offre un suono evocativo per passaggi melodici."
    },
    "Scala Persiana": {
        "Struttura": "S - T+S - T - S - S - T+S - S",
        "Caratteristica": "Conosciuta per l'intervallo di tre semitoni al secondo grado, crea atmosfere esotiche e misteriose."
    },
    "Scala Araba": {
        "Struttura": "T+S - S - T+S - S - S - T+S - S",
        "Caratteristica": "Presenta due intervalli aumentati, conferendo un sound medio-orientale distintivo."
    },
    "Scala Hindu": {
        "Struttura": "T - S - T+S - S - T - S - T",
        "Caratteristica": "Utilizzata nella musica classica indiana, offre un suono ricco e complesso."
    },
    "Scala Balinese": {
        "Struttura": "T+S - S - T - T - T",
        "Caratteristica": "Pentatonica con intervalli unici, crea un sound esotico e suggestivo."
    },
    "Scala Tzigana": {
        "Struttura": "T - T - S - T - S - T+S - S",
        "Caratteristica": "Scala zigana, nota per il suo intervallo aumentato al sesto grado, crea un sound drammatico e caratteristico."
    },
    "Scala Pelog": {
        "Struttura": "T+S - S - T+S - S - T+S - S - S",
        "Caratteristica": "Utilizzata nella musica gamelan indonesiana, offre un suono distintivo e mistico."
    },
    "Scala Kumoi": {
        "Struttura": "T - S - T+S - T - T",
        "Caratteristica": "Pentatonica giapponese con un sound delicato e melodico."
    },
    "Scala Hijaz": {
        "Struttura": "S - T+S - S - T - S - T+S - S",
        "Caratteristica": "Scala araba con un intervallo aumentato al secondo grado, crea un suono esotico e malinconico."
    }
}

print(scale_orientali_struttura)

scale_orientali = {
    "Scala Minore Ungherese": {
        "Do": ["Do", "Re", "Mib", "Fa#", "Sol", "Lab", "Si"],
        "Do#": ["Do#", "Re#", "Mi", "Sol", "Sol#", "La", "Do"],
        "Re": ["Re", "Mi", "Fa", "Sol#", "La", "Sib", "Do#"],
        "Mib": ["Mib", "Fa", "Solb", "La", "Sib", "Do", "Re"],
        "Mi": ["Mi", "Fa#", "Sol", "La#", "Si", "Do#", "Re#"],
        "Fa": ["Fa", "Sol", "Lab", "Si", "Do", "Reb", "Mi"],
        "Fa#": ["Fa#", "Sol#", "La", "Do", "Do#", "Re", "Fa"],
        "Sol": ["Sol", "La", "Sib", "Reb", "Re", "Mi", "Fa#"],
        "Lab": ["Lab", "Sib", "Si", "Re", "Mib", "Fa", "Sol"],
        "La": ["La", "Si", "Do", "Re#", "Mi", "Fa#", "Sol#"],
        "Sib": ["Sib", "Do", "Reb", "Mi", "Fa", "Sol", "La"],
        "Si": ["Si", "Do#", "Re", "Fa", "Fa#", "Sol#", "La#"]
    },
    "Scala Giapponese (In Sen)": {
        "Do": ["Do", "Re", "Mib", "Sol", "La"],
        "Do#": ["Do#", "Re#", "Mi", "Sol#", "La#"],
        "Re": ["Re", "Mi", "Fa", "La", "Si"],
        "Mib": ["Mib", "Fa", "Solb", "Lab", "Si"],
        "Mi": ["Mi", "Fa#", "Sol", "La", "Do#"],
        "Fa": ["Fa", "Sol", "Lab", "Si", "Do"],
        "Fa#": ["Fa#", "Sol#", "La", "Do", "Re"],
        "Sol": ["Sol", "La", "Sib", "Reb", "Re"],
        "Lab": ["Lab", "Sib", "Si", "Re", "Mi"],
        "La": ["La", "Si", "Do", "Re#", "Mi"],
        "Sib": ["Sib", "Do", "Reb", "Mi", "Sol"],
        "Si": ["Si", "Do#", "Re", "Fa", "Sol#"]
    },
    "Scala Giapponese (Yo Sen)": {
        "Do": ["Do", "Re", "Mi", "Sol", "La"],
        "Do#": ["Do#", "Re#", "Mi#", "Sol#", "La#"],
        "Re": ["Re", "Mi", "Fa#", "Sol", "La"],
        "Re#": ["Re#", "Mi#", "Fa#", "Sol#", "La#"],
        "Mi": ["Mi", "Fa#", "Sol#", "La", "Si"],
        "Fa": ["Fa", "Sol", "La", "Do", "Re"],
        "Fa#": ["Fa#", "Sol#", "La#", "Do#", "Re#"],
        "Sol": ["Sol", "La", "Si", "Re", "Mi"],
        "Sol#": ["Sol#", "La#", "Si", "Re#", "Mi#"],
        "La": ["La", "Si", "Do", "Mi", "Fa"],
        "La#": ["La#", "Si#", "Do#", "Mi#", "Fa#"],
        "Si": ["Si", "Do#", "Re", "Fa#", "Sol#"]
    },

    "Scala Persiana": {
        "Do": ["Do", "Reb", "Mi", "Fa", "Solb", "Lab", "Si"],
        "Do#": ["Do#", "Re", "Mi#", "Fa#", "Sol", "La", "Do"],
        "Re": ["Re", "Mib", "Fa#", "Sol", "Lab", "Sib", "Do#"],
        "Mib": ["Mib", "Mi", "Sol", "Lab", "La", "Si", "Re"],
        "Mi": ["Mi", "Fa", "Sol#", "La", "Sib", "Do#", "Re#"],
        "Fa": ["Fa", "Solb", "La", "Sib", "Do", "Re", "Mi"],
        "Fa#": ["Fa#", "Sol", "La#", "Si", "Do#", "Mib", "Fa"],
        "Sol": ["Sol", "Lab", "Si", "Do", "Reb", "Mi", "Sol#"],
        "Lab": ["Lab", "La", "Do", "Reb", "Re", "Fa", "Sol"],
        "La": ["La", "Sib", "Do#", "Re", "Mib", "Fa#", "Sol#"],
        "Sib": ["Sib", "Si", "Re", "Mi", "Fa", "Sol#", "La"],
        "Si": ["Si", "Do", "Re#", "Fa", "Sol", "La", "Si"]
    },
    "Scala Araba": {
        "Do": ["Do", "Reb", "Mi", "Fa", "Solb", "Lab", "Si"],
        "Do#": ["Do#", "Re", "Mi#", "Fa#", "Sol", "La", "Do"],
        "Re": ["Re", "Mib", "Fa#", "Sol", "Lab", "Sib", "Do#"],
        "Mib": ["Mib", "Mi", "Sol", "Lab", "La", "Si", "Re"],
        "Mi": ["Mi", "Fa", "Sol#", "La", "Sib", "Do#", "Re#"],
        "Fa": ["Fa", "Solb", "La", "Sib", "Do", "Re", "Mi"],
        "Fa#": ["Fa#", "Sol", "La#", "Si", "Do#", "Mib", "Fa"],
        "Sol": ["Sol", "Lab", "Si", "Do", "Reb", "Mi", "Sol#"],
        "Lab": ["Lab", "La", "Do", "Reb", "Re", "Fa", "Sol"],
        "La": ["La", "Sib", "Do#", "Re", "Mib", "Fa#", "Sol#"],
        "Sib": ["Sib", "Si", "Re", "Mi", "Fa", "Sol#", "La"],
        "Si": ["Si", "Do", "Re#", "Fa", "Sol", "La", "Si"]
    },
    "Scala Hindu": {
        "Do": ["Do", "Re", "Mib", "Fa#", "Sol", "Lab", "Si"],
        "Do#": ["Do#", "Re#", "Mi", "Sol", "Sol#", "La", "Do"],
        "Re": ["Re", "Mi", "Fa", "Sol#", "La", "Sib", "Do#"],
        "Mib": ["Mib", "Fa", "Solb", "La", "Sib", "Do", "Re"],
        "Mi": ["Mi", "Fa#", "Sol", "La#", "Si", "Do#", "Re#"],
        "Fa": ["Fa", "Sol", "Lab", "Si", "Do", "Reb", "Mi"],
        "Fa#": ["Fa#", "Sol#", "La", "Do", "Do#", "Re", "Fa"],
        "Sol": ["Sol", "La", "Sib", "Reb", "Re", "Mi", "Fa#"],
        "Lab": ["Lab", "Sib", "Si", "Re", "Mib", "Fa", "Solb"],
        "La": ["La", "Si", "Do", "Re#", "Mi", "Fa#", "Sol#"],
        "Sib": ["Sib", "Do", "Reb", "Mi", "Fa", "Sol", "Lab"],
        "Si": ["Si", "Do#", "Re", "Fa", "Fa#", "Sol#", "La#"]
    },
    "Scala Balinese": {
        "Do": ["Do", "Reb", "Mi", "Sol", "Lab"],
        "Do#": ["Do#", "Re", "Mi#", "Sol#", "La"],
        "Re": ["Re", "Mib", "Fa", "La", "Sib"],
        "Mib": ["Mib", "Mi", "Sol", "Lab", "Si"],
        "Mi": ["Mi", "Fa", "Sol#", "La", "Do"],
        "Fa": ["Fa", "Solb", "La", "Sib", "Do#"],
        "Fa#": ["Fa#", "Sol", "La#", "Si", "Re"],
        "Sol": ["Sol", "Lab", "Si", "Do", "Re#"],
        "Lab": ["Lab", "La", "Do", "Re", "Fa"],
        "La": ["La", "Sib", "Do#", "Re", "Sol"],
        "Sib": ["Sib", "Si", "Re", "Mi", "Solb"],
        "Si": ["Si", "Do", "Re#", "Fa", "La"]
    },
    "Scala Tzigana": {
        "Do": ["Do", "Re", "Mib", "Fa", "Solb", "La", "Si"],
        "Do#": ["Do#", "Re#", "Mi", "Fa#", "Sol", "La#", "Do"],
        "Re": ["Re", "Mi", "Fa", "Sol", "Lab", "Sib", "Do#"],
        "Mib": ["Mib", "Fa", "Solb", "Lab", "La", "Si", "Re"],
        "Mi": ["Mi", "Fa#", "Sol", "La", "Sib", "Do#", "Re#"],
        "Fa": ["Fa", "Sol", "Lab", "Si", "Do", "Reb", "Mi"],
        "Fa#": ["Fa#", "Sol#", "La", "Do", "Do#", "Re", "Fa"],
        "Sol": ["Sol", "La", "Sib", "Reb", "Re", "Mi", "Fa#"],
        "Lab": ["Lab", "Sib", "Si", "Re", "Mib", "Fa", "Solb"],
        "La": ["La", "Si", "Do", "Re#", "Mi", "Fa#", "Sol#"],
        "Sib": ["Sib", "Do", "Reb", "Mi", "Fa", "Sol", "Lab"],
        "Si": ["Si", "Do#", "Re", "Fa", "Fa#", "Sol#", "La#"]
    },

    "Scala Pelog": {
        "Do": ["Do", "Reb", "Mi", "Fa", "Solb", "Lab", "Si"],
        "Do#": ["Do#", "Re", "Mi#", "Fa#", "Sol", "La", "Do"],
        "Re": ["Re", "Mib", "Fa", "Sol", "Lab", "Si", "Do#"],
        "Mib": ["Mib", "Mi", "Sol", "Lab", "La", "Si", "Re"],
        "Mi": ["Mi", "Fa", "Sol#", "La", "Sib", "Do#", "Re#"],
        "Fa": ["Fa", "Solb", "La", "Sib", "Do", "Re", "Mi"],
        "Fa#": ["Fa#", "Sol", "La#", "Si", "Do#", "Mib", "Fa"],
        "Sol": ["Sol", "Lab", "Si", "Do", "Reb", "Mi", "Sol#"],
        "Lab": ["Lab", "La", "Do", "Reb", "Re", "Fa", "Sol"],
        "La": ["La", "Sib", "Do#", "Re", "Mib", "Fa#", "Sol#"],
        "Sib": ["Sib", "Si", "Re", "Mi", "Fa", "Sol#", "La"],
        "Si": ["Si", "Do", "Re#", "Fa", "Sol", "La", "Si"]
    },
    "Scala Kumoi": {
        "Do": ["Do", "Re", "Mib", "Sol", "La"],
        "Do#": ["Do#", "Re#", "Mi", "Sol#", "La#"],
        "Re": ["Re", "Mi", "Fa", "La", "Si"],
        "Mib": ["Mib", "Fa", "Solb", "Lab", "Si"],
        "Mi": ["Mi", "Fa#", "Sol", "La", "Do#"],
        "Fa": ["Fa", "Sol", "Lab", "Si", "Do"],
        "Fa#": ["Fa#", "Sol#", "La", "Do", "Re"],
        "Sol": ["Sol", "La", "Sib", "Reb", "Re"],
        "Lab": ["Lab", "Sib", "Si", "Re", "Mi"],
        "La": ["La", "Si", "Do", "Re#", "Mi"],
        "Sib": ["Sib", "Do", "Reb", "Mi", "Sol"],
        "Si": ["Si", "Do#", "Re", "Fa", "Sol#"]
    },
    "Scala Hijaz": {
        "Do": ["Do", "Reb", "Mi", "Fa", "Sol", "Lab", "Si"],
        "Do#": ["Do#", "Re", "Mi#", "Fa#", "Sol#", "La", "Do"],
        "Re": ["Re", "Mib", "Fa#", "Sol", "Lab", "Sib", "Do#"],
        "Mib": ["Mib", "Mi", "Sol", "Lab", "La", "Si", "Re"],
        "Mi": ["Mi", "Fa", "Sol#", "La", "Sib", "Do#", "Re#"],
        "Fa": ["Fa", "Solb", "La", "Sib", "Do", "Re", "Mi"],
        "Fa#": ["Fa#", "Sol", "La#", "Si", "Do#", "Mib", "Fa"],
        "Sol": ["Sol", "Lab", "Si", "Do", "Reb", "Mi", "Sol#"],
        "Lab": ["Lab", "La", "Do", "Reb", "Re", "Fa", "Sol"],
        "La": ["La", "Sib", "Do#", "Re", "Mib", "Fa#", "Sol#"],
        "Sib": ["Sib", "Si", "Re", "Mi", "Fa", "Sol#", "La"],
        "Si": ["Si", "Do", "Re#", "Fa", "Sol", "La", "Si"]
    },

    "Tibetana": {
        "Do": ["Do", "Reb", "Mi", "Fa", "Sol", "Lab", "Si"],
        "Do#": ["Do#", "Re", "Mi#", "Fa#", "Sol#", "La", "Si#"],
        "Re": ["Re", "Mib", "Fa", "Sol", "Lab", "Si", "Do"],
        "Re#": ["Re#", "Fa", "Sol", "La", "Si", "Do#", "Re"],
        "Mi": ["Mi", "Fa", "Sol", "La", "Si", "Do", "Re"],
        "Fa": ["Fa", "Solb", "Lab", "Si", "Do", "Re", "Mi"],
        "Fa#": ["Fa#", "Sol", "La", "Si", "Do#", "Re#", "Mi#"],
        "Sol": ["Sol", "Lab", "Si", "Do", "Re", "Mi", "Fa"],
        "Sol#": ["Sol#", "La", "Si", "Do#", "Re#", "Mi#", "Fa#"],
        "La": ["La", "Sib", "Do", "Re", "Mi", "Fa", "Sol"],
        "La#": ["La#", "Si", "Do#", "Re#", "Mi#", "Fa#", "Sol#"],
        "Si": ["Si", "Do", "Re", "Mi", "Fa#", "Sol#", "La"]
    }
}
'''






accordi = {
    # Accordatura per C
    "C": ["Do", "Mi", "Sol"],
    "Cm": ["Do", "Mib", "Sol"],
    "C7": ["Do", "Mi", "Sol", "Sib"],
    "Cm7": ["Do", "Mib", "Sol", "Sib"],
    "Cmaj7": ["Do", "Mi", "Sol", "Si"],
    "Cdim": ["Do", "Mib", "Solb"],
    "Cdim7": ["Do", "Mib", "Solb", "La"],
    "Caug": ["Do", "Mi", "Sol#"],
    "C6": ["Do", "Mi", "Sol", "La"],
    "Cm6": ["Do", "Mib", "Sol", "La"],
    "C9": ["Do", "Mi", "Sol", "Sib", "Re"],
    "Cm9": ["Do", "Mib", "Sol", "Sib", "Re"],
    "Cmaj9": ["Do", "Mi", "Sol", "Si", "Re"],
    "C11": ["Do", "Mi", "Sol", "Sib", "Re", "Fa"],
    "Cmaj11": ["Do", "Mi", "Sol", "Si", "Re", "Fa"],
    "C13": ["Do", "Mi", "Sol", "Sib", "Re", "La"],
    "Cmaj13": ["Do", "Mi", "Sol", "Si", "Re", "La"],

    # Accordatura per F
    "F": ["Fa", "La", "Do"],
    "Fm": ["Fa", "Lab", "Do"],
    "F7": ["Fa", "La", "Do", "Mib"],
    "Fm7": ["Fa", "Lab", "Do", "Mib"],
    "Fmaj7": ["Fa", "La", "Do", "Mi"],
    "Fdim": ["Fa", "Lab", "Dobb"],
    "Fdim7": ["Fa", "Lab", "Dobb", "Re"],
    "Faug": ["Fa", "La", "Do#"],
    "F6": ["Fa", "La", "Do", "Re"],
    "Fm6": ["Fa", "Lab", "Do", "Re"],
    "F9": ["Fa", "La", "Do", "Mib", "Sol"],
    "Fm9": ["Fa", "Lab", "Do", "Mib", "Sol"],
    "Fmaj9": ["Fa", "La", "Do", "Mi", "Sol"],
    "F11": ["Fa", "La", "Do", "Mib", "Sol", "Sib"],
    "Fmaj11": ["Fa", "La", "Do", "Mi", "Sol", "Sib"],
    "F13": ["Fa", "La", "Do", "Mib", "Sol", "Re"],
    "Fmaj13": ["Fa", "La", "Do", "Mi", "Sol", "Re"],

    # Accordi per B♭
    "Bb": ["Sib", "Re", "Fa"],
    "Bbm": ["Sib", "Dob", "Fa"],
    "Bb7": ["Sib", "Re", "Fa", "Lab"],
    "Bbm7": ["Sib", "Dob", "Fa", "Lab"],
    "Bbmaj7": ["Sib", "Re", "Fa", "La"],
    "Bbdim": ["Sib", "Dob", "Fab"],
    "Bbdim7": ["Sib", "Dob", "Fab", "Lab"],
    "Bbaug": ["Sib", "Re", "Solb"],
    "Bb6": ["Sib", "Re", "Fa", "Sol"],
    "Bbm6": ["Sib", "Dob", "Fa", "Sol"],
    "Bb9": ["Sib", "Re", "Fa", "Lab", "Do"],
    "Bbm9": ["Sib", "Dob", "Fa", "Lab", "Do"],
    "Bbmaj9": ["Sib", "Re", "Fa", "La", "Do"],
    "Bb11": ["Sib", "Re", "Fa", "Lab", "Do", "Mib"],
    "Bbmaj11": ["Sib", "Re", "Fa", "La", "Do", "Mib"],
    "Bb13": ["Sib", "Re", "Fa", "Lab", "Do", "Sol"],
    "Bbmaj13": ["Sib", "Re", "Fa", "La", "Do", "Sol"],

    # Accordi di E♭
    "Eb": ["Mib", "Sol", "Sib"],
    "Ebm": ["Mib", "Solb", "Sib"],
    "Eb7": ["Mib", "Sol", "Sib", "Dob"],
    "Ebm7": ["Mib", "Solb", "Sib", "Dob"],
    "Ebmaj7": ["Mib", "Sol", "Sib", "Re"],
    "Ebdim": ["Mib", "Solb", "La"],
    "Ebdim7": ["Mib", "Solb", "La", "Do"],
    "Ebaug": ["Mib", "Sol", "Si"],
    "Eb6": ["Mib", "Sol", "Sib", "Do"],
    "Ebm6": ["Mib", "Solb", "Sib", "Do"],
    "Eb9": ["Mib", "Sol", "Sib", "Dob", "Fa"],
    "Ebm9": ["Mib", "Solb", "Sib", "Dob", "Fa"],
    "Ebmaj9": ["Mib", "Sol", "Sib", "Re", "Fa"],
    "Eb11": ["Mib", "Sol", "Sib", "Dob", "Fa", "Lab"],
    "Ebmaj11": ["Mib", "Sol", "Sib", "Re", "Fa", "Lab"],
    "Eb13": ["Mib", "Sol", "Sib", "Dob", "Fa", "Do"],
    "Ebmaj13": ["Mib", "Sol", "Sib", "Re", "Fa", "Do"],

    # Accordi di A♭
    "Ab": ["Lab", "Do", "Mib"],
    "Abm": ["Lab", "Si", "Mib"],
    "Ab7": ["Lab", "Do", "Mib", "Solb"],
    "Abm7": ["Lab", "Si", "Mib", "Solb"],
    "Abmaj7": ["Lab", "Do", "Mib", "Sol"],
    "Abdim": ["Lab", "Si", "Re"],
    "Abdim7": ["Lab", "Si", "Re", "Fa"],
    "Abaug": ["Lab", "Do", "Mi"],
    "Ab6": ["Lab", "Do", "Mib", "Fa"],
    "Abm6": ["Lab", "Si", "Mib", "Fa"],
    "Ab9": ["Lab", "Do", "Mib", "Solb", "Lab"],
    "Abm9": ["Lab", "Si", "Mib", "Solb", "Lab"],
    "Abmaj9": ["Lab", "Do", "Mib", "Sol", "Lab"],
    "Ab11": ["Lab", "Do", "Mib", "Solb", "Lab", "Dob"],
    "Abmaj11": ["Lab", "Do", "Mib", "Sol", "Lab", "Dob"],
    "Ab13": ["Lab", "Do", "Mib", "Solb", "Lab", "Re"],
    "Abmaj13": ["Lab", "Do", "Mib", "Sol", "Lab", "Re"],

    # Accordi di G
    "G": ["Sol", "Si", "Re"],
    "Gm": ["Sol", "Sib", "Re"],
    "G7": ["Sol", "Si", "Re", "Fa"],
    "Gm7": ["Sol", "Sib", "Re", "Fa"],
    "Gmaj7": ["Sol", "Si", "Re", "Fa#"],
    "Gdim": ["Sol", "Sib", "Dob"],
    "Gdim7": ["Sol", "Sib", "Dob", "Mi"],
    "Gaug": ["Sol", "Si", "Re#"],
    "G6": ["Sol", "Si", "Re", "Mi"],
    "Gm6": ["Sol", "Sib", "Re", "Mi"],
    "G9": ["Sol", "Si", "Re", "Fa", "La"],
    "Gm9": ["Sol", "Sib", "Re", "Fa", "La"],
    "Gmaj9": ["Sol", "Si", "Re", "Fa#", "La"],
    "G11": ["Sol", "Si", "Re", "Fa", "La", "Do"],
    "Gmaj11": ["Sol", "Si", "Re", "Fa#", "La", "Do"],
    "G13": ["Sol", "Si", "Re", "Fa", "La", "Do"],
    "Gmaj13": ["Sol", "Si", "Re", "Fa#", "La", "Do"],

    # Accordi di D
    "D": ["Re", "Fa#", "La"],
    "Dm": ["Re", "Fa", "La"],
    "D7": ["Re", "Fa#", "La", "Do"],
    "Dm7": ["Re", "Fa", "La", "Do"],
    "Dmaj7": ["Re", "Fa#", "La", "Do#"],
    "Ddim": ["Re", "Fa", "Lab"],
    "Ddim7": ["Re", "Fa", "Lab", "Do"],
    "Daug": ["Re", "Fa#", "La#"],
    "D6": ["Re", "Fa#", "La", "Si"],
    "Dm6": ["Re", "Fa", "La", "Si"],
    "D9": ["Re", "Fa#", "La", "Do", "Mi"],
    "Dm9": ["Re", "Fa", "La", "Do", "Mi"],
    "Dmaj9": ["Re", "Fa#", "La", "Do#", "Mi"],
    "D11": ["Re", "Fa#", "La", "Do", "Mi", "Sol"],
    "Dmaj11": ["Re", "Fa#", "La", "Do#", "Mi", "Sol"],
    "D13": ["Re", "Fa#", "La", "Do", "Mi", "Sol"],
    "Dmaj13": ["Re", "Fa#", "La", "Do#", "Mi", "Sol"],

    # Accordi di A
    "A": ["La", "Do#", "Mi"],
    "Am": ["La", "Do", "Mi"],
    "A7": ["La", "Do#", "Mi", "Sol"],
    "Am7": ["La", "Do", "Mi", "Sol"],
    "Amaj7": ["La", "Do#", "Mi", "Sol#"],
    "Adim": ["La", "Do", "Mib"],
    "Adim7": ["La", "Do", "Mib", "Re"],
    "Aaug": ["La", "Do#", "Mi#"],
    "A6": ["La", "Do#", "Mi", "Fa#"],
    "Am6": ["La", "Do", "Mi", "Fa#"],
    "A9": ["La", "Do#", "Mi", "Sol", "Si"],
    "Am9": ["La", "Do", "Mi", "Sol", "Si"],
    "Amaj9": ["La", "Do#", "Mi", "Sol#", "Si"],
    "A11": ["La", "Do#", "Mi", "Sol", "Si", "Re"],
    "Amaj11": ["La", "Do#", "Mi", "Sol#", "Si", "Re"],
    "A13": ["La", "Do#", "Mi", "Sol", "Si", "Re"],
    "Amaj13": ["La", "Do#", "Mi", "Sol#", "Si", "Re"],

    # Accordi di E
    "E": ["Mi", "Sol#", "Si"],
    "Em": ["Mi", "Sol", "Si"],
    "E7": ["Mi", "Sol#", "Si", "Re"],
    "Em7": ["Mi", "Sol", "Si", "Re"],
    "Emaj7": ["Mi", "Sol#", "Si", "Do#"],
    "Edim": ["Mi", "Sol", "Lab"],
    "Edim7": ["Mi", "Sol", "Lab", "Re"],
    "Eaug": ["Mi", "Sol#", "Do"],
    "E6": ["Mi", "Sol#", "Si", "Do#"],
    "Em6": ["Mi", "Sol", "Si", "Do#"],
    "E9": ["Mi", "Sol#", "Si", "Re", "Fa#"],
    "Em9": ["Mi", "Sol", "Si", "Re", "Fa#"],
    "Emaj9": ["Mi", "Sol#", "Si", "Do#", "Fa#"],
    "E11": ["Mi", "Sol#", "Si", "Re", "Fa#", "La"],
    "Emaj11": ["Mi", "Sol#", "Si", "Do#", "Fa#", "La"],
    "E13": ["Mi", "Sol#", "Si", "Re", "Fa#", "La"],
    "Emaj13": ["Mi", "Sol#", "Si", "Do#", "Fa#", "La"],

    # Accordi di C#
    "C#": ["Do#", "Fa", "Sol#"],
    "C#m": ["Do#", "Fa", "Sol"],
    "C#7": ["Do#", "Fa", "Sol#", "Si"],
    "C#m7": ["Do#", "Fa", "Sol", "Si"],
    "C#maj7": ["Do#", "Fa", "Sol#", "Do"],
    "C#dim": ["Do#", "Fa", "Sol"],
    "C#dim7": ["Do#", "Fa", "Sol", "Si"],
    "C#aug": ["Do#", "Fa", "Sol#"],
    "C#6": ["Do#", "Fa", "Sol#", "La"],
    "C#m6": ["Do#", "Fa", "Sol", "La"],
    "C#9": ["Do#", "Fa", "Sol#", "Si", "Re#"],
    "C#m9": ["Do#", "Fa", "Sol", "Si", "Re#"],
    "C#maj9": ["Do#", "Fa", "Sol#", "Do", "Re#"],
    "C#11": ["Do#", "Fa", "Sol#", "Si", "Re#", "Fa"],
    "C#maj11": ["Do#", "Fa", "Sol#", "Do", "Re#", "Fa"],
    "C#13": ["Do#", "Fa", "Sol#", "Si", "Re#", "La"],
    "C#maj13": ["Do#", "Fa", "Sol#", "Do", "Re#", "La"],

        # Accordi di B
    "B": ["Si", "Re#", "Fa#"],
    "Bm": ["Si", "Re", "Fa#"],
    "B7": ["Si", "Re#", "Fa#", "La"],
    "Bm7": ["Si", "Re", "Fa#", "La"],
    "Bmaj7": ["Si", "Re#", "Fa#", "Do#"],
    "Bdim": ["Si", "Re", "Fa"],
    "Bdim7": ["Si", "Re", "Fa", "Do"],
    "Baug": ["Si", "Re#", "Fa"],
    "B6": ["Si", "Re#", "Fa#", "Do#"],
    "Bm6": ["Si", "Re", "Fa#", "Do#"],
    "B9": ["Si", "Re#", "Fa#", "La", "Do#"],
    "Bm9": ["Si", "Re", "Fa#", "La", "Do#"],
    "Bmaj9": ["Si", "Re#", "Fa#", "Do#", "Do#"],
    "B11": ["Si", "Re#", "Fa#", "La", "Do#", "Mi"],
    "Bmaj11": ["Si", "Re#", "Fa#", "Do#", "Do#", "Mi"],
    "B13": ["Si", "Re#", "Fa#", "La", "Do#", "Mi"],
    "Bmaj13": ["Si", "Re#", "Fa#", "Do#", "Do#", "Mi"],

    # Accordi di F#
    "F#": ["Fa#", "La#", "Do#"],
    "F#m": ["Fa#", "La", "Do#"],
    "F#7": ["Fa#", "La#", "Do#", "Mi"],
    "F#m7": ["Fa#", "La", "Do#", "Mi"],
    "F#maj7": ["Fa#", "La#", "Do#", "Fa"],
    "F#dim": ["Fa#", "La", "Do"],
    "F#dim7": ["Fa#", "La", "Do", "Mi"],
    "F#aug": ["Fa#", "La#", "Do"],
    "F#6": ["Fa#", "La#", "Do#", "Re"],
    "F#m6": ["Fa#", "La", "Do#", "Re"],
    "F#9": ["Fa#", "La#", "Do#", "Mi", "Sol#"],
    "F#m9": ["Fa#", "La", "Do#", "Mi", "Sol#"],
    "F#maj9": ["Fa#", "La#", "Do#", "Fa", "Sol#"],
    "F#11": ["Fa#", "La#", "Do#", "Mi", "Sol#", "Do"],
    "F#maj11": ["Fa#", "La#", "Do#", "Fa", "Sol#", "Do"],
    "F#13": ["Fa#", "La#", "Do#", "Mi", "Sol#", "Re"],
    "F#maj13": ["Fa#", "La#", "Do#", "Fa", "Sol#", "Re"],

    # Accordi di G#
    "G#": ["Sol#", "Do", "Re#"],
    "G#m": ["Sol#", "Do", "Re"],
    "G#7": ["Sol#", "Do", "Re#", "Fa#"],
    "G#m7": ["Sol#", "Do", "Re", "Fa#"],
    "G#maj7": ["Sol#", "Do", "Re#", "Sol"],
    "G#dim": ["Sol#", "Do", "Re"],
    "G#dim7": ["Sol#", "Do", "Re", "Fa#"],
    "G#aug": ["Sol#", "Do", "Re#"],
    "G#6": ["Sol#", "Do", "Re#", "Fa"],
    "G#m6": ["Sol#", "Do", "Re", "Fa"],
    "G#9": ["Sol#", "Do", "Re#", "Fa#", "Si"],
    "G#m9": ["Sol#", "Do", "Re", "Fa#", "Si"],
    "G#maj9": ["Sol#", "Do", "Re#", "Sol", "Si"],
    "G#11": ["Sol#", "Do", "Re#", "Fa#", "Si", "Re"],
    "G#maj11": ["Sol#", "Do", "Re#", "Sol", "Si", "Re"],
    "G#13": ["Sol#", "Do", "Re#", "Fa#", "Si", "Re"],
    "G#maj13": ["Sol#", "Do", "Re#", "Sol", "Si", "Re"],
}






accordi_triadi_tonalita = {
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
# da riscrivere meglio
progressioni_base = {
    "progressione_0": {"gradi": [0, 5, 1, 4], "descrizione": "Turn Around"},
    "progressione_1": {"gradi": [0, 4, 5, 0], "descrizione": "Cadenza perfetta, stabile e risolutiva. Tipica nel rock e pop."},
    "progressione_2": {"gradi": [0, 5, 6, 4], "descrizione": "Molto usata nel pop, emotiva e aperta."},
    "progressione_3": {"gradi": [2, 5, 0], "descrizione": "Progressione jazz standard, perfetta per modulazioni."},
    "progressione_4": {"gradi": [0, 6, 4, 5], "descrizione": "Tipica delle ballate anni '50, armonia nostalgica."},
    "progressione_5": {"gradi": [0, 4, 0, 5], "descrizione": "Movimento classico con ritorno alla tonica prima della dominante."},
    "progressione_6": {"gradi": [6, 4, 0, 5], "descrizione": "Potente e malinconica, perfetta per brani emotivi."},
    "progressione_7": {"gradi": [0, 4, 6, 5], "descrizione": "Aperta e speranzosa, usata nel pop moderno."},
    "progressione_8": {"gradi": [0, 5, 4, 0], "descrizione": "Diretta e semplice, comune nel folk e rock classico."},
    "progressione_9": {"gradi": [0, 3, 4, 5], "descrizione": "Terzo grado minore crea un senso malinconico."},
    "progressione_10": {"gradi": [0, 5, 6, 3, 4], "descrizione": "Espressiva e cinematografica, usata nelle colonne sonore."},
    "progressione_11": {"gradi": [0, 2, 5, 0], "descrizione": "Armonia più aperta e leggera, usata nel folk."},
    "progressione_12": {"gradi": [0, 6, 2, 5], "descrizione": "Sospesa e malinconica, con tensione verso la dominante."},
    "progressione_13": {"gradi": [0, 4, 3, 5], "descrizione": "Un giro armonico equilibrato con un tocco di sorpresa."},
    "progressione_14": {"gradi": [0, 3, 5, 4], "descrizione": "Tipico giro rock/pop con colore minore interessante."},
    "progressione_15": {"gradi": [0, 5, 4, 2], "descrizione": "Fluida e morbida, con ritorno delicato alla tonica."}
}

progressioni_armoniche = {
    "progression_1": {"gradi": [0, 4, 5, 0], "descrizione": "Classica cadenza perfetta, molto stabile e risolutiva."},
    "progression_2": {"gradi": [0, 3, 4, 0], "descrizione": "Progressione dolce e nostalgica, usata in ballate."},
    "progression_3": {"gradi": [0, 5, 4, 0], "descrizione": "Tensione e rilascio con passaggio sul sottodominante prima della tonica."},
    "progression_4": {"gradi": [0, 2, 5, 0], "descrizione": "Movimento più aperto e leggermente malinconico."},
    "progression_5": {"gradi": [0, 3, 5, 4], "descrizione": "Tipica progressione pop/rock con un colore minore."},
    "progression_6": {"gradi": [0, 4, 2, 5], "descrizione": "Tensione e rilascio con un secondo grado sospensivo."},
    "progression_7": {"gradi": [0, 6, 4, 5], "descrizione": "Progressione pop malinconica, molto usata in power ballad."},
    "progression_8": {"gradi": [0, 2, 4, 5], "descrizione": "Carattere fresco e aperto, molto usata in folk e country."},
    "progression_9": {"gradi": [0, 5, 3, 4], "descrizione": "Giro armonico con passaggio minore che crea contrasto."},
    "progression_10": {"gradi": [0, 3, 6, 4], "descrizione": "Molto espressiva e drammatica, tipica del rock e pop emotivo."},
    
    "progression_11": {"gradi": [0, 2, 5, 4], "descrizione": "Suono leggero e pop, perfetto per melodie cantabili."},
    "progression_12": {"gradi": [0, 4, 5, 3], "descrizione": "Giro classico con finale malinconico."},
    "progression_13": {"gradi": [0, 3, 5, 6], "descrizione": "Intensa e sospesa, usata per creare tensione."},
    "progression_14": {"gradi": [0, 5, 4, 2], "descrizione": "Movimento fluido con un ritorno morbido alla tonica."},
    "progression_15": {"gradi": [0, 6, 5, 4], "descrizione": "Emozionale e struggente, tipica del pop e rock ballad."},
    "progression_16": {"gradi": [0, 2, 6, 4], "descrizione": "Molto aperta e sognante, spesso usata in colonne sonore."},
    "progression_17": {"gradi": [0, 3, 4, 5], "descrizione": "Progressione classica, con passaggio dolce tra minore e maggiore."},
    "progression_18": {"gradi": [0, 4, 3, 5], "descrizione": "Giro armonico equilibrato, adatto per pop e jazz."},
    "progression_19": {"gradi": [0, 5, 2, 4], "descrizione": "Movimento più sofisticato con un secondo grado interessante."},
    "progression_20": {"gradi": [0, 6, 2, 5], "descrizione": "Armonia sospesa con un forte senso di malinconia."},
    
    "progression_21": {"gradi": [0, 3, 2, 5], "descrizione": "Suono delicato con movimenti modali."},
    "progression_22": {"gradi": [0, 4, 6, 5], "descrizione": "Tensione crescente con risoluzione finale."},
    "progression_23": {"gradi": [0, 5, 6, 4], "descrizione": "Tipica del pop contemporaneo, molto melodica."},
    "progression_24": {"gradi": [0, 2, 3, 5], "descrizione": "Colore modale con atmosfera sospesa."},
    "progression_25": {"gradi": [0, 6, 5, 3], "descrizione": "Molto emotiva, perfetta per climax sonori."},
    "progression_26": {"gradi": [0, 3, 5, 2], "descrizione": "Progressione dolce con un finale sospensivo."},
    "progression_27": {"gradi": [0, 4, 2, 6], "descrizione": "Effetto sognante, molto usata nel dream pop."},
    "progression_28": {"gradi": [0, 5, 6, 2], "descrizione": "Armonia aperta e dal carattere epico."},
    "progression_29": {"gradi": [0, 6, 3, 5], "descrizione": "Suono oscuro e profondo, perfetto per il rock."},
    "progression_30": {"gradi": [0, 2, 4, 6], "descrizione": "Cambia colore rapidamente, creando dinamica."},
    "progression_31": {"gradi": [0, 3, 2, 6], "descrizione": "Struttura particolare con un senso di apertura."},
    "progression_32": {"gradi": [0, 4, 6, 3], "descrizione": "Intensa e cinematografica."},
    "progression_33": {"gradi": [0, 5, 2, 6], "descrizione": "Grande varietà armonica e flusso aperto."},
    "progression_34": {"gradi": [0, 6, 4, 2], "descrizione": "Perfetta per passaggi evocativi."},
    "progression_35": {"gradi": [0, 2, 5, 3], "descrizione": "Tensione e rilascio con una sfumatura malinconica."},
    "progression_36": {"gradi": [0, 3, 6, 2], "descrizione": "Melanconica e drammatica, perfetta per ballad."},
    "progression_37": {"gradi": [0, 4, 5, 6], "descrizione": "Giro tipico della musica pop."},
    "progression_38": {"gradi": [0, 5, 4, 6], "descrizione": "Cambio armonico molto espressivo."},
    "progression_39": {"gradi": [0, 6, 2, 3], "descrizione": "Tensione crescente, risoluzione finale."},
    "progression_40": {"gradi": [0, 2, 3, 6], "descrizione": "Atmosfera eterea e fluttuante."}
}




accordi_funzionali = {
    "Tonica": {
        "I": ["C", "Am"],
        "III": ["Em"],  # Terzo grado (minore) che aggiunge un senso di stabilità
        "VI": ["Am"]  # Sesto grado (minore) che rafforza la sensazione di tonica
    },
    "Sottodominante": ["IV", "II", "F", "Dm"],
    "Dominante": ["V", "VII", "G", "Bdim"],
    "Sostituto_Dominante": ["bVII", "Bb"],
    "Dominante_Secondaria": {
        "V7/II": "B7 → Em",
        "V7/III": "E7 → Am",
        "V7/IV": "C7 → F",
        "V7/V": "D7 → G"
    },
    "Prestito_Modale": {
        "bVI": "Ab",
        "bIII": "Eb",
        "bVII": "Bb"
    },
    "Tritono_Substitution": {
        "bII7": "Db7 (al posto di G7)"
    },
    "Doppia_Dominante": {
        "V7/V/V": "A7 → D7 → G7 → C"
    },
    "Dim e Aug": {
        "Diminuito": "Bdim → C",
        "Aumentato": "E+"
    }
}



def trova_accordi_funzionali(progressione, accordi_funzionali):
    accordi_complementari = []

    for grado in progressione:
        if grado == 0:
            accordi_complementari.append("Tonica")
        elif grado == 1:
            accordi_complementari.append("Sottodominante")
        elif grado == 2:
            accordi_complementari.append("Dominante")
        elif grado == 3:
            accordi_complementari.append("Dominante_Secondaria")
        elif grado == 4:
            accordi_complementari.append("Prestito_Modale")
        elif grado == 5:
            accordi_complementari.append("Tritono_Substitution")
        elif grado == 6:
            accordi_complementari.append("Doppia_Dominante")
    
    return accordi_complementari


# Esempio con la progressione_0
progressione = progressioni_base["progressione_0"]["gradi"]
accordi_complementari = trova_accordi_funzionali(progressione, accordi_funzionali)
print(accordi_complementari)











#####################################################################################
### Parte RITMO

# Tipi di Ritmi
tipi_di_ritmi = {
    "Ritmi Base": {
        "4/4": "Ritmo standard in molti generi musicali, come rock, pop e jazz.",
        "3/4": "Utilizzato principalmente nei valzer e in alcune forme di musica folk.",
        "6/8": "Comune nelle ballate e nelle marce lente."
    },
    "Ritmi Complessi": {
        "5/4": "Utilizzato in brani jazz sperimentali e progressive rock.",
        "7/8": "Trovato nella musica tradizionale balcanica e in alcuni brani di progressive rock."
    }
}
'''
pattern_ritmici = {
    "Pattern di Batteria": {
        "Facile": {
            "Backbeat": "Un pattern comune in molti generi musicali, con il rullante sui tempi 2 e 4.",
            "Four on the Floor": "Cassa su tutti e quattro i battiti, comune nella musica dance e pop.",
            "Basic Rock Beat": "Cassa sui tempi 1 e 3, rullante sui tempi 2 e 4, hi-hat in ottavi."
        },
        "Intermedio": {
            "Shuffle": "Un pattern swingato tipico del blues e del rock'n'roll.",
            "Funk Groove": "Pattern caratterizzato da un rullante sincopato e un forte accento sul primo tempo.",
            "Half-Time Shuffle": "Un groove sincopato con hi-hat swingato e ghost notes sul rullante, usato da Jeff Porcaro (Toto)."
        },
        "Avanzato": {
            "Jazz Swing": "Un pattern di swing con un'andatura terzinata e il rullante spesso sul secondo e quarto tempo.",
            "Reggae One Drop": "Pattern con il rullante sul terzo tempo e un utilizzo prominente del charleston.",
            "Linear Drumming": "Un pattern in cui nessun arto suona contemporaneamente, tipico del drumming avanzato."
        }
    },
    "Pattern di Percussioni": {
        "Facile": {
            "Clave Son": "Un pattern base nella musica afro-cubana, 3-2 o 2-3.",
            "Bossa Nova": "Un pattern brasiliano con accenti dolci e sincopati.",
            "Basic Conga Groove": "Un pattern in cui si alternano colpi bassi e slap sulle congas."
        },
        "Intermedio": {
            "Samba": "Un pattern brasiliano con ritmo veloce e accenti sincopati.",
            "Rumba Guaguancó": "Un groove sincopato con accenti distintivi sulle congas.",
            "Tumbao": "Un pattern tipico della salsa suonato sulle congas."
        },
        "Avanzato": {
            "Mozambique": "Un pattern complesso di origine cubana con un forte senso di movimento.",
            "Afrobeat Percussion": "Un groove poliritmico con interplay tra djembe e shaker.",
            "Candombe": "Un groove africano-uruguaiano con accenti particolari sui tamburi Candombe."
        }
    },
    "Pattern per Piano": {
        "Facile": {
            "Simple Block Chords": "Accordi suonati simultaneamente nei punti forti del ritmo.",
            "Boom-Chuck": "Alternanza tra basso e accordo, tipico dello stile country e folk.",
            "Basic Waltz": "Bassi suonati sul primo tempo, accordi sui successivi due tempi (tempo in 3/4)."
        },
        "Intermedio": {
            "Boogie Woogie": "Un ostinato di ottavi con la mano sinistra e una melodia sincopata con la destra.",
            "Bebop Comping": "Accordi sincopati e frasi brevi per accompagnare la melodia jazz.",
            "Latin Montuno": "Un pattern ripetitivo con accordi sincopati e percussivi."
        },
        "Avanzato": {
            "Stride Piano": "Alternanza rapida tra bassi e accordi, tipica del ragtime e dello swing.",
            "Blues Shuffle": "Struttura swingata con interplay tra basso e mano destra.",
            "Gospel Walkup": "Un passaggio armonico ascendente usato nel gospel e soul."
        }
    },
    "Pattern per Chitarra": {
        "Facile": {
            "Open Chord Strumming": "Plettro o dita sugli accordi aperti, ritmo costante.",
            "Palm Muted Power Chords": "Power chords stoppati con la mano destra per un suono ritmico.",
            "Reggae Skank": "Accordi stoppati suonati sul secondo e quarto tempo in levare."
        },
        "Intermedio": {
            "Funky Chops": "Accordi stoppati con ghost notes per un groove serrato.",
            "Blues Shuffle Strumming": "Un pattern blues in 12/8 con dinamica nelle pennate.",
            "Fingerpicking Arpeggio": "Un pattern in cui le dita suonano le corde in sequenza per creare armonie."
        },
        "Avanzato": {
            "Hybrid Picking": "Uso combinato di plettro e dita per velocità e dinamica.",
            "Fast Metal Gallop": "Un pattern ritmico tipico dell'heavy metal con pennate alternate veloci.",
            "Jazz Comping": "Accordi sincopati e voicings avanzati per accompagnamenti jazz."
        }
    },
    "Pattern per Basso": {
        "Facile": {
            "Root-Fifth Rock Groove": "Alternanza tra la tonica e la quinta per solidità ritmica.",
            "Basic Walking Bass": "Note fondamentali suonate con una progressione fluida.",
            "Disco Octaves": "Stesso suono su ottave diverse per un groove pulsante."
        },
        "Intermedio": {
            "Slap & Pop": "Colpi slap sul basso e pop sulle corde alte per un suono percussivo.",
            "Reggae One Drop": "Basso enfatizza il terzo tempo per un groove rilassato.",
            "Syncopated Funk Groove": "Un pattern sincopato tipico del funk con ghost notes."
        },
        "Avanzato": {
            "Jaco Pastorius Style": "Groove avanzati con note ghost, slides e uso creativo delle corde.",
            "Polyrhythmic Groove": "Un pattern che gioca con più ritmi simultanei.",
            "Advanced Walking Bass": "Linee jazz fluide con cromatismi e passaggi melodici complessi."
        }
    }
}


pattern_ritmici_melodici = {
    "Batteria": {
        "Facile": {
            "Backbeat": {
                "Descrizione": "Un pattern comune con il rullante sui tempi 2 e 4.",
                "Melodia Consigliata": "Melodie semplici basate su scala maggiore con accenti forti sui tempi 1 e 3."
            },
            "Four on the Floor": {
                "Descrizione": "Cassa su tutti e quattro i battiti, usato in dance e pop.",
                "Melodia Consigliata": "Linee vocali o strumentali ripetitive con un groove costante, spesso con poche variazioni ritmiche."
            }
        },
        "Intermedio": {
            "Shuffle": {
                "Descrizione": "Un pattern swingato tipico del blues.",
                "Melodia Consigliata": "Frasi melodiche blues con bending e note swingate per seguire il ritmo terzinato."
            },
            "Funk Groove": {
                "Descrizione": "Pattern sincopato con forte accento sul primo tempo.",
                "Melodia Consigliata": "Linee melodiche sincopate con uso di ghost notes e cromatismi, tipiche del funk."
            }
        }
    },
    "Chitarra": {
        "Facile": {
            "Open Chord Strumming": {
                "Descrizione": "Pennata costante sugli accordi aperti.",
                "Melodia Consigliata": "Melodie vocali o solistiche che seguono gli accordi con semplici passaggi scalari."
            },
            "Reggae Skank": {
                "Descrizione": "Accordi stoppati suonati sul secondo e quarto tempo.",
                "Melodia Consigliata": "Melodie spezzate con frasi sincopate, tipiche del reggae."
            }
        },
        "Intermedio": {
            "Funky Chops": {
                "Descrizione": "Accordi stoppati con ghost notes per un groove serrato.",
                "Melodia Consigliata": "Riff sincopati con intervalli stretti e note percussive, spesso in modalità dorica o misolidia."
            },
            "Blues Shuffle Strumming": {
                "Descrizione": "Un pattern blues in 12/8 con dinamica nelle pennate.",
                "Melodia Consigliata": "Melodie con frasi call & response, bending e note swingate per seguire il shuffle."
            }
        }
    },
    "Piano": {
        "Facile": {
            "Boom-Chuck": {
                "Descrizione": "Alternanza tra basso e accordi, tipico dello stile country e folk.",
                "Melodia Consigliata": "Linee vocali o melodiche con movimenti scalari e poche sincopi."
            },
            "Basic Waltz": {
                "Descrizione": "Bassi sul primo tempo, accordi sui successivi due (tempo in 3/4).",
                "Melodia Consigliata": "Frasi lunghe e liriche, spesso con un movimento fluido tra le note per enfatizzare il tempo ternario."
            }
        },
        "Intermedio": {
            "Boogie Woogie": {
                "Descrizione": "Un ostinato di ottavi con la mano sinistra e una melodia sincopata con la destra.",
                "Melodia Consigliata": "Frasi melodiche rapide con approccio call & response, spesso con note cromatiche."
            },
            "Bebop Comping": {
                "Descrizione": "Accordi sincopati e frasi brevi per accompagnare la melodia jazz.",
                "Melodia Consigliata": "Linee melodiche con improvvisazione su scale bebop e cromatismi."
            }
        }
    },
    "Basso": {
        "Facile": {
            "Root-Fifth Rock Groove": {
                "Descrizione": "Alternanza tra la tonica e la quinta per solidità ritmica.",
                "Melodia Consigliata": "Melodie semplici basate sugli stessi gradi della scala per enfatizzare la base armonica."
            },
            "Basic Walking Bass": {
                "Descrizione": "Note fondamentali suonate con una progressione fluida.",
                "Melodia Consigliata": "Linee vocali fluide e legate, spesso seguendo il basso per creare un dialogo musicale."
            }
        },
        "Intermedio": {
            "Slap & Pop": {
                "Descrizione": "Colpi slap sul basso e pop sulle corde alte per un suono percussivo.",
                "Melodia Consigliata": "Melodie con frasi brevi e sincopate, spesso con salti di intervalli per seguire l'energia dello slap."
            },
            "Reggae One Drop": {
                "Descrizione": "Basso enfatizza il terzo tempo per un groove rilassato.",
                "Melodia Consigliata": "Linee vocali spezzate con frasi lunghe e note sostenute per contrastare il basso sincopato."
            }
        }
    }
}


drum_patterns = {
    "backbeat": {
        "pattern": ["D", "-", "D", "U", "-", "D", "-", "U"],
        "descrizione": "Un pattern classico usato in molti generi musicali, con il rullante sui tempi 2 e 4."
    },
    "four_on_the_floor": {
        "pattern": ["D", "-", "D", "-", "D", "-", "D", "-"],
        "descrizione": "Cassa su tutti e quattro i battiti, comune nella musica dance e pop."
    },
    "basic_rock_beat": {
        "pattern": ["D", "-", "D", "-", "U", "-", "D", "-", "U"],
        "descrizione": "Cassa sui tempi 1 e 3, rullante sui tempi 2 e 4, hi-hat in ottavi."
    },
    "shuffle": {
        "pattern": ["D", "-", "D", "U", "-", "D", "-", "U", "-", "D"],
        "descrizione": "Un pattern swingato tipico del blues e rock'n'roll, caratterizzato da un ritmo terzinato."
    },
    "funk_groove": {
        "pattern": ["D", "U", "-", "D", "U", "-", "D", "-", "U", "-"],
        "descrizione": "Un groove sincopato tipico del funk con forte accento sul primo tempo."
    },
    "half_time_shuffle": {
        "pattern": ["D", "-", "U", "-", "D", "-", "U", "-", "D"],
        "descrizione": "Un groove sincopato con hi-hat swingato e ghost notes sul rullante, tipico del rock e del pop."
    },
    "jazz_swing": {
        "pattern": ["D", "-", "D", "-", "U", "-", "D", "-", "U", "-", "D", "-", "U"],
        "descrizione": "Un pattern di swing con un'andatura terzinata e il rullante sui tempi 2 e 4."
    },
    "reggae_one_drop": {
        "pattern": ["D", "-", "-", "D", "-", "-", "U", "-", "D"],
        "descrizione": "Il rullante è suonato sul terzo tempo, mentre il charleston accentua il secondo e quarto tempo."
    },
    "linear_drumming": {
        "pattern": ["D", "-", "-", "-", "U", "-", "-", "-", "D"],
        "descrizione": "Un pattern avanzato dove nessun arto suona simultaneamente, usato per creare groove complessi."
    },
    "bossa_nova": {
        "pattern": ["D", "-", "-", "-", "U", "-", "-", "-", "D"],
        "descrizione": "Un pattern tipico della musica brasiliana, con un ritmo sincopato e dinamico."
    },
    "samba": {
        "pattern": ["D", "-", "D", "-", "-", "U", "-", "D", "-", "U"],
        "descrizione": "Ritmo veloce e sincopato, tipico del Brasile, con un forte accento sul primo tempo."
    },
    "rumba_guaguanco": {
        "pattern": ["D", "-", "-", "-", "-", "D", "-", "U", "-", "D"],
        "descrizione": "Un groove sincopato utilizzato nella musica cubana, con forti accenti sulle congas."
    },
    "tumbao": {
        "pattern": ["D", "-", "U", "-", "D", "-", "-", "-", "U"],
        "descrizione": "Un pattern tipico della salsa, con un forte ritmo di congas e accentuazione sincopata."
    },
    "blues_shuffe": {
        "pattern": ["D", "-", "-", "D", "-", "U", "-", "D", "-", "U"],
        "descrizione": "Un pattern blues in 12/8, con il ritmo in levare e una dinamica che alterna il rullante."
    },
    "mozaambique": {
        "pattern": ["D", "-", "-", "U", "-", "-", "-", "D", "-", "U"],
        "descrizione": "Pattern complesso di origine cubana, con un forte senso di movimento."
    },
    "afrobeat_percussion": {
        "pattern": ["D", "-", "U", "-", "-", "D", "-", "-", "U"],
        "descrizione": "Un groove poliritmico con interplay tra djembe, shaker e altri strumenti a percussione."
    },
    "candombe": {
        "pattern": ["D", "-", "-", "-", "U", "-", "D", "-", "-", "U"],
        "descrizione": "Groove africano-uruguaiano, con accenti particolari sui tamburi Candombe."
    },
    "open_chord_strumming": {
        "pattern": ["D", "-", "D", "-", "-", "D", "-", "D", "U"],
        "descrizione": "Accordi aperti suonati con un ritmo regolare, tipico dello stile country e folk."
    },
    "palm_muted_power_chords": {
        "pattern": ["D", "-", "-", "-", "D", "-", "-", "U", "-", "D"],
        "descrizione": "Power chords stoppati con la mano destra per ottenere un suono ritmico e secco."
    },
    "reggae_skank": {
        "pattern": ["D", "-", "D", "-", "-", "-", "D", "-", "U"],
        "descrizione": "Accordi stoppati sul secondo e quarto tempo, tipici del reggae."
    },
    "funky_chops": {
        "pattern": ["D", "-", "-", "D", "-", "-", "U", "-", "D", "-", "U"],
        "descrizione": "Accordi stoppati con ghost notes per un groove più serrato e funky."
    },
    "fingerpicking_arpeggio": {
        "pattern": ["D", "-", "U", "-", "D", "-", "-", "U", "-", "D"],
        "descrizione": "Arpeggio con un utilizzo alternato delle dita per produrre un effetto melodico e ritmico."
    },
    "hybrid_picking": {
        "pattern": ["D", "-", "-", "U", "-", "-", "D", "-", "U"],
        "descrizione": "Uso combinato di plettro e dita per velocità e dinamica nelle pennate."
    },
    "fast_metal_gallop": {
        "pattern": ["D", "-", "D", "-", "D", "-", "D", "-", "U"],
        "descrizione": "Pattern rapido tipico del metal, con pennate alternate veloci."
    },
    "jazz_comping": {
        "pattern": ["D", "-", "-", "D", "-", "-", "U", "-", "-", "D"],
        "descrizione": "Accordi sincopati e voicings avanzati per creare groove nel jazz."
    },
    "root_fifth_rock_groove": {
        "pattern": ["D", "-", "-", "U", "-", "-", "-", "-", "D"],
        "descrizione": "Alternanza tra la tonica e la quinta, creando una solida base ritmica per il rock."
    },
    "basic_walking_bass": {
        "pattern": ["D", "-", "-", "-", "-", "D", "-", "-", "-", "U"],
        "descrizione": "Note fondamentali suonate con una progressione fluida, spesso usata nel jazz."
    },
    "disco_octaves": {
        "pattern": ["D", "-", "D", "-", "D", "-", "-", "D", "U"],
        "descrizione": "Utilizzo di ottave per creare un groove pulsante, tipico della musica disco."
    },
    "slap_pop": {
        "pattern": ["D", "-", "-", "U", "-", "-", "D", "-", "U", "-", "D"],
        "descrizione": "Tecnica di slap e pop per ottenere un suono ritmico e percussivo."
    },
    "syncopated_funk_groove": {
        "pattern": ["D", "-", "-", "D", "-", "-", "U", "-", "U"],
        "descrizione": "Pattern sincopato tipico del funk, con ghost notes e accenti tra i tempi."
    },
    "jaco_pastorius_style": {
        "pattern": ["D", "-", "-", "-", "-", "U", "-", "D", "-", "-", "U"],
        "descrizione": "Groove avanzato con l'uso creativo delle corde e dei glissandi tipico di Jaco Pastorius."
    },
    "polyrhythmic_groove": {
        "pattern": ["D", "-", "D", "-", "-", "U", "-", "D", "-", "U"],
        "descrizione": "Un pattern che gioca con più ritmi simultanei, tipico delle composizioni complesse."
    },
    "advanced_walking_bass": {
        "pattern": ["D", "-", "U", "-", "-", "D", "-", "U", "-", "D"],
        "descrizione": "Linee fluide e complesse con cromatismi e passaggi melodici, tipiche del jazz avanzato."
    }
}
'''

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
        "linear_drumming": ["D", "-", "-", "-", "U", "-", "-", "-", "D"],
        "bossa_nova": ["D", "-", "-", "-", "U", "-", "-", "-", "D"],
        "samba": ["D", "-", "D", "-", "-", "U", "-", "D", "-", "U"],
        "rumba_guaguanco": ["D", "-", "-", "-", "-", "D", "-", "U", "-", "D"],
        "tumbao": ["D", "-", "U", "-", "D", "-", "-", "-", "U"],
        "blues_shuffe": ["D", "-", "-", "D", "-", "U", "-", "D", "-", "U"],
        "mozaambique": ["D", "-", "-", "U", "-", "-", "-", "D", "-", "U"],
        "afrobeat_percussion": ["D", "-", "U", "-", "-", "D", "-", "-", "U"],
        "candombe": ["D", "-", "-", "-", "U", "-", "D", "-", "-", "U"],
        "open_chord_strumming": ["D", "-", "D", "-", "-", "D", "-", "D", "U"],
        "palm_muted_power_chords": ["D", "-", "-", "-", "D", "-", "-", "U", "-", "D"],
        "reggae_skank": ["D", "-", "D", "-", "-", "-", "D", "-", "U"],
        "funky_chops": ["D", "-", "-", "D", "-", "-", "U", "-", "D", "-", "U"],
        "fingerpicking_arpeggio": ["D", "-", "U", "-", "D", "-", "-", "U", "-", "D"],
        "hybrid_picking": ["D", "-", "-", "U", "-", "-", "D", "-", "U"],
        "fast_metal_gallop": ["D", "-", "D", "-", "D", "-", "D", "-", "U"],
        "jazz_comping": ["D", "-", "-", "D", "-", "-", "U", "-", "-", "D"],
        "root_fifth_rock_groove": ["D", "-", "-", "U", "-", "-", "-", "-", "D"],
        "basic_walking_bass": ["D", "-", "-", "-", "-", "D", "-", "-", "-", "U"],
        "disco_octaves": ["D", "-", "D", "-", "D", "-", "-", "D", "U"],
        "slap_pop": ["D", "-", "-", "U", "-", "-", "D", "-", "U", "-", "D"],
        "syncopated_funk_groove": ["D", "-", "-", "D", "-", "-", "U", "-", "U"],
        "jaco_pastorius_style": ["D", "-", "-", "-", "-", "U", "-", "D", "-", "-", "U"],
        "polyrhythmic_groove": ["D", "-", "D", "-", "-", "U", "-", "D", "-", "U"],
        "advanced_walking_bass": ["D", "-", "U", "-", "-", "D", "-", "U", "-", "D"]
    },
    
    "piano": {
        "basic_chord_progression": ["C", "-", "F", "-", "G", "-", "C", "-"],
        "ii_V_I": ["D-", "-", "G7", "-", "Cmaj7", "-"],
        "blues_progression": ["C7", "-", "F7", "-", "G7", "-", "C7", "-"],
        "walking_bass": ["C", "-", "E", "-", "G", "-", "B", "-"],
        "rock_piano": ["D", "-", "A", "-", "E", "-", "G", "-"],
        "major_scale_arpeggio": ["C", "-", "E", "-", "G", "-", "B", "-"],
        "minor_scale_arpeggio": ["C-", "-", "E-", "-", "G-", "-", "B-", "-"],
        "chord_inversions": ["C", "-", "E", "-", "G", "-", "C", "-"],
        "piano_roll": ["D", "-", "F", "-", "A", "-", "C", "-"],
        "jazz_progression": ["Cmaj7", "-", "Fmaj7", "-", "G7", "-", "Cmaj7", "-"],
        "dominant_seventh": ["D7", "-", "G7", "-", "C7", "-", "F7", "-"],
        "tension_chords": ["Cmaj7", "-", "Bm7", "-", "F#7", "-", "Ebm7", "-"],
        "swing_rythm": ["C", "-", "G", "-", "Am", "-", "F", "-"],
        "arpeggiated_progression": ["C", "-", "G", "-", "F", "-", "D", "-"],
        "baroque_progression": ["C", "-", "F", "-", "G", "-", "C", "-"],
        "tritone_substitution": ["Cmaj7", "-", "D7", "-", "G7", "-", "Cmaj7", "-"],
        "jazz_blues": ["C7", "-", "F7", "-", "C7", "-", "G7", "-"],
        "funk_piano": ["C", "-", "F", "-", "G", "-", "C", "-"],
        "classical_arpeggio": ["C", "-", "E", "-", "G", "-", "C", "-"],
        "octave_chord_progression": ["C", "-", "G", "-", "F", "-", "C", "-"],
        "seven_chords_progression": ["D7", "-", "G7", "-", "C7", "-", "F7", "-"],
        "pop_piano": ["C", "-", "Am", "-", "F", "-", "G", "-"],
        "walking_bass_jazz": ["C", "-", "E", "-", "G", "-", "B", "-"],
        "rock_n_roll": ["C", "-", "F", "-", "G", "-", "C", "-"],
        "minor_blues": ["C-", "-", "F7", "-", "G7", "-", "C7", "-"],
        "dominant_seventh_progression": ["C7", "-", "F7", "-", "G7", "-", "C7", "-"],
        "octave_pattern": ["C", "-", "E", "-", "G", "-", "C", "-"]
    },
    
    "basso": {
        "root_notes": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "arpeggios": ["C", "-", "E", "-", "G", "-", "C", "-"],
        "walking_bass": ["C", "-", "D", "-", "E", "-", "F", "-"],
        "blues_bass": ["C", "-", "F", "-", "G", "-", "C", "-"],
        "rock_bass": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "octave_bass": ["C", "-", "G", "-", "A", "-", "D", "-"],
        "syncopated_bass": ["C", "-", "-", "E", "-", "G", "-", "C", "-"],
        "slap_bass": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "funk_bass": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "arpeggiated_bass": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "bass_pedal": ["C", "-", "C", "-", "G", "-", "C", "-"],
        "walking_bass_jazz": ["C", "-", "E", "-", "G", "-", "B", "-"],
        "blues_walk": ["C", "-", "F", "-", "G", "-", "C", "-"],
        "octave_progression": ["C", "-", "E", "-", "G", "-", "C", "-"],
        "chord_bass_line": ["C", "-", "E", "-", "G", "-", "B", "-"],
        "rock_bassline": ["C", "-", "A", "-", "D", "-", "G", "-"],
        "jazz_bassline": ["C", "-", "F", "-", "D", "-", "G", "-"],
        "syncopated_rock": ["C", "-", "-", "D", "-", "-", "E", "-"],
        "pop_bassline": ["C", "-", "A", "-", "F", "-", "G", "-"],
        "funk_bassline": ["C", "-", "E", "-", "G", "-", "A", "-"],
        "walking_bass_pattern": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "blues_progression": ["C", "-", "F", "-", "G", "-", "C", "-"],
        "pop_arpeggio": ["C", "-", "G", "-", "A", "-", "F", "-"],
        "tension_bass": ["C", "-", "G", "-", "A", "-", "F", "-"],
        "slap_pop_bass": ["C", "-", "G", "-", "D", "-", "A", "-"]
    },
    
    "chitarra": {
        "open_chords": ["C", "-", "G", "-", "Am", "-", "F", "-"],
        "power_chords": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "strumming": ["D", "-", "D", "-", "U", "-", "D", "U"],
        "fingerpicking": ["D", "-", "U", "-", "D", "-", "-", "U", "-", "D"],
        "palm_muting": ["D", "-", "-", "U", "-", "-", "D", "-", "U"],
        "slap_picking": ["D", "-", "-", "U", "-", "-", "D", "-", "U"],
        "pentatonic_scale": ["C", "-", "D", "-", "E", "-", "G", "-"],
        "arpeggio": ["C", "-", "E", "-", "G", "-", "B", "-"],
        "rock_strumming": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "blues_picking": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "country_plucking": ["C", "-", "E", "-", "G", "-", "D", "-"],
        "funk_strumming": ["D", "-", "-", "U", "-", "-", "D", "-", "U"],
        "pop_strumming": ["C", "-", "Am", "-", "F", "-", "G", "-"],
        "walking_bass_strum": ["C", "-", "E", "-", "G", "-", "A", "-"],
        "speed_riffing": ["C", "-", "D", "-", "E", "-", "F", "-"],
        "power_riff": ["C", "-", "A", "-", "G", "-", "E", "-"],
        "blues_riff": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "jazz_plucking": ["C", "-", "E", "-", "G", "-", "B", "-"],
        "rock_riff": ["C", "-", "A", "-", "G", "-", "D", "-"],
        "syncopated_riff": ["C", "-", "-", "D", "-", "-", "E", "-"],
        "slide_picking": ["C", "-", "D", "-", "E", "-", "F", "-"],
        "arpeggiated_picking": ["C", "-", "E", "-", "G", "-", "C", "-"],
        "speed_chords": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "acoustic_fingerstyle": ["C", "-", "E", "-", "G", "-", "C", "-"],
        "blues_licks": ["C", "-", "G", "-", "D", "-", "A", "-"],
        "strum_arpeggio": ["C", "-", "F", "-", "G", "-", "D", "-"],
        "strumming_patterns": ["C", "-", "G", "-", "Am", "-", "F", "-"]
    }
}



# import music21
'''
Per cominciare, ti mostro come puoi configurare e usare Music21 per creare note, durate e spartiti, seguendo i tuoi obiettivi. Qui ci sono i passaggi fondamentali:

Passo 1: Installazione di Music21
Prima di tutto, assicurati di avere Music21 installato. Puoi farlo facilmente usando pip:

bash
Copia
Modifica
pip install music21
Passo 2: Creazione di note e durate
Music21 ti permette di definire note con durate precise. Le durate possono essere espresse in valori come quarterLength (durata in battiti) o con simboli convenzionali come interi e frazioni (esempio: 1/4, 1/8).

Per creare una semplice nota, puoi farlo così:

python
Copia
Modifica
from music21 import *

# Creiamo una nota di durata intera (whole note)
nota = note.Note('C4', quarterLength=4)

# Creiamo una nota di durata di un quarto di battito (quarter note)
nota_quarter = note.Note('D4', quarterLength=1)

# Creiamo una nota di ottavo (eighth note)
nota_eighth = note.Note('E4', quarterLength=0.5)

# Mostriamo le note
nota.show('text')
nota_quarter.show('text')
nota_eighth.show('text')
Passo 3: Creare pattern ritmici complessi
Puoi creare pattern ritmici combinando queste note. Supponiamo di voler creare un pattern ritmico che alterna una croma e una semiminima (esempio: "D, -, D, U, -"):

python
Copia
Modifica
from music21 import *

# Creiamo un flusso di note con durate differenti
ritmo = stream.Stream()

# Pattern "D, -, D, U, -"
ritmo.append(note.Note('C4', quarterLength=1))  # D (semiminima)
ritmo.append(note.Rest(quarterLength=0.5))  # Rest (pausa)
ritmo.append(note.Note('E4', quarterLength=1))  # D (semiminima)
ritmo.append(note.Note('F4', quarterLength=0.5))  # U (croma)
ritmo.append(note.Rest(quarterLength=0.5))  # Rest (pausa)

# Mostriamo il pattern ritmico
ritmo.show('text')
Passo 4: Creazione di un'intera progressione ritmica
Ora possiamo usare questi pattern per costruire una progressione musicale completa:

python
Copia
Modifica
from music21 import *

# Crea una sequenza ritmica con diverse durate
progressione = stream.Stream()

# Pattern con diverse durate
progressione.append(note.Note('C4', quarterLength=1))  # D
progressione.append(note.Rest(quarterLength=0.5))     # -
progressione.append(note.Note('D4', quarterLength=1))  # D
progressione.append(note.Note('E4', quarterLength=0.5))  # U
progressione.append(note.Rest(quarterLength=0.5))     # -

# Mostriamo la progressione completa
progressione.show('text')
Passo 5: Visualizzazione dello spartito
Music21 ti consente di visualizzare il tuo spartito in modo grafico, ad esempio in formato PDF o MusicXML. Per farlo, basta usare:

python
Copia
Modifica
# Mostra la notazione grafica in un formato visualizzabile
progressione.show()
Passo 6: Aggiungere le note puntate e legato
Puoi anche aggiungere note puntate (doppia durata della nota) e legati (che collegano due note):

python
Copia
Modifica
from music21 import *

# Crea una nota di quarta puntata
nota_puntata = note.Note('C4', quarterLength=1.5)  # 1.5 significa una semiminima puntata

# Creiamo un legato
nota_legata1 = note.Note('D4', quarterLength=1)
nota_legata2 = note.Note('E4', quarterLength=1)
nota_legata1.quarterLength = 1
nota_legata2.quarterLength = 1
legato = chord.Chord([nota_legata1, nota_legata2])

# Aggiungiamo il legato
legato.quarterLength = 2  # Durata totale del legato (unita)
Passo 7: Creazione di accordi e progressioni armoniche
Infine, puoi utilizzare gli accordi per costruire progressioni armoniche. Ecco un esempio di una progressione di accordi con Music21:

python
Copia
Modifica
from music21 import *

# Creiamo una progressione di accordi (esempio: I-IV-V)
accordo1 = chord.Chord(['C4', 'E4', 'G4'])  # Accordo di Do maggiore
accordo2 = chord.Chord(['F4', 'A4', 'C5'])  # Accordo di Fa maggiore
accordo3 = chord.Chord(['G4', 'B4', 'D5'])  # Accordo di Sol maggiore

# Aggiungiamo gli accordi alla progressione
progressione_accordi = stream.Stream([accordo1, accordo2, accordo3])

# Mostriamo la progressione degli accordi
progressione_accordi.show()
Passo 8: Esportazione del risultato
Puoi anche esportare il tuo spartito in formati come MusicXML, MIDI o PDF per ulteriori usi:

python
Copia
Modifica
# Esportiamo la partitura in formato MusicXML
progressione_accordi.write('musicxml', fp='progressione.xml')

# Esportiamo in formato MIDI
progressione_accordi.write('midi', fp='progressione.mid')
Conclusioni
Music21 ti permette di manipolare le note, gli accordi e i pattern ritmici in modo molto flessibile. Puoi utilizzarlo per generare e visualizzare spartiti, aggiungere dinamiche e espressioni, e perfino analizzare la musica. Questo ti dà una potente base per costruire l'app musicale che desideri, permettendo anche personalizzazioni avanzate come note puntate, legato e vari valori ritmici.
'''