# SCATTER CHART


from matplotlib import pyplot as plt


plt.style.use('classic')

x = [1,5,6,8,3,2,2,7,9,1]

y = [8,8,4,6,2,7,1,3,1,7]

color = [2,4,6,6,1,9,4,6,2,8]

sizes = [200,250,120,500,430,567,312,435,211,320]


# customizziamolo

# s= dimensione punti: da 0 a infinito, ma fai 1000 come max, altrimenti si sovrappongono tutti
# c= colore punti
# marker = segno 'x' ad esempio... il punto di default
# edgecolor = colore contorno
# linewidth = grandezza del contorno da 0 a 100, ma già con 5 è molto evidente
# alpha = opacità del segno da 0 a 1

#####################################
# PRIMO CODICE DA USARE

# plt.scatter(x,y, s=200, c='green', edgecolor='purple', linewidth=5, alpha=0.5)

#####################################


##### il grafico a dispersione ci da informazioni anche con l'intensità del colore e la grandezza del punto

# definiamo sotto x e y color da 1 a 9 per definire l'intensità
# c=colors ---> definiamo vari colori
# cmapp   ---> prendiamo un colore per tutti i punti e ne definiamo invece l'intensità

plt.scatter(x,y,s=sizes, c = color, cmap='Greens')

# creiamo una label che indica l'intensità

cbar= plt.colorbar()
cbar.set_label('Intensità')

# anche la dimensione del punto è un altro dato, mettiamo sotto x, y, color, sizes
# modifichiamo la nostra s e mettiamo s=sizes

plt.title('Nome del grafico')

plt.show()