# metronomo
#
# Metronomo Semplice


########################################
# questo il prompt da cui siamo partiti


##ragiona come un insegnante di musica: cosa mi faresti fare: dammi tre esempi da unire alla programmazione


########################################



'''
2. Metronomo Visuale
Un semplice metronomo basato su testo che insegna i concetti di tempo e ritmo:
Concetti musicali:

Tempo (BPM - battiti per minuto)
Time signatures (4/4, 3/4, ecc.)
Accenti metrici (primo battito più forte)
Organizzazione in battute

Concetti di programmazione:

Cicli for annidati (per battute e beat)
Gestione del tempo con sleep()
Input utente e convalida
Visualizzazione di uno stato che cambia

Attività per gli studenti:

Sperimentare con diversi tempi e time signatures
Aggiungere pattern ritmici personalizzati
Implementare un accelerando (aumento graduale del tempo)

'''











"""
Metronomo Semplice
-----------------
Uno strumento per esercitarsi con il tempo musicale.
Questo script visualizza un metronomo basato su testo che aiuta a mantenere
un tempo costante durante le esercitazioni musicali.
"""

import time
import os

def clear_screen():
    """Pulisce lo schermo per diversi sistemi operativi."""
    # Per Windows
    if os.name == 'nt':
        os.system('cls')
    # Per Mac e Linux
    else:
        os.system('clear')

def metronomo_visuale(bpm, battute=4, beat_per_battuta=4):
    """
    Visualizza un metronomo basato su testo.
    
    Args:
        bpm (int): Battiti al minuto
        battute (int): Numero di battute da suonare
        beat_per_battuta (int): Numero di beat per battuta (es. 4 per 4/4)
    """
    # Calcola l'intervallo di tempo tra i beat
    intervallo = 60.0 / bpm
    
    print(f"Metronomo impostato a {bpm} BPM in {beat_per_battuta}/4")
    print(f"Suonerà per {battute} battute")
    print("Premi Ctrl+C per interrompere")
    print("3... 2... 1... Via!")
    time.sleep(1)
    
    try:
        # Ciclo per ogni battuta
        for battuta in range(1, battute + 1):
            # Ciclo per ogni beat nella battuta
            for beat in range(1, beat_per_battuta + 1):
                clear_screen()
                
                # Visualizza la battuta e il beat corrente
                print(f"BPM: {bpm} | Battuta: {battuta}/{battute} | Beat: {beat}/{beat_per_battuta}")
                
                # Visualizza un indicatore grafico del beat
                beat_display = ""
                for i in range(1, beat_per_battuta + 1):
                    if i == beat:
                        beat_display += "X "  # Beat corrente
                    else:
                        beat_display += "- "  # Altri beat
                print(beat_display)
                
                # Visualizza indicatore speciale per il primo beat della battuta
                if beat == 1:
                    print("FORTE")  # Il primo beat è accentuato
                else:
                    print("piano")  # Altri beat sono più leggeri
                
                # Aspetta fino al prossimo beat
                time.sleep(intervallo)
                
        print("\nMetronomo completato!")
        
    except KeyboardInterrupt:
        print("\nMetronomo interrotto dall'utente.")

def metronomo_interattivo():
    """Versione interattiva del metronomo con input dell'utente."""
    try:
        # Richiedi i parametri all'utente
        bpm = int(input("Inserisci i BPM (battiti al minuto, es. 60-120): "))
        beat_per_battuta = int(input("Quanti beat per battuta? (es. 4 per 4/4, 3 per 3/4): "))
        battute = int(input("Per quante battute vuoi suonare? "))
        
        # Controlla che i valori siano validi
        if bpm <= 0 or beat_per_battuta <= 0 or battute <= 0:
            print("I valori devono essere positivi!")
            return
            
        # Avvia il metronomo
        metronomo_visuale(bpm, battute, beat_per_battuta)
        
    except ValueError:
        print("Errore: inserisci solo numeri interi!")

# Esempi di utilizzo
def main():
    print("=== METRONOMO SEMPLICE ===")
    print("1. Usa un preset")
    print("2. Personalizza il metronomo")
    
    scelta = input("Scelta: ")
    
    if scelta == "1":
        print("\nPreset disponibili:")
        print("1. Lento (60 BPM, 4/4)")
        print("2. Moderato (90 BPM, 4/4)")
        print("3. Veloce (120 BPM, 4/4)")
        print("4. Valzer (90 BPM, 3/4)")
        
        preset = input("Scegli un preset: ")
        
        if preset == "1":
            metronomo_visuale(60, 4, 4)
        elif preset == "2":
            metronomo_visuale(90, 4, 4)
        elif preset == "3":
            metronomo_visuale(120, 4, 4)
        elif preset == "4":
            metronomo_visuale(90, 4, 3)
        else:
            print("Preset non valido!")
    
    elif scelta == "2":
        metronomo_interattivo()
    
    else:
        print("Scelta non valida!")

# Esercizi per studenti
def esercizi_studenti():
    print("\n=== ESERCIZI PER STUDENTI ===")
    print("1. Aggiungi un suono per ogni beat (richiede libreria aggiuntiva)")
    print("2. Implementa pattern ritmici diversi (es. accentuare solo certi beat)")
    print("3. Crea una funzione per aumentare gradualmente il BPM (utile per esercitarsi)")

if __name__ == "__main__":
    main()
    esercizi_studenti()