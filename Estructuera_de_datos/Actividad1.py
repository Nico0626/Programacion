nombres=[]
for i in range(10):
    nombre=input("Ingrese el nombre: ")
    while nombre in nombres:
        print("¡El nombre ya existe! Por favor, ingresa otro.")
        nombre = input("Ingresa un nombre: ")
    nombres.append(nombre)
print(f"Los nombres ingresados son: ")
for nombre in nombres:
    print(nombre)

del nombres[2]  
del nombres[-1]  

nombres.sort()

print(nombres)

persona_uno={}
persona_uno["nombre"]=input ("Ingrese el nombre: ")
persona_uno["apellido"]=input ("Ingrese el apellido: ")
persona_uno["dni"]=input ("Ingrese el dni: ")
persona_uno["email"]=input ("Ingrese el email: ")
persona_uno["fecha_nacimiento"]=input ("Ingrese la fecha nacimiento: ")



familia = {}
for i in range(4):
    persona={}
    nombre = input("Ingrese el nombre de la persona {}: ".format(i+1))
    apellido = input("Ingrese el apellido de la persona {}: ".format(i+1))
    dni = input("Ingrese el DNI de la persona {}: ".format(i+1))
    email = input("Ingrese el email de la persona {}: ".format(i+1))
    fecha_nacimiento = input("Ingrese la fecha de nacimiento de la persona {} (DD/MM/AAAA): ".format(i+1))
    familia["persona{}".format(i+1)] = persona

print("Datos de la familia guardados en un diccionario:")
print(familia)



n = int(input("Ingrese el valor de n para los primeros números pares: "))

numeros_pares = []

i = 1
while len(numeros_pares) < n:
    if i % 2 == 0:
        numeros_pares.append(i)
    i += 1

numeros_pares_tupla = tuple(numeros_pares)

print("Los primeros {} números pares son:".format(n))
print(numeros_pares_tupla)