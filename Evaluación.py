#Evaluación 1
# ===== PARTE A =====

# 1. Análisis de datos y código
# Respuestas: 
# a.) La variable "nombre" es de tipo string, la variable "edad" es de tipo entero, la variable "promedio" es de tipo flotante y la variable "cursos" es de tipo lista.
# b.) Lo que mostrará el código al ejecutarse es:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'list'>
# c.) len(nombre) mostrará el número de caracteres que tiene la variable "nombre".

# 2. Comprensión conceptual
# Respuestas: 
# a.) La diferencia entre print() e input() es que print() se utiliza para mostrar un mensaje en la terminal, mientras que input () se utiliza para introducir un dato externo al programa.
# b.) Porque un dato ingresado con input () se considera de tipo string, lo que invalida la operación matemática.
# c.) "/" es el operador de división que puede devolver un número con decimales, "//" es el operador de la división entera que devuelve el cociente sin decimales, y "%" es el operador de módulo que devuelve el residuo de la división.
# d.) la instrucción es: 
    # import sys
    # print(sys.version)
# e.) La instrucción es: 
    # import keyword
    # print(keyword.kwlist)



# ===== PARTE B =====
# 3. Corrección de código
# %%
# Código original
ancho = input("Ingrese el ancho del terreno: ")
largo = input("Ingrese el largo del terreno: ")
precio = input("Ingrese el precio por metro cuadrado: ")
area = ancho * largo
costo = area * precio
print("Área total: " + area)
print("Costo estimado: " + costo)

# %%
# Código corregido
ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * largo
costo = area * precio
print("Área total: " + str(area))
print("Costo estimado: " + str(costo))

#Respuestas:
# a) Los datos ingresados en las variables ancho, largo y precio se consideran de tipo string por la función de input(), lo que invalida la operación matemática. Además, con la instrucción print() se intentaba unir un string con un número, lo que también genera un error.
# b) Porque al convertir los datos ingresados a tipo float, se pueden realizar operaciones matemáticas correctamente. Además, al convertir el resultado de area y costo a string, se puede mostrar el mensaje completo sin generar un error de tipo.

# %%
# 4. Construcción breve
frase = "Tecnología para todos"
print(frase.upper())
print(len(frase))
print("Python" in frase)
print(frase.replace("Tecnología", "Programación"))
print(frase.split())

