"""
Merge:
    Combina duas listas já ordenadas e retorna elas combinadas


Merge Sort:
    Recebe uma lista de tamanho n, divide ela ao meio recursivamente até ter n listas com 1 elemento apenas.
    Depois combina essas listas com a função Merge, e ao combinar, elas são ordenadas.
    O(n log n) TC, pois merge tem complexidade n, e merge_sort tem complexidade log n.
    O(n) SC, pois cria várias listas até ter n listas de 1 elemento.
"""


def merge(lista1, lista2):
    combinada = []

    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            combinada.append(lista1[i])
            i += 1
        else:
            combinada.append(lista2[j])
            j += 1

        
    while i < len(lista1):
        combinada.append(lista1[i])
        i += 1

    while j < len(lista2):
        combinada.append(lista2[j])
        j += 1

    return combinada


print(merge([1,2,7,8], [3,4,5,6]))


def merge_sort(lista):
    if len(lista) == 1:
        return lista

    mid = int(len(lista)/2)  # int() arredonda pra um inteiro e evita floats.
    left = lista[:mid]  # lista de index 0 até mid, sem incluir mid.
    right = lista[mid:] # lista de index mid até o último index.
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([3,1,4,2]))
