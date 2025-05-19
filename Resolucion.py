array1=[1,4,3,9]
array2=[1,2,4,4]

"""
Consigna 1
"""
def sumaEsIgual8Recursivo (array):
    if not array[1]:
        return False
    elif array[0]+array[1]==8:
        return True
    else:
        return sumaEsIgual8Recursivo(array[1,])


"""
Consigna 2
"""
def sumaEsIgual8Iterativo(array):
    long= len(array) - 1
    for i in range (0,long,1):
        if array[i]+array[i+1]==8:
            return True
    return False  
      

print(sumaEsIgual8Recursivo(array1))
print(sumaEsIgual8Recursivo(array2)) 
print(sumaEsIgual8Iterativo(array1))
print(sumaEsIgual8Iterativo(array2))      