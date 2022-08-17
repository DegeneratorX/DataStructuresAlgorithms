- ==Notação que limita funções superiormente==

    - Seja n um inteiro positivo, e sejam f(n) e g(n) funções positivas. Dizemos que:

        - f(n) = O(g(n))
        - Ou f(n) é O(g(n))

    - ...se existem constantes positivas c ≠ 0 e n₀ tais que:

        - f(n) ≤ c ∙ g(n) ∀n ≥ n₀

        - Ou seja, f(n) SEMPRE será menor ou igual a c ∙ g(n)
        - Ou seja, sempre será limitada superiormente por c ∙ g(n)

    - Ex: f(n) = 5tn + 3t é:

        - O(g₁(n)), onde g₁(n) = n?

            - Certamente 5tn + 3t ≤ 5tn + 3tn
            - 5tn + 3t ≤ (8t)∙(n)
            - Ou seja, mostrei que a função inicial f(n) = 5tn - 3t é menor ou igual a uma constante c vezes n.
            - c = 8t, n₀ = 1
            - Portanto, f(n) é O(g₁(n))

        - O(g₂(n)), onde g₂(n) = n²?

            - Certamente 5tn + 3t ≤ 5tn + 3tn = 8tn
            - Certamente 8tn ≤ 8tn². Portanto, 5tn + 3t ≤ 8tn²
            - Ou seja, mostrei que f(n) é menor ou igual a c ∙ n²
            - c = 8t, n₀ = 1
            - Portanto, f(n) é O(g₂(n)).
            - EXTRA: se vale pra n e n², com certeza vale pra n³, n⁴... infinito. E também O(n ∙ logn)

        - O(g₃(n)), onde g₃(n) = √n?

            - Lembrando que √n = n¹/². O fato é que por ser raíz de n, é menor que n. Mas será que se eu multiplicar por uma constante, será que ainda dá pra dizer que 5tn + 3t ≤ c√n?

            - Vou dividir dos dois lados por √n.

            - (5tn + 3t)/√n ≤ c
            - 5t√n + (3t)/√n ≤ c

            - Ou seja, c tem que ser maior que essa expressão, sempre que n for maior que um valor n₀
            - Analisando, temos que (3t)/√n, ao aumentar muito o n, (3t)/√n tende a zero. Porém, se eu aumentar n, 5t√n aumenta também. Portanto, a expressão como um todo cresce conforme n cresce.
            - Como que eu vou encontrar uma constante c que seja ainda maior do que isso? Sabendo que a expressão do lado direito não depende de n?

            - Fixo um valor c = 1,000,000. Ainda sim, vai ter um n do lado esquerdo que vai ser ainda maior do que c. Então eu não consigo fixar o c. Não vai existir um c que satisfaça essa expressão.

            - Conclusão: assumi que f(n) é O(√n) verdade. Por causa disso, esse c que satisfaz deveria existir, mas ocorre uma contradição, pois esse c não pode existir. Portanto, o que eu assumi não vale. Ou seja, f(n) não é O(√n).

            - Não tem como ela ser limitada superiormente por √n, por mais que eu possa multiplicar essa √n por um número.

            - EXTRA: Com essa prova, também prova que:
                - f(n) também não é O(log n).
                - f(n) também não é O(1).