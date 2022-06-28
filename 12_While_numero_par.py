cont = 0
val = int(input("ingrese un valor, 0 finaliza"))
while val !=0:
    if val % 2 == 0:
        cont = cont + 1
    val = int(input("ingrese un valor, 0 finaliza"))
print("la cantidad de valores pares es", cont)

