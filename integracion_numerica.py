#!/usr/bin/env pyrhon3

from scipy.integrate import quad

def f(x):
    return x**2

resultado, error = quad(f, 0, 1)

print("El resultado de la integración es:", resultado)