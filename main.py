#!/usr/bin/env python
# coding: utf-8

#from globals import * # src globals.py
#from util import * # src util.py
from process import * # src process.py
from threads import * # src threads.py
from time import time

'''
Multiprocessing:  -> 
PROS: 
	1. Aproveita múltiplas CPUs e núcleos, se houverem
	2. Ótimo para aplicações CPU-bound, poucas operações de entrada e saída
CONTRAS:
	1. Maior consumo de memória, geralmente mais lento
	2. IPC (Interprocess Communication) mais complicado

Threading:  -> 
PROS:
	1. Mais rápido de criar e gerenciar, menor consumo de memória
	2. Torna as aplicações mais responsivas
	3. Ótima para aplicações I/O-bound, muitas operações de entrada e saída, ou consultas a banco de dados, por exemplo
CONTRAS:
	1. primitivas de controle (locks) para memória compartilhada 
	2. difícil de depurar, potenciais condições de corrida
	3. Apenas uma thread controla a GIL (Global Interpreter Lock)
Ou seja, nas threads para o python, as máquinas tem sempre 1 core
'''

if __name__ == '__main__':
	
	## Criar matriz de num aleatorios
	globals.init(100) # Tamanho da matriz
	#printMatriz(globals.matriz)
	#print('Matriz gerada.')
	n = len(globals.matriz) # qnt de processos 

if globals.modo=='multiprocessing' or globals.modo=='both': # Executar processos concorrentes

	print('criando processos...')
	fila = Queue() # Fila com os valores de retorno
	
	# Cria processos-flihos e os add na lista
	## Criar processos para cada rotina
	processos = [Process(name='worker{}'.format(i),target=pRoutine,args=(fila,i)) for i in range(n)]
	tempo = time()
	#print('Tempo inicial da CPU: {}'.format(tempo))

	# Inicia a execução concorrente
	for p in processos:
		p.start()
	
	# Espera o término dos processos-filhos
	for p in processos:
		p.join()
	
	globals.contaPrimos = soma(fila,n) # ContaPrimos
	print('{} num primos encontrados.'.format(globals.contaPrimos))
	fim = time()
	
	#print('Tempo final da CPU: {}'.format(tempo))
	print('Intervalo de execução {}.'.format(fim - tempo))
	
if globals.modo=='threading' or globals.modo=='both': # # Executar threads

	globals.contaPrimos = 0
	print('criando threads...')
	
	# criar threads
	threads = [Thread(name='thread {}'.format(i),target=tRoutine,args=(i,)) for i in range(n)]

	tempo = time()
	#print('Tempo inicial da CPU: {}'.format(tempo))

	# Inicia a execução das threads
	for t in threads:
		t.start()
	
	# Espera o término das threads
	for t in threads:
		t.join()

	print('{} num primos encontrados.'.format(globals.contaPrimos))
	fim = time()

	#print('Tempo final da CPU: {}'.format(tempo))
	
	print('Intervalo de execução {}.'.format(fim - tempo))

######################################################
######################################################
######################################################
######################################################
######################################################
"""
import threading

def calc_square(number):
    print('Square:' , number * number)
def calc_quad():
    print('Quad:' , number * number * number * number)
if __name__ == "__main__":
    number = 7
    thread1 = threading.Thread(target=calc_square, args=(number,))
    thread2 = threading.Thread(target=calc_quad, args=())
    # Will execute both in parallel
    thread1.start()
    thread2.start()
    # Joins threads back to the parent process, which is this
    # program
    thread1.join()
    thread2.join()

# This program reduces the time of execution by running tasks in parallel
"""