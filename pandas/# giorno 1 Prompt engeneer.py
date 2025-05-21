# giorno 1 Prompt engeneer

lista_note = ['C', 'E', 'G', 'B']

#scrivo una funzione che assegna ad ogni nota un colpo ritmico
def colpo_ritmico(nota):
    if nota == 'C':
        return 'Kick'
    elif nota == 'E':
        return 'Snare'
    elif nota == 'G':
        return 'kick'
    elif nota == 'B':
        return 'Snare'
    else:
        return '0'  # valore di default se la nota non è riconosciuta
    

#applico la funzione a ogni nota della lista
note_e_ritmo = colpo_ritmico('C') + ' ' + colpo_ritmico('E') + ' ' + colpo_ritmico('G') + ' ' + colpo_ritmico('B')
# creo una stringa che contiene i colpi ritmici associati alle note
print(note_e_ritmo)  # stampa il risultato



"""
Prompt da usare:

Ho una lista di note ["C", "E", "G", "B"]. Voglio scrivere una funzione Python che assegna a ogni nota un colpo ritmico (es: C → kick, E → snare, ecc). Mi aiuti a strutturarla con commenti?

Come posso trasformare questa funzione in una versione più estensibile, dove i pattern sono personalizzabili via input dell’utente?

Puoi suggerirmi come salvare l output ritmico su un file .txt?
    
    """




######
# questo esercizio è inutile, dato che non serve a niente, ma è un esercizio di programmazione
# e di scrittura di codice, quindi lo facciamo lo stesso
# e lo commentiamo

# creando la lista di note associate ad un pattern ritmico infatti non ha senso, dato che non serve a niente
# e non ha un significato musicale, ma è solo un esercizio di programmazione

# l'AI non ha compreso che non ha senso, ma lo fa lo stesso

# IL PROSSSIMO PASSO SARà QUELLO DI CREARE UN GENERATORE DI PATTERN RITMICI

# E DI CREARE UN FILE .TXT CON I PATTERN RITMICI


# CHIEDIAMO PERCIò ALL'AI
# DI CREARE UN GENERATORE DI PATTERN RITMICI

'''
ragiona come un insegnante di python e musica, da dove partiresti?
'''
# Iniziamo a creare un generatore di pattern ritmici musicali



"""
Generatore di Pattern Ritmici
-----------------------------
Questo script permette di creare, modificare e salvare pattern ritmici musicali
utilizzando la notazione comune per la programmazione di batterie elettroniche.
"""

class RhythmPattern:
    def __init__(self, beats_per_measure=4, measures=1):
        """
        Inizializza un pattern ritmico.
        
        Args:
            beats_per_measure (int): Numero di beat per battuta (default: 4 per 4/4)
            measures (int): Numero di battute nel pattern (default: 1)
        """
        self.beats_per_measure = beats_per_measure
        self.measures = measures
        self.total_beats = beats_per_measure * measures
        
        # Inizializza gli strumenti di batteria con pattern vuoti
        self.instruments = {
            "kick": ["0"] * self.total_beats,
            "snare": ["0"] * self.total_beats,
            "hi-hat": ["0"] * self.total_beats,
            "crash": ["0"] * self.total_beats,
            "tom": ["0"] * self.total_beats
        }
    
    def add_hit(self, instrument, beat_positions):
        """
        Aggiunge colpi a uno strumento su beat specifici.
        
        Args:
            instrument (str): Nome dello strumento (kick, snare, hi-hat, ecc.)
            beat_positions (list): Lista di posizioni (1-based) dove aggiungere colpi
        """
        if instrument not in self.instruments:
            print(f"Strumento '{instrument}' non valido. Strumenti disponibili: {list(self.instruments.keys())}")
            return
            
        for pos in beat_positions:
            # Converti dalla notazione 1-based a 0-based per l'indice
            index = pos - 1
            if 0 <= index < self.total_beats:
                self.instruments[instrument][index] = "X"
            else:
                print(f"Posizione {pos} fuori range (1-{self.total_beats})")
    
    def clear_instrument(self, instrument):
        """Cancella tutti i colpi per uno strumento specifico."""
        if instrument in self.instruments:
            self.instruments[instrument] = ["0"] * self.total_beats
        else:
            print(f"Strumento '{instrument}' non valido.")
    
    def set_accent(self, instrument, beat_positions):
        """Imposta un accento (colpo più forte) su beat specifici."""
        if instrument not in self.instruments:
            print(f"Strumento '{instrument}' non valido.")
            return
            
        for pos in beat_positions:
            index = pos - 1
            if 0 <= index < self.total_beats:
                self.instruments[instrument][index] = "A"  # A per accento
            else:
                print(f"Posizione {pos} fuori range (1-{self.total_beats})")
    
    def display(self):
        """Mostra il pattern ritmico in formato leggibile."""
        print(f"\nPattern ritmico ({self.measures} battute in {self.beats_per_measure}/4):")
        print("=" * (self.total_beats * 2 + 10))
        
        # Stampa i numeri dei beat come riferimento
        beat_numbers = "    "
        for i in range(1, self.total_beats + 1):
            beat_numbers += f"{i} "
        print(beat_numbers)
        
        # Stampa misure separate
        measures_separator = "    "
        for m in range(self.measures):
            measures_separator += "| " + "- " * (self.beats_per_measure - 1) + "| "
        print(measures_separator)
        
        # Stampa ogni strumento
        for instrument, pattern in self.instruments.items():
            display_line = f"{instrument.ljust(7)}"
            for beat in pattern:
                display_line += f"{beat} "
            print(display_line)
        
        print("=" * (self.total_beats * 2 + 10))
    
    def save_to_file(self, filename="rhythm_pattern.txt"):
        """Salva il pattern ritmico su un file di testo."""
        try:
            with open(filename, 'w') as file:
                file.write(f"Pattern ritmico ({self.measures} battute in {self.beats_per_measure}/4):\n")
                file.write("=" * (self.total_beats * 2 + 10) + "\n")
                
                # Scrivi i numeri dei beat
                beat_numbers = "    "
                for i in range(1, self.total_beats + 1):
                    beat_numbers += f"{i} "
                file.write(beat_numbers + "\n")
                
                # Scrivi i separatori di misura
                measures_separator = "    "
                for m in range(self.measures):
                    measures_separator += "| " + "- " * (self.beats_per_measure - 1) + "| "
                file.write(measures_separator + "\n")
                
                # Scrivi gli strumenti
                for instrument, pattern in self.instruments.items():
                    display_line = f"{instrument.ljust(7)}"
                    for beat in pattern:
                        display_line += f"{beat} "
                    file.write(display_line + "\n")
                
                file.write("=" * (self.total_beats * 2 + 10) + "\n")
                
                # Aggiungi una legenda
                file.write("\nLegenda:\n")
                file.write("X = colpo normale\n")
                file.write("A = colpo accentato\n")
                file.write("0 = silenzio\n")
                
            print(f"Pattern salvato con successo in '{filename}'")
        except Exception as e:
            print(f"Errore durante il salvataggio: {e}")

    def create_from_rhythm_string(self, instrument, rhythm_string):
        """
        Crea un pattern da una stringa ritmmica (es. "X00X0X00").
        
        Args:
            instrument (str): Nome dello strumento
            rhythm_string (str): Stringa di X (colpi) e 0 (silenzi)
        """
        if instrument not in self.instruments:
            print(f"Strumento '{instrument}' non valido.")
            return
            
        # Tronca o estendi la stringa se necessario
        if len(rhythm_string) < self.total_beats:
            rhythm_string = rhythm_string.ljust(self.total_beats, '0')
        elif len(rhythm_string) > self.total_beats:
            rhythm_string = rhythm_string[:self.total_beats]
            
        self.instruments[instrument] = list(rhythm_string)


# Esempi di utilizzo
def main():
    # Esempio 1: Creare un basic beat (4/4)
    print("Esempio 1: Pattern base 4/4")
    pattern = RhythmPattern(beats_per_measure=4, measures=1)
    pattern.add_hit("kick", [1, 3])  # Kick sul beat 1 e 3
    pattern.add_hit("snare", [2, 4])  # Snare sul beat 2 e 4
    pattern.add_hit("hi-hat", [1, 2, 3, 4])  # Hi-hat su tutti i beat
    pattern.display()
    
    # Esempio 2: Pattern più complesso
    print("\nEsempio 2: Pattern più complesso 4/4 con due battute")
    complex_pattern = RhythmPattern(beats_per_measure=4, measures=2)
    complex_pattern.add_hit("kick", [1, 3, 5, 7])
    complex_pattern.add_hit("snare", [2, 4, 6, 8])
    complex_pattern.add_hit("hi-hat", [1, 2, 3, 4, 5, 6, 7, 8])
    complex_pattern.set_accent("hi-hat", [1, 5])  # Accenti sul primo beat di ogni battuta
    complex_pattern.display()
    
    # Esempio 3: Creare pattern da stringa ritmica
    print("\nEsempio 3: Pattern da stringa ritmica")
    string_pattern = RhythmPattern(beats_per_measure=4, measures=2)
    string_pattern.create_from_rhythm_string("kick", "X00X00X0")
    string_pattern.create_from_rhythm_string("snare", "00X000X0")
    string_pattern.create_from_rhythm_string("hi-hat", "XXXXXXXX")
    string_pattern.display()
    string_pattern.save_to_file("pattern_esempio.txt")
    
    # Esempio 4: Pattern in 3/4
    print("\nEsempio 4: Pattern in 3/4 (valzer)")
    waltz = RhythmPattern(beats_per_measure=3, measures=2)
    waltz.add_hit("kick", [1, 4])
    waltz.add_hit("snare", [2, 3, 5, 6])
    waltz.create_from_rhythm_string("hi-hat", "X0XX0X")
    waltz.display()

# Interfaccia interattiva
def interactive_mode():
    print("\n=== GENERATORE DI PATTERN RITMICI ===")
    
    # Imposta il time signature
    beats = int(input("Quanti beat per battuta? (es. 4 per 4/4): "))
    measures = int(input("Quante battute nel pattern? "))
    
    pattern = RhythmPattern(beats_per_measure=beats, measures=measures)
    
    while True:
        print("\nCosa vuoi fare?")
        print("1. Aggiungi colpi a uno strumento")
        print("2. Cancella uno strumento")
        print("3. Crea pattern da stringa")
        print("4. Visualizza pattern attuale")
        print("5. Salva pattern su file")
        print("6. Esci")
        
        choice = input("Scelta: ")
        
        if choice == "1":
            instr = input("Strumento (kick, snare, hi-hat, crash, tom): ")
            positions = input("Posizioni dei colpi (numeri separati da spazi): ")
            try:
                pos_list = [int(p) for p in positions.split()]
                pattern.add_hit(instr, pos_list)
            except ValueError:
                print("Inserisci solo numeri separati da spazi.")
        
        elif choice == "2":
            instr = input("Strumento da cancellare: ")
            pattern.clear_instrument(instr)
            
        elif choice == "3":
            instr = input("Strumento: ")
            rhythm = input(f"Stringa ritmica (X per colpi, 0 per silenzi, {pattern.total_beats} caratteri): ")
            pattern.create_from_rhythm_string(instr, rhythm)
            
        elif choice == "4":
            pattern.display()
            
        elif choice == "5":
            filename = input("Nome del file: ")
            if not filename:
                filename = "pattern.txt"
            pattern.save_to_file(filename)
            
        elif choice == "6":
            print("Arrivederci!")
            break
            
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()  # Esegui gli esempi
    
    # Chiedi all'utente se vuole utilizzare la modalità interattiva
    use_interactive = input("\nVuoi utilizzare la modalità interattiva? (s/n): ")
    if use_interactive.lower() in ['s', 'si', 'sì', 'y', 'yes']:
        interactive_mode()











# In questo modo abbiamo creato un generatore di pattern ritmici musicali
# che permette di creare, modificare e salvare pattern ritmici musicali
# utilizzando la notazione comune per la programmazione di batterie elettroniche.























################################################################################################



