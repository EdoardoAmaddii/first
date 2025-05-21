# giorno 1 metronomo 2


# Metronomo Visuale con Tkinter
# ----------------------------------
'''
import time
import threading
import tkinter as tk
from tkinter import ttk

class Metronomo:
    def __init__(self, bpm=60, battute=4, beat_per_battuta=4):
        self.bpm = bpm
        self.battute = battute
        self.beat_per_battuta = beat_per_battuta
        self.running = False

    def avvia(self, callback_visuale):
        self.running = True
        intervallo = 60.0 / self.bpm
        for battuta in range(1, self.battute + 1):
            for beat in range(1, self.beat_per_battuta + 1):
                if not self.running:
                    return
                callback_visuale(battuta, beat)
                time.sleep(intervallo)
        self.running = False

    def ferma(self):
        self.running = False

# ---- GUI ----

class MetronomoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Metronomo Visuale")

        self.metronomo = None
        self.thread = None

        self.bpm_var = tk.IntVar(value=60)
        self.beat_var = tk.IntVar(value=4)
        self.battute_var = tk.IntVar(value=4)
        self.status = tk.StringVar(value="Inattivo")

        self.crea_widgets()

    def crea_widgets(self):
        tk.Label(self.root, text="BPM:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.bpm_var, width=5).grid(row=0, column=1)

        tk.Label(self.root, text="Beats per battuta:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.beat_var, width=5).grid(row=1, column=1)

        tk.Label(self.root, text="Numero di battute:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.battute_var, width=5).grid(row=2, column=1)

        self.visual = tk.Label(self.root, text="---", font=("Courier", 24))
        self.visual.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(self.root, text="Avvia", command=self.avvia_metronomo).grid(row=4, column=0)
        ttk.Button(self.root, text="Ferma", command=self.ferma_metronomo).grid(row=4, column=1)

        tk.Label(self.root, textvariable=self.status).grid(row=5, column=0, columnspan=2)

    def aggiorna_visuale(self, battuta, beat):
        display = ""
        for i in range(1, self.beat_var.get() + 1):
            display += "X " if i == beat else "- "
        testo = f"Battuta {battuta} - Beat {beat}\n{display}"
        self.visual.config(text=testo)
        self.status.set(f"BPM: {self.bpm_var.get()}")

    def avvia_metronomo(self):
        self.metronomo = Metronomo(
            bpm=self.bpm_var.get(),
            battute=self.battute_var.get(),
            beat_per_battuta=self.beat_var.get()
        )

        self.thread = threading.Thread(
            target=self.metronomo.avvia,
            args=(self.aggiorna_visuale,)
        )
        self.thread.start()
        self.status.set("In esecuzione...")

    def ferma_metronomo(self):
        if self.metronomo:
            self.metronomo.ferma()
        self.status.set("Interrotto")

# Avvio GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = MetronomoGUI(root)
    root.mainloop()

'''
#########################################################################################





# Metronomo con aggiunta di suono

# ----------------------------------




'''
import tkinter as tk
from tkinter import ttk
import time
import threading
import winsound

class Metronomo:
    def __init__(self, bpm=60, battute=4, beat_per_battuta=4):
        self.bpm = bpm
        self.battute = battute
        self.beat_per_battuta = beat_per_battuta
        self.running = False

    def suona_beat(self, beat):
        if beat == 1:
            winsound.Beep(880, 150)  # più acuto per il primo beat
        else:
            winsound.Beep(700, 130)  # più grave per gli altri

    def avvia(self, callback_visuale):
        self.running = True
        intervallo = 60.0 / self.bpm
        for battuta in range(1, self.battute + 1):
            for beat in range(1, self.beat_per_battuta + 1):
                if not self.running:
                    return
                self.suona_beat(beat)
                callback_visuale(battuta, beat)
                time.sleep(intervallo)
        self.running = False

    def ferma(self):
        self.running = False


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Metronomo Visuale")
        self.metronomo = None
        self.thread = None

        self.bpm_var = tk.IntVar(value=60)
        self.beat_var = tk.IntVar(value=4)
        self.battute_var = tk.IntVar(value=4)

        self.crea_interfaccia()

    def crea_interfaccia(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.grid()

        ttk.Label(frame, text="BPM:").grid(row=0, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.bpm_var, width=5).grid(row=0, column=1)

        ttk.Label(frame, text="Beats per battuta:").grid(row=1, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.beat_var, width=5).grid(row=1, column=1)

        ttk.Label(frame, text="Numero di battute:").grid(row=2, column=0, sticky="e")
        ttk.Entry(frame, textvariable=self.battute_var, width=5).grid(row=2, column=1)

        self.start_btn = ttk.Button(frame, text="Avvia", command=self.avvia_metronomo)
        self.start_btn.grid(row=3, column=0, pady=10)

        self.stop_btn = ttk.Button(frame, text="Ferma", command=self.ferma_metronomo, state="disabled")
        self.stop_btn.grid(row=3, column=1)

        self.visual = ttk.Label(frame, text="Pronto", font=("Helvetica", 16))
        self.visual.grid(row=4, column=0, columnspan=2, pady=20)

    def aggiorna_visuale(self, battuta, beat):
        def update():
            beats = ["X" if i + 1 == beat else "-" for i in range(self.beat_var.get())]
            testo = f"Battuta {battuta}, Beat {beat}   {' '.join(beats)}"
            self.visual.config(text=testo)
        self.root.after(0, update)

    def avvia_metronomo(self):
        bpm = self.bpm_var.get()
        beat = self.beat_var.get()
        battute = self.battute_var.get()

        self.metronomo = Metronomo(bpm, battute, beat)
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")

        self.thread = threading.Thread(target=self.metronomo.avvia, args=(self.aggiorna_visuale,))
        self.thread.daemon = True
        self.thread.start()

    def ferma_metronomo(self):
        if self.metronomo:
            self.metronomo.ferma()
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.visual.config(text="Fermato")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()


    







##########################################
    ci sono problemi col suono che si annulla, costruiamo una versione migliorata

'''










##########################################################################
# Metronomo Visuale con Tkinter e Suono
# ----------------------------------
# usiamo winsound per il suono e tkinter per l'interfaccia grafica


# opzione per accellerare di 1 BPM ogni battuta
# opzione per fermare il metronomo



import tkinter as tk
import winsound

class MetronomoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metronomo Visuale")

        self.bpm = tk.IntVar(value=60)
        self.beat_per_battuta = tk.IntVar(value=4)
        self.battute = tk.IntVar(value=4)
        self.accelera = tk.BooleanVar(value=False)

        self.is_running = False
        self.current_beat = 1
        self.current_battuta = 1

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="BPM iniziale").pack()
        tk.Entry(self.root, textvariable=self.bpm).pack()

        tk.Label(self.root, text="Beat per battuta").pack()
        tk.Entry(self.root, textvariable=self.beat_per_battuta).pack()

        tk.Label(self.root, text="Numero di battute").pack()
        tk.Entry(self.root, textvariable=self.battute).pack()

        tk.Checkbutton(self.root, text="Accelera automaticamente", variable=self.accelera).pack()

        self.start_button = tk.Button(self.root, text="Avvia", command=self.start_metronome)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_metronome)
        self.stop_button.pack(pady=5)

        self.status_label = tk.Label(self.root, text="", font=("Courier", 14))
        self.status_label.pack(pady=10)

        self.beat_display = tk.Label(self.root, text="", font=("Courier", 24))
        self.beat_display.pack()

    def start_metronome(self):
        if not self.is_running:
            try:
                self.is_running = True
                self.current_beat = 1
                self.current_battuta = 1
                self.interval = int(60000 / self.bpm.get())
                self.total_beats = self.battute.get() * self.beat_per_battuta.get()
                self.start_button.config(state=tk.DISABLED)
                self.tick()
            except Exception as e:
                self.status_label.config(text=f"Errore: {e}")

    def tick(self):
        if not self.is_running or self.current_battuta > self.battute.get():
            self.stop_metronome()
            return

        beat_pos = self.current_beat % self.beat_per_battuta.get()
        if beat_pos == 0:
            beat_pos = self.beat_per_battuta.get()

        # Visualizza stato
        self.status_label.config(
            text=f"Battuta: {self.current_battuta}/{self.battute.get()} | Beat: {beat_pos}/{self.beat_per_battuta.get()} | BPM: {self.bpm.get()}"
        )

        # Visualizzazione visiva
        beat_visual = ""
        for i in range(1, self.beat_per_battuta.get() + 1):
            beat_visual += "X " if i == beat_pos else "- "
        self.beat_display.config(text=beat_visual)

        # Suono
        if beat_pos == 1:
            winsound.Beep(880, 150)
        else:
            winsound.Beep(440, 150)

        self.current_beat += 1

        if beat_pos == self.beat_per_battuta.get():
            self.current_battuta += 1
            # Se accelerazione attiva, aumenta BPM
            if self.accelera.get():
                self.bpm.set(self.bpm.get() + 1)

        self.interval = int(60000 / self.bpm.get())
        self.root.after(self.interval, self.tick)

    def stop_metronome(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.status_label.config(text="Fermato.")
        self.beat_display.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetronomoApp(root)
    root.mainloop()

