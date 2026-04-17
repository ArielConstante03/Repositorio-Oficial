""" Ariel Constante
    08 04 2026
    Actividad 2 """
#Ariel Constante
# 08 04 2026
#Actividad 2
    #Ejercicio 1
# %%
first_name, last_name, country, age, is_married, is_true, light_on = "Ariel", "Constante", "Ecuador", 17, False, False, True
print(first_name, last_name, country, age, is_married, is_true, light_on)
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)
print("Married:", is_married)
print("Is True:", is_true)
print("Light On:", light_on)
# %%
first_name, last_name, country, age, is_married, is_true, light_on = "Ariel", "Constante", "Ecuador", 17, False, False, True
print(f'First Name: {first_name}')
print(f'Last Name: {last_name}')
print(f'Country: {country}')
print(f'Age: {age}')
print(f'Married: {is_married}')
print(f'Is True: {is_true}')
print(f'Light On: {light_on}')
# Varias variables en una sola línea
# %%
a, b, c = 1, 2, 3

# Nivel 2

# 1. Tipos de datos
# %%
print(type(first_name))
print(type(last_name))
print(type(first_name))
print(type(country))
print(type(country))
print(type(age))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(light_on))

# 2. Longitud del nombre
# %%
print(len(first_name))

# 3. Comparación de longitudes
# %%
print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))
print(len(first_name) == len(last_name))

# 4. Números
# %%
numeroUno = 5
numeroDos = 4

# 5-11 Operaciones
total = numeroUno + numeroDos
diferencia = numeroUno - numeroDos
producto = numeroUno * numeroDos
division = numeroUno / numeroDos
residuo = numeroDos % numeroUno
potencia = numeroUno ** numeroDos
divisionEntera = numeroUno // numeroDos

print(total, diferencia, producto, division, residuo, potencia, divisionEntera)

# 12-14 Círculo
# %%
radio = 30
pi = 3.1416

areaCirculo = pi * radio ** 2
circunferenciaCirculo = 2 * pi * radio

print(areaCirculo)
print(circunferenciaCirculo)

# 15. Área con input
radioUsuario = float(input("Ingrese el radio: "))
areaUsuario = pi * radioUsuario ** 2
print("Área:", areaUsuario)

# 16. Datos del usuario
nombreUsuario = input("Nombre: ")
apellidoUsuario = input("Apellido: ")
paisUsuario = input("País: ")
edadUsuario = input("Edad: ")

print(nombreUsuario, apellidoUsuario, paisUsuario, edadUsuario)

# 17. Palabras reservadas
help('keywords')
# %%
