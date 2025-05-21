# matplotlib

from matplotlib import pyplot as plt

x  = [25,26,27,28,29,30]

y = [100,120,140,110,150,145]

y2 = [90,80,120,150,170,140]


# print(plt.style.available)
plt.style.use('ggplot') # ad esempio ggplot ha la griglia incorporata
# alcuni stili hanno la grid incorporata e per questo se la mettiamo noi viene eliminata


plt.plot(x,y, label = 'italiani', color = 'red', linewidth=3, linestyle='--', marker='o')    # 1a riga nel grafico
plt.plot(x,y2, label = 'francesi', color = '#212121', linewidth=1, linestyle='dotted', marker='x')   # 2a riga nel grafico

plt.title('Nome del grafico')
plt.xlabel('età')
plt.ylabel('valori')
# plt.legend(['italiani', 'francesi'])   # possiamo scriverlo qui, ma anche dentro i plot iniziali
plt.legend() # avendo inserito le label della legenda nelle plot

# plt.grid() # inserisci una griglia



plt.show()


# personalizzazione grafico
# figure  =  finestra

# titolo, etichette, seconda linea, legenda
# griglia, colore, dimensione, stile linea, marcatori e stile grafico







