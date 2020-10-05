#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Queue, current_process
import os
from util import *

## Info do processo
def pPrintInfo(message):
	#print('\n----------------------')
	name = current_process().name
	pid = os.getpid()
	#print('nome:{}\tprocesso-pai:{}\tid do processo:{}'.format(__name__,os.getppid(),os.getpid()))
	print('{} (PID {})\t {}'.format(name,pid,message))
	#print('----------------------\n')
	pass

# Rotina que implementa contagem de primos
def pRoutine(lista,fila):
	#pPrintInfo('antes')
	fila.put(countPrime(lista))
	#pPrintInfo('depois')
	pass
