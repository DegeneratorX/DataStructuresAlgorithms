"""
Pilhas são exatamente listas encadeadas, só que para remoção ou adição, existem algumas diferenças.

O primeiro elemento que entrar é o último a sair.
O último elemento que entrar é o primeiro a sair.

FILO (First in, last out)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value, size=1):  # Usuário declara o tamanho da pilha. Por padrão, ela terá tamanho 1.
        new_node = Node(value)
        self.top = new_node  # Só irei precisar do valor do topo, pois não me interessa o bottom, afinal não conseguimos vê-lo.
        self.size = size
        self.height = 1
        

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def isfull(self):  # Procuro saber se a pilha está cheia
        if self.height == self.size:  # Se a quantidade de elementos (altura) é igual ao tamanho da pilha, então retorna True.
            return True
        return False

    def isempty(self):  # Opcional: se a instância assim desejar, pode querer saber se a pilha está vazia no momento que chamar.
        if self.height == 0:
            return True
        return False

        
    def push_node(self, value):  # Mesma coisa do prepend de lista encadeada simples.
        if self.isfull():  # Se a pilha estiver cheia, retorna False (stack overflow). Não é possível adicionar nó à pilha.
            return False

        new_node = Node(value)  # Criação do nó que será adicionado
        if self.height == 0:  # Se a pilha estiver vazia
            self.top = new_node  # O topo é o novo nó.
        else:  # Se a pilha tiver ao menos 1 elemento
            new_node.next = self.top   # O próximo do novo nó aponta pro topo atual da pilha
            self.top = new_node  # O topo atual vira o novo nó.

        self.height += 1
        return True


    def pop_node(self):  # Remover elemento da pilha é idêntico com o pop_first da lista encadeada.
        if self.height == 0:  # Se pilha vazia
            return None
        
        temp = self.top  # Guardo o topo da pilha

        if self.height == 1:  # Se tiver 1 elemento
            self.top = None
            self.height = 0
            return temp

        if self.height > 1:
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp
        

# ABAIXO SÃO APENAS TEST PURPOSE.

pilha = Stack(25, 10)  # Pilha de tamanho 10. Cabe 10 elementos. Inicia com um elemento 4.

for i in range(10):
    pilha.push_node(i)

pilha.print_stack()

print(pilha.isfull())
