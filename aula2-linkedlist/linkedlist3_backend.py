"""
Lista encadeada - Backend
Resumindo basicamenteo que ocorre por trás dos panos.

Head                          Tail
 \/                            \/
 11  ->  3  ->  23  ->  7  ->  4  ->  None

Head                   Tail
 \/                     \/                       POP
 11  ->  3  ->  23  ->  7  ->  None          4  ->  None

Isso é um NÓ. Contém um ponteiro e um valor.
[4  ->  None]

Basicamente um dicionário.
{
    "value": 4,
    "next": None
}
"""
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": {
                    "value": 4,
                    "next": None
                }
            }
        }
    }
}
print(head['next']['next']['value'])  # Busca do número 23

# Mas a implementação real seria essa aqui:
# print(lista_encadeada.head.next.next.value)
