
nombre_alumno = input("Anota el nombre: ")
calificacion = int(input("Anota tu calificación correctamente: "))
mensaje = None
if 0<= calificacion <=69:
    mensaje = "Insuficiente (N/A)"
elif 70 <= calificacion <= 74:
    mensaje = "Suficiente"
elif 75 <= calificacion <= 84:
    mensaje = "Bueno"
elif 85 <= calificacion <= 94:
    mensaje = "Notable"
elif 95 <= calificacion <= 100:
    mensaje = "Excelente"
else:
    mensaje = "Calificacion no permitida"
print(f"Tienes {calificacion} de calificacion, significa ", mensaje)