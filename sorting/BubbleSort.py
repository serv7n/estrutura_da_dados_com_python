lista = [1,3,2,5,4]


ln,rn = 0,0
# variaveis que guardam os numeros de r e l

max = len(lista)

while max > 2:
    # enquanto o max for maior que 2 ja que so existem 2 ponteiros
    l,r = 0,1
    is_sorted = True
    while r < max:
        # r menor que maximo para evitar um array nulo
        if(lista[l] > lista[r]):
            is_sorted = False
            ln = lista[l]
            rn = lista[r]
            lista[l] = rn
            lista[r] = ln
        r+=1
        l+=1
    print(lista)
    if(is_sorted):
        break
    max -=1

# O ALGORITMOS FUNCIONA BEM O is_sorted verifica se todos estao na posicao certa ja que o lista verifica 
# cada posicao se nao tiver nenhuma maior e menor no lugar errado o algoritmo esta certo