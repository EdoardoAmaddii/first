### 
# INDICIZZAZIONE ARRAY

import numpy as np

#esempio con lista
lista = [1, 2, 3, 4, 5]
print(lista[4]) # Output: 5

# esempio con array numpy
array1d = np.array([1, 2, 3, 4, 5])
print(array1d[4]) # Output: 5


# esempio con array 2D
array2d = np.array([[1, 2, 3], [4, 5, 6]])

print(array2d[1, 2]) # Output: 6
print(array2d[0, 1]) # Output: 2

# prendiamo il 2, il 4 e il 5 insieme
print(array2d[0, 1], array2d[1, 0:2]) 

# esempio con array 3D
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array3d[1, 1, 0]) # Output: 10
print(array3d[0, 1, 2]) # Output: 6



## indicizzazione negativa

# esempio con array 1D
array1d = np.array([1, 2, 3, 4, 5])
print(array1d[-1]) # Output: 5
print(array1d[-2]) # Output: 4

# esempio con array 2D
array2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array2d[-1, -1]) # Output: 6
print(array2d[-2, -1]) # Output: 3
print(array2d[-1, -2]) # Output: 5

# esempio con array 3D
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d[-1, -1, -1]) # Output: 12
print(arr3d[-1, -1, -2]) # Output: 11
print(arr3d[-1, -2, -1]) # Output: 9
print(arr3d[-2, -1, -1]) # Output: 6
print(arr3d[-2, -1, -2]) # Output: 5
print(arr3d[-2, -2, -1]) # Output: 3
print(arr3d[-2, -2, -3]) # Output: 1



# esempio con array 4D
array4d = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], [[[13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24]]]])
print(array4d[-1, -1, -1, -1]) # Output: 24
print(array4d[-1, -1, -1, -2]) # Output: 23
print(array4d[-1, -1, -2, -1]) # Output: 21
print(array4d[-2, -2, -2, -2]) # Output: 2








################################################

# Slicing: selezionare un sottoinsieme di un array



# esempio con lista
lista = [1, 2, 3, 4, 5]
print(lista[1:4]) # Output: [2, 3, 4]
print(lista[:3]) # Output: [1, 2, 3]
print(lista[1:]) # Output: [2, 3, 4, 5]
print(lista[::2]) # Output: [1, 3, 5] # seleziona ogni secondo elemento
print(lista[::-1]) # Output: [5, 4, 3, 2, 1] # seleziona gli elementi in ordine inverso

# con slicing negativo
print(lista[0:-1]) # Output: 5 # seleziona l'ultimo elemento escluso
print(lista[:-4]) # Output: [1] # seleziona gli elementi fino al quarto da destra escluso
print(lista[-4:-1]) # Output: [2, 3, 4] # seleziona gli elementi dal quarto da destra fino al'ultimo escluso
print(lista[-4:]) # Output: [2, 3, 4, 5] # seleziona gli elementi dal quarto da destra fino all'ultimo incluso


# esempio con array numpy


# esempio con array 1D
array1d = np.array([1, 2, 3, 4, 5])
print(array1d[1:4]) # Output: [2 3 4]
print(array1d[:3]) # Output: [1 2 3]
print(array1d[1:]) # Output: [2 3 4 5]
print(array1d[::2]) # Output: [1 3 5] # seleziona ogni secondo elemento
print(array1d[::-1]) # Output: [5 4 3 2 1] # seleziona gli elementi in ordine inverso
print(array1d[0:-1]) # Output: [1 2 3 4] # seleziona gli elementi fino all'ultimo escluso
print(array1d[:-4]) # Output: [1] # seleziona gli elementi fino al quarto da destra escluso
print(array1d[-4:-1]) # Output: [2 3 4] # seleziona gli elementi dal quarto da destra fino al'ultimo escluso







# esempio con array 2D
array2d = np.array([[1, 2, 3], [4, 5, 6]])


# voglio l'array 1, i numeri 5 e 6
print(array2d[1, 1:]) # Output: [5 6]


# complichiamo un po' le cose

# il primo numero indica la riga, il secondo numero indica la colonna
               # il terzo numero indica il passo (step) da utilizzare per selezionare gli elementi
               # ad esempio, se vogliamo selezionare ogni secondo elemento, possiamo usare il passo 2

print(array2d[0:2, 1:3]) # Output: [[2 3] [5 6]]
print(array2d[0:2, :]) # Output: [[1 2 3] [4 5 6]]
print(array2d[:, 1:3]) # Output: [[2 3] [5 6]] # non da lo 0 perchè non abbiamo selezionato la prima colonna
print(array2d[0:1, 0:2]) # Output: [[1 2]] # perchè abbiamo selezionato solo la prima riga e le prime due colonne
print(array2d[0:1, :]) # Output: [[1 2 3]] # perchè abbiamo selezionato solo la prima riga e tutte le colonne
print(array2d[:, 0:2]) # Output: [[1 2] [4 5]] 
print(array2d[0:2, 0:1]) # Output: [[1] [4]] # perchè abbiamo selezionato solo la prima colonna
print(array2d[0:2, :]) # Output: [[1 2 3] [4 5 6]]







# esempio con array 3D
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# esempio baase

print(array3d[0, 0, 0]) # Output: 1
print(array3d[0, 0, 1]) # Output: 2

# voglio l'ultimo tris di array

print(array3d[1,1,0:]) # Output: 10,11,12



# il primo numero indica il blocco, il secondo numero indica la riga, il terzo numero indica la colonna
              # il quarto numero indica il passo (step) da utilizzare per selezionare gli elementi



print(array3d[0:2, 0:2, 0:2]) # Output: [[[1 2] [4 5]] [[7 8] [10 11]]]
print(array3d[0:2, 0:2, :]) # Output: [[[1 2 3] [4 5 6]] [[7 8 9] [10 11 12]]]
print(array3d[0:2, :, 0:2]) # Output: [[[1 2] [4 5]] [[7 8] [10 11]]]
print(array3d[:, 0:2, 0:2]) # Output: [[[1 2] [4 5]] [[7 8] [10 11]]]
print(array3d[:, :, 0:2]) # Output: [[[1 2] [4 5]] [[7 8] [10 11]]]
print(array3d[0:2, 0:2, :]) # Output: [[[1 2 3] [4 5 6]] [[7 8 9] [10 11 12]]]
print(array3d[0:2, :, 0:2]) # Output: [[[1 2] [4 5]] [[7 8] [10 11]]]
print(array3d[:, 0:2, :]) # Output: [[[1 2 3] [4 5 6]] [[7 8 9] [10 11 12]]]


print('\n\n')

# 
# N.B. 
#
# questo non va bene perchè dobbiamo avere lo stesso numero di dati: deve essere omogeneo
#
# array3dv = np.array([[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# vogliamo prendere solo i numeri pari nel primo array
#

array3dv = np.array([[[0, 1, 2, 3, 4, 5], [4, 5, 6, 7, 8, 9]], [[7, 8, 9, 10, 11, 12], [10, 11, 12, 13, 14, 15]]])


print(array3dv[0,0,::2])
