- ==Notação que limita funções inferiormente==

    - Seja n um inteiro positivo, e sejam f(n) e g(n) funções positivas. Dizemos que:
    
        - f(n) = Ω(g(n))
        - Ou f(n) é Ω(g(n))
    
    - ...se existem constantes positivas c ≠ 0 e n₀ tais que:

        - f(n) ≥ c ∙ g(n) ∀n ≥ n₀

        - Ou seja, f(n) SEMPRE será maior ou igual a c ∙ g(n)
        - Ou seja, sempre será limitada inferiormente por c ∙ g(n)

        - ![image](https://user-images.githubusercontent.com/98990221/185800875-a6c2276e-2c7d-41b4-b6b6-b867692e8cca.png)

    - Ex: f(n) = 5tn + 3t é:

        - Ω(g₁(n)), onde g₁(n) = n?

            - Certamente 5tn + 3t ≥ 5tn
            - 5tn + 3t ≥ (5t) ∙ n
            - Ou seja, mostrei que a função inicial f(n) = 5tn - 3t é maior ou igual a uma constante c vezes n.
            - c = 5t, n₀ = 1
            - Portanto, f(n) é Ω(g₁(n)), ou seja, limitada inferiormente.

        - Ω(g₂(n)), onde g₂(n) = n²?

            - Isso talvez não seja certo 5tn + 3t ≥ 5tn²
            - 5tn + 3t ≥ (5t) ∙ n²
            - Suponha que f(n) = Ω(g₂(n)) ∀n ≥ n₀
            - (5tn + 3t)/n² ≥ (5tn²)/n²
            - (5tn + 3t)/n² ≥ 5t
            - (5t/n) + (3t/n²) ≥ 5t
            - Para n enorme, a equação acima vira 0 ≥ c
            - Perceba que esses dois carinhas acima tendem a 0 quando n tende ao infinito. E 0 certamente não é maior ou igual a constante c, já sabendo que c ≠ 0.
            - Portanto, provamos por absurdo que f(n) não é Ω(n²)
            - EXTRA: se não vale pra n e n², com certeza não vale pra n³, n⁴... infinito. E também O(n ∙ logn)

        - Ω(g₃(n)), onde g₃(n) = √n

            - Certamente como 5tn + 3t ≥ 5tn, 5tn ≥ 5t√n vale.
            - Portanto, f(n) é Ω(g₃(n))
            - EXTRA: Com essa prova, também prova que:
                - f(n) também é O(log n).
                - f(n) também é O(1).
