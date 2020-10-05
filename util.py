import random

# Cria matriz com numeros aleatorios
def criaMatriz(tam):
	matriz = []
	if tam>0:
		for i in range(tam):
			linha = []
			for j in range(tam):
				num = random.randint(1,99999)
				linha.append(num)
			matriz.append(linha)
	return matriz

# Imprimir matriz
def printMatriz(matriz):
	tam = len(matriz)
	#print(tam)
	print('-------MATRIZ-------')
	for i in range(tam): # range(n) -> [0..n-1]
		for j in range(tam):
			print('{}\t'.format(matriz[i][j]))
		print('\n')
	print('-------')
	pass

# Se o num é primo	
def isPrime(n):
	# É divisível só por 1 e ele mesmo?
	div = 0 # Quantidade de divisores desse número
	for i in range(1,n+1): # n+1 devido range(a,b) compreende [a..b-1]
		if n%i==0:
			div += 1
	#print(div)
	return True if div==2 else False

# Conta primos em uma lista
def countPrime(lista):
	counter = 0
	for number in lista:
		counter += 1 if isPrime(number) else 0
    	#print(counter)
	return counter
