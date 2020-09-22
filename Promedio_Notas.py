#Escribe el código que lea las cuatro notas de un estudiante
# (Cada nota en la escala entre 1 y 5) e imprima el promedio de las mismas.

def reto1():
    n1 = float(input("Ingrese la nota 1: "))
    n2 = float(input("Ingrese la nota 2: "))
    n3 = float(input("Ingrese la nota 3: "))
    
    resultado =(n1+n2+n3)/3
    # Escribe tu código aquí. Manten la identación!!
    
    return("El promedio de las notas es: ",resultado) # Reemplaza 0 por la variable que tiene el resultado

reto1()
