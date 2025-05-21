# UFUNC

import numpy as np

# funzioni che agiscono sugli nd.array
# ci permettono di fare operazioni di vario genere

# add
# subtract
# multiply
# divide
# power
# mod  /  reminder     == stessa funzione : abbiamo il resto
# trunc / fix / around / ceil / floor == arrotonda i float




## non tutte le funzioni sono ufunc (es. concatenate non lo è)


# definiamo una funzione che aggiunge 5 ogni volta

def addCinque(x):
    return x + 5


# creiamo un array
arr = np.array([1,2,3,4,5,6])


# registriamo la funzione 
addCinque = np.frompyfunc(addCinque, 1, 1) # primo 1 = quanti elementi in input, secondo 1 = quanti elementi abbiamo in output



# invoke nel print
print(addCinque(arr))



print('\n\n')
#######
# vediamo alcune ufunc

arr1 = np.array([10,20,30,40,50])

arr2 = np.array([5,10,15,20,25])

newarr = np.subtract(arr1, arr2)

print(newarr)




# notiamo che potrei avere semplici liste e con le ufunc diventerebbero array di numpy

arr1 = [10,20,30,40,50]

arr2 = [5,10,15,20,25]

newarr = np.add(arr1, arr2) # ce li va a concatenare con add

newarrsub = np.subtract(arr1, arr2)

print(newarr)

print('\n\n')

print(newarrsub) # sottrazione tra i due / moltiplicazione = tra i due / power =