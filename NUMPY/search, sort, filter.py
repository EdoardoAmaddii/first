# search, sort, filter

import numpy as np

arr = np.array([1,2,3,4,5,4,4,6,7,8,9])


# vediamo gli indici della nostra ricerca con WHERE
# troviamo il 4

arrindici = np.where(arr == 4)

print(arrindici)  

# troviamo i pari

arrpari = np.where(arr%2 == 0)

print('\n', arrpari)




# SORT

# ci ritorna un nuovo array

arrdasortare = np.array([6,8,7,5,2,3,1,9,4])

arrordinato = np.sort(arrdasortare)

print('\n', arrordinato)


# possiamo frlo anche con le stringhe


arrdasortare = np.array(['Edoardo', 'Anna', 'Marco', 'Luca'])

arrordinato = np.sort(arrdasortare)

print('\n', arrordinato)


# ordiniamo un array 2D

arr2D = np.array([[3,7,2],[4,9,1]])

ordinato = np.sort(arr2D)

print('\n', ordinato)






##
# filtrare con un esempio statico, dinamico, scorciatoia

# STATICO perchè il codice lo scriviamo direttamente noi

array = np.array([1,2,3,4]) 

filtropari = [False, True, False, True]  # fosse un filtro per i pari avremmo FALSE; TRUE; FALSE; TRUE

arrayfiltrato = array[filtropari]

print('\n', arrayfiltrato)




##
# DINAMICO


array = np.array([1,2,3,4]) 

filtro = []

# vogliamo prendere un array di elementi pari

for x in array:
    if x%2 == 0:
        filtro.append(True)
    
    else:
        filtro.append(False)


arrayfiltrato = array[filtro]

print('\n', arrayfiltrato)




# scorciatoia

filtroscorc = array%2 == 0

arrayfiltroscor = array[filtroscorc]

print(arrayfiltroscor)








###########################