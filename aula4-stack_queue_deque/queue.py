"""
Filas são exatamente listas encadeadas simples, só que para remoção ou adição, existem algumas diferenças.

O primeiro elemento que entrar é o primeiro a sair.
O primeiro elemento que entrar é o primeiro a sair.

FIFO (First in, First out)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value, size=1):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.size = size
        self.length = 1

    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def isfull(self):  # Procuro saber se a fila está cheia
        if self.length == self.size:  # Se a quantidade de elementos (largura) é igual ao tamanho da fila, então retorna True.
            return True
        return False

    def isempty(self):  # Opcional: se a instância assim desejar, pode querer saber se a fila está vazia no momento que chamar.
        if self.length == 0:
            return True
        return False

    
    def enqueue(self, value):  # Idêntico ao append da lista encadeada simples
        if self.isfull():
            return False

        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return True

    def dequeue(self):  # Idêntico ao pop_first da lista encadeada simples.
        if self.isempty():
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1
        return temp




# ABAIXO SÃO APENAS TEST PURPOSE.

fila = Queue(4,10)

fila.enqueue(2)
fila.dequeue()

fila.print_queue()
