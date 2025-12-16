#1.- Suma de elementos en una lista
#Crea una lista con numeros definidos por el usuario y muestra la suma total de sus elementos
"""print("Hola bienvenido, necesitamos crear una lista de numeros!")
cantidad_numeros=int(input("Que cantidad de numeros quieres que tenga tu lista?: "))
lista_numeros=[]

while len(lista_numeros)<cantidad_numeros:
    numeros=int(input("Dame un numero: "))
    lista_numeros.append(numeros)

print(f"La suma de tu lista hace un total de {sum(lista_numeros)}")"""

#2.- Numero mayor y menor en una lista
#Pide una lista de numeros y muestra cual es el mayor y cual es el menor.
"""print("Hola bienvenido, necesitamos crear una lista de numeros!")
cantidad_numeros=int(input("Que cantidad de numeros quieres que tenga tu lista?: "))
lista_numeros=[]

while len(lista_numeros)<cantidad_numeros:
    numeros=int(input("Dame un numero: "))
    lista_numeros.append(numeros)

print(f"De tu lista, el numero mayor es el {max(lista_numeros)} y el numero menor es el {min(lista_numeros)}")"""

#3.- Eliminar duplicados
#Crea una lista con elementos repetidos y 
#genera una nueva lista sin duplicados (usa set() o logica propia)
"""lista_compras=["-Leche","-Platanos","-Cafe","-Platanos","-Sal","-Atun","Cafe","-Galletas","-Galletas"]
print(f"Hoy me toca hacer las compras.\nPor las prisas he repetido algunos productos de la lista!.\n\n>>LISTA DE COMPRAS<<\n{lista_compras}")
print(f"\n\nSabes que? La volvere a hacer.\n>>LISTA DE COMPRAS NUEVA<<\n{set(lista_compras)} ")"""

#4.- Contar apariciones
#Pide una lista de palabras y una palabra a buscar; muestra cuantas veces aparece.
"""print("Hola, creemos una lista de palabras!")
numero_elementos_lista=int(input("Cuantos elementos quieres que contenga tu lista?: "))
lista=[]

while len(lista)!=numero_elementos_lista:
    elementos_lista=str(input("Dame palabras hasta completar la cantidad, no importa si se repiten: "))
    lista.append(elementos_lista)

buscar_palabra=str(input("Busquemos las palabras que se repiten en tu lista, cual quieres buscar?: "))
if buscar_palabra in lista:
    print(f"Esta palabra se repite {lista.count(buscar_palabra)} veces.")

else:
    print(f"No existe.")"""

#5.- Lista invertida.
#Pide una lista de elementos y muestrala al reves (usa reversed() o slicing[::-1])
"""print("Hola, creemos una lista de palabras!")
numero_elementos_lista=int(input("Cuantos elementos quieres que contenga tu lista?: "))
lista=[]

while len(lista)!=numero_elementos_lista:
    elementos_lista=str(input("Dame palabras hasta completar la cantidad, no importa si se repiten: "))
    lista.append(elementos_lista)

print(f"Esta es tu lista de palabras: {lista}")
print(f"Esta es tu lista de palabras de reversa: {lista[::-1]}")"""

#6.- Promedio con funcion
#Crea una funcion promedio(lista) que reciba una lsita de numeros y devuelva el promedio.
"""def promedio(lista):
    lista_vacia=[]
    cantidad_calificaciones=int(input("Cuantos numeros quieres que se le saque promedio?: "))

    while len(lista_vacia)!=cantidad_calificaciones:
        lista_promedios=float(input("Dame un numero: "))
        lista_vacia.append(lista_promedios)
    total=sum(lista_vacia)/len(lista_vacia)
    return total
print(f"Tu lista hace un promedio de: {round(promedio(promedio),2)}")"""

#7.- Factorial con funcion
#Define una funcion factorial(n) que calcule el factorial de un numero usando un bucle
"""import math
numero=int(input("Dame un numero y yo te doy su factorial: "))
factorial=math.factorial(numero)
print(f"El factorial de {numero} es {factorial}")"""

"""def factorial(n):
    if n<0:
        return "No se define factorial para numeros negativos"
    elif n==0:
        return 1
    else:
        resultado=1
        for i in range(1,n+1):
            resultado*=i
        return resultado
numero=int(input("Dame un numero y yo te doy su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}")"""

#8.- Filtrar numeros pares
#Crea una funcion que reciba una lista de numeros y devuelva una nueva lista solo con los pares
"""def pares(lista):
    lista_nueva=[]
    for n in lista:
        if n%2==0:
            lista_nueva.append(n)
    return lista_nueva
        
lista=[]
cantidad_numeros=int(input("Cuantos numeros quieres que tenga tu lista?: "))

while len(lista)!=cantidad_numeros:
    numeros=float(input("Dame numeros: "))
    lista.append(numeros)
print(f"Aqui te doy una lista con los numeros pares que ingresaste: {pares(lista)}")"""

#9.- Convertir grados Celsius a Fahrenheit
#Crea una funcion celsius_a_fahrenheit(c) que convierta temperaturas.
#Luego, pide al usuario una lista de valores en Celsius y muestra los equivalentes en Fahrenheit
"""def celsius_a_fahrenheit(lista_c):
    lista_f=[]
    for n in lista_c:
        if n in lista_c:
            lista_f.append(n*1.8+32)
    return lista_f

lista_c=[]
cantdad_temperaturas=int(input("Cuantas temperaturas quieres que se conviertan Farenheit?: "))
if cantdad_temperaturas>0:
    pass
else:
    print("Solo numeros positivos")
        
while len(lista_c)!=cantdad_temperaturas:
    c=float(input("Dame temperaturas, las convertire a fahrenheit: "))
    lista_c.append(c)
        
print(f"Tu lista con las temperaturas en Celsius: {lista_c}")
print(f"Tu lista con las temperaturas en fahrenheit: {celsius_a_fahrenheit(lista_c)}")"""

#10.- Diccionario de contactos
#Crea un diccionario donde las claves sean nombres y los valores sean numeros de telefono.
#Permite al usuario agregar, buscar y eliminar contactos mediante un menu simple

"""Directorio_de_contactos={'Juan':12345678,'Diego':234567890,'Ricardo':345678901}

print("Bienvenido a tu directorio de contactos :).")
while True:
    opcion=int(input("\nQue quieres hacer?\n1. Ver los contactos actuales\n2. Agregar contactos.\n3. Buscar contactos.\n4. Eliminar contactos.\n5. Salir del menu\n\nTu eleccion: "))

    if opcion==1:
        print("\n1. Ver los contactos actuales")
        print(f"{Directorio_de_contactos}")

    elif opcion==2:
        print("\n2. Agregar contacto")
        nombre=str(input("Dame un nombre: "))
        numero=int(input("Dame un numero: "))

        Directorio_de_contactos.update({nombre:numero})
        print(f"Lista de contactos actualizada: {Directorio_de_contactos}")

    elif opcion==3:
        print("\n3. Buscar contactos")
        contacto=str(input("Ingresa el nombre del contacto a buscar: "))
        numero_contacto=Directorio_de_contactos.get(contacto)

        if contacto in Directorio_de_contactos.keys():
            print(f"\nContacto encontrado. {contacto} de numero: {numero_contacto}")

        elif contacto is not Directorio_de_contactos.keys():
            print(f"\nEste contacto no existe")

    elif opcion==4:
        print("\n4. Eliminar contactos")
        eliminar_contacto=str(input("Ingresa el nombre del contacto a eliminar: "))

        if eliminar_contacto in Directorio_de_contactos.keys():
            del Directorio_de_contactos[eliminar_contacto]
            print("\nEl contacto fue eliminado.")
            print(f"\nLista de contactos actual: {Directorio_de_contactos}")

        elif eliminar_contacto is not Directorio_de_contactos.keys():
            print("\nEste contacto no existe")
        
    elif opcion==5:
        print("\n5. Salir")
        print("Hasta luego!\n")
        break """