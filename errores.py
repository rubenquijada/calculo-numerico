#!/usr/bin/env pyrhon3

def error_absoluto(valor_real,valor_aprox):
    
    return abs(valor_real-valor_aprox)
    #para calcular el error absoluto se hace una resta
    #de un valor real y un valor aproximado que devuelve el valor absoluto


def error_relativo(error_absoluto, valor_real):
    
    return abs(error_absoluto/valor_real)
    #se calcula el error relativo con una divison entre el error absoluto
    #y el valor real dando el valor absoluto de la operacion


if __name__=="__main__":

    #caso 1

    valor_real = 5
    valor_aproximado = 4 
    #aqui se ingresan los valores real y aproximado para la operacion

    error_abs = error_absoluto(valor_real ,valor_aproximado)
    error_rela = error_relativo(error_abs ,valor_real)
    #se hacen los calculos en los modulos y se retornan para ser usados en print

    print(f"Error absoluto caso 1: {error_abs}")
    print(f"Error relativo caso 1: {error_rela}")

    #caso 2

    valor_real = 20000
    valor_aproximado = 19999
    #aqui se ingresan los valores para la operacion

    error_abs = error_absoluto(valor_real,valor_aproximado)
    error_rela = error_relativo(error_abs,valor_real)
    #procede a hacerse el calculo del segundo caso para mostrarse en pantalla

    print(f"Error absoluto caso 2: {error_abs}")
    print(f"Error relativo caso 2: {error_rela}")

