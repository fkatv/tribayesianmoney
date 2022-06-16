import numpy as np

def calcular(mx,P):
	tol = 0.001
	p1,v1,p2,v2 = mx
	maxlim = int(np.max([P/p1, P/v2]).item())
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

def probar (v, tol, pr, m1):
	apr = 1-pr
	xnorm, ynorm = normalizar(v)
	if (enIntervaloConfianza(tol, pr, xnorm)):
		if (enIntervaloConfianza(tol, apr, ynorm)):
			print(v, pr*100,"% de cantidad de monedas de", m1)
			return True
	else:
		return False

def normalizar(v):
	norma = np.sum(v)
	return [k/norma for k in v]

def agregarSolucion(vector, vectorSoluciones, tol, pr,m1):
	if(probar(vector, tol, pr, m1) and vector not in vectorSoluciones):
		vectorSoluciones.append(vector)
	return vectorSoluciones

def enIntervaloConfianza(alfa, media, valor_test ):
	if (media - alfa < valor_test < media + alfa):
		return True
	else:
		return False
	
calcular([3.5,10,9,100], 39)