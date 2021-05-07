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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra)

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

print ("palabra 1")
palabra1 = str(input())



print ("palabra 2")
palabra2 = str(input())



print ("palabra 3")
palabra3 = str(input())





print ("operacion")
operacion = str(input())



palabras = [palabra1, palabra2, palabra3]


if operacion == "1":
    palabras.sort()
    print (palabras)
else:
    lenpal1 = int(len(palabra1))
    lenpal2 = int(len(palabra2))
    lenpal3 = int(len(palabra3))
    
    lenpals = [lenpal1, lenpal2, lenpal3]
    lenpals.sort(reverse = True)
    print (lenpals)





