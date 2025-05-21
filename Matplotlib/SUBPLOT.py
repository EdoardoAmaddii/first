# subplot   : possibilità di creare più grafici su una finestra o più finestre
# con 1 grafico
# 2 e più grafici
# 2 e più finestre


from matplotlib import pyplot as plt

plt.style.use('ggplot')


# introdurre il concetto di FIGURE = finestra e AXIS = grafico

# inserisco nrows=*,ncols=* per creare più grafici: righe di grafici e colonne di grafici

# spacchettiamo ax  --> (ax1,ax2)


#              fig1, (ax1, ax2) = plt.subplots(nrows=2,ncols=1,sharex=True)

# ci da noia il fatto che siano segnati i tick per entrambi i grafici mettiamo sharex=True



###########
# ora vogliamo creare più finestre: ci basta copiare il nostro subplot, ma dobbiamo cancellare i due ax dal codice, rimanendo solo con uno per figura
fig1, (ax1a, ax1b) = plt.subplots(nrows=2, ncols=1)

fig2, ax2 = plt.subplots()



x = [1,2,3,4,5]

y= [3,6,7,2,5]


# invece che plt.plot(), mettiamo ax.plot()
ax1a.plot(x,y)
ax2.plot(x,y)

#### abbiamo creato un oggetto a partire da plt... in questo senso ax corrisponde al grafico e utilizziamo lui al posto di plt


# # una volta che usiamo i subplot non è più 
#        plt.title('nome del grafico')      per inserire il titolo, ma

ax1a.set_title('nome del grafico')
######            ax2.set_title('nome del grafico')
# una volta che usiamo i subplot non è più 
#      plt.xlabel('prova')     per inserire etichetta sotto asse x, ma

####              ax1.set_xlabel('Prova')
ax2.set_xlabel('Prova')

## non ci servono tutte le etichette che si sovrappongono, teniamo solo il nome in cima e l'etichetta della x in fondo

plt.show()
