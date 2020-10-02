#!/usr/bin/env python
# coding: utf-8

from process import * # src process.py
from util import * # src util.py
from time import process_time_ns

modo = 'multiprocessing' # 'multiprocessing' ou 'threading'
processos = [] # Fila que guarda processos em execução
matriz = []
contaPrimos = 0

if __name__ == '__main__':
	
	## Criar matriz de num aleatorios

	matriz = criaMatriz(100)
	#printMatriz(matriz)
	#print('Matriz gerada.')

  matriz = criaMatriz(4)
	printMatriz(matriz)
	
	if modo=='multiprocessing': # Executar processos concorrentes
		
		fila = Queue() # Fila com os valores de retorno
		# Cria processos-flihos e os add na lista
		n = len(matriz) # qnt de processos 
		## Criar processos para cada rotina
		processos = [ Process(name='worker{}'.format(i),target=pRoutine,args=(matriz[i],fila)) for i in range(n)]
		
		pTempo = process_time_ns()
		print('Tempo inicial da CPU (ns): {}'.format(pTempo))

		# Inicia a execução concorrente
		for p in processos:
			p.start()
		
		# Espera o término dos processos-filhos
		for p in processos:
			p.join()
      
		fim = process_time_ns()

		# ContaPrimos
		for i in range(n):
			contaPrimos += fila.get()
		# Tempo final gasto pela CPU (não é tempo de relógio, considera apenas tempo em execução)
		print('Tempo final da CPU: {}'.format(pTempo))
		print('Intervalo de execução {} ns.'.format(fim - pTempo))
		print('{} num primos encontrados.'.format(contaPrimos))
		
	elif modo=='threading': # # Executar threads

		print('criando threads...')

	## Cada rotina verificará se um elemento da matriz é num primo
	
	## Retorna a qnt. de primos na matriz
