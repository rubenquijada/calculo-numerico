#!/usr/bin/env python3

def Valor_intermedio(f,a,b):
	return f(a)*f(b)<0


if __name__ == '__main__':
	f= lambda x :x**2-4
	a=0
	b=5
	print(Valor_intermedio(f,a,b))