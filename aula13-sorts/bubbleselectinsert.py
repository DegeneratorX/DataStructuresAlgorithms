"""
Bubble Sort:
    Começa pelo primeiro da lista e compara com o segundo
    Se o primeiro for maior, troca com o segundo
    E assim sucessivamente...
    O(n²) no pior ou melhor caso


Selection Sort:
    Guarda o indice com o menor valor da lista e compara com o resto da lista.
    O(n²) no pior ou melhor caso

Insertion Sort:
    Começa pelo segundo e compara com o primeiro da lista.
    O(n²) no pior caso, O(n) no melhor caso (quando está praticamente ou totalmente ordenado)

Complexidade de Espaço O(1), pois não cria cópias de listas adicionais.
"""


def bubble_sort(lista):
    for i in range(len(lista) - 1, 0, -1):  # Tamanho 5, vai até 0, decrementa -1
        print(lista)
        for j in range(i):  # Após sair do loop, o próximo i será decrementado. Isso pq o maior valor da lista já foi colocado no final.
            #                 Então só restaria ordenar os primeiros.
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista

print(bubble_sort([4,2,6,5,1,3]))

##########################################
print()
print("#"*20)
print()


def selection_sort(lista):
    for i in range(len(lista)-1):
        min_index = i
        print(lista, f"<- guardo o indice {i} e dai pra frente comparo com o resto da lista até achar o menor valor. Quando achar, troca entre eles. Se não achar, se mantém.")
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        
        if i != min_index:
            temp = lista[i]
            lista[i] = lista[min_index]
            lista[min_index] = temp
    return lista

print(selection_sort([4,2,6,5,1,3]))


##########################################
print()
print("#"*20)
print()


def insertion_sort(lista):
    for i in range(1, len(lista)):
        temp = lista[i]
        j = i-1
        while temp < lista[j] and j > -1:
            lista[j+1] = lista[j]
            lista[j] = temp
            j -= 1
    return lista

print(insertion_sort([4,2,6,5,1,3]))
