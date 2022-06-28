

from alumno import *

#creando objetos
persona1=persona("Nicolas","Guzman",30)
print("Me llamo", persona1.nombre)
print("Mis apellidos", persona1.apellidos)
print("Y tengo", persona1.edad,"años")
persona1.comer()
persona1.caminando()

#llamando alumno
alumno1=alumno("Miguel", "S0202201")
print(alumno1.promedio())
print(alumno1.comer())

#w=escribir
#r=leer
mi_archivo=open("Mis_notas_fundamentos.txt","w")
try:
    mi_archivo.write(f"esta es una persona {alumno1.nombre}\n")
    mi_archivo.write(f"Otra persona {persona1.nombre}")
finally:
    mi_archivo.close()

