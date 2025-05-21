### grafici a barre [ BAR CHARTS ]

import numpy as np
from matplotlib import pyplot as plt

x  = [25,26,27,28,29,30]

y = [100,120,140,110,150,145]

y2 = [90,80,120,150,170,140]



plt.style.use('ggplot')
indexs = np.arange (6) # tanti quanti gli elementi
width = 0.3


plt.bar(indexs,y, label = 'italiani', width=width, color = 'red')   # invece che plot mettiamo bar
plt.bar(indexs+width,y2, label = 'francesi',width=width, color = '#212121')   # possiamo avere righe e barre insieme
# se mettiamo due grafici a barrre ce li sovrappone (si capisce abbastanza per via dei colori, ma non è comodo)
# non c'è un metodo veloce per affiancare le barre, dobbiamo importare NUMPY
# indexs     :     specifichiamo gli indici innanzitutto
# mettiamo i numeri delle x sugli indici
##################### l'idea è quella di dividere la barra e usarla a metà per le due valutazioni
# width
# index+width : ci divide le barre
#################### rimane il problema che i tick sono sulla prima barra e noi li vogliamo nel mezzo tra le due
# tick al centro e rinominati
# plt.xticks




plt.title('Nome del grafico')
plt.xlabel('età')
plt.ylabel('valori')
plt.legend() 

plt.xticks(indexs+width/2, x) # me li metti in posizione sull'indice + la width/2  # se arriviamo fino a qui ci sono i numeri degli indici # dopo la virgola mettiamo la x come nome


plt.show()



# voglio mettere il grafico in orizzontale

# plt.barh

# c'è problema con questo codice perchè chiaramente stiamo spostando tutto sull'asse delle y
# dovremmo mettere tutto il codice sull'asse delle y

