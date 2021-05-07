# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio


nmr1 = int(input())
nmr2 = int(input())
nmr3 = int(input())



nmr1f = nmr1 % 2
nmr2f = nmr2 % 2
nmr3f = nmr3 % 2



print (nmr1f)
print (nmr2f)
print (nmr3f)



if nmr1f == 1:
    print ("El primer numero es impar")
else:
    print ("El primer numero es par")

if nmr2f == 1:
    print ("El segundo numero es impar")
else:
    print ("El segundo numero es par")

if nmr3f == 1:
    print ("El tercer numero es impar")
else:
    print ("El tercer numero es par")


