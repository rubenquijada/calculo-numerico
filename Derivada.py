#!/usr/bin/env pyrhon3

def derivada (f,h=0.01):
   def dx(x):
     return((f(x+h)-f(x)))/h
   return dx 

f=lambda x: x**2
df=derivada(f)
df(2)
print(df(2))