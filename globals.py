#!/usr/bin/env python
# coding: utf-8

import threading
from util import criaMatriz

def init(tam,mode='both'):
	
	global modo
	modo = mode
	
	global matriz 
	matriz = criaMatriz(tam)
	
	global lock 
	lock = threading.Lock() # Lock para as threads

	global contaPrimos
	contaPrimos = 0

	pass