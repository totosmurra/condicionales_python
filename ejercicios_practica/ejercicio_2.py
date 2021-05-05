# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda


#  ------------------------
#  |      ACA EMPIEZA     |
#  ------------------------



# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print ("La palabra {} es mayor alfabeticamente que la palabra {}".format(texto_1, texto_2))
else:
    print ("La palabra {} es mayor alfabeticamente que la palabra {}".format(texto_2, texto_1))




# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
lt1 = len(texto_1)

lt2 = len(texto_2)

if lt1 > lt2:
    print ("La palabra {} es mas larga que la palabra {}".format(texto_1, texto_2))
else:
    print ("La palabra {} es mas larga que la palabra {}".format(texto_2, texto_1))




# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
# (Se entiende como mayor alfabeticamente)

if texto_1[0] > texto_2[0]:
    print (texto_1, "(es mayor su primera letra que)", texto_2)
else:
    print (texto_2, "(es mayor su primera letra que)", texto_1)



# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print ("La copia es igual al original")
else:
    print ("Uy...")

if copia_texto_1 == texto_2:
    print("La copia de {} es lo mismo que {}".format(texto_1,texto_2))
else:
    print("La copia de {} no es lo mismo que {}".format(texto_1,texto_2))

