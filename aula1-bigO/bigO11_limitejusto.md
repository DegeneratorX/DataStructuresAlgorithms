- ==Notação que limita funções justamente==

    - Seja n um inteiro positivo, e sejam f(n) e g(n) funções positivas. Dizemos que:
        
        - f(n) = Θ(g(n)) 
        - Ou f(n) é Θ(g(n))

    - ...se existem constantes positivas c₁ ≠ 0, c₂ ≠ 0 e n₀ tais que;

        - c₁∙g(n) ≤ f(n) ≤ c₂∙g(n) ∀n ≥ n₀
        - Ou seja, f(n) SEMPRE será maior ou igual a c₁ ∙ g(n) e menor ou igual a c₂ ∙ g(n)
        - Ou seja, sempre será limitada inferiormente por c₁ ∙ g(n) e superiormente por c₂ ∙ g(n).
        - IMPORTANTÍSSIMO: f(n) é Θ(g(n)) sse f(n) é O(g(n)) e é Ω(g(n))

    - Ex: f(n) = 5tn + 3t é:
        
        - 