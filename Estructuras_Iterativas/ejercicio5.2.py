numero = int(input("¿cual tabla quiere ver? "))

if numero < 1 or numero > 10:
    print("El número ingresado no esta en el rango valido.")
else:
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")