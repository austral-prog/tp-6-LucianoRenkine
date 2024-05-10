def remove_elements(lista):
	if len(lista) >= 6:
		del lista[5]
		del lista[4]
		del lista[0]
		return lista
	elif len(lista) == 5:
		del lista[4]
		del lista[0]
		return lista
	else:
		del lista[0]
		return lista

def add_elements(lista_2):
	lista_2.append("Yellow")
	lista_2.insert(0,"Pink")
	return lista_2

def is_empty(lista_3):
	if len(lista_3) == 0:
		return True
	else:
		return False

def check_list(a, b):
	if len(a) >= 3 and len(b) >= 3:
		if a[2] == b[2]:
			return True
		else:
			return False
	else:
		return False

def list_of_lists(c):
	if  len(c[0])>=2 and len(c[1])>=4 and len(c[2])>=2:
		c[0] = c[0][0:2]
		c[1] = c[1][1:4]
		c[2] = c[2][-2:]
		return c
