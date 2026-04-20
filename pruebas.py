nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país de residencia: ")
ancho = float(input("Ingrese el ancho de su pared: "))
largo = float(input("Ingrese el largo de su pared: "))
precio = float(input("Ingrese el precio por metro cuadrado de pintura: "))
area = ancho * largo
costo = area * precio
nombre_completo = nombre + " " + apellido
print(f"{nombre_completo} {pais} {area} {costo}")
print(nombre_completo.upper())
print(len(nombre_completo))
print("a" in nombre_completo)
print(costo > 100)