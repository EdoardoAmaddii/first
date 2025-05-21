# dividere gli array

# array_split
# split sugli assi, vsplit, hsplit, dsplit


import numpy as np

arr = np.array([1,2,3,4,5,6])

arr2 = np.array_split(arr,2) # se fosse diviso 4 splitta l'ultimo in 2

arr2s = np.split(arr,3) # se fosse diviso 4 ci darebbe errore

print(arr2)

# accediamo agli array interni
print(arr2[0])



# array 2D

arr2D = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

arrspl = np.array_split(arr2D,3) # diviso 3 ci divide l'ultima coppia 

print(arrspl)

# split per assi

arrass1 = np.array_split(arr2D, 3, axis= 1)

print(arrass1)


print('\n\n')
# vsplit, hsplit, dplit

arrvh = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]) # 2D

arrv = np.vsplit(arrvh, 3) # come il normale split

print(arrv)

print('\n\n')
arrh = np.hsplit(arrvh, 3) # singolo elemento = split per axis = 1: prendendo il primo di ogni insieme, il secondo, il terzo

print(arrh)


print('\n\n')
# per dsplit dobbiamo avere un array di 3D

arrd = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])

arrdsplit = np.dsplit(arrd, 3)

print(arrdsplit)