"""
- Recursão:
    Uma função que se chama, até não poder mais.

- Caso base: quando retorna o objeto em si, e não executa mais a função recursiva.
- Caso recursivo: quando executa a função recursiva e não retorna o objeto.
"""


def open_gift_box(ball=False):
    if ball:
        return ball
    open_gift_box(True)


#####################################
# Call Stack: Quando as funções se empilham de forma que uma é executada para
# a outra ser executada.
#
#  _       _
# |funcThree|
# |funcTwo  |
# |funcOne  |
# \_________/
#
# Mesmo que a funcOne tenha sido executada primeiro, a funcThree é quem irá executar,
# pois quando a funcOne é executada, a funcTwo é executada e pausa a funcOne, e assim
# sucessivamente.

def funcThree():
    print('Three')


def funcTwo():
    funcThree()
    print('Two')


def funcOne():
    funcTwo()
    print('One')


funcOne()
