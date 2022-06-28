

import funciones_practica
funciones_practica.menu()
funciones_practica.validando_opciones()

while True:
    decision = input ("¿Desea realizar otra operacion (S=Si N=No): ")
    funciones_practica.menu()
    funciones_practica.validando_opciones()

    if decision == "n" or decision == "N":
        break
print("Fin de la calculadora")