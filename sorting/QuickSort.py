def quicksort(arr,left,right):
    # enquanto o left for menor que o right o array nao chegou ao fim vai ser assim recursivamente
    if left < right:
        pi = pivation(arr,left,right)
        # pivo que vai ser a variavel de comparacao com outras
        quicksort(arr,left,pi-1)
        # o menos e + 1 serve pera ignora o valor pi
        quicksort(arr,pi+1,right)
def pivation(arr,left,right):
    i = left-1
    # i que comeca no -1 no inicio
    pivot = arr[right]
    # na teoria eu teria que pegar ou escolher um e colococar no final
    # mas aqui eu ja escolho o ultimo se quiser adicionar alguma logica e so fazer ela e 
    # colocar no ultimo elemento que vai funcionar
    for j in range(left,right):
        if arr[j] <= pivot:
            # aqui o j  emenor que pivot pivot inicial 5 e j 2
            # se isso acontecer o i+=1 e sobe
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    print(arr[i+1],arr[right])
    arr[i+1],arr[right] = arr[right],arr[i+1]
    # troca do i pelo ultimo ja que o pivot e o ultimo
    # 5 pelo 5 ja que o i vai aumentando ate achar o JA QUE O RIGHT E O I ESTAO NO MSM LUGAR

    
    return i+1
    # aqui eu rentorno o i que seria o numero de index do pivot
arr = [2, 1, 3, 4, 5]
quicksort(arr,0,len(arr)-1)

print(arr)

# RECOMENDO DEBUGAR O CODIGO DEPOIS RESCREVI VARIAS VEZES ATE CONSEGUIR ENTENDER 80%