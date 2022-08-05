"""
Lista Duplamente Encadeada

{
"value": 7,
"next": None,
"prev": None
}
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    def append(self, value):
        new_node = Node(value)  # Criação do nó
        if self.length == 0:  # se lista vazia
            self.tail = new_node  # Cabeça e cauda é o valor inserido
            self.head = new_node
        else:  # Se tem pelo menos 1 elemento
            self.tail.next = new_node  # Próximo da cauda atual vira o novo nó inserido
            new_node.prev = self.tail  # Anterior do nó inserido aponta pra cauda atual
            self.tail = new_node  # A nova cauda agora passa a ser o novo nó inserido
        self.length += 1
        return True


    def pop(self):
        if self.length == 0:
            return None

        tail_guardado = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return tail_guardado
        
        self.tail = self.tail.prev
        self.tail.next = None
        tail_guardado.prev = None
        self.length -= 1
        return tail_guardado


    def prepend(self, value):  # OBS: Por ser duplamente encadeada, praticamente é a mesma coisa do append, só que espelhado.
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.prev = new_node  # Anterior da cabeça atual vira o novo nó inserido
            new_node.next = self.head  # Próximo do nó inserido aponta pra cabeça atual
            self.head = new_node  # A nova cabeça agora passa a ser o novo nó inserido
        self.length += 1
        return True


    def pop_first(self):  # OBS: Por ser duplamente encadeada, praticamente é a mesma coisa do pop, só que espelhado.
        if self.length == 0:
            return None

        head_guardado = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return head_guardado
        
        self.head = self.head.next  # A nova cabeça passa a ser o próximo da cabeça
        self.head.prev = None  # O anterior da cabeça aponta pra None
        head_guardado.next = None  # O próximo do nó retirado aponta pra None (lembrando que o anterior do nó retirado já apontava pra None)
        self.length -= 1
        return head_guardado


    def get_value(self, indice):
        if indice < 0 or indice >= self.length:  # Se o índice passado for negativo ou acima da lista
            return None

        if indice < self.length/2:  # Se o índice estiver na primeira metade da lista
            temp = self.head  # Percorro a lista de trás pra frente
            for i in range(indice):
                temp = temp.next
        else:  # Se o índice estiver na segunda metade da lista
            temp = self.tail  # Percorro a lista de frente para trás, assim é muito mais otimizado em n° de operações.
            for i in range(self.length - 1, indice, -1):  # Contador começa no 'tamanho-1' (tamanho da lista em índices), termina no índice informado, e pula -1 casas. Frente pra trás.
                temp = temp.prev
        return temp


    def set_value(self, indice, value):  # Idêntico a lista encadeada simples. A diferença grande está no get.
        new_node = Node(value)
        temp = self.get_value(indice)
        
        if temp is not None:
            temp.value = value
            return True
        return False


    def insert(self, indice, value):
        if indice < 0 or indice > self.length:  # Se o índice é fora da lista
            return False

        if indice == 0:  # Se o índice é o começo da lista
            return self.prepend(value)

        if indice == self.length:  # Se o índice é no final da lista
            return self.append(value)

        new_node = Node(value)  # Criação do nó

        temp = self.get_value(indice-1)  # Pego o nó anterior ao índice que deseja inserir
        temp_after = temp.next  # Pego o nó que vem depois desse nó escolhido, pois precirarei dele

        new_node.prev = temp  # digo que o anterior do nó novo aponta pro índice anterior
        new_node.next = temp_after  # digo que o próximo do nó novo aponta pro índice posterior
        temp.next = new_node  # digo que o próximo do nó guardado de trás agora passa a ser o novo nó inserido
        temp_after = new_node # e o anterior do nó da frente passa a ser o novo nó inserido
        
        self.length -= 1
        return True


    def remove(self, indice):
        if indice < 0 or indice >= self.length:  # Se o índice é fora da lista
            return None  # Não retorna nada

        if indice == 0:
            return self.pop_first()
        if indice == self.length-1:
            return self.pop()

        node_guardado = self.get_value(indice)  # Guardo o nó que desejo remover
        antes = node_guardado.prev  # Guardo o valor antes do nó que quero remover
        depois = node_guardado.next  # Guardo o valor depois no nó que quero remover
        antes.next = depois  # Faço o antes e depois apontarem entre si
        depois.prev = antes

        # Outra forma de fazer, economizando memória e linha de código, porém mais complexo:
        # 
        # node_guardado.next.prev = temp.prev
        # node_guardado.prev.next = temp.next

        node_guardado.next = None  # Faço o nó removido apontar pra nada
        node_guardado.prev = None


        self.length -= 1
        return node_guardado


lista_dup_encadeada = DoublyLinkedList(4)


# ABAIXO SÃO APENAS TEST PURPOSE.

lista_dup_encadeada.append(10002)
lista_dup_encadeada.append(1003)
lista_dup_encadeada.append(50)
lista_dup_encadeada.append(333)

lista_dup_encadeada.remove(3)

lista_dup_encadeada.print_list()

print()
