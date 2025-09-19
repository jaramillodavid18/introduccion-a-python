'''
Escriba un programa que capture del usuario dos
valores a y b en dos inputs sucesivos. Pida al
usuario desde la función input que los valores a
ingresar deben contener al menos un número
decimal. Al ejecutar, el programa debe realizar la
multiplicación entre los dos valores y entregar la
respuesta en un formatted string que contenga
una variable llamada resultado y el texto de su
preferencia.
'''


# instrucción al usuario para poder capturar los valores
a = float(input("Ingrese el primer número (debe contener al menos un número decimal): "))
b = float(input("Ingrese el segundo número (debe contener al menos un numero decimal): "))

# Operación
resultado = a * b

# Mostrar el resultado en un formato string
print(f"El resultado de la multiplicación es: {resultado}")

# Ejercicio 2.23
# Uso de items()
print("=== Ejercicio 2.23 ===")
print("Resultado de calificaciones.items():", calificaciones.items())
print("Tipo de dato devuelto:", type(calificaciones.items()))
print("Nota: items() devuelve un objeto dict_items, similar a una lista de tuplas.")
print("\n")

# Ejercicio 2.24
# Usar update() para cambiar la nota de Liliana
print("=== Ejercicio 2.24 ===")
calificaciones.update({"Liliana": 4.7})
print("Diccionario después de update():", calificaciones)
