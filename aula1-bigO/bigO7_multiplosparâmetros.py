"""
Quando se tem múltiplos parãmetros, não se usa mais O(n).
"""

def print_items(a, b): # Na verdade agora é O(a+b)
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

##############################

def print_items_quadrado(a, b): # Aqui vira O(a*b)
    for i in range(a):
        for j in range(b):
            print(i, j)
