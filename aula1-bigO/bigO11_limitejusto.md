- ==Notação que limita funções justamente==

    - Seja n um inteiro positivo, e sejam f(n) e g(n) funções positivas. Dizemos que:
        
        - f(n) = Θ(g(n)) 
        - Ou f(n) é Θ(g(n))

    - ...se existem constantes positivas c₁ ≠ 0, c₂ ≠ 0 e n₀ tais que;

        - c₁∙g(n) ≤ f(n) ≤ c₂∙g(n) ∀n ≥ n₀
        - Ou seja, f(n) SEMPRE será maior ou igual a c₁ ∙ g(n) e menor ou igual a c₂ ∙ g(n)
        - Ou seja, sempre será limitada inferiormente por c₁ ∙ g(n) e superiormente por c₂ ∙ g(n).
        - IMPORTANTÍSSIMO: f(n) é Θ(g(n)) sse f(n) é O(g(n)) e é Ω(g(n))

        - ![image](https://user-images.githubusercontent.com/98990221/185801812-f5a25b18-1274-4e3b-942f-cefc43c82bc4.png)

    - Ex: f(n) = 5tn + 3t é:

        - Θ(g₁(n)), onde g₁(n) = n?
            - Vimos isso. Sim, pois posso colocar 5tn ≤ 5tn + 3t ≤ 8tn
            - Portanto, f(n) é Θ(n).

        - Θ(g₂(n)), onde g₂(n) = n²?
            - Será que c₁∙n² ≤ 5tn + 3t ≤ c₂∙n²?
            - A gente viu que o c₁∙n² ≤ 5tn + 3t não é verdade.
            - Portanto, f(n) não é Θ(n²)

        - Θ(g₃(n)), onde g₃(n) = √n
            - A gente já viu que f(n) não é O(√n).
            - Portanto, f(n) não é Θ(√n).