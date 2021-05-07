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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio



temp1 = int(input())
temp2 = int(input())
temp3 = int(input())



# 1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
if temp1 > temp2 and temp1 > temp3:
    print ("La primera temperatura es mayor")
elif temp2 > temp1 and temp2 > temp3:
    print ("La segunda temperatura es mayor")
else:
    print ("La tercera temperatura es mayor")




# 2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
if temp1 < temp2 and temp1 < temp3:
    print ("La primera temperatura es menor")
elif temp2 < temp1 and temp2 < temp3:
    print ("La segunda temperatura es menor")
else:
    print ("La tercera temperatura es menor")



# 3 - ¿Cuál es el promedio de las temperaturas ingresadas?
tempprom = (temp1 + temp2 + temp3)/3
print (tempprom)
