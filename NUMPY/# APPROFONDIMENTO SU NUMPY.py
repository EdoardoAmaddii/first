# APPROFONDIMENTO SU NUMPY



'''

liste = lente

numpy_array = very fast, less memory

'''




import numpy as np

a = np.array([1,2,3]) # 1 dim array

a2 = np.array([[1,2,3],[4,5,6]])

a3 = np.array([[[1,2],[3,4,]],[[5,6],[7,8]]])

print(f'a:{a}\n\n a2:{a2}\n\n a3:{a3}')

















###
# ACCESSING, CHANGING specific element


a = np.array([[1,2,3,4],[5,6,7,8]])

print(a[1,3]) #a(riga,colonna)

print(a[0,:]) # tutta la riga

print(a[:,1]) # tutta la colonna


#startindex, endindex,stepsize

print(a[0,1:-1:2])


# cambiamo elemento

a[1,3] = 20

print(a)


a[:,2] = 5

print(a)

a[:,2] = [10,34]

print(a)


# es 3D

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

# get specific element (work outside in)

print(b[0,1,1])








# inizializing different array


print(np.zeros((2,3), dtype='int32'))

print(np.ones((4,2,2)))


print(np.full((2,2),99))


print(np.full(a.shape, 4)) # tutti quattro con le dimensioni di un'array che abbiamo

print(np.full_like(a,4)) # stessa cosa di sopra


# random decimal numbers

print(np.random.rand(4,2))

print(np.random.random_sample(a.shape))


# random integer values

print(np.random.randint(-3,7, size=(3,3))) # primo numero opzionale, fino a 7


# identity matrix

print(np.identity(5))



# repeat array

arr = np.array([1,2,3])

r1 = np.repeat(arr,3)

print('\n\n')
print(r1)


arr2 = np.array([[1,2,3]])

r2 = np.repeat(arr2,3,axis=0)

print('\n')
print(r2)










print('\n\n')
# inizializing array problem


output = np.ones((5,5))

z = np.zeros((3,3))

#fill 0 con un 1 in mezzo

z[1,1] = 9

output[1:4,1:4] = z

print(output)





## be careful with copying

a = np.array([1,2,3])

b = a

b[0] = 100

print(b)

print(a) # cambia anche a !

# possiamo prevenire la cosa mettendo .copy

c = b.copy()

c[0] = 7

print(c)

print(b)








# mathematics

a = np.array([1,2,3,4])

print(a + 2)

b = np.array([1,0,1,0])

print(a*b)

print(np.sin(a))




##### LINEAR ALGEBRa

arr2 = np.full((3,2),2)

arr1 = np.ones((2,3))

# non possiamo fare direttamente l'operazione perchè abbiamo differenti sizes

print(np.matmul(arr2,arr1))





# statistics

np.min(arr1)

np.max(arr1, axis=0)


np.sum(arr1)



a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
b = np.max(a, axis=1).sum()


















# reorganizing arrays



before = np.array([[1,2,3,4],[5,6,7,8]])

after = before.reshape((4,2))

print(after)


# vertical and horizontal stacking : uniamo i due array   
v1 = np.array([1,2,3,4])

v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2]))

print(np.hstack((v1,v2)))




















###
# Load data from file
'''

filedata = np.genfromtxt('data.txt', delimiter=',')

print(filedata) # ci stampa un array con i valori che abbiamo nel file divisi da virgole



# boolean indexing

print(filedata > 50) #True or False

print(filedata[filedata > 50]) #i valori sopra 50
'''


# index with a list in Numpy

a = np.array([1,2,3,4,5,6,7,8,9])

print(a[[1,3,-1]])