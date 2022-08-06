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
            self.root = new_node  # Insere apenas.
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
                temp = temp.left  # Caso contrário, continua percorrendo a árvore pela esquerda e essa ramificação, e assim repito o loop como se fosse uma sub árvore nova.

            else:  # Se o valor inserido for maior que algum parente
                if temp.right is None:  # Se o direito desse parente não tiver nada, insere lá
                    temp.right = new_node
                    return True
                temp = temp.right  # Caso contrário, continuará percorrendo a árvore pela direita e essa ramificação.


    def contains(self, value):
        pass # TODO


    def min_value(self):
        pass # TODO

    
abb = BinarySearchTree()

abb.insert(2)
abb.insert(1)
abb.insert(3)
