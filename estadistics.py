import numpy as np

def probar (v, tol, pr, m1):
	apr = 1-pr
	xnorm, ynorm = normalizar(v)
	if (enIntervaloConfianza(tol, pr, xnorm)):
		if (enIntervaloConfianza(tol, apr, ynorm)):
			print(v, pr*100,"% de cantidad de monedas de $", m1)
			return True
	else:
		return False

def probar3 (v, tol, pr1,pr2,pr3, m1):
	xnorm, ynorm,znorm = normalizar(v)
	if (enIntervaloConfianza(tol, pr1, xnorm)):
		if (enIntervaloConfianza(tol, pr2, ynorm)):
			if (enIntervaloConfianza(tol, pr3, znorm)):
				print(v, pr1*100,"% de cantidad de monedas de $", m1)
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