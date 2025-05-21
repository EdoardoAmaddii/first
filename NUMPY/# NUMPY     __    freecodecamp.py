# NUMPY      # usato principalmente per processi numerici

import numpy as np

a = np.array(5)

print(a + 20)


#slicing

b = np.array([5,7,9,11,20])

print(b[:3])


# indexing

i = np.array([5,7,9,11,20])

print(i[0],i[3],i[-1])


####
# array types

print(a.dtype)



print('\n\n')
######
# multidimensional array
#2D

A = np.array([
    [1,2,3],
    [4,5,6]
])

print(A,A.shape,A.ndim,A.size)

print('\n')

print(A[1,0])            # ci stampa in entrambi i casi 4
print(A[1][0])


print('\n\n')

#3D

B = np.array([
    [
        [12,13,14],
        [4,5,6]
    ],
    [
        [3,2,1],
        [9,7,0]
    ]
])

print(B,B.shape,B.ndim,B.size)


## N.B. : dobbiamo avere lo stesso numero di array per dimensione

## vediamo come il print cambia a seconda delle dimensioni
# 
print('\n\n')
print(B[1])   # seconda matrice

print(B[1][0]) # prima lista della seconda matrice








print('\n\n')

########
# broadcasting and vectorized operations

# svolgiamo operazioni direttamente sugli array

x = np.arange(4)

print(x)
print(x+20) # operazione applicata su tutti gli elementi degli array

# si può anche scrivere così modificando l'array iniziale

x+=100
print(x)


## usiamo anche una list comprehension

l = [x*10 for i in x]

print(l)  # ci stampa 4 array da (1000,1010,1020,1030) perchè ci sono quattro elementi nell'array e su ognuno va fatta un operazione



print('\n\n')

## operazioni tra array

print(x+l)   # somma gli elementi in ordine











######
print('\n\n')


# BOOLEAN ARRAYS



array = np.arange(4)

print(array[[0,-1]])     # stessa stampa, qui una lista
print(array[0],array[-1])    # qui i singoli valori


print(array[[True,False,False,True]]) # stessa stampa del primo


# possiamo pensarla anche con operatori booleani
print(array>=2)
# ci ridarà False, False, True, True


# messo così invece ci ridarà gli elementi che gli richiediamo definendoli True o False
print(array[array>=2])

print(array.mean())

# stampiamo tutti gli elementi sopra la media

print(array[array>array.mean()])

# tutti gli elementi che non sono sopra la media

print(array[~(array>array.mean())])

# usiamo operatori booleani or e and

print(array[(array==0) | (array==1)])

print(array[(array<=2) & (array%2==0)])





print('\n\n')



## usiamo operatori per costruire array con random e randint

rand = np.random.randint(100, size=(3,3))

print(rand)

print('\n\n')

### ci stamperà solo i 5 valori True dentro un unico array
print(rand[np.array([
    [True, False, True],
    [False, True, False],
    [True, False, True]
])  
           ])

# vediamo con gli operatori booleani

print(rand>30)

print(rand[rand>30])





