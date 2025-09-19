'''funciones

son procedimientos personalizados 
podemos describir una actividad a ejecutar
tenemos 2 consideraciones
uso
'''

#Definiciones
#uso de palabra reservada def
#nombre
#parametros 
#return
def mi_funcion():
    return True

# uso
#llamamos a la funcion entregandole datos en los argumentos
print(mi_funcion())

def mi_aleatorio():
    return random.randint(1,100)

print(mi_aleatorio())

x=90
y=100

def multiples_retornos():
    return x,y

print(multiples_retornos())