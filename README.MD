# TriBayesian Money

### Descripción

Este es un proyecto simple de cálculo algoritmico que simula una aproximación de un contador de monedas metálicas y cálculo de su monto  bajo un montón discreto y limitado de monedas, empleando como entrada su peso en gramos y los posibles tipos de monedas. Sin embargo, como no hay certeza de las proporciones de las cantidades exactas de monedas, se procede a estimar con parámetros bayesianos aplicadas a las estimaciones porcentuales de las cantidades de monedas con respecto al conteo total.


### Ejemplo

**Caso Perfecto entre dos monedas:**

- Entrada 1: **39** [gramos] 
- Entrada 2: [$10, $100] (A posteriori se sabe que 21gr son de $10 y 18gr de $100 antiguas)
- Entrada 3: 0.75 (El 75% de las cantidades de monedas son de la primera moneda ($10) )

**RESULTADO:** [6, 2] (Hay 6 monedas de $10 y 2 monedas de $100_old, 6/8 % de $10 = 75%)

### Desarrollo

En cada país, se tiene un conjunto M de monedas metálicas. Pongamos el caso de Chile tal como sigue:

> - Etiquetas de monedas por valor: $10, $50, $100_old, $100_mapu, $500
- Valor de monedas: 10, 50, 100, 100, 500
- Peso de monedas: 3.5, 7, 9, 7.58, 6.5

