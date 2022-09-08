"""
Questão 1

a) Vamos provar que n³/100 - 25n² - 100n + 7 = Θ(g(n)), onde g(n) é n³.

Será que: c₁∙g(n) ≤ f(n) ≤ c₂∙g(n) ∀n ≥ n₀ ?

Para isso, precisamos por partes. 
Provar que f(n) é Θ(g(n)) sse f(n) é O(g(n)) e é Ω(g(n))

Certamente (n³/100 - 25n² - 100n + 7) ≤ (n³/100 - 25n² - 100n + 7n)
Certamente (n³/100 - 25n² - 93n) ≤ (n³/100 - 25n² + 93n²)
Certamente (n³/100 + 68n²) ≤ (n³/100 + 68n³)
Certamente (680.1n³) possui uma constante c = 680.1 e um n₀ em que vale:
(n³/100 - 25n² - 100n + 7) ≤ (680.1n³)

Portanto, f(n) é O(n³).

Por conta da prova direta pro limite superior ter dado certo, precisamos
provar por absurdo o limite inferior, pois:
Certamente isso não vale: (n³/100 - 25n² - 100n + 7) ≥ (c ∙ n³), ∀n ≥ n₀

Suponha que de fato f(n) = Ω(n³), ∀n ≥ n₀

(n³/100 - 25n² - 100n + 7) ≥ (n³/100 - 25n² - 100n)
(n³/100 - 25n² - 100n + 7)/n³ ≥ (n³/100)/n³
Para n enorme, uma hora o lado esquerdo ficará menor que 1/100 do lado direito.
Portanto, a inequação é falsa.

Portanto, f(n) é O(n³) e não é Ω(n³), o que implica que f(n) não é Θ(n³).



"""