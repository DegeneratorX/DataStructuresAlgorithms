- Append (adicionar) o último da lista: O(1) 
    - Pois não importa quantos elementos tem na lista. O número de operações sempre será o mesmo (1).

- Pop (remover) o último da lista: O(n)
    - É preciso iterar sobre a lista toda para achar o ponteiro que aponta pro último elemento.

- Append o primeiro da lista: O(1)

- Pop o primeiro da lista: O(1)
    - Pois por ser o primeiro, não é necessário percorrer a lista. Basta ver o nó cabeça.

- Append e Pop no meio da lista: O(n)
    - É preciso iterar sobre a lista para adicionar o elemento no pior caso.


'''TABELA DE COMPARAÇÃO ENTRE LINKED LIST E LIST DO PYTHON

                LL      List
Append          O(1)    O(1)
Pop             O(n)    O(1)
Prepend         O(1)    O(n)
Pop First       O(1)    O(n)
Insert          O(n)    O(n)
Remove          O(n)    O(n)
Lookup by Index O(n)    O(1)
Lookup by Value O(n)    O(n)'''