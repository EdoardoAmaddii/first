#####################################################

from datetime import datetime, timedelta
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import matplotlib.ticker as ticker
import matplotlib.lines as mlines

import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import numpy as np
import pandas as pd




# GLOBAL API
# 1. importare la libreria
# 2. creare una figura e un asse
# 3. creare i dati
# 4. creare il grafico
# 5. mostrare il grafico
# 6. salvare il grafico
# 7. chiudere il grafico

# 8. creare un grafico a dispersione
# 9. creare un grafico a dispersione con una linea di regressione
# 10. creare un grafico a dispersione con una linea di regressione e una curva di regressione
# 11. creare un grafico a dispersione con una linea di regressione e una curva di regressione e una retta di regressione

# 12 creare un istogramma con i dati x
# 13 creare un istogramma con i dati x e una curva di regressione
# 14 creare un istogramma con i dati x e una curva di regressione e una retta di regressione

x = np.arange(-10, 11) # crea un array di valori da -10 a 10
y = np.arange(-10, 11) 


# iniziamo a creare un grafico a dispersione con i dati x
# non mi interessa il valore di y, ma voglio vedere i punti x, posso inserire i valory di y nel plot

plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='red', label='Dati x')  # scatter è un grafico a dispersione, mentre plot è un grafico a linee


plt.title('Grafico a dispersione')
plt.xlabel('Asse x')
plt.ylabel('Asse y')
plt.legend('LEGENDA QUI')  # mostra la legenda
plt.grid(True)  # mostra la griglia
plt.gca().set_aspect('equal', adjustable='box')  # imposta l'aspetto del grafico
plt.gca().set_aspect('equal', adjustable='box')  # imposta l'aspetto del grafico

plt.gca().set_xlim(-10, 10)  # imposta i limiti dell'asse x
plt.gca().set_ylim(-10, 10)  # imposta i limiti dell'asse y

plt.show()
plt.savefig('grafico_a_dispersione.png')  # salva il grafico in un file

plt.close()  # chiude il grafico




# ora creiamo un grafico a dispersione con una linea di regressione
# creiamo un array di valori casuali per y

y = (2 *x + 1 + 0.5 * np.random.randn(len(x)))  # crea un array di valori casuali per y

# diamo un errore casuale di 0.5

# creiamo un array anche per la retta di regressione

y_fit = 2 * x + 1  # crea un array di valori casuali per y
# creiamo un array anche per la retta di regressione

plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='red', label='Dati x')  # scatter è un grafico a dispersione, mentre plot è un grafico a linee
plt.plot(x, y_fit, color='blue', label='Retta di regressione')  # plot è un grafico a linee
plt.title('Grafico a dispersione con retta di regressione')
plt.xlabel('Asse x')
plt.ylabel('Asse y')
plt.legend('LEGENDA QUI')  
plt.grid(True)  # mostra la griglia
plt.gca().set_aspect('equal', adjustable='box')  # imposta l'aspetto del grafico

plt.show()
plt.savefig('grafico_a_dispersione_con_retta_di_regressione.png')  # salva il grafico in un file
plt.close()  # chiude il grafico




# ora creiamo un grafico a dispersione con una curva di regressione
# creiamo un array di valori casuali per y
y = (2 *x**2 + 1 + 0.5 * np.random.randn(len(x)))  # crea un array di valori casuali per y
# diamo un errore casuale di 0.5
# creiamo un array anche per la retta di regressione
y_fit = 2 * x**2 + 1  # crea un array di valori casuali per y

# creiamo un array anche per la retta di regressione

plt.figure(figsize=(10, 5))
plt.scatter(x, y, color='red', label='Dati x')  # scatter è un grafico a dispersione, mentre plot è un grafico a linee
plt.plot(x, y_fit, color='blue', label='Curva di regressione')  # plot è un grafico a linee
plt.title('Grafico a dispersione con curva di regressione')
plt.xlabel('Asse x')
plt.ylabel('Asse y')
plt.legend('LEGENDA QUI')
plt.grid(False)  # mostra la griglia

plt.gca().set_aspect('equal', adjustable='box')  # imposta l'aspetto del grafico


plt.show()
plt.savefig('grafico_a_dispersione_con_curva_di_regressione.png')  # salva il grafico in un file
plt.close()  # chiude il grafico



# creiamo un istogramma con i dati x
# creiamo un array di valori casuali per y
y = (2 *x + 1 + 0.5 * np.random.randn(len(x)))  # crea un array di valori casuali per y

plt.figure(figsize=(10, 5))
plt.hist(x, bins=10, color='red', label='Dati x', edgecolor = 'green')  # istogramma è un grafico a dispersione, mentre plot è un grafico a linee

plt.xlim(-10, 10)  # imposta i limiti dell'asse x
plt.ylim(0, 10)  # imposta i limiti dell'asse y

plt.title('Istogramma')
plt.xlabel('Asse x')
plt.ylabel('Asse y')
plt.legend('LEGENDA QUI')
plt.grid(True)  # mostra la griglia


plt.show()
plt.savefig('istogramma.png')  # salva il grafico in un file
plt.close()  # chiude il grafico




# ora creiamo un istogramma con i dati x e una curva di regressione
# creiamo un array di valori casuali per y
y = (2 *x + 1 + 0.5 * np.random.randn(len(x)))  # crea un array di valori casuali per y
# diamo un errore casuale di 0.5

# creiamo un array anche per la retta di regressione
y_fit = 2 * x + 1  # crea un array di valori casuali per y


plt.figure(figsize=(10, 5))
plt.hist(x, bins=10, color='red', label='Dati x', edgecolor = 'green')  # istogramma è un grafico a dispersione, mentre plot è un grafico a linee
plt.plot(x, y_fit, color='blue', label='Retta di regressione')  # plot è un grafico a linee
plt.title('Istogramma con retta di regressione')
plt.xlabel('Asse x')
plt.ylabel('Asse y')

plt.show()
plt.savefig('istogramma_con_retta_di_regressione.png')  # salva il grafico in un file
plt.close()  # chiude il grafico
