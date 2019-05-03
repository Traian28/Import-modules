def cargar_datos():
	lista=[]
	for x in range(5):
		lista.append(int(input("Ingrese un valor: ")))
	return lista

def verificar_mayor(lista):
	return max(lista)

def verificar_suma(lista):
	suma=0
	for i in range(len(lista)):
		suma += lista[i]
	return suma