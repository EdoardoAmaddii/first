# tipi di dati in numpy

#i - integer
#b - boolean
#u - unsigned integer
#f - float
#c - complex float
#m - timedelta
#M - datetime
#O - object
#S - string
#U - unicode string
#V - fixed chunk of memory for other type ( void )




import numpy as np

# controllare il tipo di dato

arr = np.array([True, False])

print(arr.dtype)



# come creare un array di un determinato tipo di dato

array = np.array([1,2,3,4,5], dtype='S')

print(array)

arra = np.array(['1','2','3'], dtype='i')

print(arra)

# convertire un array

arraydaconvertire = np.array([1,2,3,4])

arraystr = arraydaconvertire.astype('S')
print(arraystr)






print('\n\n\n')




####################

## VIEW E COPY ##

# copy fa una copia effettiva dei dati 

# view è la vista sul foglio del proprietario


arr = np.array([1,2,3,4])

arraycopy = arr.copy()

arrayview = arr.view()

# mettiamo di modificare il primo dato una volta creata la copia, non succede nulla alla copia, ma cambia il primo array

arr[0] = 10

print(arr)

print(arraycopy)

print(arrayview)


## vediamo se è la base e quindi ne abbiamo una copia oppure non siamo proprietari della base e dunque vediamo la base

print(arr.base) # NONE

print(arraycopy.base) # NONE

print(arrayview.base)





print('\n\n\n')





#############################

# SHAPE E RESHAPE

# vediamo la forma del nostro array


arr = np.array([1,2,3,4,5])

print(arr.shape) # (5,) il primo gli elementi dell'array, il secondo la dimensione, in questo caso è vuoto perchè ad una dimensione


arr2 = np.array([[1,2,3],[4,5,6]])

print(arr2.shape) # (2,3) il primo elemento la dimensione: 2 , il secondo gli elementi contenuti: 3


# cambiamo la forma al nostro array

print(arr2.reshape(-1)) # [1 2 3 4 5 6]  

# questa è una view, non il proprietario dei dati
# se infatti scrivo base, mi ritorna l'array originale

print(arr2.reshape(-1).base) # [[1 2 3] [4 5 6]]



# cambiamo la forma di un array ad una dimensione in uno da più

arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# trasformiamolo in un array a 2 dimensioni composto da 3 elementi per 4 insiemi e 4 elementi per 3 insiemi

print(arr1.reshape(4,3))

print(arr1.reshape(3,4))



#####
# non possiamo sempre fare reshape perchè dobbiamo utilizzare combinazioni che abbiano come risultato la lunghezza dell'array effettivo
#####


# passiamo da 1D a 3D

print(arr1.reshape(2,3,2))


##
# array con dimensioni sconosciute utilizziamo -1, ovunque vogliamo, così numpy lo crea dassolo

print(arr1.reshape(2,2,-1))


# posso specificare solo una dimensione sconosciuta
print(arr1.reshape(3,2,-1))



print('\n\n\n')

# spianare l'array = FLATTENING

# passare da un array di 2D o + ad uno di 1D

arr3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) # array da 3D

forma = arr3D.shape

print(forma)

formameno1 = arr3D.reshape(-1)
print(formameno1)

flatten = arr3D.flatten()

print(flatten)
print(flatten.shape)




