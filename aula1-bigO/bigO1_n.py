"""
Notação Big O

É o pior caso de um algoritmo.

O(n) -> notação principal
"""

def print_items(n):  # Algoritmo O(n)
    for i in range(n):
        print(i, end="")
    
print_items(10)

print("\n")

def print_items_duplo(n):  # Algoritmo O(2n)? Não. Se tratando de BigO, nós eliminamos qualquer constante.
    # Portanto, continuará sendo O(n). O gráfico é uma linha reta 45° constante subindo. Quando maior n, maior o número de operações 1:1.
    for i in range(n):
        print(i, end="")
    print()
    for j in range(n):
        print(j, end="")

print_items_duplo(10)
