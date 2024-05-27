Algoritmo sin_titulo
	Definir numero, multiplicador, resultado Como Entero
	
    Escribir "Ingrese un número entre 1 y 10:"
    Leer numero
	
    Si numero < 1 O numero > 10 Entonces
        Escribir "El número ingresado no está en el rango válido."
    Sino
        multiplicador <- 1
        Mientras multiplicador <= 10 Hacer
            resultado <- numero * multiplicador
            Escribir numero, "x", multiplicador, "=", resultado
            multiplicador <- multiplicador + 1
        Fin Mientras
    Fin Si

FinAlgoritmo
