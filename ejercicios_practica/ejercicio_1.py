# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

#  ------------------------
#  |      ACA EMPIEZA     |
#  ------------------------


# Calcula cual es mayor
if numero_1>numero_2:
    print("Es mayor el", numero_1)

else: print("Es mayor el", numero_2)




# Calcula positividad/negatividad/o si es cero y ademas si es 100>x>0
if numero_1 > 0:
    print ((numero_1), "es positivo")
    if 100>numero_1>0:
        print ("Es menor que 100 y mayor 0")
    else:
        print ("No es menor que 100 y mayor 0")
elif numero_1 == 0:
    print ((numero_1), "es cero")

else: print ((numero_1),"es negativo")




# Calcula si numero_1 es menor a 10 o el numero_2 es mayor a -2
if numero_1 < 10 or numero_2 > (-2):
    print("Cumple la condicion pedida")
else:
    print("No cumple la condicion pedida")

