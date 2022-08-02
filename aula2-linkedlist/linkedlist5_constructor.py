"""
Implementação de uma lista encadeada com 1 elemento, onde a cabeça e a cauda apontam pro único valor.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)  # Instanciação da classe Node
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):  # função simples para iterar sobre a lista e printar ela completamente
        temp = self.head  # atribuo a cabeça a um valor temporário para que eu possa iterar no início da lista
        while temp is not None:
            print(temp.value)
            temp = temp.next  # Quando next == None, sai do loop. Lembrnado que temp recebe head, e head tem acesso a 'value' e 'next'.


lista_encadeada = LinkedList(4)  # Instanciação da classe LinkedList
print(lista_encadeada.head.value)
