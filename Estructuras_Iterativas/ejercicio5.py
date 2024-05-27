numero=int(input("¿Cual tabla quiere ver? "))
multiplicador=0
resultado=0
if numero<1 or numero >10:
    print("Error valor no valido")
else:
    multiplicador=1
    while multiplicador <11:
        resultado=numero*multiplicador
        print(f"{numero}x{multiplicador}={resultado}")
        multiplicador=multiplicador+1