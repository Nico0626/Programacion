Algoritmo sin_titulo
	Definir numero, multiplicador, resultado Como Entero
	
    Escribir "Ingrese un n�mero entre 1 y 10:"
    Leer numero
	
    Si numero < 1 O numero > 10 Entonces
        Escribir "El n�mero ingresado no est� en el rango v�lido."
    Sino
        multiplicador <- 1
        Mientras multiplicador <= 10 Hacer
            resultado <- numero * multiplicador
            Escribir numero, "x", multiplicador, "=", resultado
            multiplicador <- multiplicador + 1
        Fin Mientras
    Fin Si

FinAlgoritmo
