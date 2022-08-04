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
            temp = temp.next


    def append(self, value):  # Recebe o valor para adicionar no final da lista
        new_node = Node(value)  # Instancio para trabalhar como um nó inicial e isolado
        if self.length == 0:  # Verifico se a lista está vazia
            self.head = new_node  # Se estiver vazia, insiro o nó na lista. Digo que a cabeça e a cauda da lista é o valor inserido, pois só terá ele, já que previamente estava vazia.
            self.tail = new_node
        else:  # Se tiver pelo menos com 1 elemento...
            self.tail.next = new_node  # ...mexe apenas na cauda (último elemento). O próximo do atual último elemento deve apontar pro novo elemento inserido
            self.tail = new_node  # E o elemento inserido deve ser a nova cauda. Ou seja, ser considerado o último elemento da lista.
        self.length += 1  # Tamanho da lista aumenta
        return True  # Retorna True para ser usado em outro momento por outro método.


    def pop(self):  # Retirar o último elemento, não importa qual seja
        if self.length == 0:  # Se a lista estiver vazia, retira nada.
            return None

        tail_guardado = self.tail  # Se ela não está vazia, tem pelo menos 1 elemento. Guardo o último elemento.

        if self.length == 1:  # Se tiver 1 elemento...
            self.head = None  # ...digo que a lista agora é vazia.
            self.tail = None
            self.length = 0  # De tamanho 0, e retorno o valor que guardei, afinal era o único.
            return tail_guardado

        else:  # Tendo dois ou mais elementos
            temp = self.head  # Uso uma variável temporária pra iterar sobre a lista.
            while temp.next.next:  # Procuro sempre o próximo do próximo do nó, se for None, sai do loop.
                temp = temp.next  # Pego o próximo e atribuo ao atual. Assim posso trabalhar com o próximo do próximo do próximo, etc...
            temp.next = None  # Ao achar o final da lista, digo que o próximo do último aponta pra nada.
            self.tail = temp  # E finalmente atribuo como a nova cauda da lista.
            self.length -= 1  # Diminuo o tamanho dela
            return tail_guardado  # Retorno o que foi, antes de tudo, guardado como último da lista.


    def prepend(self, value):  # Coloca um elemento informado (value) no início da lista encadeada
        new_node = Node(value)  # Crio um nó, recebo o valor adicionado
        if self.length == 0:  # Se lista vazia
            self.head = new_node  # Simplesmente adiciono o nó como cabeça e cauda
            self.tail = new_node
        else:  # Se não...
            new_node.next = self.head  # Digo qeu o próximo do novo nó aponta pra atual cabeça
            self.head = new_node  # E a cabeça se torna o novo nó criado
        self.length += 1
        return True


    def pop_first(self):  # Tira o primeiro elemento da lista encadeada
        if self.length == 0:  # Se vazio, tira nada
            return None

        head_guardado = self.head  # Variável temporária do que queremos retirar

        if self.length == 1:  # Se tiver 1 elemento
            self.head = None  # Esvazia a lista
            self.tail = None
            self.length = 0
            return head_guardado  # Retorna o que foi retirado/guardado

        if self.length > 1:  # Se tiver mais de 1 elemento
            self.head = self.head.next  # Defino como a nova cabeça da lista o próximo da mesma cabeça, afinal não tem como a cabeça se manter, dado que irei tirar ela.
            head_guardado.next = None  # E digo que o pŕoximo da antiga cabeça guardada aponta pra Nada
            self.length -= 1
            return head_guardado  # Assim, retorno o nó limpinho com o valor retirado da lista + ponteiro apontando pra nada.


    def get_value(self, indice):  # A função basicamente percorre a lista até achar o que tem no índice da lista que o usuário deseja saber.
        if indice < 0 or indice >= self.length:  # Verifico se o índice é válido. Se não, retorna nada.
            return None
        
        temp = self.head  # Variável de controle para iterar sobre a lista
        for i in range(indice):  # Procuro o índice informado iterando
            temp = temp.next  # Vejo nó por nó até a iteração acabar. Quando acabar, é o índice correto.
        return temp  # Retorno o nó. Posso usar temp.value para retornar o valor do nó. Posso usar temp.next pra saber o próximo desse valor.


    def set_value(self, indice, value):  # A função faz a mesma coisa que o get, mas configura o valor ao passar o index e o value.
        temp = self.get_value(indice)  # Reutilizo o código do método anterior e guardo o nó que foi retornado em set_value()
        if temp is not None:  # Se não retornar None
            temp.value = value  # Configuro o valor do nó
            return True
        return False


    def insert(self, indice, value):  # Inserir um nó na lista. Basicamente é um append, só que em qualquer lugar, incluindo meio.
        new_node = Node(value)

        if indice < 0 or indice > self.length:  # Se o índice é muito maior que a lista ou negativo, é inválido
            return False

        if indice == 0:
            return self.prepend(value)  # Se o índice é o valor inicial, basicamente a inserção é um prepend.

        if indice == self.length:
            return self.append(value)  # Se o índice é o valor final, basicamente a inserção é um append.

        temp = self.get_value(indice-1)  # Preciso passar o nó no índice-1 escolhido pois quero o nó anterior para apontar pro novo nó. O da frente não me interessa.

        new_node.next = temp.next  # Próximo do novo nó aponta pro próximo do nó anterior (óbvio)
        temp.next = new_node  # e o próximo do nó anterior aponta pro novo nó.  3 -> 5   =>   3 -> 10 -> 5
        self.length +=1  # Aumento o tamanho da lista
        return True


    def remove(self, indice):  # Remove um valor da lista baseado no índice passado
        if indice < 0 or indice >= self.length:  # Se for negativo ou índice muito maior que a lista
            return None  # Retorna nada
        if indice == 0:  # Se o índice for 0...
            return self.pop_first()  # Se o índice é o valor inicial, basicamente a remoção é um pop no primeiro da lista. Lembrando que a função também verifica se tem 0 ou 1 elemento.
        if indice == self.length - 1:
            return self.pop()  # Se o índice é o valor final, basicamente a remoção é um pop no último da lista.

        temp = self.get_value(indice-1)  # Preciso do nó anterior ao que vai ser deletado.
        deletado_guardado = temp.next  # Guardo o valor que quero deletar, que é o próximo do anterior (óbvio), pois vou retornar o que foi removido.

        # deletado_guardado = self.get_value(indice)  AVISO: Assim também está correto, PORÉM é menos eficiente, pois usa 2 funções com TC (Time Complexity) O(n)
        # temp = self.get_value(indice-1)

        temp.next = deletado_guardado.next  # digo que o próximo do nó anterior é igual ao próximo do que vai ser deletado
        deletado_guardado.next = None  # Digo que o próximo do nó deletado aponta pra None, assim isolo o nó completamente da lista.
        self.length -= 1  # Diminuo o tamanho
        return deletado_guardado  # Retorno o nó removido.


    def reverse(self):  # Algoritmo bem complexo e que levou tempo pra entender. Reverte uma lista encadeada por completo.
        temp = self.head  # Faço um swap de cabeça e cauda
        self.head = self.tail
        self.tail = temp  # Lembrando que temp ainda é de certa forma o "inicio" da lista

        after = temp.next  # Digo que o que vem depois de temp é after
        before = None  # E antes vem nada

        for i in range(self.length):  # Itero a lista para reverter ela completamente
            after = temp.next  # o after aponta pro próximo de temp
            temp.next = before  # o próximo de temp aponta pro antes (none). Isso inverte a seta do nó temp pra esquerda.
            before = temp  # antes aponta pro temp
            temp = after  # e temp aponta pro depois
        # O recomendado é fazer um desenho passo a passo de como funciona esses apontamentos, pois é complexo.


lista_encadeada = LinkedList(4)

# ABAIXO SÃO APENAS COMENTÁRIOS TEST PURPOSE.

lista_encadeada.append(5)
lista_encadeada.append(10)
lista_encadeada.append(12)
lista_encadeada.append(23)

print()

print(lista_encadeada.head.next.next.next.value)

print()

lista_encadeada.print_list()