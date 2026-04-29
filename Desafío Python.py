#Ariel Constante
#29 04 2026
#Desafío 1
#%%
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
puntaje = float(input("Ingrese su puntaje: "))
asistencia = float(input("Ingrese su asistencia: "))
codigo_invitacion = str(input("Ingrese el código de invitación: "))
Mensaje_adicional = str("nada")
print("Participante: " + nombre.upper())
nombre = nombre.replace(" ", "")
print("Longitud del nombre: " + str(len(nombre)))
promedio = float((puntaje + asistencia) / 2)
print("Promedio de puntaje y asistencia: " + str(promedio))
if edad >= 14:
    if promedio >= 80:
        if codigo_invitacion == "PYTHON2026":
            print("Acceso VIP")
        else:
            print("Acceso regular")
    elif promedio >= 60 and promedio <= 79:
        print("Acceso con observación")
    else:
        print("No puede ingresar por bajo rendimiento")
else: 
    if codigo_invitacion == "PYTHON2026":
        print("Acceso especial con acompañante")
    else:
        print("No cumple la edad mínima")
if puntaje >= 90 and asistencia >= 90:
    Mensaje_adicional = "Candidato destacado"
elif puntaje < 50 or asistencia < 50:
    Mensaje_adicional = "Requiere refuerzo previo"
print("Mensaje adicional: " + Mensaje_adicional)
# %%

