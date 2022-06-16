# TriBayesian Money

### Descripción

Este es un proyecto simple de cálculo algoritmico que simula una aproximación de un contador de monedas metálicas y cálculo de su monto  bajo un montón discreto y limitado de monedas. Se emplea como entrada el peso total en gramos del montón y los posibles tipos de monedas. Sin embargo, como no hay certeza de las proporciones de las cantidades exactas de monedas, esto puede provocar más de una solución. Para ello, se procede a estimar con parámetros bayesianos aplicadas a las estimaciones porcentuales de las cantidades de monedas con respecto al conteo total.


### Ejemplo

**Caso Perfecto entre dos monedas:**

- Entrada 1: **39** [gramos] 
- Entrada 2: [$10, $100] (A posteriori se sabe que 21gr son de $10 y 18gr de $100 antiguas)
- Entrada 3 opcional: 0.75 (El 75% de las cantidades de monedas son de la primera moneda ($10) )

**RESULTADO:** [6, 2] (Hay 6 monedas de $10 y 2 monedas de $100_old, 6/8 % de $10 = 75%)

### Desarrollo

En cada país, se tiene un conjunto M de monedas metálicas. Pongamos el caso de Chile tal como sigue:

> - Etiquetas de monedas por valor: $10, $50, $100_old, $100_mapu, $500
> - Valor de monedas: 10, 50, 100, 100, 500
> - Peso de monedas: 3.5, 7, 9, 7.58, 6.5

Analíticamente, para un tipo de moneda cuyo peso es $p_{1}$ con una cantidad $x$ de monedas, tenemos que la relación de la cantidad con el peso total $P$ esta dado por:

$$ x \cdot p_{1} = P$$

Para el caso de dos tipos de monedas, cuyo peso para la primera es $p_{1}$ con una cantidad $x$ de monedas, $p_{2}$ con una cantidad $y$ del segundo tipo de moneda,   tenemos que la relación de éstas con el peso total $P$ esta dado por: 

$$ x \cdot p_{1} + y \cdot p_{2} = P$$

Dado que aún no se han contado las monedas, y no sabemos la cantidad exacta de ellas, para efecto de la simulación que minimice el rango de error en los cálculos, formalmente se define: 

Sea:

- $\hat{x}$ = cantidad i-ésima iterado para la moneda 1

- $\hat{y}$ = cantidad i-ésima iterado para la moneda 2


$$x \sim \hat{x}$$

$$y \sim \hat{y}$$

$$ x \cdot \hat{p_{1}} + y \cdot \hat{p_{2}} = \hat{P}$$


El iterador debe tener un límite máximo para no caer en loops infinitos, considerando un numero **maxlim** como el entero máximo entre el peso total $P$ y los pesos de las dos monedas escogidas.

$$maxlim = max{ \frac{P}{p1}, \frac{P}{p2}}$$

La función que se debe minimizar es la diferencia de pesos, que en la práctica es el error absoluto entre el peso estimado por la simulación $\hat{P}$ y el peso total $P$ de la entrada. 

$$|P - \hat{P}| \sim 0$$

Cuando se encuentra una posible solución, llámese *vector tentativo*, se agregará dicha solución, considerando una tolerancia < 0.01 si:

Se prueba que para una probabilidad $\rho$:
- La norma de la cantidad $\hat{x}$ 
está dentro del intervalo de confianza entre una tolerancia $\tau$ 
y una probabilidad bayesiana $\rho$.
- La norma de la cantidad $\hat{y}$ 
está dentro del intervalo de confianza entre una tolerancia $\tau$ y una probabilidad bayesiana $1 - \rho$
- El vector tentativo no se encuentra en el vector de soluciones.


Se itera el valor de la probabilidad desde $0 < \tau <= 100$ con un paso de 5 unidades.


