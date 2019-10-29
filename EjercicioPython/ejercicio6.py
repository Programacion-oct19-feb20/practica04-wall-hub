"""
    @autor: wall-hub
    nombre: ejercicio6.py
    descripción: ...
	
	Yorki Correa -- 18
	Su suma de notas es: 30
	Su promedio es: 15

"""

nombre = input("Ingrese su nombre: ")
edad   = input("Ingrese su edad: \n")
nota1  = input("Ingrese el valor de su nota 1: ")
nota2  = input("Ingrese el valor de su nota 2: ")

suma = int(nota1) + int(nota2);
promedio = suma / 2;

print("%s -- %s\nSu suma de notas es %s\nSu promedio es %s\n" 
	% (nombre, edad, suma, promedio))
