

# #condicionales
# #uso de if
# x=1000
# y=200
# if x>y:
#     ("x es mayor que y")

# a=20

# b=20
# if a==b:
#      ("a es igual a b")

# print(a==b) #True
# if a<b:
#     print("a es menor que b")
# else:
#     print("a es mayor que b")
# #uso de if-elif-else
# if x<y: 
#     print("x es menor que y")
# elif x==y:
#     print("x es igual a y")
# elif 2*x==y:
#     print("y es el doble de x")
# else:
#     print("x es mayor que y")
# #1.1.4 if anidados 
# a='azul'
# b='rojo'
# # if a=='azul':
# #     if b=='rojo':
# #         print("si mezclas los colores tienen purpura")
    
# if a=="azul" and b=="rojo":
#     print("si mezclas los colores tienes purpura")



'''bucles'''
universidades='Univalle'
# uso de FOR

for letra in universidades:
    print(letra)

mi_lista=[]
for numero in range(1,10):
    mi_lista.append(numero)
    print(mi_lista)
# uso de while

j=10
while j<10:
    print(j)
    j=j+1

#uso de switch (Match Case)
x=50

match x:
    case 20: 
        print("x es 20")
    case 10: 
        print("x es 10")
    case 8:
        print("x es 8")
    case _:
        print(("caso por defecto x es este valor {x} "))

            
