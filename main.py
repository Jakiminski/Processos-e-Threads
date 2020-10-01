#!/usr/bin/env python
# coding: utf-8

from process import * # src process.py
from util import * # src util.py

modo = 'multiprocessing' # 'multiprocessing' ou 'threading'
pQueue = [] # Fila que guarda processos em execução
matriz = []
contaPrimos = 0

if __name__ == '__main__':
	
	## Criar matriz de num aleatorios
	matriz = criaMatriz(4)
	printMatriz(matriz)
	
	## Criar processos (alternativamente, threads) para cada rotina
	if modo=='multiprocessing':
		# Executar processos concorrentes
		print('Criando processos-filhos...')

		for linha in matriz:
			queue = Queue() # Lista com os valores de retorno
			p = Process(target=pRoutine,args=(linha,queue))
			pQueue.append(p)
			p.start()

		# print('{} processos criados.'.format(len(pQueue)))
		
		for proc in pQueue:
			proc.join()
			contaPrimos += queue.get()
			pQueue.remove(proc)
			

	elif modo=='threading':
		# Executar threads
		print('criando threads...')

	## Cada rotina verificará se um elemento da matriz é num primo
	
	## Retorna a qnt. de primos na matriz
