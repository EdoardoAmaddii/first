# grafico a linee riempito

# rifare il plot a linee, riempire area, alpha
#riempire tra linea e punto, aggiungere condizione

import numpy as np
from matplotlib import pyplot as plt

plt.style.use('ggplot')

# ricreiamo il grafico a linee

x = np.array([25,26,27,28,29,30])
y = np.array([80,150,170,130,140,190])

media = sum(y)/len(y)


plt.plot(x,y)

# riempire la parte del grafico sotto alla linea
#    alpha = opacizzare il colore   1=max opaco // 0=min opaco

# media/ come qualsiasi altro valore possibile ci colora fuori dalla linea fino al valore, sopra il valore entro la riga
# il valore entro cui colorare deve essere messo prima la scelta e la vividezza dei colori, non in mezzo nè in fondo


# aggiungiamo una condizione con where, ma vediamo che non supporta il calcolo tra una lista e un intero. 
# sapendo che numpy ci permette di farlo importiamo e utilizziamo degli array
# se abbiamo anche la media(un altrovalore) assieme a where usiamo interpolate
## (solo con where ci colora la linea che si alza sulla x con valori sopra a 150 come abbiamo messo)
plt.fill_between(x,y, media, where=(y>150), color='blue', alpha=0.3, interpolate=True)





plt.title('Nome del grafico')

plt.show()