array1=[1,4,3,9]
array2=[1,2,4,4]

"""
Consigna 1 adyacente
"""
def sumaEsIgual8Recursivo (array):
    if not array[1]:
        return False
    elif array[0]+array[1]==8:
        return True
    else:
        return sumaEsIgual8Recursivo(array[1,])


"""
Consigna 2 adyacente
"""
def sumaEsIgual8Iterativo(array):
    long= len(array) - 1
    for i in range (0,long,1):
        if array[i]+array[i+1]==8:
            return True
    return False  
      

"""
Consigna 1 total
"""     
def sumaEsIgual8(array):
    for i in range (len(array)-1):
        for j in range (i+1,len(array),1):
            if array[i]+array[j]==8:
                return True
    return False

"""
Consigna 2 total
""" 
def sumaEsIgual8(array):
    vistos = set()
    for num in array:
        if 8 - num in vistos:
            return True
        vistos.add(num)
    return False
