import numpy as np
import estadistics as st

nombres = ['$10','$50','$100_old','$100_mapu', '$500']
pesos = [3.5, 7, 9, 7.58, 6.5]
valor = [10, 50, 100, 100, 500]

def tbMoney(v, peso):
	i1 = nombres.index(v[0])
	if len(v) == 1:
		return calcular1([pesos[i1], valor[i1]], peso)
	elif len(v) == 2:
		i2 = nombres.index(v[1])
		return calcular2([pesos[i1], valor[i1], pesos[i2], valor[i2]], peso)


def calcular1(mx, P):
	print('Entradas:',mx, P)
	p1,v1 = mx
	print(P/p1)

def calcular2(mx,P):
	print('Entradas:',mx, P)
	tol = 0.001
	p1,v1,p2,v2 = mx
	maxlim = int(np.max([P/p1, P/p2]).item())
	pesos = [p1,p2]
	V = []
	for p in range(5,100,5):
		pr = p/100
		for a in range(0,maxlim+1):
			for b in range(0,maxlim+1):
				c1=(a*pesos[0]+b*pesos[1] - P)
				c2=(b*pesos[0]+a*pesos[1] - P)
				if (c1 == 0 and c1 == c2 == 0):
					V = agregarSolucion([a,b], V, tol, pr,v1)
				elif (c2 == 0):
					V = agregarSolucion([b,a], V, tol, pr,v2)
	print(V)

def agregarSolucion(vector, vectorSoluciones, tol, pr,m1):
	if(st.probar(vector, tol, pr, m1) and vector not in vectorSoluciones):
		vectorSoluciones.append(vector)
	return vectorSoluciones


tbMoney(["$100_old"], 27)