"""
Busca Binária em um vetor já ordenado (crescente)
Não recursiva e recursiva
"""


class Vetor:
    def __init__(self, vector, size, last_index, first_index=0):
        self.vector = vector
        self.size = size
        self.first_index = first_index
        self.last_index = last_index

    def busca(self, elemento):
        while(self.first_index <= self.last_index):
            q = round((self.first_index+self.last_index)/2)
            if self.vector[q] < elemento:
                self.first_index = q + 1
            elif self.vector[q] > elemento:
                self.last_index = q - 1
            else:
                return q
        return None

lista = [1,2,3,5,10]
vetor1 = Vetor(lista, len(lista), 0, len(lista)-1)
print(vetor1.busca(5))