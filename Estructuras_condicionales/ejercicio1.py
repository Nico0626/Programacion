unidadesDeLeche=int(input("Ingrese la cantidad de leches que lleva: "))
esJubilado=input("¿Es jubilado?si/no: ")
if esJubilado!="si" or "no":
    print("error")
else:
    montoParcial = unidadesDeLeche * 1000
    print(f"unidadesDeLeche {unidadesDeLeche}, {esJubilado} es Jubilado")
    descuento=0

    if(unidadesDeLeche <=12 and not esJubilado):
        print("unidadesDeLeche <=12 and not esJubilado")
        montoAPagar = montoParcial        
    elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubilado):
        print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and not esJubilado")
        montoAPagar = montoParcial * 0.9
        descuento=10
    elif(unidadesDeLeche > 24 and not esJubilado):
        print("unidadesDeLeche > 24 and not esJubilado")
        montoAPagar = montoParcial * 0.85
        descuento=15
    if(unidadesDeLeche <=12 and esJubilado):
        print("unidadesDeLeche <=12 and esJubilado")
        montoAPagar = montoParcial * 0.9
        descuento=10
    elif((unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubilado):
        print("(unidadesDeLeche >12 and unidadesDeLeche <= 24) and esJubilado")
        montoAPagar = montoParcial * 0.8
        descuento=20
    elif(unidadesDeLeche > 24 and esJubilado):
        print("unidadesDeLeche > 24 and esJubilado")
        montoAPagar = montoParcial * 0.75
        descuento=25

    print(f"El monto sin descuento es: {montoParcial}, el descuento es del {descuento}% y el monto total a pagar es: {montoAPagar}")
    