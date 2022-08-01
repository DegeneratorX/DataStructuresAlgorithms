"""
O(log n) é muito poderoso, pois é utilizado em muitos algoritmos
de ordenamento ou busca, e é extremamente eficiente.

Suponha uma lista de 1 a 8
Desejo procurar um número 8, por exemplo.

1 2 3 4 5 6 7 8

Normalmente se iteraria sobre essa lista 1 por 1 até chegar no 8. O(n)

Porém, alguns algoritmos de busca utilizam essa técnica com complexidade de tempo O(log n)
para achar valores sem perder muito tempo.

Ao invés de iterar, divido a lista no meio e capto a banda onde pode estar o valor

5 6 / 7 8 => 7 / 8 => 8

Veja que fiz 3 operações. 3 cortes.

2³ = 8 => log2(8) = 3

Agora imagina 1,073,741,824 números na lista

log2(1,073,741,824) = ?
? = 31. 

Sim. 31 operações para achar o número desejado no pior caso.
Agora imagina percorrer isso em um algoritmo com ct(complexidade de tempo) O(n)
levaria 1 bilhão de operações que, dependendo do computador, iria demorar muito.
"""