'''
NUMPY

numpy è una libreria fondamentale per il calcolo scientifico in Python.
Essa fornisce supporto per array multidimensionali e funzioni matematiche ad alte prestazioni.

Essa è una libreria open source e può essere installata tramite pip:
pip install numpy

---
gli Array sono simili a liste, ma sono più efficienti in termini di memoria e velocità.
Gli array numpy sono omogenei, ovvero contengono solo un tipo di dato.
Gli array numpy sono più veloci delle liste Python, poiché sono implementati in C e ottimizzati per le operazioni matematiche.

'''



import numpy as np

# Creazione di un array numpy a partire da una lista Python
a = np.array([1, 2, 3, 4, 5])
print(a)  # Output: [1 2 3 4 5]

# Creazione di un array numpy a partire da una tupla Python
b = np.array((1, 2, 3, 4, 5))
print(b) # Output: [1 2 3 4 5]

# Creazione di un array numpy a partire da una lista di liste Python
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)  # Output: [[1 2 3] [4 5 6]]

# Creazione di un array numpy a partire da una tupla di tuple Python
d = np.array(((1, 2, 3), (4, 5, 6)))
print(d)  # Output: [[1 2 3] [4 5 6]]


# differenza liste e array numpy

lista = [1, 2, 3, 4, 5]
print(lista*5) # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(lista+5) # Output: TypeError: can only concatenate list (not "int") to list

# con gli array numpy, l'operatore * esegue la moltiplicazione elemento per elemento
print(a*5) # Output: [ 5 10 15 20 25]
print(a+5) # Output: [ 6  7  8  9 10]




#####

# creare array 0D, 1D, 2D, 3D

# 0D: array scalare (un singolo valore)
a0 = np.array(42)
print(a0)  # Output: 42

#1D: array unidimensionale (vettore)
array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d)  # Output: [1 2 3 4 5]


#2D: array bidimensionale (matrice)
array_2d = np.array([[1, 2, 3], 
                     [4, 5, 6]])
print(array_2d)  # Output: [[1 2 3] [4 5 6]]


#3D: array tridimensionale (tensor)
array_3d = np.array([[[1, 2, 3], 
                       [4, 5, 6]],
                      [[7, 8, 9], 
                       [10, 11, 12]]])
print(array_3d)  # Output: [[[ 1  2  3] [ 4  5  6]] [[ 7  8  9] [10 11 12]]]


# ndim: vediamo il numero di dimensioni dell'array

print("Numero di dimensioni dell'array 0D:", a0.ndim)  # Output: 0

print("Numero di dimensioni dell'array 1D:", array_1d.ndim)  # Output: 1

print("Numero di dimensioni dell'array 2D:", array_2d.ndim)  # Output: 2

print("Numero di dimensioni dell'array 3D:", array_3d.ndim)  # Output: 3


## vediamo come generare velocemente un'array di più dimesioni
## ndmin=5

array_5d = np.array([1,2,3], ndmin=5)
print(array_5d)  # Output: [[[[[1 2 3]]]]]
print("Numero di dimensioni dell'array 5D:", array_5d.ndim)  # Output: 5





# usiamo arange, zeros e ones per creare array di più dimensioni

# arange: crea un array con valori in un intervallo specificato
# zeros: crea un array di zeri
# ones: crea un array di uni


####
arrArange = np.arange(10)  # crea un array con valori da 0 a 9
print("Array creato con arange:", arrArange)  # Output: [0 1 2 3 4 5 6 7 8 9]

arrArange = np.arange(5, 50, 5)  # crea un array con valori da 5 a 50 con passo 5
print("Array creato con arange:", arrArange)  # Output: [ 5 10 15 20 25 30 35 40 45]

####
arrZeros = np.zeros(3)  # crea un array di zeri con 3 elementi
print("Array creato con zeros:", arrZeros)  # Output: [0. 0. 0.]

arrZeros2D = np.zeros((2, 3))  # crea un array di zeri con 2 righe e 3 colonne: 2 arrays di 3 elementi
print("Array 2D creato con zeros:", arrZeros2D)  # Output: [[0. 0. 0.] [0. 0. 0.]]

arrZeros3D = np.zeros((2, 3, 4))  # crea un array di zeri con 2 matrici di 3 righe e 4 colonne
print("Array 3D creato con zeros:", arrZeros3D)  # Output: [[[0. 0. 0. 0.] [0. 0. 0. 0.] [0. 0. 0. 0.]] [[0. 0. 0. 0.] [0. 0. 0. 0.] [0. 0. 0. 0.]]]



####
arrOnes = np.ones(3)  # crea un array di uni con 3 elementi
print("Array creato con ones:", arrOnes)  # Output: [1. 1. 1.]

arrOnes2D = np.ones((2, 3))  # crea un array di uni con 2 righe e 3 colonne: 2 arrays di 3 elementi
print("Array 2D creato con ones:", arrOnes2D)  # Output: [[1. 1. 1.] [1. 1. 1.]]

arrOnes3D = np.ones((2, 3, 4))  # crea un array di uni con 2 matrici di 3 righe e 4 colonne 
print("Array 3D creato con ones:", arrOnes3D)  # Output: [[[1. 1. 1. 1.] [1. 1. 1. 1.] [1. 1. 1. 1.]] [[1. 1. 1. 1.] [1. 1. 1. 1.] [1. 1. 1. 1.]]]




# Creazione di un array con valori casuali
arrRandom = np.random.rand(3)  # crea un array di 3 valori casuali tra 0 e 1
print("Array creato con valori casuali:", arrRandom)  # Output: [0.12345678 0.23456789 0.3456789]

# valori casuali tra 0 e 10
arrRandom = np.random.randint(0, 10, size=5)  # crea un array di 5 valori casuali tra 0 e 10
print("Array creato con valori casuali tra 0 e 10:", arrRandom)  # Output: [3 7 1 9 4]


# valori casuali tra 0 e 10, 2 righe e 3 colonne
arrRandom2D = np.random.randint(0, 10, size=(2, 3))  # crea un array di 2 righe e 3 colonne con valori casuali tra 0 e 10
print("Array 2D creato con valori casuali tra 0 e 10:", arrRandom2D)  # Output: [[3 7 1] [9 4 6]]


# valori casuali tra 0 e 10, 2 matrici di 3 righe e 4 colonne
arrRandom3D = np.random.randint(0, 10, size=(2, 3, 4))  # crea un array di 2 matrici di 3 righe e 4 colonne con valori casuali tra 0 e 10
print("Array 3D creato con valori casuali tra 0 e 10:", arrRandom3D)  # Output: [[[3 7 1 9] [4 6 2 8] [5 0 3 1]] [[7 8 9 0] [1 2 3 4] [5 6 7 8]]]













