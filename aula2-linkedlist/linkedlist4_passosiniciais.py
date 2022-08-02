"""
Antes de criar uma nova lista, precisamos verificar o que mais se repete no código.

É nítido que a criação de um Node é o que mais se repete em todos os métodos.
Portanto, precisamos eliminar essa repetição criando um class Node.
"""

class LinkedList:
    def __init__(self, value):  # Cria um novo Node
        pass

    def append(self, value):  # Cria um novo Node e coloca no final (da lista)
        pass

    def prepend(self, value):  # Cria um novo Node e coloca no começo
        pass

    def insert(self, index, value):  # Cria um novo Node e insere o Node no índice onde você quer
        pass

# Eliminaremos essa criação de nodes repetitivas no próximo arquivo.
