"""
Implementação completa da lista encadeada simples, com todos os métodos possíveis de modificação da lista.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next;


    def append(self, value):  # Recebe o valor para adicionar
        new_node = Node(value)  # Instancio para trabalhar como um nó inicial e isolado
        if self.length == 0:  # Verifico se a lista está vazia
            self.head = new_node  # Se estiver vazia, insiro o nó na lista. Digo que a cabeça e a cauda da lista é o valor inserido, pois só terá ele, já que previamente estava vazia.
            self.tail = new_node
        else:  # Se tiver pelo menos com 1 elemento...
            self.tail.next = new_node  # ...mexe apenas na cauda (último elemento). O próximo do atual último elemento deve apontar pro novo elemento inserido
            self.tail = new_node  # E o elemento inserido deve ser a nova cauda. Ou seja, ser considerado o último elemento da lista.
        self.length += 1  # Tamanho da lista aumenta
        return True  # Retorna True para ser usado em outro momento por outro método.


    def pop(self):
        pass # TODO


    def prepend(self):
        pass # TODO


    def pop_first(self):
        pass # TODO


    def get(self):
        pass # TODO


    def set(self):
        pass # TODO


    def insert(self):
        pass # TODO


    def remove(self):
        pass # TODO


    def reverse(self):
        pass # TODO

lista_encadeada = LinkedList(4)

lista_encadeada.append(5)
lista_encadeada.print_list()

lista_encadeada.append(10)
lista_encadeada.append(12)
lista_encadeada.append(23)

print()
print(lista_encadeada.head.next.next.next.value)
