

# Music Tutor      17-27/02/2025           Conclusione del primo ciclo python 100 giorni per passare da livello 0, a base, a livello intermedio (6h al giorno circa per 100 giorni mi hanno portato a sviluppare questa app come esercizio e prova di ciò che ho imparato in questi tre mesi)

                                           # 60 h circa di lavoro

# questa è la mia prima applicazione, essendo un appassionato e studioso di musica, ho avuto la necessità di imparare scale, accordi, progressioni: 
# il Tutor è un compagno di viaggio nel magico mondo musicale, giocando con le sue funzioni potrai imparare la musica in modo divertente ed avere un manuale che risponde rapidamente ad ogni tua esigenza.
# il Tutor è adatto a tutti coloro che hanno bisogno di un aiuto nella creazione e comprensione della musica: 
# per coloro che si approcciano per la prima volta i termini saranno difficilmente comprensibili, sarà perciò mio compito di implementare la parte iniziale con un manuale generale.
# ma per coloro che hanno anche un minimo di dimestichezza il Tutor è perfetto per risolvere i loro dubbi musicali e può essere un affidabile alleato anche per i professionisti.

############################################################################


#        DATI 

# le scale, gli accordi, le tonalità, le progressioni e i pattern ritmici chiaramente non sono completi, sarà da implementare con lv.avanzati

############################################################################################################################################################################

note = ["Do", "Do#/Reb", "Re", "Re#/Mib", "Mi", "Fa", "Fa#/Solb", "Sol", "Sol#/Lab", "La", "La#/Sib", "Si"]

note_anglosassoni = {
    "C": "Do",     "C#": "Do#",    "D": "Re",     "D#": "Re#",    "E": "Mi",
    "F": "Fa",     "F#": "Fa#",    "G": "Sol",    "G#": "Sol#",   "A": "La",
    "A#": "La#",   "B": "Si",     "Cb": "Do",    "B#": "Do#",    "Db": "Re",
    "Eb": "Mib",   "Fb": "Mi",    "Gb": "Fa",    "Ab": "Sol",    "Bb": "Lab"
}

note_dies_e_bem = {
    "diesis": [
        "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"
    ],
    "bemolle": [
        "Do", "Reb", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib", "Si"
    ]
}

scale = {
    # Scala Maggiore
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

    # Scale Minori
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
    "Si Minore Melodica": ["Si", "Do#", "Re", "Mi", "Fa#", "Sol#", "La#"],


    # Scale Pentatoniche Maggiori
    "Do Pentatonica": ["Do", "Re", "Mi", "Sol", "La"],
    "Do# Pentatonica": ["Do#", "Re#", "Mi#", "Sol#", "La#"],
    "Reb Pentatonica": ["Reb", "Mib", "Fa", "Lab", "Sib"],
    "Re Pentatonica": ["Re", "Mi", "Fa#", "La", "Si"],
    "Re# Pentatonica": ["Re#", "Mi#", "Fa##", "La#", "Si#"],
    "Mib Pentatonica": ["Mib", "Fa", "Sol", "Sib", "Do"],
    "Mi Pentatonica": ["Mi", "Fa#", "Sol#", "Si", "Do#"],
    "Fa Pentatonica": ["Fa", "Sol", "La", "Do", "Re"],
    "Fa# Pentatonica": ["Fa#", "Sol#", "La#", "Do#", "Re#"],
    "Solb Pentatonica": ["Solb", "Lab", "Sib", "Reb", "Mib"],
    "Sol Pentatonica": ["Sol", "La", "Si", "Re", "Mi"],
    "Sol# Pentatonica": ["Sol#", "La#", "Si#", "Re#", "Mi#"],
    "Lab Pentatonica": ["Lab", "Sib", "Do", "Mib", "Fa"],
    "La Pentatonica" : ["La", "Si", "Do#", "Mi", "Fa#"],
    "La# Pentatonica": ["La#", "Si#", "Do##", "Mi#", "Fa##"],
    "Sib Pentatonica": ["Sib", "Do", "Re", "Fa", "Sol"],
    "Si Pentatonica": ["Si", "Do#", "Re#", "Fa#", "Sol#"],

    # Scale Pentatoniche Minori
    "Do Pentatonica Min": ["Do", "Mib", "Fa", "Sol", "Sib"],
    "Do# Pentatonica Min": ["Do#", "Mi", "Fa#", "Sol#", "Si"],
    "Reb Pentatonica Min": ["Reb", "Fb", "Solb", "Lab", "Dob"],
    "Re Pentatonica Min": ["Re", "Fa", "Sol", "La", "Do"],
    "Re# Pentatonica Min": ["Re#", "Fa#", "Sol#", "La#", "Do#"],
    "Mib Pentatonica Min": ["Mib", "Solb", "Lab", "Sib", "Reb"],
    "Mi Pentatonica Min": ["Mi", "Sol", "La", "Si", "Re"],
    "Fa Pentatonica Min": ["Fa", "Lab", "Sib", "Do", "Mib"],
    "Fa# Pentatonica Min": ["Fa#", "La", "Si", "Do#", "Mi"],
    "Solb Pentatonica Min": ["Solb", "Sibb", "Dob", "Reb", "Fb"],
    "Sol Pentatonica Min": ["Sol", "Sib", "Do", "Re", "Fa"],
    "Sol# Pentatonica Min": ["Sol#", "Si", "Do#", "Re#", "Fa#"],
    "Lab Pentatonica Min": ["Lab", "Dob", "Reb", "Mib", "Solb"],
    "La Pentatonica Min": ["La", "Do", "Re", "Mi", "Sol"],
    "La# Pentatonica Min": ["La#", "Do#", "Re#", "Mi#", "Sol#"],
    "Sib Pentatonica Min": ["Sib", "Reb", "Mib", "Fa", "Lab"],
    "Si Pentatonica Min": ["Si", "Re", "Mi", "Fa#", "La"],

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
# Aggiungiamo le scale modali principali e andremo avanti con altri tipi di scale più complessi in futuro
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



### vedere meglio nomenclatura e sistemare possibili errori
accordi = {
    # Accordatura per C
    "Do": ["Do", "Mi", "Sol"],
    "Do min": ["Do", "Mib", "Sol"],
    "Do 7": ["Do", "Mi", "Sol", "Sib"],
    "Do min7": ["Do", "Mib", "Sol", "Sib"],
    "Do maj7": ["Do", "Mi", "Sol", "Si"],
    "Do dim": ["Do", "Mib", "Solb"],
    "Do min7b5": ["Do", "Mib", "Solb", "La"],
    "Do aug": ["Do", "Mi", "Sol#"],
    "Do sus2": ["Do", "Re", "Sol"],
    "Do sus4": ["Do", "Fa", "Sol"],
    "Do sus6": ["Do", "Sol", "La"],
    "Do min add2": ["Do", "Re", "Mib", "Sol"],
    "Do min add4": ["Do", "Mib", "Fa", "Sol"],
    "Do add2": ["Do", "Re", "Mi", "Sol"],
    "Do add4": ["Do", "Mi", "Fa", "Sol"],
    "Do add6": ["Do", "Mi", "Sol", "La"],
    "Do minadd6": ["Do", "Mib", "Sol", "La"],
    "Do 9": ["Do", "Mi", "Sol", "Sib", "Re"],
    "Do min9": ["Do", "Mib", "Sol", "Sib", "Re"],
    "Do maj9": ["Do", "Mi", "Sol", "Si", "Re"],
    "Do 11": ["Do", "Mi", "Sol", "Sib", "Re", "Fa"],
    "Do maj11": ["Do", "Mi", "Sol", "Si", "Re", "Fa"],
    "Do 13": ["Do", "Mi", "Sol", "Sib", "Re", "La"],
    "Do maj13": ["Do", "Mi", "Sol", "Si", "Re", "La"],

    # Accordatura per F
    "Fa": ["Fa", "La", "Do"],
    "Fa min": ["Fa", "Lab", "Do"],
    "Fa 7": ["Fa", "La", "Do", "Mib"],
    "Fa min7": ["Fa", "Lab", "Do", "Mib"],
    "Fa maj7": ["Fa", "La", "Do", "Mi"],
    "Fa dim": ["Fa", "Lab", "Dobb"],
    "Fa min7b5": ["Fa", "Lab", "Dobb", "Re"],
    "Fa aug": ["Fa", "La", "Do#"],
    "Fa sus2": ["Fa", "Sol", "Do"],
    "Fa sus4": ["Fa", "Sib", "Do"],
    "Fa sus6": ["Fa", "Do", "Re"],
    "Fa min add2": ["Fa", "Sol", "Lab", "Do"],
    "Fa min add4": ["Fa", "Lab", "Sib", "Do"],
    "Fa add2": ["Fa", "Sol", "La", "Do"],
    "Fa add4": ["Fa", "La", "Sib", "Do"],
    "Fa add6": ["Fa", "La", "Do", "Re"],
    "Fa minadd6": ["Fa", "Lab", "Do", "Re"],
    "Fa 9": ["Fa", "La", "Do", "Mib", "Sol"],
    "Fa min9": ["Fa", "Lab", "Do", "Mib", "Sol"],
    "Fa maj9": ["Fa", "La", "Do", "Mi", "Sol"],
    "Fa 11": ["Fa", "La", "Do", "Mib", "Sol", "Sib"],
    "Fa maj11": ["Fa", "La", "Do", "Mi", "Sol", "Sib"],
    "Fa 13": ["Fa", "La", "Do", "Mib", "Sol", "Re"],
    "Fa maj13": ["Fa", "La", "Do", "Mi", "Sol", "Re"],

    # Accordi per B♭
    "Sib": ["Sib", "Re", "Fa"],
    "Sib min": ["Sib", "Dob", "Fa"],
    "Sib 7": ["Sib", "Re", "Fa", "Lab"],
    "Sib min7": ["Sib", "Dob", "Fa", "Lab"],
    "Sib maj7": ["Sib", "Re", "Fa", "La"],
    "Sib dim": ["Sib", "Dob", "Fab"],
    "Sib min7b5": ["Sib", "Dob", "Fab", "Lab"],
    "Sib aug": ["Sib", "Re", "Solb"],
    "Sib sus2": ["Sib", "Do", "Fa"],
    "Sib sus4": ["Sib", "Mib", "Fa"],
    "Sib sus6": ["Sib", "Fa", "Sol"],
    "Sib min add2": ["Sib", "Do", "Dob", "Fa"],
    "Sib min add4": ["Sib", "Dob", "Mib", "Fa"],
    "Sib add2": ["Sib", "Do", "Re", "Fa"],
    "Sib add4": ["Sib", "Re", "Mib", "Fa"],
    "Sib add6": ["Sib", "Re", "Fa", "Sol"],
    "Sib minadd6": ["Sib", "Dob", "Fa", "Sol"],
    "Sib 9": ["Sib", "Re", "Fa", "Lab", "Do"],
    "Sib min9": ["Sib", "Dob", "Fa", "Lab", "Do"],
    "Sib maj9": ["Sib", "Re", "Fa", "La", "Do"],
    "Sib 11": ["Sib", "Re", "Fa", "Lab", "Do", "Mib"],
    "Sib maj11": ["Sib", "Re", "Fa", "La", "Do", "Mib"],
    "Sib 13": ["Sib", "Re", "Fa", "Lab", "Do", "Sol"],
    "Sib maj13": ["Sib", "Re", "Fa", "La", "Do", "Sol"],

    # Accordi di E♭
    "Mib": ["Mib", "Sol", "Sib"],
    "Mib min": ["Mib", "Solb", "Sib"],
    "Mib 7": ["Mib", "Sol", "Sib", "Dob"],
    "Mib min7": ["Mib", "Solb", "Sib", "Dob"],
    "Mib maj7": ["Mib", "Sol", "Sib", "Re"],
    "Mib dim": ["Mib", "Solb", "La"],
    "Mib min7b5": ["Mib", "Solb", "La", "Do"],
    "Mib aug": ["Mib", "Sol", "Si"],
    "Mib sus2": ["Mib", "Fa", "Sib"],
    "Mib sus4": ["Mib", "Lab", "Sib"],
    "Mib sus6": ["Mib", "Sib", "Do"],
    "Mib min add2": ["Mib", "Fa", "Solb", "Sib"],
    "Mib min add4": ["Mib", "Solb", "Lab", "Sib"],
    "Mib add2": ["Mib", "Fa", "Sol", "Sib"],
    "Mib add4": ["Mib", "Sol", "Lab", "Sib"],
    "Mib mindd6": ["Mib", "Sol", "Sib", "Do"],
    "Mib madd6": ["Mib", "Solb", "Sib", "Do"],
    "Mib 9": ["Mib", "Sol", "Sib", "Dob", "Fa"],
    "Mib min9": ["Mib", "Solb", "Sib", "Dob", "Fa"],
    "Mib maj9": ["Mib", "Sol", "Sib", "Re", "Fa"],
    "Mib 11": ["Mib", "Sol", "Sib", "Dob", "Fa", "Lab"],
    "Mib maj11": ["Mib", "Sol", "Sib", "Re", "Fa", "Lab"],
    "Mib 13": ["Mib", "Sol", "Sib", "Dob", "Fa", "Do"],
    "Mib maj13": ["Mib", "Sol", "Sib", "Re", "Fa", "Do"],

    # Accordi di A♭
    "Lab": ["Lab", "Do", "Mib"],
    "Lab min": ["Lab", "Si", "Mib"],
    "Lab 7": ["Lab", "Do", "Mib", "Solb"],
    "Lab min7": ["Lab", "Si", "Mib", "Solb"],
    "Lab maj7": ["Lab", "Do", "Mib", "Sol"],
    "Lab dim": ["Lab", "Si", "Solb"],
    "Lab min7b5": ["Lab", "Si", "Re", "Fa"],
    "Lab aug": ["Lab", "Do", "Mi"],
    "Lab sus2": ["Lab", "Sib", "Mib"],
    "Lab sus4": ["Lab", "Reb", "Mib"],
    "Lab sus6": ["Lab", "Mib", "Fa"],
    "Lab min add2": ["Lab", "Si", "Dob", "Mib"],
    "Lab min add4": ["Lab", "Dob", "Re", "Mib"],
    "Lab add2": ["Lab", "Sib", "Do", "Mib"],
    "Lab add4": ["Lab", "Do", "Reb", "Mib"],
    "Lab add6": ["Lab", "Do", "Mib", "Fa"],
    "Lab minadd6": ["Lab", "Si", "Mib", "Fa"],
    "Lab 9": ["Lab", "Do", "Mib", "Solb", "Lab"],
    "Lab min9": ["Lab", "Si", "Mib", "Solb", "Lab"],
    "Lab maj9": ["Lab", "Do", "Mib", "Sol", "Lab"],
    "Lab 11": ["Lab", "Do", "Mib", "Solb", "Lab", "Dob"],
    "Lab maj11": ["Lab", "Do", "Mib", "Sol", "Lab", "Dob"],
    "Lab 13": ["Lab", "Do", "Mib", "Solb", "Lab", "Re"],
    "Lab maj13": ["Lab", "Do", "Mib", "Sol", "Lab", "Re"],

    # Accordi di G
    "Sol": ["Sol", "Si", "Re"],
    "Sol min": ["Sol", "Sib", "Re"],
    "Sol 7": ["Sol", "Si", "Re", "Fa"],
    "Sol min7": ["Sol", "Sib", "Re", "Fa"],
    "Sol maj7": ["Sol", "Si", "Re", "Fa#"],
    "Sol dim": ["Sol", "Sib", "Dob"],
    "Sol min7b5": ["Sol", "Sib", "Dob", "Mi"],
    "Sol aug": ["Sol", "Si", "Re#"],
    "Sol sus2": ["Sol", "La", "Re"],
    "Sol sus4": ["Sol", "Do", "Re"],
    "Sol sus6": ["Sol", "Re", "Mi"],
    "Sol min add2": ["Sol", "La", "Sib", "Re"],
    "Sol min add4": ["Sol", "Sib", "Do", "Re"],
    "Sol add2": ["Sol", "La", "Si", "Re"],
    "Sol add4": ["Sol", "Si", "Do", "Re"],
    "Sol add6": ["Sol", "Si", "Re", "Mi"],
    "Sol minadd6": ["Sol", "Sib", "Re", "Mi"],
    "Sol 9": ["Sol", "Si", "Re", "Fa", "La"],
    "Sol min9": ["Sol", "Sib", "Re", "Fa", "La"],
    "Sol maj9": ["Sol", "Si", "Re", "Fa#", "La"],
    "Sol 11": ["Sol", "Si", "Re", "Fa", "La", "Do"],
    "Sol maj11": ["Sol", "Si", "Re", "Fa#", "La", "Do"],
    "Sol 13": ["Sol", "Si", "Re", "Fa", "La", "Do"],
    "Sol maj13": ["Sol", "Si", "Re", "Fa#", "La", "Do"],

    # Accordi di D
    "Re": ["Re", "Fa#", "La"],
    "Re min": ["Re", "Fa", "La"],
    "Re 7": ["Re", "Fa#", "La", "Do"],
    "Re min7": ["Re", "Fa", "La", "Do"],
    "Re maj7": ["Re", "Fa#", "La", "Do#"],
    "Re dim": ["Re", "Fa", "Lab"],
    "Re min7b5": ["Re", "Fa", "Lab", "Do"],
    "Re aug": ["Re", "Fa#", "La#"],
    "Re sus2": ["Re", "Mi", "La"],
    "Re sus4": ["Re", "Sol", "La"],
    "Re sus6": ["Re", "La", "Si"],
    "Re min add2": ["Re", "Mi", "Fa", "La"],
    "Re min add4": ["Re", "Fa", "Sol", "La"],
    "Re add2": ["Re", "Mi", "Fa#", "La"],
    "Re add4": ["Re", "Fa#", "Sol", "La"],
    "Re add6": ["Re", "Fa#", "La", "Si"],
    "Re minadd6": ["Re", "Fa", "La", "Si"],
    "Re 9": ["Re", "Fa#", "La", "Do", "Mi"],
    "Re min9": ["Re", "Fa", "La", "Do", "Mi"],
    "Re maj9": ["Re", "Fa#", "La", "Do#", "Mi"],
    "Re 11": ["Re", "Fa#", "La", "Do", "Mi", "Sol"],
    "Re maj11": ["Re", "Fa#", "La", "Do#", "Mi", "Sol"],
    "Re 13": ["Re", "Fa#", "La", "Do", "Mi", "Sol"],
    "Re maj13": ["Re", "Fa#", "La", "Do#", "Mi", "Sol"],

    # Accordi di A
    "La": ["La", "Do#", "Mi"],
    "La min": ["La", "Do", "Mi"],
    "La 7": ["La", "Do#", "Mi", "Sol"],
    "La min7": ["La", "Do", "Mi", "Sol"],
    "La maj7": ["La", "Do#", "Mi", "Sol#"],
    "La dim": ["La", "Do", "Mib"],
    "La min7b5": ["La", "Do", "Mib", "Sol"],
    "La aug": ["La", "Do#", "Mi#"],
    "La sus2": ["La", "Si", "Mi"],
    "La sus4": ["La", "Re", "Mi"],
    "La sus6": ["La", "Mi", "Fa#"],
    "La min add2": ["La", "Si", "Do", "Mi"],
    "La min add4": ["La", "Do", "Re", "Mi"],
    "La add2": ["La", "Si", "Do#", "Mi"],
    "La add4": ["La", "Do#", "Re", "Mi"],
    "La add6": ["La", "Do#", "Mi", "Fa#"],
    "La minadd6": ["La", "Do", "Mi", "Fa#"],
    "La 9": ["La", "Do#", "Mi", "Sol", "Si"],
    "La min9": ["La", "Do", "Mi", "Sol", "Si"],
    "La maj9": ["La", "Do#", "Mi", "Sol#", "Si"],
    "La 11": ["La", "Do#", "Mi", "Sol", "Si", "Re"],
    "La maj11": ["La", "Do#", "Mi", "Sol#", "Si", "Re"],
    "La 13": ["La", "Do#", "Mi", "Sol", "Si", "Re"],
    "La maj13": ["La", "Do#", "Mi", "Sol#", "Si", "Re"],

    # Accordi di E
    "Mi": ["Mi", "Sol#", "Si"],
    "Mi min": ["Mi", "Sol", "Si"],
    "Mi 7": ["Mi", "Sol#", "Si", "Re"],
    "Mi min7": ["Mi", "Sol", "Si", "Re"],
    "Mi maj7": ["Mi", "Sol#", "Si", "Do#"],
    "Mi dim": ["Mi", "Sol", "Lab"],
    "MI min7b5": ["Mi", "Sol", "Lab", "Re"],
    "Mi aug": ["Mi", "Sol#", "Do"],
    "Mi sus2": ["Mi", "Fa#", "Si"],
    "Mi sus4": ["Mi", "La", "Si"],
    "Mi sus6": ["Mi", "Si", "Do#"],
    "Mi min add2": ["Mi", "Fa", "Sol", "Si"],
    "Mi min add4": ["Mi", "Sol", "La", "Si"],
    "Mi add2": ["Mi", "Fa#", "Sol#", "Si"],
    "Mi add4": ["Mi", "Sol#", "La", "Si"],
    "Mi add6": ["Mi", "Sol#", "Si", "Do#"],
    "Mi minadd6": ["Mi", "Sol", "Si", "Do#"],
    "Mi 9": ["Mi", "Sol#", "Si", "Re", "Fa#"],
    "Mi min9": ["Mi", "Sol", "Si", "Re", "Fa#"],
    "Mi maj9": ["Mi", "Sol#", "Si", "Do#", "Fa#"],
    "Mi 11": ["Mi", "Sol#", "Si", "Re", "Fa#", "La"],
    "Mi maj11": ["Mi", "Sol#", "Si", "Do#", "Fa#", "La"],
    "Mi 13": ["Mi", "Sol#", "Si", "Re", "Fa#", "La"],
    "Mi maj13": ["Mi", "Sol#", "Si", "Do#", "Fa#", "La"],

    # Accordi di C#
    "Do#": ["Do#", "Fa", "Sol#"],
    "Do# min": ["Do#", "Fa", "Sol"],
    "Do# 7": ["Do#", "Fa", "Sol#", "Si"],
    "Do# min7": ["Do#", "Fa", "Sol", "Si"],
    "Do# maj7": ["Do#", "Fa", "Sol#", "Do"],
    "Do# dim": ["Do#", "Fa", "Sol"],
    "Do# min7b5": ["Do#", "Fa", "Sol", "Si"],
    "Do# aug": ["Do#", "Fa", "Sol#"],
    "Do# sus2": ["Do#", "Re#", "Sol#"],
    "Do# sus4": ["Do#", "Fa#", "Sol#"],
    "Do# sus6": ["Do#", "Sol#", "La#"],
    "Do# min add2": ["Do#", "Re", "Mi", "Sol#"],
    "Do# min add4": ["Do#", "Mi", "Fa#", "Sol#"],
    "Do# add2": ["Do#", "Re#", "Fa", "Sol#"],
    "Do# add4": ["Do#", "Fa", "Fa#", "Sol#"],
    "Do# add6": ["Do#", "Fa", "Sol#", "La"],
    "Do# minadd6": ["Do#", "Fa", "Sol", "La"],
    "Do# 9": ["Do#", "Fa", "Sol#", "Si", "Re#"],
    "Do# min9": ["Do#", "Fa", "Sol", "Si", "Re#"],
    "Do# maj9": ["Do#", "Fa", "Sol#", "Do", "Re#"],
    "Do# 11": ["Do#", "Fa", "Sol#", "Si", "Re#", "Fa"],
    "Do# maj11": ["Do#", "Fa", "Sol#", "Do", "Re#", "Fa"],
    "Do# 13": ["Do#", "Fa", "Sol#", "Si", "Re#", "La"],
    "Do# maj13": ["Do#", "Fa", "Sol#", "Do", "Re#", "La"],

        # Accordi di Si
    "Si": ["Si", "Re#", "Fa#"],
    "Si min": ["Si", "Re", "Fa#"],
    "Si 7": ["Si", "Re#", "Fa#", "La"],
    "Si min7": ["Si", "Re", "Fa#", "La"],
    "Si maj7": ["Si", "Re#", "Fa#", "Do#"],
    "Si dim": ["Si", "Re", "Fa"],
    "Si min7b5": ["Si", "Re", "Fa", "Do"],
    "Si aug": ["Si", "Re#", "Fa"],
    "Si sus2": ["Si", "Do#", "Fa#"],
    "Si sus4": ["Si", "Mi", "Fa#"],
    "Si sus6": ["Si", "Fa#", "Sol#"],
    "Si min add2": ["Si", "Do#", "Re", "Fa#"],
    "Si min add4": ["Si", "Re", "Mi", "Fa#"],
    "Si add2": ["Si", "Do#", "Re#", "Fa#"],
    "Si add4": ["Si", "Re#", "Mi", "Fa#"],
    "Si add6": ["Si", "Re#", "Fa#", "Do#"],
    "Si minadd6": ["Si", "Re", "Fa#", "Do#"],
    "Si 9": ["Si", "Re#", "Fa#", "La", "Do#"],
    "Si min9": ["Si", "Re", "Fa#", "La", "Do#"],
    "Si maj9": ["Si", "Re#", "Fa#", "Do#", "Do#"],
    "Si 11": ["Si", "Re#", "Fa#", "La", "Do#", "Mi"],
    "Si maj11": ["Si", "Re#", "Fa#", "Do#", "Do#", "Mi"],
    "Si 13": ["Si", "Re#", "Fa#", "La", "Do#", "Mi"],
    "Si maj13": ["Si", "Re#", "Fa#", "Do#", "Do#", "Mi"],

    # Accordi di F#
    "Fa#": ["Fa#", "La#", "Do#"],
    "Fa# min": ["Fa#", "La", "Do#"],
    "Fa# 7": ["Fa#", "La#", "Do#", "Mi"],
    "Fa# min7": ["Fa#", "La", "Do#", "Mi"],
    "Fa# maj7": ["Fa#", "La#", "Do#", "Fa"],
    "Fa# dim": ["Fa#", "La", "Do"],
    "Fa# min7b5": ["Fa#", "La", "Do", "Mi"],
    "Fa# aug": ["Fa#", "La#", "Do"],
    "Fa# sus2": ["Fa#", "Sol#", "Do#"],
    "Fa# sus4": ["Fa#", "Si", "Do#"],
    "Fa# sus6": ["Fa#", "Do#", "Re#"],
    "Fa# min add2": ["Fa#", "Sol#", "La", "Do#"],
    "Fa# min add4": ["Fa#", "La", "Si", "Do#"],
    "Fa# add2": ["Fa#", "Sol#", "La#", "Do#"],
    "Fa# add4": ["Fa#", "La#", "Si", "Do#"],
    "Fa# add6": ["Fa#", "La#", "Do#", "Re"],
    "Fa# minadd6": ["Fa#", "La", "Do#", "Re"],
    "Fa# 9": ["Fa#", "La#", "Do#", "Mi", "Sol#"],
    "Fa# min9": ["Fa#", "La", "Do#", "Mi", "Sol#"],
    "Fa# maj9": ["Fa#", "La#", "Do#", "Fa", "Sol#"],
    "Fa# 11": ["Fa#", "La#", "Do#", "Mi", "Sol#", "Do"],
    "Fa# maj11": ["Fa#", "La#", "Do#", "Fa", "Sol#", "Do"],
    "Fa# 13": ["Fa#", "La#", "Do#", "Mi", "Sol#", "Re"],
    "Fa# maj13": ["Fa#", "La#", "Do#", "Fa", "Sol#", "Re"],

    # Accordi di G#
    "Sol#": ["Sol#", "Do", "Re#"],
    "Sol# min": ["Sol#", "Do", "Re"],
    "Sol# 7": ["Sol#", "Do", "Re#", "Fa#"],
    "Sol# min7": ["Sol#", "Do", "Re", "Fa#"],
    "Sol# maj7": ["Sol#", "Do", "Re#", "Sol"],
    "Sol# dim": ["Sol#", "Do", "Re"],
    "Sol# min7b5": ["Sol#", "Do", "Re", "Fa#"],
    "Sol# aug": ["Sol#", "Do", "Re#"],
    "Sol# sus2": ["Sol#", "La#", "Re#"],
    "Sol# sus4": ["Sol#", "Do#", "Re#"],
    "Sol# sus6": ["Sol#", "Re#", "Fa"],
    "Sol# min add2": ["Sol#", "La#", "Si", "Re#"],
    "Sol# min add4": ["Sol#", "Si", "Do#", "Re#"],
    "Sol# add2": ["Sol#", "La#", "Do", "Re#"],
    "Sol# add4": ["Sol#", "Do", "Do#", "Re#"],
    "Sol# add6": ["Sol#", "Do", "Re#", "Fa"],
    "Sol# minadd6": ["Sol#", "Do", "Re", "Fa"],
    "Sol# 9": ["Sol#", "Do", "Re#", "Fa#", "Si"],
    "Sol# min9": ["Sol#", "Do", "Re", "Fa#", "Si"],
    "Sol# maj9": ["Sol#", "Do", "Re#", "Sol", "Si"],
    "Sol# 11": ["Sol#", "Do", "Re#", "Fa#", "Si", "Re"],
    "Sol# maj11": ["Sol#", "Do", "Re#", "Sol", "Si", "Re"],
    "Sol# 13": ["Sol#", "Do", "Re#", "Fa#", "Si", "Re"],
    "Sol# maj13": ["Sol#", "Do", "Re#", "Sol", "Si", "Re"],
    # Accordi per Reb
    "Reb": ["Reb", "Fa", "Lab"],
    "Reb min": ["Reb", "Mi", "Lab"],
    "Reb 7": ["Reb", "Fa", "Lab", "Dob"],
    "Reb min7": ["Reb", "Mi", "Lab", "Dob"],
    "Reb maj7": ["Reb", "Fa", "Lab", "Do"],
    "Reb dim": ["Reb", "Mi", "Sol"],
    "Reb min7b5": ["Reb", "Mi", "Sol", "Dob"],
    "Reb aug": ["Reb", "Fa", "La"],
    "Reb sus2": ["Reb", "Mib", "Lab"],
    "Reb sus4": ["Reb", "Solb", "Lab"],
    "Reb sus6": ["Reb", "Lab", "Sib"],
    "Reb add2": ["Reb", "Mib", "Fa", "Lab"],
    "Reb add4": ["Reb", "Fa", "Solb", "Lab"],
    "Reb min add2": ["Reb", "Mib", "Mi", "Lab"],
    "Reb min add4": ["Reb", "Mi", "Solb", "Lab"],
    "Reb add6": ["Reb", "Fa", "Lab", "Sib"],
    "Reb minadd6": ["Reb", "Mi", "Lab", "Sib"],
    "Reb 9": ["Reb", "Fa", "Lab", "Dob", "Mib"],
    "Reb min9": ["Reb", "Mi", "Lab", "Dob", "Mib"],
    "Reb maj9": ["Reb", "Fa", "Lab", "Do", "Mib"],
    "Reb 11": ["Reb", "Fa", "Lab", "Dob", "Mib", "Solb"],
    "Reb maj11": ["Reb", "Fa", "Lab", "Do", "Mib", "Solb"],
    "Reb 13": ["Reb", "Fa", "Lab", "Dob", "Mib", "Sib"],
    "Reb maj13": ["Reb", "Fa", "Lab", "Do", "Mib", "Sib"],

    # Accordi per Solb
    "Solb": ["Solb", "Sib", "Reb"],
    "Solb min": ["Solb", "La", "Reb"],
    "Solb 7": ["Solb", "Sib", "Reb", "Mib"],
    "Solb min7": ["Solb", "La", "Reb", "Mib"],
    "Solb maj7": ["Solb", "Sib", "Reb", "Fa"],
    "Solb dim": ["Solb", "La", "Do"],
    "Solb min7b5": ["Solb", "La", "Do", "Mib"],
    "Solb aug": ["Solb", "Sib", "Re"],
    "Solb sus2": ["Solb", "Lab", "Reb"],
    "Solb sus4": ["Solb", "Dob", "Reb"],
    "Solb sus6": ["Solb", "Reb", "Mib"],
    "Solb add2": ["Solb", "Lab", "Sib", "Reb"],
    "Solb add4": ["Solb", "Sib", "Dob", "Reb"],
    "Solb min add2": ["Solb", "Lab", "La", "Reb"],
    "Solb min add4": ["Solb", "La", "Dob", "Reb"],
    "Solb add6": ["Solb", "Sib", "Reb", "Mib"],
    "Solb minadd6": ["Solb", "La", "Reb", "Mib"],
    "Solb 9": ["Solb", "Sib", "Reb", "Mib", "Lab"],
    "Solb min9": ["Solb", "La", "Reb", "Mib", "Lab"],
    "Solb maj9": ["Solb", "Sib", "Reb", "Fa", "Lab"],
    "Solb 11": ["Solb", "Sib", "Reb", "Mib", "Lab", "Dob"],
    "Solb maj11": ["Solb", "Sib", "Reb", "Fa", "Lab", "Dob"],
    "Solb 13": ["Solb", "Sib", "Reb", "Mib", "Lab", "Mib"],
    "Solb maj13": ["Solb", "Sib", "Reb", "Fa", "Lab", "Mib"],

    # Accordi per Dob
    "Dob": ["Dob", "Mi", "Solb"],
    "Dob min": ["Dob", "Mib", "Solb"],
    "Dob 7": ["Dob", "Mi", "Solb", "Lab"],
    "Dob min7": ["Dob", "Mib", "Solb", "Lab"],
    "Dob maj7": ["Dob", "Mi", "Solb", "Si"],
    "Dob dim": ["Dob", "Mib", "Fa"],
    "Dob min7b5": ["Dob", "Mib", "Fa", "Lab"],
    "Dob aug": ["Dob", "Mi", "Sol"],
    "Dob sus2": ["Dob", "Reb", "Solb"],
    "Dob sus4": ["Dob", "Fab", "Solb"],
    "Dob sus6": ["Dob", "Solb", "Lab"],
    "Dob add2": ["Dob", "Reb", "Mi", "Solb"],
    "Dob add4": ["Dob", "Mi", "Fab", "Solb"],
    "Dob min add2": ["Dob", "Reb", "Mib", "Solb"],
    "Dob min add4": ["Dob", "Mib", "Fab", "Solb"],
    "Dob add6": ["Dob", "Mi", "Solb", "Lab"],
    "Dob minadd6": ["Dob", "Mib", "Solb", "Lab"],
    "Dob 9": ["Dob", "Mi", "Solb", "Lab", "Reb"],
    "Dob min9": ["Dob", "Mib", "Solb", "Lab", "Reb"],
    "Dob maj9": ["Dob", "Mi", "Solb", "Si", "Reb"],
    "Dob 11": ["Dob", "Mi", "Solb", "Lab", "Reb", "Fab"],
    "Dob maj11": ["Dob", "Mi", "Solb", "Si", "Reb", "Fab"],
    "Dob 13": ["Dob", "Mi", "Solb", "Lab", "Reb", "Ab"],
    "Dob maj13": ["Dob", "Mi", "Solb", "Si", "Reb", "Ab"]
}

# mancano scale
tonalità_accordi_triadi = {
    # Scale maggiori per accordi
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
    
    # Scale minori naturali per accordi
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
    "Lab Minore": ["Lab min", "Sib dim", "Dob", "Reb min", "Mib min", "Fab", "Solb"],

    
    #scale minori armoniche per accordi

    "La Minore Armonica": ["La min", "Si dim", "Do aug", "Re min", "Mi", "Fa", "Sol# dim"],
    "Mi Minore Armonica": ["Mi min", "Fa# dim", "Sol aug", "La min", "Si", "Do", "Re# dim"],
    "Si Minore Armonica": ["Si min", "Do# dim", "Re aug", "Mi min", "Fa#", "Sol", "La# dim"],
    "Fa# Minore Armonica": ["Fa# min", "Sol# dim", "La aug", "Si min", "Do#", "Re", "Mi# dim"],
    "Do# Minore Armonica": ["Do# min", "Re# dim", "Mi aug", "Fa# min", "Sol#", "La", "Si# dim"],
    "Sol# Minore Armonica": ["Sol# min", "La# dim", "Si aug", "Do# min", "Re#", "Mi", "Fa## dim"],
    "Re# Minore Armonica": ["Re# min", "Mi# dim", "Fa# aug", "Sol# min", "La#", "Si", "Do## dim"],
    "La# Minore Armonica": ["La# min", "Si# dim", "Do# aug", "Re# min", "Mi#", "Fa#", "Sol## dim"],

    "Re Minore Armonica": ["Re min", "Mi dim", "Fa aug", "Sol min", "La", "Sib", "Do# dim"],
    "Sol Minore Armonica": ["Sol min", "La dim", "Sib aug", "Do min", "Re", "Mib", "Fa# dim"],
    "Do Minore Armonica": ["Do min", "Re dim", "Mib aug", "Fa min", "Sol", "Lab", "Si dim"],
    "Fa Minore Armonica": ["Fa min", "Sol dim", "Lab aug", "Sib min", "Do", "Reb", "Mi dim"],
    "Sib Minore Armonica": ["Sib min", "Do dim", "Reb aug", "Mib min", "Fa", "Solb", "La dim"],
    "Mib Minore Armonica": ["Mib min", "Fa dim", "Solb aug", "Lab min", "Sib", "Dob", "Re dim"],
    "Lab Minore Armonica": ["Lab min", "Sib dim", "Dob aug", "Reb min", "Mib", "Fab", "Sol dim"],



    #scale minori melodiche per accordi

    "La Minore Melodica": ["La min", "Si min", "Do aug", "Re", "Mi", "Fa# dim", "Sol# dim"],
    "Mi Minore Melodica": ["Mi min", "Fa# min", "Sol aug", "La", "Si", "Do# dim", "Re# dim"],
    "Si Minore Melodica": ["Si min", "Do# min", "Re aug", "Mi", "Fa#", "Sol# dim", "La# dim"],
    "Fa# Minore Melodica": ["Fa# min", "Sol# min", "La aug", "Si", "Do#", "Re# dim", "Mi# dim"],
    "Do# Minore Melodica": ["Do# min", "Re# min", "Mi aug", "Fa#", "Sol#", "La# dim", "Si# dim"],
    "Sol# Minore Melodica": ["Sol# min", "La# min", "Si aug", "Do#", "Re#", "Mi# dim", "Fa## dim"],
    "Re# Minore Melodica": ["Re# min", "Mi# min", "Fa# aug", "Sol#", "La#", "Si# dim", "Do## dim"],
    "La# Minore Melodica": ["La# min", "Si# min", "Do# aug", "Re#", "Mi#", "Fa## dim", "Sol## dim"],

    "Re Minore Melodica": ["Re min", "Mi min", "Fa aug", "Sol", "La", "Si dim", "Do# dim"],
    "Sol Minore Melodica": ["Sol min", "La min", "Sib aug", "Do", "Re", "Mi dim", "Fa# dim"],
    "Do Minore Melodica": ["Do min", "Re min", "Mib aug", "Fa", "Sol", "La dim", "Si dim"],
    "Fa Minore Melodica": ["Fa min", "Sol min", "Lab aug", "Sib", "Do", "Re dim", "Mi dim"],
    "Sib Minore Melodica": ["Sib min", "Do min", "Reb aug", "Mib", "Fa", "Sol dim", "La dim"],
    "Mib Minore Melodica": ["Mib min", "Fa min", "Solb aug", "Lab", "Sib", "Do dim", "Re dim"],
    "Lab Minore Melodica": ["Lab min", "Sib min", "Dob aug", "Reb", "Mib", "Fa dim", "Sol dim"]
}

tonalità_accordi_quadriadi = {
    # Scale maggiori
    "Do Maggiore7": [
        "Do maj7", "Re min7", "Mi min7", "Fa maj7", "Sol 7", "La min7", "Si min7b5"
    ],
    "Sol Maggiore7": [
        "Sol maj7", "La min7", "Si min7", "Do maj7", "Re 7", "Mi min7", "Fa# min7b5"
    ],
    "Re Maggiore7": [
        "Re maj7", "Mi min7", "Fa# min7", "Sol maj7", "La 7", "Si min7", "Do# min7b5"
    ],
    "La Maggiore7": [
        "La maj7", "Si min7", "Do# min7", "Re maj7", "Mi 7", "Fa# min7", "Sol# min7b5"
    ],
    "Mi Maggiore7": [
        "Mi maj7", "Fa# min7", "Sol# min7", "La maj7", "Si 7", "Do# min7", "Re# min7b5"
    ],
    "Si Maggiore7": [
        "Si maj7", "Do# min7", "Re# min7", "Mi maj7", "Fa# 7", "Sol# min7", "La# min7b5"
    ],
    "Fa# Maggiore7": [
        "Fa# maj7", "Sol# min7", "La# min7", "Si maj7", "Do# 7", "Re# min7", "Mi# min7b5"
    ],
    "Do# Maggiore7": [
        "Do# maj7", "Re# min7", "Mi# min7", "Fa# maj7", "Sol# 7", "La# min7", "Si# min7b5"
    ],
    
    "Fa Maggiore7": [
        "Fa maj7", "Sol min7", "La min7", "Sib maj7", "Do 7", "Re min7", "Mi min7b5"
    ],
    "Sib Maggiore7": [
        "Sib maj7", "Do min7", "Re min7", "Mib maj7", "Fa 7", "Sol min7", "La min7b5"
    ],
    "Mib Maggiore7": [
        "Mib maj7", "Fa min7", "Sol min7", "Lab maj7", "Sib 7", "Do min7", "Re min7b5"
    ],
    "Lab Maggiore7": [
        "Lab maj7", "Sib min7", "Do min7", "Reb maj7", "Mib 7", "Fa min7", "Sol min7b5"
    ],
    "Reb Maggiore7": [
        "Reb maj7", "Mib min7", "Fa min7", "Solb maj7", "Lab 7", "Sib min7", "Do min7b5"
    ],
    "Solb Maggiore7": [
        "Solb maj7", "Lab min7", "Sib min7", "Dob maj7", "Reb 7", "Mib min7", "Fa min7b5"
    ],
    "Dob Maggiore7": [
        "Dob maj7", "Reb min7", "Mib min7", "Fab maj7", "Solb 7", "Lab min7", "Sib min7b5"
    ],
    
    # Scale minori naturali
    "La Minore7": [
        "La min7", "Si min7b5", "Do maj7", "Re min7", "Mi min7", "Fa maj7", "Sol 7"
    ],
    "Mi Minore7": [
        "Mi min7", "Fa# min7b5", "Sol maj7", "La min7", "Si min7", "Do maj7", "Re 7"
    ],
    "Si Minore7": [
        "Si min7", "Do# min7b5", "Re maj7", "Mi min7", "Fa# min7", "Sol maj7", "La 7"
    ],
    "Fa# Minore7": [
        "Fa# min7", "Sol# min7b5", "La maj7", "Si min7", "Do# min7", "Re maj7", "Mi 7"
    ],
    "Do# Minore7": [
        "Do# min7", "Re# min7b5", "Mi maj7", "Fa# min7", "Sol# min7", "La maj7", "Si 7"
    ],
    "Sol# Minore7": [
        "Sol# min7", "La# min7b5", "Si maj7", "Do# min7", "Re# min7", "Mi maj7", "Fa# 7"
    ],
    "Re# Minore7": [
        "Re# min7", "Mi# min7b5", "Fa# maj7", "Sol# min7", "La# min7", "Si maj7", "Do# 7"
    ],
    "La# Minore7": [
        "La# min7", "Si# min7b5", "Do# maj7", "Re# min7", "Mi# min7", "Fa# maj7", "Sol# 7"
    ],
    
    "Re Minore7": [
        "Re min7", "Mi min7b5", "Fa maj7", "Sol min7", "La min7", "Sib maj7", "Do 7"
    ],
    "Sol Minore7": [
        "Sol min7", "La min7b5", "Sib maj7", "Do min7", "Re min7", "Mib maj7", "Fa 7"
    ],
    "Do Minore7": [
        "Do min7", "Re min7b5", "Mib maj7", "Fa min7", "Sol min7", "Lab maj7", "Sib 7"
    ],
    "Fa Minore7": [
        "Fa min7", "Sol min7b5", "Lab maj7", "Sib min7", "Do min7", "Reb maj7", "Mib 7"
    ],
    "Sib Minore7": [
        "Sib min7", "Do min7b5", "Reb maj7", "Mib min7", "Fa min7", "Solb maj7", "Lab 7"
    ],
    "Mib Minore7": [
        "Mib min7", "Fa min7b5", "Solb maj7", "Lab min7", "Sib min7", "Dob maj7", "Reb 7"
    ],
    "Lab Minore7": [
        "Lab min7", "Sib min7b5", "Dob maj7", "Reb min7", "Mib min7", "Fab maj7", "Solb 7"
    ],



    # Scale minori armoniche
    "La Minore Armonica7": [
        "La minMaj7", "Si min7b5", "Do aug7", "Re min7", "Mi 7", "Fa maj7", "Sol#dim7"
    ],
    "Mi Minore Armonica7": [
        "Mi minMaj7", "Fa# min7b5", "Sol aug7", "La min7", "Si 7", "Do maj7", "Re#dim7"
    ],
    "Si Minore Armonica7": [
        "Si minMaj7", "Do# min7b5", "Re aug7", "Mi min7", "Fa# 7", "Sol maj7", "La#dim7"
    ],
    "Fa# Minore Armonica7": [
        "Fa# minMaj7", "Sol# min7b5", "La aug7", "Si min7", "Do# 7", "Re maj7", "Mi#dim7"
    ],
    "Do# Minore Armonica7": [
        "Do# minMaj7", "Re# min7b5", "Mi aug7", "Fa# min7", "Sol# 7", "La maj7", "Si#dim7"
    ],
    "Sol# Minore Armonica7": [
        "Sol# minMaj7", "La# min7b5", "Si aug7", "Do# min7", "Re# 7", "Mi maj7", "Fa##dim7"
    ],
    "Re# Minore Armonica7": [
        "Re# minMaj7", "Mi# min7b5", "Fa# aug7", "Sol# min7", "La# 7", "Si maj7", "Do##dim7"
    ],
    
    "Re Minore Armonica7": [
        "Re minMaj7", "Mi min7b5", "Fa aug7", "Sol min7", "La 7", "Sib maj7", "Do#dim7"
    ],
    "Sol Minore Armonica7": [
        "Sol minMaj7", "La min7b5", "Sib aug7", "Do min7", "Re 7", "Mib maj7", "Fa#dim7"
    ],
    "Do Minore Armonica7": [
        "Do minMaj7", "Re min7b5", "Mib aug7", "Fa min7", "Sol 7", "Lab maj7", "Sidim7"
    ],
    "Fa Minore Armonica7": [
        "Fa minMaj7", "Sol min7b5", "Lab aug7", "Sib min7", "Do 7", "Reb maj7", "Midim7"
    ],
    "Sib Minore Armonica7": [
        "Sib minMaj7", "Do min7b5", "Reb aug7", "Mib min7", "Fa 7", "Solb maj7", "Ladim7"
    ],
    "Mib Minore Armonica7": [
        "Mib minMaj7", "Fa min7b5", "Solb aug7", "Lab min7", "Sib 7", "Dob maj7", "Redim7"
    ],

    # Scale minori melodiche
    "La Minore Melodica7": [
        "La minMaj7", "Si min7", "Do aug7", "Re 7", "Mi 7", "Fa# min7b5", "Sol# min7b5"
    ],
    "Mi Minore Melodica7": [
        "Mi minMaj7", "Fa# min7", "Sol aug7", "La 7", "Si 7", "Do# min7b5", "Re# min7b5"
    ],
    "Si Minore Melodica7": [
        "Si minMaj7", "Do# min7", "Re aug7", "Mi 7", "Fa# 7", "Sol# min7b5", "La# min7b5"
    ],    
    "Fa# Minore Melodica7": [
        "Fa# minMaj7", "Sol# min7", "La aug7", "Si 7", "Do# 7", "Re# min7b5", "Mi# min7b5"
    ],
    "Do# Minore Melodica7": [
        "Do# minMaj7", "Re# min7", "Mi aug7", "Fa# 7", "Sol# 7", "La# min7b5", "Si# min7b5"
    ],
    "Sol# Minore Melodica7": [
        "Sol# minMaj7", "La# min7", "Si aug7", "Do# 7", "Re# 7", "Mi# min7b5", "Fa## min7b5"
    ],
    
    "Re Minore Melodica7": [
        "Re minMaj7", "Mi min7", "Fa aug7", "Sol 7", "La 7", "Si min7b5", "Do# min7b5"
    ],
    "Sol Minore Melodica7": [
        "Sol minMaj7", "La min7", "Sib aug7", "Do 7", "Re 7", "Mi min7b5", "Fa# min7b5"
    ],
    "Do Minore Melodica7": [
        "Do minMaj7", "Re min7", "Mib aug7", "Fa 7", "Sol 7", "La min7b5", "Si min7b5"
    ],
    "Fa Minore Melodica7": [
        "Fa minMaj7", "Sol min7", "Lab aug7", "Sib 7", "Do 7", "Re min7b5", "Mi min7b5"
    ],
    "Sib Minore Melodica7": [
        "Sib minMaj7", "Do min7", "Reb aug7", "Mib 7", "Fa 7", "Sol min7b5", "La min7b5"
    ],
    "Mib Minore Melodica7": [
        "Mib minMaj7", "Fa min7", "Solb aug7", "Lab 7", "Sib 7", "Do min7b5", "Re min7b5"
    ]
}

# Troviamo vocabolari come valori di dizionari. esercizi con i nested dict
progressioni_base = {
    "progressione_0": {"gradi": [1, 6, 2, 5], "descrizione": "Turn Around"},
    "progressione_1": {"gradi": [1, 5, 6, 1], "descrizione": "Cadenza perfetta, stabile e risolutiva. Tipica nel rock e pop."},
    "progressione_2": {"gradi": [1, 6, 7, 5], "descrizione": "Molto usata nel pop, emotiva e aperta."},
    "progressione_3": {"gradi": [2, 5, 1], "descrizione": "Progressione jazz standard, perfetta per modulazioni."},
    "progressione_4": {"gradi": [1, 6, 4, 5], "descrizione": "Tipica delle ballate anni '50, armonia nostalgica."},
    "progressione_5": {"gradi": [1, 5, 1, 5], "descrizione": "Movimento classico con ritorno alla tonica prima della dominante."},
    "progressione_6": {"gradi": [6, 4, 1, 5], "descrizione": "Potente e malinconica, perfetta per brani emotivi."},
    "progressione_7": {"gradi": [1, 4, 6, 5], "descrizione": "Aperta e speranzosa, usata nel pop moderno."},
    "progressione_8": {"gradi": [1, 5, 4, 1], "descrizione": "Diretta e semplice, comune nel folk e rock classico."},
    "progressione_9": {"gradi": [1, 3, 4, 5], "descrizione": "Terzo grado minore crea un senso malinconico."},
    "progressione_10": {"gradi": [1, 5, 6, 3, 4], "descrizione": "Espressiva e cinematografica, usata nelle colonne sonore."},
    "progressione_11": {"gradi": [1, 2, 5, 1], "descrizione": "Armonia più aperta e leggera, usata nel folk."},
    "progressione_12": {"gradi": [1, 6, 2, 5], "descrizione": "Sospesa e malinconica, con tensione verso la dominante."},
    "progressione_13": {"gradi": [1, 4, 3, 5], "descrizione": "Un giro armonico equilibrato con un tocco di sorpresa."},
    "progressione_14": {"gradi": [1, 3, 5, 4], "descrizione": "Tipico giro rock/pop con colore minore interessante."},
    "progressione_15": {"gradi": [1, 5, 4, 2], "descrizione": "Fluida e morbida, con ritorno delicato alla tonica."}
}

progressioni_armoniche_lv1 = {
    "progression_1": {"gradi": [1, 4, 5, 1], "descrizione": "Classica cadenza perfetta, molto stabile e risolutiva."},
    "progression_2": {"gradi": [1, 3, 4, 1], "descrizione": "Progressione dolce e nostalgica, usata in ballate."},
    "progression_3": {"gradi": [1, 5, 4, 1], "descrizione": "Tensione e rilascio con passaggio sul sottodominante prima della tonica."},
    "progression_4": {"gradi": [1, 2, 5, 1], "descrizione": "Movimento più aperto e leggermente malinconico."},
    "progression_5": {"gradi": [1, 3, 5, 4], "descrizione": "Tipica progressione pop/rock con un colore minore."},
    "progression_6": {"gradi": [1, 4, 2, 5], "descrizione": "Tensione e rilascio con un secondo grado sospensivo."},
    "progression_7": {"gradi": [1, 6, 4, 5], "descrizione": "Progressione pop malinconica, molto usata in power ballad."},
    "progression_8": {"gradi": [1, 2, 4, 5], "descrizione": "Carattere fresco e aperto, molto usata in folk e country."},
    "progression_9": {"gradi": [1, 5, 3, 4], "descrizione": "Giro armonico con passaggio minore che crea contrasto."},
    "progression_10": {"gradi": [1, 3, 6, 4], "descrizione": "Molto espressiva e drammatica, tipica del rock e pop emotivo."},
    "progression_11": {"gradi": [1, 2, 5, 4], "descrizione": "Suono leggero e pop, perfetto per melodie cantabili."},
    "progression_12": {"gradi": [1, 4, 5, 3], "descrizione": "Giro classico con finale malinconico."},
    "progression_13": {"gradi": [1, 3, 5, 6], "descrizione": "Intensa e sospesa, usata per creare tensione."},
    "progression_14": {"gradi": [1, 5, 4, 2], "descrizione": "Movimento fluido con un ritorno morbido alla tonica."},
    "progression_15": {"gradi": [1, 6, 5, 4], "descrizione": "Emozionale e struggente, tipica del pop e rock ballad."},
    "progression_16": {"gradi": [1, 2, 6, 4], "descrizione": "Molto aperta e sognante, spesso usata in colonne sonore."},
    "progression_17": {"gradi": [1, 3, 4, 5], "descrizione": "Progressione classica, con passaggio dolce tra minore e maggiore."},
    "progression_18": {"gradi": [1, 4, 3, 5], "descrizione": "Giro armonico equilibrato, adatto per pop e jazz."},
    "progression_19": {"gradi": [1, 5, 2, 4], "descrizione": "Movimento più sofisticato con un secondo grado interessante."},
    "progression_20": {"gradi": [1, 6, 2, 5], "descrizione": "Armonia sospesa con un forte senso di malinconia."}
}

progressioni_armoniche_lv2 = {  
    "progression_21": {"gradi": [1, 3, 2, 5], "descrizione": "Suono delicato con movimenti modali."},
    "progression_22": {"gradi": [1, 4, 6, 5], "descrizione": "Tensione crescente con risoluzione finale."},
    "progression_23": {"gradi": [1, 5, 6, 4], "descrizione": "Tipica del pop contemporaneo, molto melodica."},
    "progression_24": {"gradi": [1, 2, 3, 5], "descrizione": "Colore modale con atmosfera sospesa."},
    "progression_25": {"gradi": [1, 6, 5, 3], "descrizione": "Molto emotiva, perfetta per climax sonori."},
    "progression_26": {"gradi": [1, 3, 5, 2], "descrizione": "Progressione dolce con un finale sospensivo."},
    "progression_27": {"gradi": [1, 4, 2, 6], "descrizione": "Effetto sognante, molto usata nel dream pop."},
    "progression_28": {"gradi": [1, 5, 6, 2], "descrizione": "Armonia aperta e dal carattere epico."},
    "progression_29": {"gradi": [1, 6, 3, 5], "descrizione": "Suono oscuro e profondo, perfetto per il rock."},
    "progression_30": {"gradi": [1, 2, 4, 6], "descrizione": "Cambia colore rapidamente, creando dinamica."},
    "progression_31": {"gradi": [1, 3, 2, 6], "descrizione": "Struttura particolare con un senso di apertura."},
    "progression_32": {"gradi": [1, 4, 6, 3], "descrizione": "Intensa e cinematografica."},
    "progression_33": {"gradi": [1, 5, 2, 6], "descrizione": "Grande varietà armonica e flusso aperto."},
    "progression_34": {"gradi": [1, 6, 4, 2], "descrizione": "Perfetta per passaggi evocativi."},
    "progression_35": {"gradi": [1, 2, 5, 3], "descrizione": "Tensione e rilascio con una sfumatura malinconica."},
    "progression_36": {"gradi": [1, 3, 6, 2], "descrizione": "Melanconica e drammatica, perfetta per ballad."},
    "progression_37": {"gradi": [1, 4, 5, 6], "descrizione": "Giro tipico della musica pop."},
    "progression_38": {"gradi": [1, 5, 4, 6], "descrizione": "Cambio armonico molto espressivo."},
    "progression_39": {"gradi": [1, 6, 2, 3], "descrizione": "Tensione crescente, risoluzione finale."},
    "progression_40": {"gradi": [1, 2, 3, 6], "descrizione": "Atmosfera eterea e fluttuante."}
}
# per utilizzare certi segni abbiamo avuto la necessità di creare un vocabolario dentro un vocabolario, abbiamo deciso quindi di inserire due vocabolari all'interno del principale con valori diversi per entrambi
pattern_ritmici = {
    "base": {
        "Pattern base": {
            "linear_drumming": ["K", "-", "S", "-", "H", "-", "K", "-"],
            "backbeat": ["K", "-", "S", "-", "H", "-", "S", "-"],
            "four_on_the_floor": ["K", "-", "K", "-", "K", "-", "K", "-"],
            "basic_rock_beat": ["K", "-", "S", "-", "H", "-", "K", "-"],
            "shuffle": ["K", "-", "S", "-", "H", "-", "K", "-"],
            "funk_groove": ["K", "H", "-", "S", "H", "-", "K", "H"]
        }
    },
    "avanzati": {
        "Pattern Avanzati Livello 1": {
            "blues_shuffle": ["K", "-", "S", "-", "H", "-", "K", "-"],
            "fast_metal_gallop": ["K", "-", "K", "-", "S", "-", "K", "-"]
        },
        "Pattern Avanzati Livello 2": {
            "disco_octaves": ["K", "-", "S", "-", "K", "-", "H", "-"],
            "slap_pop": ["K", "-", "H", "-", "S", "-", "H", "-"]
        }
    }
}

##################
### Nella Parte RITMO ###
#   IN FUTURO   --->   import music21: libreria per una migliore suddivisione metrica futura
##################

################################################################################################################################################################à






###############################################


#    FUNZIONI


#########################################################################################################################################################


#   PRIMA PARTE: FUNZIONI MOSTRA
#              Le 5 funzioni di seguito hanno il compito di mostrare i dati (liste, dizionari) a seconda degli input suggeriti all'utente.
#              viene Mostrato il Database completo


def mostranote():
    
    formatonote = input('\nCome vuoi vedere le note:\nFormato Latino o vuoi una mano a tradurre le note dal formato Anglosassone?\n[1 o 2]:')
    
    if formatonote == '1':
        print(f'\n\nNote formato Latino:\n{', '.join(note)}\n') #stampiamo la lista senza parentesi
    elif formatonote == '2':
        print('\nNote formato Anglosassone e relative in formato Latino:\n')
        for k, v in note_anglosassoni.items():     #potremmo stampare il dizionario senza farlo in un ciclo
            print (f'{k}: {v}\n')
    else:
        print('\n\nForse hai scritto male qualcosa\n')
    
    continua = continuare()
    # Se continuare() restituisce (None), che succede quando continua=='1',
    # allora richiama la stessa funzione
    if continua is None:
        mostranote()
    # Altrimenti, continuare() ha già gestito gli altri casi (menù o uscita)
    
    
def mostrascale():
    qualiscale = input('\nChe scale vuoi vedere:\n[0 : tutte le scale, 1 : maggiori , 2 : minori , 3 : modali, ! : cerca per parola chiave]\n')

    if qualiscale == '0':
        for nome, gradi in scale.items():
            print(f"{nome}: {', '.join(gradi)}")

    elif qualiscale == '1':  # Filtra solo le scale maggiori
        qualemaggiore = input('vuoi vedere la scala Maggiore o la Pentatonica?\n[scrivi "Maggiore" o "Pentatonica"]: ').strip().title()
        
        scale_maggiori_utente = {}
        # andiamo a cercare le notre scale utilizzando direttamente l'input dell'utente
        for k, v in scale.items():
            if qualemaggiore in k:
                scale_maggiori_utente[k] = v

        for nome, gradi in scale_maggiori_utente.items():
            print(f"{nome}: {', '.join(gradi)}\n")



    elif qualiscale == '2':  # Filtra solo le scale minori
        # ATTENZIONE: MANTENIAMO UNIFORMITà, ma PER ESERCIZIO: qui si può usare una comprehension per prendere tutte le scale minori
        # scale_minori = {k: v for k, v in scale.items() if 'Minore' in k}
        qualeminore = input('Quale scala minore vuoi vedere?\n[scrivi "Naturale" o "Armonica" o "Melodica" o "Pentatonica" o "Blues"]:').strip().capitalize()

        scale_minori_utente = {}

        for k, v in scale.items():
            if qualeminore in k:
                scale_minori_utente[k] = v

        for nome, gradi in scale_minori_utente.items():
            print(f"{nome}: {', '.join(gradi)}\n")


    elif qualiscale == '3':
        scalamodutente = input('Scrivi il numero della scala modale per vedere le sue note:\n[1: Dorica, 2: Frigia, 3: Lidia, 4: Misolidia, 5: Locria]: ').strip()
            #PER ESERCIZIO inseriamo un passaggio ulteriore, per controllare l'input dell'utente (che può essere qualsiasi) e andare noi a scrivere la key per andare a prendere il dizionario
            # L'UTENTE CI DA UN NUMERO, SIAMO NOI A CERCARE LA CHIAVE NEL DIZIONARIO.  nell'esercizio prima utilizziamo l'input dell'utente come stringa da cercare tra le nostre chiavi del dizionario
        scalaperutente = {}
        for k,v in scale_modali.items():
            if scalamodutente == '1':
                if 'Dorica' in k:
                    scalaperutente[k] = v

            elif  scalamodutente == '2':
                if 'Frigia' in k:
                    scalaperutente[k] = v

            elif  scalamodutente == '3':
                if 'Lidia' in k:
                    scalaperutente[k] = v
            
            elif  scalamodutente == '4':
                if 'Misolidia' in k:
                    scalaperutente[k] = v

            elif  scalamodutente == '5':
                if 'Locria' in k:
                    scalaperutente[k] = v

        for nome, gradi in scalaperutente.items():
            print(f"{nome}: {', '.join(gradi)}\n")

    elif qualiscale == '!':
        chiavediricerca = input('Inserisci una chiave di ricerca per trovare una o più scale precisamente:\n').strip().title()

    # questa funzione di ricerca per parola chiave è stata pensata per gli accordi e poi riproposta qui, dove abbiamo anche l'update dei due vocabolari in uno 
    elif qualiscale == '!':
        chiavediricerca = input('Inserisci una chiave di ricerca per trovare una o più scale precisamente:\n').strip().title()

        scaletrovate = {}

        # Combina i due dizionari in uno
        tutte_le_scale = {**scale, **scale_modali}

        for k, v in tutte_le_scale.items():
            if chiavediricerca in k:
                scaletrovate[k] = v

        if scaletrovate:
            for nome, note in scaletrovate.items():
                print(f"{nome}: {', '.join(note)}\n")
        else:
            print("Nessuna scala trovata con questa chiave di ricerca.\n")

    
    else:
        print('Forse hai scritto male qualcosa.\n')

    
    continua = continuare()
    # Se continuare() restituisce (None), che succede quando continua=='1',
    # allora richiama la stessa funzione
    if continua is None:
        mostrascale()


def mostraaccordi():
    accordidavedere = input("\nChe accordi vuoi vedere?\n[0 : tutti gli accordi, oppure inserisci una parola chiave per filtrare]\n\n[Notazione Tutor per ricerche complesse fraintendibili(ES. .accordi_sus = Si9,Do11,Mib13.  .minore = Rem.  .semidiminuito = Soldim7.)]\n")

    if accordidavedere == '0':
        for nome, note in accordi.items():
            print(f"{nome}: {', '.join(note)}\n")

    else:
        trovati = {k: v for k, v in accordi.items() if accordidavedere.lower() in k.lower()}
        
        # COSì, come prima, SE VOGLIAMO UTILIZZARE UN CICLO E NON UNA COMPREHENSION
        #for k, v in accordi.items():
            #if accordidavedere.lower() in k.lower():
            #    trovati[k] = v

        if trovati:
            for nome, note in trovati.items():
                print(f"{nome}: {', '.join(note)}\n")
        else:
            print("Nessun accordo trovato con questa chiave di ricerca.\n")

    # invoke della funzione e chiamata
    continua = continuare()
    if continua is None:
        mostraaccordi()

# dizionari dentro un dizionario : Nello specifico dobbiamo stampare i valori delle chiavi(che sono valoridi un dizionario): dizionari come valori delle chiavi di un dizionario
def mostraprogressioni():

    chiediprog = input('\nvuoi vedere le progressioni base o quelle avanzate?\n[scrivi "base" o "avanzate"]: ').strip().lower()
    
    if chiediprog == 'base':
        for nome, progr in progressioni_base.items():
            print(f'{nome}: {progr['gradi'], progr['descrizione']}\n')

        print('\nLegenda dei simboli:\n -> grado == indice accordo in riferimento alla scala che stiamo usando\n[Es. pensando alla scala di Do Maggiore: 1 = Do maggiore, 2= Re min]\n\n')


    elif chiediprog == 'avanzate':
        sceglilivello = input('che difficoltà vuoi vedere?\nLv[1-2]: ')

        if sceglilivello == '1':
            ### troviamo il valore di dizionari dentro dizionari
            for nome, progr in progressioni_armoniche_lv1.items():
                print(f"{nome}: {progr['gradi']},{progr['descrizione']}\n")

            print('\nLegenda dei simboli:\n -> grado == indice accordo in riferimento alla scala che stiamo usando\n[Es. pensando alla scala di Do Maggiore: 1 = Do maggiore, 2= Re min]\n\n')



        elif sceglilivello == '2':
            
            for nome, progr in progressioni_armoniche_lv2.items():
                print(f"{nome}: {progr['gradi']},{progr['descrizione']}\n")

            print('\nLegenda dei simboli:\n -> grado == indice accordo in riferimento alla scala che stiamo usando\n[Es. pensando alla scala di Do Maggiore: 1 = Do maggiore, 2= Re min]\n\n')

    else:
        print('Probabilmente hai scritto male\n')


    continua = continuare()
    if continua is None: # è None perchè la funzione continuare() non return niente e quindi è NONE!!!!!!!!!!!!!!!
        mostraprogressioni()

# come nel caso precedente abbiamo dizionari dentro dizionari. 
# in questo caso però i dizionari sono due diversi dentro uno, che contengono un dizionario ciascuno come valore
# dobbiamo prendere i valori di quello nested
def mostrapatternritmici():

    ## essendo questi pattern ritmici all'interno di un dizionario in un dizionario utilizziamo .get() per prendere quelli nested come riferimento e definiamolo come variabile

    chiedipattern = input('\nVuoi vedere i pattern ritmici base o quelli avanzati?\n[scrivi "base" o "avanzati"]: ').strip().lower()

    if chiedipattern == 'base':
        patternlv0 = pattern_ritmici.get("base")
        if patternlv0:
            for nome, ritmo in patternlv0.items():
                print(f"\n{nome}\n")
                for k,v in ritmo.items():
                    print(f'\n{k}: {', '.join(v)}\n')

        print('\nLegenda dei simboli:\nK = Cassa (Kick), S = Rullante (Snare), H = Hi-Hat, - = Pausa, Ogni riga rappresenta una misura in 4/4, dove il primo elemento 1 del tempo.\n\n')


    # la cosa è appena più complicata qui, perchè abbiamo due dizionari nested dentro uno che è nested e contiene più vocabolari
    elif chiedipattern == 'avanzati':
        sceglilivello = input('Che difficoltà vuoi vedere?\nLv[1-2]: ').strip()

        livello = f'Pattern Avanzati Livello {sceglilivello}'  # Costruisce la chiave corretta
        patternlivello = pattern_ritmici["avanzati"].get(livello)  # Prende solo il livello richiesto

        for nome, ritmo in patternlivello.items():
            print(f"\n{nome}: {' '.join(ritmo)}\n")
        else:
            print("Livello non valido. Inserisci 1 o 2.")

        print('\nLegenda dei simboli:\nK = Cassa (Kick), S = Rullante (Snare), H = Hi-Hat, - = Pausa, Ogni riga rappresenta una misura in 4/4, dove il primo elemento 1 del tempo.\n\n')

    continua = continuare()
    if continua is None:
        mostrapatternritmici()


#####################################################

#   SECONDA PARTE: FUNZIONI RECUPERA
#
#

def chiediscala_ottieninote():
    print('\nCHIEDI SCALA -> OTTIENI NOTE\n')
    print('[Utilizza questa notazione: *NOTA* *NOME SCALA* (Es.: Do Minore Naturale)]\n')
    print('Questi i NOME SCALA disponibili:\n[Maggiore - Minore Naturale - Minore Armonica - Minore Melodica - Pentatonica - Pentatonica min - Blues]\n')

    chiediscala = input('\nLe note di che scala vuoi sapere?\n').strip().title()
    
    scalaxutente = {}

    for k, v in scale.items():
        if chiediscala in k:
            scalaxutente[k] = v

        else:
            pass

    for x, y in scalaxutente.items():
        print(f'\n{x}:{','.join(y)} \n')
    
   
    continua = continuare()
    if continua is None:
        chiediscala_ottieninote()


def chiedinota_ottieniscala():
    print('CHIEDI NOTA -> OTTIENI SCALE ASSOCIATE\n')
    print('Queste sono le NOTE disponibili: "Do", "Do#/Reb", "Re", "Re#/Mib", "Mi", "Fa", "Fa#/Solb", "Sol", "Sol#/Lab", "La", "La#/Sib", "Si"\n\n')

    chiedinota = input('Dimmi una nota, ti dirò le scale associate ad essa:\n').strip().capitalize()

    scaleassociateanota = {}

    for scala, note in scale.items():
        if chiedinota in note:
            scaleassociateanota[scala] = note
        else: 
            pass

    for x ,y in scaleassociateanota.items():
        print(f'{x}: {','.join(y)}\n')


    continua = continuare()
    if continua is None:
        chiedinota_ottieniscala()


### DA RIVEDERE PER CAPIRE APPROFONDITAMENTE, MA FUNZIONA
def chiedinote_ottieniscalecomplementari():
    print('CHIEDI NOTE -> OTTIENI SCALE COMPLEMENTARI\n')
    print('Queste sono le NOTE disponibili: "Do", "Do#/Reb", "Re", "Re#/Mib", "Mi", "Fa", "Fa#/Solb", "Sol", "Sol#/Lab", "La", "La#/Sib", "Si"\n\n')

    print('Dammi fino a 3 note, vediamo le scale in cui compaiono insieme:\n')

    #puliamo l'imput dell'utente eliminando gli spazi eventuali in fondo e all'inizio, mettiamo lettere grandi dopo ogni spazio e alla prima parola
    chiedinote = input("Inserisci le note separate da spazio:\n").strip().title().split()
    #dividiamo le parole e ne creiamo quindi una lista con .split(), che poi trasformiamo in un set(): per avere a che fare con una ricerca su una collezione non ordinata
    
    if not (1 <= len(chiedinote) <= 3):  # questo in uno stile meno pythonic sarebbe: if len(noteutente) < 1 or len(noteutente) >= 4:
        print("Errore: inserisci da 1 a 3 note.\n")
        return

    scale_contenenti_tutte = {}
    ##
    # il codice così può funzionare, ma per la notazione che abbiamo dobbiamo applicare un criterio più stretto di ricerca
    #
    #noteutente = set(chiedinote)
    #for nome, note in scale.items():
     #   if noteutente & set(note):
      #      scale_contenenti_tutte[nome] = note
       #
        # facendo solo questo ciclo abbiamo un problema: il codice considera una stringa esatta da cercare, ma nelle scale potremmo avere varianti come "Mib" o "Mi#" che contengono "Mi" come sottostringa, causando falsi positivi.

    for nome, note in scale.items():
        # Confronto esatto tra le note dell'utente e quelle nella scala
        # Assicuriamoci che tutte le note dell'utente siano nella scala (come elementi esatti)
        trovate_tutte = True
        for nota_utente in chiedinote:
            if nota_utente not in note:  # Confronto esatto, non parziale
                trovate_tutte = False
                break
        
        if trovate_tutte:
            scale_contenenti_tutte[nome] = note


    print("\nScale che contengono tutte le note inserite:\n")
    if scale_contenenti_tutte:
        for nome_scala, note_scala in scale_contenenti_tutte.items():
            print(f'{nome_scala}: {', '.join(note_scala)}\n')
    else:
        print("Nessuna scala trovata.\n")


    continua = continuare()
    if continua is None:
        chiedinote_ottieniscalecomplementari()


# funzione appena più complessa di quella prima
def chiedinote_ottieniaccordi():
    print('\nCHIEDI NOTE -> OTTIENI ACCORDI')
    print('Queste sono le note disponibili: "Do", "Do#/Reb", "Re", "Re#/Mib", "Mi", "Fa", "Fa#/Solb", "Sol", "Sol#/Lab", "La", "La#/Sib", "Si"\n\n')
    print('Dammi 3 o 4 note, troverò gli accordi che le contengono esattamente e quelli che le includono con altre note.')

    # nella pulizia dell'input stavolta, invece di avere degli spazi tra gli input, chiediamo all'utente di usare una virgola, gli elementi della lista saranno dunque splittati ad ogni ,
    chiedinotxacc = input("Inserisci le note separate da virgola e uno spazio:\n").strip().title().split(', ')

    set_noteutente = set(chiedinotxacc)

    if not (3 <= len(set_noteutente) <= 4):
        print('Errore: inserisci 3 o 4 note.\n')
        return

    accordi_esatti = []
    accordi_contenenti = []

    for nome, note in accordi.items():
        set_note = set(note)

        if set_noteutente == set_note:
            accordi_esatti.append(nome)
        elif set_noteutente.issubset(set_note):  # Contiene tutte le note inserite ma può avere altre note       /// errore usare l'intersezione dei set perchè ti trova tutti gli accordi contenenti ogni nota, ogni due note e ogni tre note, gli accordi esatti non esistono più inoltre
            accordi_contenenti.append(nome)

    print("\nAccordi esatti (composti esattamente dalle note inserite):\n")
    if accordi_esatti:
        for accordo in accordi_esatti:
            print(f'{accordo}: {", ".join(accordi[accordo])}')
    else:
        print("Nessun accordo trovato.")

    print("\nAccordi contenenti tutte le note inserite (ma con altre note in aggiunta):\n")
    if accordi_contenenti:
        for accordo in accordi_contenenti:
            print(f'{accordo}: {", ".join(accordi[accordo])}\n')
    else:
        print("Nessun accordo trovato.\n")


    continua = continuare()
    if continua is None:
        chiedinote_ottieniaccordi()


def chiediaccordi_ottieninote():
    print('\nCHIEDI ACCORDI -> OTTIENI NOTE\n')
    print('Usa questa notazione: *NOTA*, *DESCRIZIONE*\n')
    print('Queste sono le NOTE disponibili: "Do", "Do#/Reb", "Re", "Re#/Mib", "Mi", "Fa", "Fa#/Solb", "Sol", "Sol#/Lab", "La", "La#/Sib", "Si"\n')
    print('Queste sono le DESCRIZIONI disponibili:\n(*N.B.:Nessuna descrizione per la Triade Maggiore)')
    print('[min, 7, min7, maj7, dim, min7b5, aug, sus2-4-6, add2-4-6, 9-11-13, min9-11-13, maj9-11-13]\n')
    print('Dimmi uno o più accordi separati da una virgola,e uno spazio, ne recupererò le note: (Es. Do 7, Mi maj7)')

    #un altro modo per pulire gli input
    chiediaccordi = input().strip().split(', ')

    accordiperutente = {}
    
    #for chord in chiediaccordi:
     #   for x, y in accordi.items():
      #      if chord in x:
       #         accordiperutente[x] = y
        #    
        #else:
         #   print('Accordo non trovato.\n')

    for chord in chiediaccordi:
        trovato = False
        for x, y in accordi.items():
            # Confronto esatto invece di controllo di substring
            if chord == x:
                accordiperutente[x] = y
                trovato = True
                break
        
        if not trovato:
            print(f'Accordo "{chord}" non trovato.\n')

    if accordiperutente:
        print('\nQueste sono le note per gli accordi da te richiesti:\n')

        for k, v in accordiperutente.items():
            print(f'{k}: {', '.join(v)}\n')
    
    continua = continuare()
    if continua is None:
        chiediaccordi_ottieninote()


def chieditonalità_ottieniaccordi():
    print("\nCHIEDI TONALITA' -> OTTIENI ACCORDI\n")
    print('Usa questa notazione: *NOTA* *DESCRIZIONE*\n')
    print('Queste sono le NOTE disponibili: "Do", "Do#/Reb", "Re", "Re#/Mib", "Mi", "Fa", "Fa#/Solb", "Sol", "Sol#/Lab", "La", "La#/Sib", "Si"')
    print('Queste sono le DESCRIZIONI disponibili: Maggiore(7), Minore(7), Minore armonica(7), Minore Melodica(7)\n\n')
    
    sceglitonalità = input('Scegli una tonalità ti mostrerò gli accordi connessi(Es. "Do Maggiore", "Sib Minore Melodica7"):\n').strip().title()

    tonalitàaccordiutente = {}

        # in questa funzione accettiamo la corrispondenza parziale perchè vogliamo vedere sia l'accordo triade che quello in quadriade
    # Controlla nelle triadi
    for x, y in tonalità_accordi_triadi.items():
        if sceglitonalità in x:  # Manteniamo la corrispondenza parziale \\ nelle altre funzioni cerchiamo invece l'uguaglianza della stringa e non, come in questo caso, la presenza della sottostringa.
            tonalitàaccordiutente[x] = y
        else:
            pass

    # Controlla nelle quadriadi
    for x, y in tonalità_accordi_quadriadi.items():
        if sceglitonalità in x:  # Manteniamo la corrispondenza parziale
            tonalitàaccordiutente[x] = y
        else:
            pass

    if tonalitàaccordiutente:
        for x, y in tonalitàaccordiutente.items():
            print(f'\n{x}: {', '.join(y)}\n')
    else:
        print("Nessun accordo trovato.\n")


    continua = continuare()
    if continua is None:
        chieditonalità_ottieniaccordi()


def chiediaccordi_ottienitonalita():
    print("CHIEDI ACCORDI -> OTTIENI TONALITA'")
    print('Usa questa notazione: *NOTA*, *DESCRIZIONE*\n')
    print('Queste sono le NOTE disponibili: "Do", "Do#/Reb", "Re", "Re#/Mib", "Mi", "Fa", "Fa#/Solb", "Sol", "Sol#/Lab", "La", "La#/Sib", "Si"')
    print('Queste sono le DESCRIZIONI disponibili:     *NO DESCRIZIONE per accordi maggiori\n["min", "dim", "maj7", "min7", "7", "aug", "aug7", "min7b5"]')
    print('N.B.: cerca accordi senza settima per ricevere tonalità in TRIADI, cerca accordi con settima per ricevere tonalità in QUADRIADI\n\n')

    chords = input("Inserisci fino a 4 accordi, separati da una virgola e uno spazio, ti dirò a quale tonalità appartengono:\n").strip()
 
    # Altro modo: Pulizia dell'input qui
    chordsutente = chords.split(', ')
    if not(1 <= len(chordsutente) <= 4):
        print('Inserisci un numero adeguato di accordi')
        return
    
    # Cerca le tonalità in cui sono presenti tutti gli accordi inseriti: 1.creandone un set
    set_noteutente = set(chordsutente)

    tonalitaaccordiutente = {}
    
    for nome, note in tonalità_accordi_triadi.items():
        set_note = set(note)                 # 2. confrontando il set con le liste del dizionario rese set()

        if set_noteutente.issubset(set_note):  
            tonalitaaccordiutente[nome] = note

    for nome, note in tonalità_accordi_quadriadi.items():
        set_note = set(note)

        if set_noteutente.issubset(set_note):  
            tonalitaaccordiutente[nome] = note
    
    if tonalitaaccordiutente:
        print("\nScale contenenti gli accordi richiesti:\n")
        for nome, accordi in tonalitaaccordiutente.items():
                print(f'{nome}: {", ".join(accordi)}\n')
    else:
        print("Nessuna scala trovata.")


    continua = continuare()
    if continua is None:
        chiediaccordi_ottienitonalita()



########################################
# Funzioni per il menù
########################################

def continuare():

    while True:
        continua = input('premere:\n1: Continua con la stessa funzione\n2: Torna al menù\n0: Esci da Music Tutor\n')

        if continua == '1':
            return 
        elif continua == '2':
            main_menu()
        elif continua == '0':
            exit('Alla prossima con il Music Tutor')
            break


def main_menu():    
    menu_options = {

        'FUNZIONI MOSTRA': 'PRIMA PARTE',

        '1': 'Mostra Note',
        '2': 'Mostra Scale',
        '3': 'Mostra Accordi',
        '4': 'Mostra Progressioni',
        '5': 'Mostra Pattern Ritmici',


        'FUNZIONI RECUPERA': 'SECONDA PARTE',


        '6': 'Chiedi Scala, ottieni note',
        '7': 'Chiedi Nota, ottieni scale',
        '8': 'Chiedi Note, ottieni scale complementari',
        '9': 'Chiedi Note, ottieni accordi',
        '10': 'Chiedi Accordo, ottieni note',
        '11': 'Chiedi Tonalità, ottieni accordi',
        '12': 'Chiedi Accordi, ottieni tonalità',
        
        '0': 'Esci'
    }
    
    print('\nBENVENUTO NEL MUSIC TUTOR:\n\n        Scegli una delle seguenti opzioni e segui le istruzioni dedicate:\n        N.B. La notazione usata nel MUSIC TUTOR è quella Latina\n\n        BUONA MUSICA\n\n')
    
        
    for x,y in menu_options.items():
        print(f'{x} : {y}\n')

    opzioni = input('DI COSA HAI BISOGNO? INSERISCI IL NUMERO PER ACCEDERE, PUOI CONTARE SU DI ME:\n')

    if opzioni == '1':
        mostranote()

    elif opzioni == '2':
        mostrascale()

    elif opzioni == '3':
        mostraaccordi()

    elif opzioni == '4':
        mostraprogressioni()

    elif opzioni == '5':
        mostrapatternritmici()

    elif opzioni == '6':
        chiediscala_ottieninote()

    elif opzioni == '7':
        chiedinota_ottieniscala()

    elif opzioni == '8':
        chiedinote_ottieniscalecomplementari()

    elif opzioni == '9':
        chiedinote_ottieniaccordi()

    elif opzioni == '10':
        chiediaccordi_ottieninote()

    elif opzioni == '11':
        chieditonalità_ottieniaccordi()

    elif opzioni == '12':
        chiediaccordi_ottienitonalita()

    elif opzioni == '0':
        print('\n\nUn saluto dal tuo Music Tutor\n\n')
        

if __name__ == '__main__':
    main_menu()