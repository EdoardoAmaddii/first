# ITERARE ARRAY

import numpy as np



arr = np.array([1,2,3,4,5,6])

for x in arr:
    print(x)
    



print('\n\n\n')


arr2D = np.array([[1,2,3],[4,5,6]])

for x in arr2D:
    for y in x:
        print(y)



print('\n\n\n')




arr3D = np.array([ [[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]] ])


for x in arr3D:
    for y in x:
        print(y)  # l'y adesso sono gli array non gli elementi all'interno


print('\n\n')


for x in arr3D:
    for y in x:
        for z in y:
            print(z)


print('\n\n')

# per fare tutto in una volta sola, senza la necessità di fare sottoiterazioni

# usiamo:   NDITER

for x in np.nditer(arr3D):
    print(x)


print('\n\n')
# ci permette anche di cambiare dati in corsa

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)




print('\n\n')
#### 
# ITERIAMO PER STEP       --     usiamo lo slicing
####


arr2 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# sulla 1D vogliamo tutti gli array, sulla seconda li vogliamo tutti, ma per salti di 2
for x in np.nditer(arr2[:,::2]):
    print(x)



# voglio trovare l'indice degli elementi che sto prendondo
## NDENUMERATE

for index in np.ndenumerate(arr2):
    print(index)



# combiniamo le cose

for ind, x in np.ndenumerate(arr2):
    print(ind, x)





print('\n\n')

############################################################################################

### uniamo gli array

# concatenate
# stack


# unire array 1D

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

arrayfinale = np.concatenate((array1,array2))

print(arrayfinale)

print('\n\n')



# unire array 2D

array12D = np.array([[1,2,3],[7,8,9]])
array22D = np.array([[4,5,6],[10,11,12]])


arrayfinale2D = np.concatenate((array12D,array22D))

print(arrayfinale2D)

print('\n\n')

arrayfinalesuasse1 = np.concatenate((array12D,array22D), axis = 1) # prendi il primo rispetto alle dimensioni e poi il secondo

print(arrayfinalesuasse1)









print('\n\n\n')

# stack, h(orizzontale)stack, v(verticale)stack, d(dev)stack



arra1 = np.array([1,2,3])
arra2 = np.array([4,5,6])

arrconc = np.concatenate((arra1,arra2), axis = 0)

arrstack = np.stack((arra1,arra2), axis = 0)
arrstackax1 = np.stack((arra1,arra2), axis = 1) # prenderà il primo elemento dai due assi, il secondo, il terzo...

print(arrconc) # ad 1D
print('\n\n')
print(arrstack) # a 2D
print('\n\n')
print(arrstackax1) # 2D con 2 elementi in 3 insiemi

print('\n\n')

# facciamo con hstack e otteniamo la stessa cosa di concatenate

arrstackorizz = np.hstack((arra1,arra2))
print(arrstackorizz)


print('\n\n')            
# con vstack fa la stessa cosa di stack su axis=0

arrstackvert = np.vstack((arra1,arra2))
print(arrstackvert)


print('\n\n')
# con dstack fa la stessa cosa di stack su axis = 1 ma in 3D

arrstackdev = np.dstack((arra1,arra2))
print(arrstackdev)

                        