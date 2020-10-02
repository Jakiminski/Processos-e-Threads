#!/usr/bin/env python
# coding: utf-8

from process import * # src process.py
from util import * # src util.py

modo = 'multiprocessing' # 'multiprocessing' ou 'threading'
processos = [] # Fila que guarda processos em execução
matriz = []
contaPrimos = 0

if __name__ == '__main__':
	
	## Criar matriz de num aleatorios
	matriz = criaMatriz(4)
	printMatriz(matriz)
	
	
	if modo=='multiprocessing': # Executar processos concorrentes
		
		fila = Queue() # Fila com os valores de retorno
		# Cria processos-flihos e os add na lista
		n = len(matriz) # qnt de processos 
		## Criar processos para cada rotina
		processos = [ Process(name='worker{}'.format(i),target=pRoutine,args=(matriz[i],fila)) for i in range(n)]
		
		# Inicia a execução concorrente
		for p in processos:
			p.start()
		
		# Espera o término dos processos-filhos
		for p in processos:
			p.join()

		# Cont
		for i in range(n):
			contaPrimos += fila.get()
		
		print('qnt. de num primos encontrados: {}'.format(contaPrimos))
		
		'''
		
		for i in range(len(matriz)):
			linha = matriz[i]
			fila = Queue() # Fila com os valores de retorno
			# Criando processo-filho
			p = Process(name='worker{}'.format(i),target=pRoutine,args=(linha,fila))
			processos.append(p)
			p.start() # Permite a execução do processo-filho

		#print('{} processos criados.'.format(len(processos)))
		'''
		'''
		for proc in processos:
			proc.join()
			contaPrimos += fila.get()
			processos.remove(proc)
		'''
		'''
		for i in range(len(processos)):
			p = processos[i]
			p.join()
			processos.remove(p)
			contaPrimos += fila.get()
		'''
	elif modo=='threading':
		# Executar threads
		print('criando threads...')

	## Cada rotina verificará se um elemento da matriz é num primo
	
	## Retorna a qnt. de primos na matriz
