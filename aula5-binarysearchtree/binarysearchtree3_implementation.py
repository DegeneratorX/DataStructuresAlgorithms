class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    # def __init__(self, value):  # MÉTODO ANTIGO PARA INICIALIZAÇÃO DE UMA ESTRUTURA
        # new_node = Node(value)
        # self.root = new_node
        # self.height = 1v

    def __init__(self):  # MÉTODO NOVO PARA INICIALIZAÇÃO DE UMA ESTRUTURA: A árvore começará vazia.
        self.root = None  # Meio que é equivalente a passar value = None.
        self.height = 0


    def insert(self, value):  # O(log n)
        new_node = Node(value)
        if self.root == None:  # Se vazia
            self.root = new_node  # Insere  apenas.
            return True

        temp = self.root  # Variável para iterar na árvore. Não quero modificar o self.root, é meu único ponto de referência, não posso perdê-lo ou a árvore
                          # terá valores perdidos e será impercorrível.
        while True:  # Looping while, pois será breakado com returns.
            if new_node.value == temp.value:  # Se o nó inserido tiver valor igual a algum nó na árvore, é impossível inserir.
                return False
            
            if new_node.value < temp.value:  # Se o valor inserido for menor que algum parente
                if temp.left is None:  # Se o esquerdo desse parente não tiver nada, insere lá.
                    temp.left = new_node
                    return True
                else: 
                    temp = temp.left  # Caso contrário, continua percorrendo a árvore pela esquerda e essa ramificação, e assim repito o loop como se fosse uma sub árvore nova.

            else:  # Se o valor inserido for maior que algum parente
                if temp.right is None:  # Se o direito desse parente não tiver nada, insere lá
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right  # Caso contrário, continuará percorrendo a árvore pela direita e essa ramificação.


    def contains(self, value):  # Retorna True se um valor específico informado está na árvore. Retorna False caso contrário.

        # if self.root == None:  # Opcional, mas redundante, pois o While faz o trabalho para nós.
        #     return False

        temp = self.root  # Variável de iteração
        while temp is not None:  # Enquanto a variável não se chocar com um None (pois se sim, significa que o valor não existe na árvore)
            if value < temp.value:  # Se o valor informado for menor do que o valor do nó iterador
                temp = temp.left  # Move pra esquerda
            elif value > temp.value:
                temp = temp.right  # Move pra direita
            else:  # if value == temp.value
                return True  # Significa que achou o valor dentro da árvore.
        return False  # Ao sair do while, significa que o iterador é None, ou seja, chegou no fim da árvore e não achou o valor. Pode significar também que a árvore é vazia.


    def __get_successor(self, node):  # Método para ser utilizado com a condição 3 do método Remove().
        successor_parent = node
        successor = node
        temp = node.right
        while temp is not None:
            successor_parent = successor
            successor = temp
            temp = temp.left
        if successor != node.right:
            successor_parent.left = successor.right
            successor.right = node.right
        return successor


    def remove(self, value):  # TODO: Estudar essa p**** dps, pq foi difícil pra p**** implementar isso aqui
        temp = self.root
        parent = self.root
        is_left = True

        while temp.value != value:  # Percorrimento da árvore
            parent = temp  # Necessário para capturar o valor anterior ao temp.
            if value < temp.value:  # Percorre esquerda
                is_left = True
                temp = temp.left
            else:  #                  Percorre direita
                is_left = False
                temp = temp.right
            if temp == None:  # Se não achou o valor pra deletar, retorna nada.
                return None

        # Encontrado o elemento, vamos para as condições complexas
        
        if temp.left == None and temp.right == None:  # CONDIÇÃO 1: o nó não tem filhos (é uma folha)
            if temp == self.root:  # Se tiver 1 elemento na árvore
                self.root = None  # Esvazia a árvore.
            elif is_left:  # Se não, se estiver pela esquerda
                parent.left = None  # Removo o ponteiro para esquerda que aponta pro elemento que desejo remover.
            else:  # Se tiver pela direita...
                parent.right = None  # Removo o ponteiro pra direita que aponta pro elemento que desejo remover.

        elif temp.right == None:  # CONDIÇÃO 2: o nó tem apenas 1 filho (esquerdo)
            if temp == self.root:
                self.root = temp.left
            elif is_left:
                parent.left = temp.left
            else:
                parent.right = temp.left

        elif temp.left == None:  # CONDIÇÃO 2: o nó tem apenas 1 filho (direito)
            if temp == self.root:
                self.root = temp.right
            elif is_left:
                parent.left = temp.right
            else:
                parent.right = temp.right

        else:  # CONDIÇÃO 3: o nó tem 2 filhos.
            successor = self.__get_successor(temp)

            if temp == self.root:
                self.root = successor
            elif is_left:
                parent.left = successor
            else:
                parent.right = successor
            
            successor.left = temp.left

        return True  # Feedback pra dizer que apagou com sucesso


    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    
    def max_value_nude(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value


abb = BinarySearchTree()

abb.insert(2)
abb.insert(1)
abb.insert(3)

print(abb.min_value_node(abb.root))
