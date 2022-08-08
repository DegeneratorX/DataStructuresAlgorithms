class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    # def __init__(self, value):  # MÉTODO ANTIGO PARA INICIALIZAÇÃO DE UMA ESTRUTURA
        # new_node = Node(value)
        # self.root = new_node
        # self.height = 1

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


    def min_value_node(self, current_node=root):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


abb = BinarySearchTree()

abb.insert(2)
abb.insert(1)
abb.insert(3)
