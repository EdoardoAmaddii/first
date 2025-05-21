# RANDOM # evita di chiamare i file con lo stesso nome dei moduli/librerie perchè si potrebbe creare una ricorsione infinita

import numpy as np

# randint e rand

from numpy import random

numero = random.randint(100) # intero compreso tra 0 e 100

print(numero)

num = random.rand() # numero compreso tra 0 e 1

print(num)



# creiamo allora degli array 1D e 2D

# randint [dobbiamo specificare l'intero massimo]

#  1D
arr = random.randint(100, size=(5))

print(arr)


#  2D - 3D
arr2D = random.randint(100, size=(3, 5, 4))

print(arr2D)


# rand --> non dobbiamo specificare il nostro campione e inserire direttamete il size degli array

arrrand = random.rand(3,5)

print('\n', arrrand)





# usiamo CHOICE su un array 

# ci prenderà un numero casuale nel nostro array

arr = np.array([1,2,3,4,5])

print('\n', random.choice(arr))


# possiamo creare con CHOICE un nuovo array decidendo la size, usando sempre gli stessi numeri presenti nell'array campione che stiamo utilizzando

arrchoice = random.choice(arr, size=(3,4))

print('\n', arrchoice)





##########################

# data distribution con probabilità
# N.B. dobbiamo avere il 100%

values = np.array([1,2,3,4,5])

probability = np.array([0.1, 0.2, 0.4, 0.1, 0.2]) # specifichiamo per ogni valore una certa probabilità di inserimento

# l'1 avrà il 10% di essere inserito, il 2 il 20%, il 3 il 40% .......

# usiamo sempre choice, ma inseriamo la probabilità (((  p = [0.1, 0.3......]  ))) 
# potevamo scrivere anche direttamente nel nostro array choice la probabilità
arrChoice = random.choice(arr, p=probability, size = (4, 7))

print('\n', arrChoice)







##############################

# shuffle (agisce sull'array) - permutation (ritorna un nuovo array)

values = np.array([1,2,3,4,5])

random.shuffle(values)

print('\n', values)


# dobbiamo assegnarlo ad un nuovo array
newarr = random.permutation(values)

print(newarr)
