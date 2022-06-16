import numpy as np

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

def enIntervaloConfianza(alfa, media, valor_test ):
	if (media - alfa < valor_test < media + alfa):
		return True
	else:
		return False