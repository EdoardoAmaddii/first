



'''
🔹 BLOCCO 1 - Fondamenti (Livello 1)
💡 Obiettivo: Approfondire liste, dizionari, input dell'utente e gestione dei dati in modo più avanzato.

1️⃣ Creare una lista di note musicali (Espansa)
📌 Cosa fare:

Crea una lista con le 12 note della scala cromatica con diesis e bemolli.
Stampa la lista in due formati:
Notazione normale
Con numerazione (1. Do, 2. Do#, ecc.)
python
Copia
Modifica
note_cromatiche = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]

print("Scala cromatica:", note_cromatiche)

for i, nota in enumerate(note_cromatiche, start=1):
    print(f"{i}. {nota}")
2️⃣ Recuperare una nota dalla lista (Espansa)
📌 Cosa fare:

Chiedi all’utente un numero da 1 a 12.
Stampa la nota corrispondente.
Se l’input è fuori range, mostra un messaggio di errore e chiedi di nuovo.
python
Copia
Modifica
while True:
    try:
        scelta = int(input("Inserisci un numero da 1 a 12 per ottenere la nota corrispondente: "))
        if 1 <= scelta <= 12:
            print(f"La nota corrispondente è: {note_cromatiche[scelta - 1]}")
            break
        else:
            print("Errore: il numero deve essere tra 1 e 12.")
    except ValueError:
        print("Errore: inserisci un numero valido.")
3️⃣ Creare un dizionario di scale (Espansa)
📌 Cosa fare:

Crea un dizionario con almeno 5 scale musicali.
Le scale devono avere le note in lista, non solo il nome.
Stampa le scale in modo chiaro.
python
Copia
Modifica
scale = {
    "Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Minore Naturale": ["Do", "Re", "Mib", "Fa", "Sol", "Lab", "Sib"],
    "Pentatonica Maggiore": ["Do", "Re", "Mi", "Sol", "La"],
    "Pentatonica Minore": ["Do", "Mib", "Fa", "Sol", "Sib"],
    "Blues": ["Do", "Mib", "Fa", "Fa#", "Sol", "Sib"]
}

for nome, note in scale.items():
    print(f"{nome}: {', '.join(note)}")
4️⃣ Recuperare una scala dal dizionario (Espansa)
📌 Cosa fare:

Chiedi all’utente il nome di una scala e mostra le note.
Se la scala non esiste, offrire una lista delle scale disponibili.
python
Copia
Modifica
while True:
    scelta = input("Inserisci il nome della scala musicale (es. Maggiore, Minore Naturale): ").strip().title()
    if scelta in scale:
        print(f"La scala {scelta} contiene le note: {', '.join(scale[scelta])}")
        break
    else:
        print("Scala non trovata. Ecco le scale disponibili:")
        print(", ".join(scale.keys()))
5️⃣ Creare un dizionario di accordi (Espansa)
📌 Cosa fare:

Crea un dizionario con almeno 5 accordi comuni (Maggiore, Minore, Dominante, ecc.).
Ogni accordo contiene le note che lo compongono.
Stampa la lista in modo leggibile.
python
Copia
Modifica
accordi = {
    "Do Maggiore": ["Do", "Mi", "Sol"],
    "Do Minore": ["Do", "Mib", "Sol"],
    "Sol Settima": ["Sol", "Si", "Re", "Fa"],
    "La Minore": ["La", "Do", "Mi"],
    "Re Maggiore": ["Re", "Fa#", "La"]
}

for nome, note in accordi.items():
    print(f"{nome}: {', '.join(note)}")
6️⃣ Recuperare un accordo dal dizionario (Espansa)
📌 Cosa fare:

Chiedi all’utente un accordo.
Se esiste, mostra le note.
Se non esiste, suggerisci gli accordi disponibili.
python
Copia
Modifica
scelta = input("Inserisci un accordo (es. Do Maggiore, La Minore): ").strip().title()

if scelta in accordi:
    print(f"L'accordo {scelta} è composto da: {', '.join(accordi[scelta])}")
else:
    print("Accordo non trovato. Ecco gli accordi disponibili:")
    print(", ".join(accordi.keys()))
7️⃣ Verificare se una nota appartiene a una scala (Espansa)
📌 Cosa fare:

Chiedi all’utente una scala e una nota.
Verifica se la nota è nella scala e stampa un messaggio.
python
Copia
Modifica
nome_scala = input("Inserisci il nome della scala: ").strip().title()
nota = input("Inserisci una nota: ").strip().capitalize()

if nome_scala in scale:
    if nota in scale[nome_scala]:
        print(f"La nota {nota} è nella scala {nome_scala}.")
    else:
        print(f"La nota {nota} NON è nella scala {nome_scala}.")
else:
    print("Scala non trovata.")
8️⃣ Trova il grado di una nota in una scala (Espansa)
📌 Cosa fare:

Chiedi all’utente una scala e una nota.
Se la nota è nella scala, mostra il grado (1°, 2°, ecc.).
python
Copia
Modifica
nome_scala = input("Inserisci il nome della scala: ").strip().title()
nota = input("Inserisci una nota: ").strip().capitalize()

if nome_scala in scale:
    if nota in scale[nome_scala]:
        grado = scale[nome_scala].index(nota) + 1
        print(f"La nota {nota} è il {grado}° grado della scala {nome_scala}.")
    else:
        print(f"La nota {nota} NON è nella scala {nome_scala}.")
else:
    print("Scala non trovata.")
9️⃣ Creare un menu interattivo (Espansa)
📌 Cosa fare:

Crea un menu con più opzioni per gestire scale e accordi.
python
Copia
Modifica
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Mostra una scala")
        print("2. Mostra un accordo")
        print("3. Verifica una nota in una scala")
        print("4. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            nome = input("Nome della scala: ").strip().title()
            print(scale.get(nome, "Scala non trovata."))
        elif scelta == "2":
            nome = input("Nome dell'accordo: ").strip().title()
            print(accordi.get(nome, "Accordo non trovato."))
        elif scelta == "3":
            nome_scala = input("Nome della scala: ").strip().title()
            nota = input("Inserisci una nota: ").strip().capitalize()
            print(f"La nota {nota} è nella scala {nome_scala}.") if nota in scale.get(nome_scala, []) else print("Nota non trovata.")
        elif scelta == "4":
            break
        else:
            print("Opzione non valida.")

menu()
🔟 Salvare e leggere dati da un file (Espansa)
📌 Cosa fare:

Scrivi il dizionario scale su un file .json.
Poi rileggi i dati.
python
Copia
Modifica
import json

with open("scale.json", "w") as file:
    json.dump(scale, file, indent=4)

with open("scale.json", "r") as file:
    dati = json.load(file)

print("Scale caricate dal file:", dati)
🔥 Questa versione ti dà una base più solida per sviluppi futuri!











#1️⃣ Creare una lista di note musicali (Espansa)
#Crea una lista con le 12 note della scala cromatica con diesis e bemolli.
#Stampa la lista in due formati:
#Notazione normale
#Con numerazione (1. Do, 2. Do#, ecc.)


note_cromatiche_diesis = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
note_cromatiche_bemolle = ["Do", "Reb", "Re", "Mib", "Mi", "Fa", "Solb", "Sol", "Lab", "La", "Sib", "Si"]

print (note_cromatiche_diesis)
print(note_cromatiche_bemolle)

#in un ciclo
for indice, nota in enumerate(note_cromatiche_bemolle, start=1):
    print(f"{indice}. {nota}")


#con dizionario

nuovodiziodiesis = {}
count = 0
for nota in note_cromatiche_bemolle:
    count += 1
    nuovodiziodiesis[count] = nota
print(nuovodiziodiesis)

#con dizio enumerate()
nuovodiziobemolle = {}        
for indice, nota in enumerate(note_cromatiche_diesis, start=1):
    nuovodiziobemolle[indice] = nota
print(nuovodiziobemolle)


# Creazione dizionario con enumerate()
dizionario_note = {indice: nota for indice, nota in enumerate(note_cromatiche_diesis, start=1)}
print("\nDizionario scala cromatica (diesis):", dizionario_note)


#con lista viene una cosa simile
nuovalista = []
for indice, nota in enumerate(note_cromatiche_diesis, start=1):
    nuovalista.append(indice)
    nuovalista.append(nota)
print(nuovalista)


# Creazione lista di tuple (indice, nota)
lista_numerata = [(indice, nota) for indice, nota in enumerate(note_cromatiche_diesis, start=1)]
print("\nLista numerata (diesis):", lista_numerata)


















print('\n\n\n\n')


#2️⃣ Recuperare una nota dalla lista (Espansa)
#📌 Cosa fare:

#Chiedi all’utente un numero da 1 a 12.
#Stampa la nota corrispondente.
#Se l’input è fuori range, mostra un messaggio di errore e chiedi di nuovo.

print(f'Dizionario diesis: {nuovodiziodiesis}')
print(f'Dizionario diesis: {nuovodiziobemolle}')

#se chiedi float input poi devi lavorare con i numeri: ricorda: i numeri che sono scritti in input diventano stringhe, puoi convertirli dopo

while True:
    chiedinota = input('Dammi un numero da 1 a 12, ti dirò la nota corrispondente (scrivi "q" per uscire):\n')

    if chiedinota.lower() == 'q':  # Controllo prima di convertire
        print('Arrivederci!')
        break

    if not chiedinota.isdigit():  # Controllo se è un numero
        print("Errore: devi inserire un numero tra 1 e 12.")
        continue

    numeronota = int(chiedinota)  # Conversione solo dopo i controlli

    if numeronota < 1 or numeronota > 12:  # Controllo del range
        print("Errore: il numero deve essere tra 1 e 12.")
        continue

    print(f"Nota diesis: {nuovodiziodiesis[numeronota]}, Nota bemolle: {nuovodiziobemolle[numeronota]}")



#con try except

while True:
    try:
        scelta = int(input("Inserisci un numero da 1 a 12 per ottenere la nota corrispondente: "))
        if 1 <= scelta <= 12:
            print(f"La nota corrispondente è: {note_cromatiche[scelta - 1]}")
            break
        else:
            print("Errore: il numero deve essere tra 1 e 12.")
    except ValueError:
        print("Errore: inserisci un numero valido.")
'''












#3️⃣ Creare un dizionario di scale (Espansa)
#📌 Cosa fare:

#Crea un dizionario con almeno 5 scale musicali.
#Le scale devono avere le note in lista, non solo il nome.
#Stampa le scale in modo chiaro.


scale = {
    "Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Minore Naturale": ["Do", "Re", "Mib", "Fa", "Sol", "Lab", "Sib"],
    "Pentatonica Maggiore": ["Do", "Re", "Mi", "Sol", "La"],
    "Pentatonica Minore": ["Do", "Mib", "Fa", "Sol", "Sib"],
    "Blues": ["Do", "Mib", "Fa", "Fa#", "Sol", "Sib"]
}

for nome, note in scale.items():
    print(f"{nome}: {', '.join(note)}")


#4️⃣ Recuperare una scala dal dizionario (Espansa)
#📌 Cosa fare:

#Chiedi all’utente il nome di una scala e mostra le note.
#Se la scala non esiste, offrire una lista delle scale disponibili.

qualescala = input('quale scala vuoi sapere?').strip().capitalize()
if qualescala in scale.keys():
    print(scale[qualescala])
else:
    print(f'la scala non esiste ancora o il programma è in fase di aggiornamento: queste sono le scale disponibili\n: {scale}')



#5️⃣ Creare un dizionario di accordi (Espansa)
#📌 Cosa fare:

#Crea un dizionario con almeno 5 accordi comuni (Maggiore, Minore, Dominante, ecc.).
#Ogni accordo contiene le note che lo compongono.
#Stampa la lista in modo leggibile.


accordi = {
    "Do Maggiore": ["Do", "Mi", "Sol"],
    "Do Minore": ["Do", "Mib", "Sol"],
    "Sol Settima": ["Sol", "Si", "Re", "Fa"],
    "La Minore": ["La", "Do", "Mi"],
    "Re Maggiore": ["Re", "Fa#", "La"]
}

for nome, note in accordi.items():
    print(f"{nome}: {', '.join(note)}")




#6️⃣ Recuperare un accordo dal dizionario (Espansa)
#📌 Cosa fare:

#Chiedi all’utente un accordo.
#Se esiste, mostra le note.
#Se non esiste, suggerisci gli accordi disponibili.

scegliaccordo = input('che accordo vuoi scomporre?').title()

for nome,accordo in accordi.items():
    if scegliaccordo not in accordi:
        print("Accordo non trovato. Ecco gli accordi disponibili:")
        print(", ".join(accordi.keys()))
    
    else:
        if scegliaccordo == nome:
            print(f'le note per questo accordo {scegliaccordo} sono: {accordo}')










#7️⃣ Verificare se una nota appartiene a una scala (Espansa)#
#📌 Cosa fare:
#
#Chiedi all’utente una scala e una nota.
#Verifica se la nota è nella scala e stampa un messaggio.


scale = {
    "Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Minore Naturale": ["Do", "Re", "Mib", "Fa", "Sol", "Lab", "Sib"],
    "Pentatonica Maggiore": ["Do", "Re", "Mi", "Sol", "La"],
    "Pentatonica Minore": ["Do", "Mib", "Fa", "Sol", "Sib"],
    "Blues": ["Do", "Mib", "Fa", "Fa#", "Sol", "Sib"]
}

scegliscala = input('dammi una scala:\n')
sceglinota = input('dammi una nota e vediamo se è nella scala:\n')

for scala, note in scale.items():
    if scegliscala == scala:
        for nota in note:
            if sceglinota == nota:
                print(f'la nota {sceglinota} è nella scala {scegliscala}')





'''

versione ottimizzata dei codici


Il codice è ben strutturato e copre tutte le funzionalità richieste, ma ci sono alcuni punti migliorabili:

Nella ricerca di un accordo, il controllo if scegliaccordo not in accordi: è dentro il ciclo for, il che porta a stamparlo più volte se l'accordo non esiste. Meglio verificare prima dell'iterazione.
Nella verifica della nota in una scala, il ciclo for non è necessario: basta usare l'operatore in per controllare se la nota è nella lista.
Migliore formattazione per rendere l'output più leggibile.
Gestione input con .strip().title() per evitare problemi con spazi o maiuscole/minuscole.
'''




# 5️⃣ Creare un dizionario di accordi
accordi = {
    "Do Maggiore": ["Do", "Mi", "Sol"],
    "Do Minore": ["Do", "Mib", "Sol"],
    "Sol Settima": ["Sol", "Si", "Re", "Fa"],
    "La Minore": ["La", "Do", "Mi"],
    "Re Maggiore": ["Re", "Fa#", "La"]
}

print("\n🎸 Lista degli accordi disponibili:")
for nome, note in accordi.items():
    print(f"{nome}: {', '.join(note)}")

# 6️⃣ Recuperare un accordo dal dizionario
scegliaccordo = input("\n🎵 Quale accordo vuoi scomporre?\n").strip().title()

if scegliaccordo in accordi:
    print(f"Le note dell'accordo {scegliaccordo} sono: {', '.join(accordi[scegliaccordo])}")
else:
    print("❌ Accordo non trovato. Ecco gli accordi disponibili:")
    print(", ".join(accordi.keys()))

# 7️⃣ Verificare se una nota appartiene a una scala
scale = {
    "Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Minore Naturale": ["Do", "Re", "Mib", "Fa", "Sol", "Lab", "Sib"],
    "Pentatonica Maggiore": ["Do", "Re", "Mi", "Sol", "La"],
    "Pentatonica Minore": ["Do", "Mib", "Fa", "Sol", "Sib"],
    "Blues": ["Do", "Mib", "Fa", "Fa#", "Sol", "Sib"]
}

scegliscala = input("\n🎼 Inserisci una scala musicale:\n").strip().title()
sceglinota = input("🎶 Inserisci una nota per verificare se è nella scala:\n").strip().capitalize()

if scegliscala in scale:
    if sceglinota in scale[scegliscala]:
        print(f"✅ La nota {sceglinota} è nella scala {scegliscala}.")
    else:
        print(f"❌ La nota {sceglinota} NON è nella scala {scegliscala}.")
else:
    print("❌ Scala non trovata. Ecco le scale disponibili:")
    print(", ".join(scale.keys()))

'''













#8️⃣ Trova il grado di una nota in una scala (Espansa)
#📌 Cosa fare:

#Chiedi all’utente una scala e una nota.
#Se la nota è nella scala, mostra il grado (1°, 2°, ecc.).

'''
scale = {
    "Maggiore": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
    "Minore Naturale": ["Do", "Re", "Mib", "Fa", "Sol", "Lab", "Sib"],
    "Pentatonica Maggiore": ["Do", "Re", "Mi", "Sol", "La"],
    "Pentatonica Minore": ["Do", "Mib", "Fa", "Sol", "Sib"],
    "Blues": ["Do", "Mib", "Fa", "Fa#", "Sol", "Sib"]
}


scegliscala = input("\n Inserisci una scala musicale:\n").strip().title()
sceglinota = input(" Inserisci una nota per verificare se è nella scala:\n").strip().capitalize()

if scegliscala in scale:
    if sceglinota in scale[scegliscala]:
        grado = scale[scegliscala].index(sceglinota) + 1
        print(f" La nota {sceglinota} è nella scala {scegliscala} al grado {grado}.")
    else:
        print(f" La nota {sceglinota} NON è nella scala {scegliscala}.")
else:
    print(" Scala non trovata. Ecco le scale disponibili:")
    print(", ".join(scale.keys()))













