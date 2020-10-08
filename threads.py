#!/usr/bin/env python
# coding: utf-8

from threading import Thread
#import os
import globals # src globals.py
from util import * # src

# Rotina que implementa contagem de primos
def tRoutine(index):
	l = globals.lock
	m = globals.matriz
	count = countPrime(m[index])
	l.acquire() 
	globals.contaPrimos += count
	l.release()
	pass
