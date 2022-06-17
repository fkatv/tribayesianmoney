import numpy as np
import estadistics as st

nombres = ['$10','$50','$100_old','$100_mapu', '$500']
peso = [3.5, 7, 9, 7.58, 6.5]
valor = [10, 50, 100, 100, 500]

def tbMoney(v, p):
    i1 = nombres.index(v[0])
    i2 = nombres.index(v[1])
    i3 = nombres.index(v[2])
    return calcular3([peso[i1], valor[i1], peso[i2], valor[i2],peso[i3], valor[i3]], p)

def calcular3(mx,P):
	print('Entradas:',mx, P)
	tol = 0.00001
	p1,v1,p2,v2,p3,v3 = mx
	maxlim = int(np.max([P/p1, P/p2, P/p3]).item())
	pesos = [p1,p2,p3]
	v = [v1,v2,v3]
	V = []
	for p in range(0,105,5):
		pr1 = p/100
		for h in range(0,105,5):
			pr2= h/100
			for a in range(0,maxlim+1):
				for b in range(0,maxlim+1):
					for c in range(0,maxlim+1):
						c1=(a*pesos[0]+b*pesos[1]+c*pesos[2]- P)
						c2=(b*pesos[0]+a*pesos[1]+c*pesos[2]- P)
						if (pr1 + pr2  < 1):
							pr3 = 1 - (pr1 + pr2)
							iterar(a,b,c,pr1,pr2,pr3,c1,c2,tol,V,v)
						else:
							pr3 = 0	
							iterar(a,b,c,pr1,pr2,pr3,c1,c2,tol,V,v)

		
	print(V)

def iterar(a,b,c,pr1,pr2,pr3,c1,c2,tol,V,v):
	if (c1==0 or c2==0 and [a,b,c] not in V and [b,a,c] not in V):
		if (c1 == 0 and  c1==c2==0):
			V = agregarSolucion([a,b,c],V, tol, pr1, pr2, pr3 ,v)
		elif (c2 == 0):
			V = agregarSolucion([b,a,c],V, tol, pr1, pr2, pr3 ,v)

def agregarSolucion(vector, vectorSoluciones, tol, pr1,pr2,pr3,v):
	if(st.probar3(vector, tol, pr1,pr2,pr3, v[0]) and vector not in vectorSoluciones):
		vectorSoluciones.append([vector, valorTotal(vector, v)])
		print(vector, pr1,pr2,pr3)
	return vectorSoluciones

def valorTotal(vector, val):
	return vector[0]*val[0] + vector[1]*val[1] + vector[2]*val[2]

tbMoney(["$10","$100_old","$100_mapu"], 61.66)