from multiprocessing import Process, Queue
import os
from util import *

## Info do processo
def pPrintInfo():
	print('\n----------------------')
	print('nome:{}\tprocesso-pai:{}\tid do processo:{}'.format(__name__,os.getppid(),os.getpid()))
	print('----------------------\n')
	pass

# Rotina que implementa contagem de primos
def pRoutine(lista,queue):
	pPrintInfo()
	queue.put(countPrime(lista))
	pass
