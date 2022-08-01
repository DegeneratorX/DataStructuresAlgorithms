"""
O(n²) no gráfico é uma curva acentuada pra cima. Metade de uma parábola.
"""

def print_items(n):  # O(n²)
    for i in range(n):
        for j in range(n):
            print(i,j)  # 100 números printados

print_items(10)
