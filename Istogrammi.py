# ISTOGRAMMI

# basico con bins, usare bins personalizzati, color e edgecolor
#axvline


from matplotlib import pyplot as plt

plt.style.use('ggplot')


x = [13,18,18,22,25,27,29,29,30,35,36,37,40,41,45,45,54,56,65]
# quante categorie per età
# settiamo i bins = le scatole
# ce le divide automaticamente per fasce: da 10-20/20-30.....

# possiamo creare noi dei bins --> y in questo momento equivale alla somma degli elementi che rientrano in un range di età; x = il range di età
bins = [10,20,30,40,50,60,70]

#plt.hist(x, bins=6)
plt.hist(x,bins=bins, color='blue', edgecolor='black')

# potrebbe non piacerci il colore ed avere la necessità di usare un edge color per capire meglio la divisione

# possiamo inserire una linea verticale all'interno del nostro grafico; ad esempio per segnare l'etàmedia
plt.axvline(sum(x)/len(x), color='red', linewidth="3")




plt.title('nome del grafico')

plt.show()