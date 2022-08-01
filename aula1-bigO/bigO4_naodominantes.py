def print_items(n):  # O(n²)
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):  # O(n)
        print(k)


# O(n²) + O(n) -> O(n² + n)
# Porém, se temos um valor beeem mais alto, n² simplesmente engole n em número de operações.
# Portanto, nós eliminamos 'n', e no final, o algoritmo tem complexidade de tempo O(n²).

print_items(10)  # Total: 110 números
