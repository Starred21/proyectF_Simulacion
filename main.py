# Este es un programa para la cracion de numeros 
# aleatorios para la materia de simulacion de sistemas.

import math


def menu (cantidad,aux):
    opc = int(input("Ingrese el numero del metodo que de desee usar"))
    if (opc==1) :
        print("metodo de la transformada inversa")
        resultado = cantidad + aux
        return(resultado)
    elif(opc==2):
        print("metodo de ###")
    else :
        return()

# pantalla principal----------------------------------------------------------------------------------------

print("bienvenido al sistema de cracion de numéros aleatorios")
ini = int(input('ingrese clave de ingreso:'))

if (ini == 1234): 
    print("bienvenido al sistema de cracion de numéros aleatorios")
    print("seleccione una el metodo con el que desea crear numeros Aleatorios")
    cantidad = int(input("ingrese el numero de cantidad de numeros aleatorios que desee generar"))
    aux = int(input("aux"))
    numeros = menu(cantidad,aux)
    print(numeros) 
else :
    print("la clave es incorrecta")


