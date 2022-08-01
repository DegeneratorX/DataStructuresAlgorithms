"""
Mesmo que sejam 1000 valores, se tratando de complexidade do tempo,
assumimos que continuará O(n²). O(n³) não é considerado.
"""

def print_items(n):  # O(n²)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)  # 1000 números printados

print_items(10)
