#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Queue, current_process
import os
import globals # src globals.py
from util import * # src util.py

# Rotina que implementa contagem de primos
def pRoutine(fila,index):
	mat = globals.matriz
	lista = mat[index]
	fila.put(countPrime(lista))
	pass

def soma(fila,n):
	counter = 0
	for i in range(n):
		counter += fila.get()
	return counter