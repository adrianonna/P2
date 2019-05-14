def BubbleSort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
                #print(lista)
    return lista


def InsertionSort(lista):
    for index in range(1, len(lista)):
        currentvalue = lista[index]
        position = index
        while position > 0 and lista[position - 1] > currentvalue:
            lista[position] = lista[position - 1]
            position = position - 1
        lista[position] = currentvalue
        #print(lista)
    return lista


def SelectionSort(lista):
    for i in range(len(lista) - 1):
        minIndx = i
        minVal= lista[i]
        j = i + 1
        while j < len(lista):
            if minVal > lista[j]:
                minIndx = j
                minVal= lista[j]
            j += 1
        temp = lista[i]
        lista[i] = lista[minIndx]
        lista[minIndx] = temp
        #print(lista)
    return lista


def ShellSort(lista):
    inc = len(lista) // 2
    while inc:
        for i, el in enumerate(lista):
            while i >= inc and lista[i - inc] > el:
                lista[i] = lista[i - inc]
                i -= inc
            lista[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
        #print("After increments of size", inc, "The list is", lista)
    return lista


def QuickSort(lista):
    if len(lista) <= 1: return lista
    m = lista[0]
    #print(lista)
    return  QuickSort([i for i in lista if i < m]) + \
            [i for i in lista if i == m] + \
            QuickSort([i for i in lista if i > m])


def MergeSort(lista):
    #print("Splitting ",lista)
    if len(lista)>1:
        mid = len(lista)//2
        lefthalf = lista[:mid]
        righthalf = lista[mid:]
        MergeSort(lefthalf)
        MergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lista[k]=lefthalf[i]
                i=i+1
            else:
                lista[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            lista[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            lista[k]=righthalf[j]
            j=j+1
            k=k+1
    return lista
    #print("Merging ",lista)


import time
def CalculaTempo(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista)
    fim = time.time()
    diferenca = fim - inicio
    print("O tempo de execução foi de {:.4f} segundos".format(diferenca))
    print('\n')
    return diferenca


'''def ss(l): #SelectionSort
    for i in range(0,len(l)):
        d=l.index(min(l[i:]))
        c=l[i]
        l[i]=min(l[i:])
        l[d]=c
        print(l)  #it prints each step of selection sort
y=[10,9,1,5,0,6]
ss(y)'''

#L = [120,11,0,10,3,120,3,4,5,6,7,8,9,10]
#print(SelectionSort(L))

#lista = [64, 88, 51, 65, 90, 51, 75, 34, 79, 46, 36]
#print(InsertionSort(lista))

#lista = [64, 88, 51, 65, 90, 51, 75, 34, 79, 46, 36]
#print(BubbleSort(lista))