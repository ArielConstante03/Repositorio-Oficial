#Ariel Constante
#22 04 2026
#Actividad 1
a = int(input("Ingrese un número: "))
if a > 0 and a % 2 == 0:
    print('A is a positive even number')  # A is a positive even number
elif a < 0 and a % 2 == 0:
    print('A is a negative even number')  # A is a negative even number
elif a > 0 and a % 2 != 0:
    print('A is a positive odd number')  # A is a positive odd number
elif a < 0 and a % 2 != 0:
    print('A is a negative odd number')  # A is a negative odd number
else:
    print('A is zero')  # A is zero

# %%
#Mi versión
a = int(input("Ingrese un número: "))
if a > 0:
    if a % 2 == 0:
        print('A is a positive even number')  # A is a positive even number
    else:
        print('A is a positive odd number')  # A is a positive odd number
        if a < 0:
            if a % 2 == 0:
                print('A is a negative even number')  # A is a negative even number
            else:
                print('A is a negative odd number')  # A is a negative odd number
else:
    print('A is zero')  # A is zero
# %%
