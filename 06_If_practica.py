
edad = int(input("Anota tu edad: "))
mensaje = None
if 0 <= edad < 10:
    mensaje = "La infancia es increible..."
elif 10 <= edad < 20:
    mensaje = "Muchos cambios, mucho estudio..."
elif 20 <= edad < 30:
    mensaje = "Amor y mucho trabajo..."
elif 30 <= edad < 40:
    mensaje = "Etapa de hacer muchas cosas..."
else:
    mensaje = "Edad no encontrada, estás cañon"
print(f"Tienes {edad} años de edad y ", mensaje)