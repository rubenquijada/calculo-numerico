#!/usr/bin/env pyrhon3

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Implementación del método de Newton-Raphson para encontrar la raíz de una función f.
    
    :param f: función de la que se desea encontrar la raíz
    :param df: derivada de la función f
    :param x0: valor inicial de x
    :param tol: tolerancia del error relativo
    :param max_iter: número máximo de iteraciones permitidas
    :return: valor aproximado de la raíz de f
    """
    i = 0
    while i < max_iter:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol * abs(x1):
            return x1
        x0 = x1
        i += 1
    raise ValueError("El método de Newton-Raphson no converge después de %d iteraciones." % max_iter)

def f(x):
    return x**2 - 2

def df(x):
    return 2*x

x0 = 1.5  # valor inicial de x
raiz = newton_raphson(f, df, x0)  # encontrar la raíz de f
print(raiz)  # imprimir el resultado