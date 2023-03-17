#!/usr/bin/env python3

def biseccion(f, a, b, tol):
    """
    Esta función aproxima la solución de la ecuación f(x) = 0 en el intervalo [a,b]
    utilizando el método de bisección con una tolerancia tol.
    """
    if f(a) * f(b) >= 0:
        print("La función no cambia de signo en el intervalo dado.")
        return None
    
    c = a
    while (b-a)/2 > tol:
        c = (a+b)/2
        if f(c) == 0.0:
            break
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    print("La solución aproximada es:", c)
    return c

f = lambda x: x**2 - 2
a = 0
b = 3
tol = 0.0001
solucion = biseccion(f, a, b, tol)