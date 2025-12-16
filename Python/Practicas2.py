#1.- Contar hasta un numero
#Pide al usuario un numero entero y muestra todos los numeros desde 1 hasta ese numero (usando un for)
"""print("Hola, yo cuento todos los numeros que hay hasta el numero que tu escojas.")
numero=int(input("Dame un numero: "))
for n in range(1,numero+1):
    print(n)"""

#2.- Sumar una serie de numeros
#Pide al usuario un numero n y calcula la suma de todos los numeros del 1 al n usando un bucle for.
"""print("Hola, hago la suma de todos los numeros que hay hasta el numero que escojas.")
numero=int(input("Dame un numero: "))
print(f"La suma de numeros del 1 al {numero} es: {sum(range(numero+1))}")"""

"""print("Hola, yo hago la suma de todos los numeros hasta tu numero escogido.")
numero=int(input("Dame un numero: "))
lista=[]
for n in range(numero+1):
    lista.append(n)
print(f"La suma hasta tu numero da: {sum(lista)}")"""

#3.- Tabla de multiplicar
#Solicita un numero y muestra su tabla de multiplicar del 1 al 10
"""print("Hola, yo digo la tabla de multiplicar del numero que me des.")
numero=int(input("Dame un numero: "))
print(f"La tabla del {numero}.")
for n in range(1,11):
    print(f"{numero} x {n}: {numero*n}")"""
#4.- Contar vocales en una palabra
#Pide al usuario una palabra y cuenta cuantas vocales tiene sin usar .count(), solo con un bucle for.
"""print("Hola, dame una palabra y yo contare las vocales que tenga")
palabra=str(input("Dame una palabra: "))
contador=0
vocales="aeiouAEIOU"
for letra in palabra:
    if letra in vocales:
        contador+=1
print(f"Tu palabra tiene {contador} vocales.")"""

#5.- Numeros pares e impares en un rango.
#Pide al usuario dos numeros (inicio y fin) muestras todos los numeros pares e impares entre ellos.
"""print("Hola, dame dos numeros y te dire cuantos numeros pares e impares hay entre esos dos.")
inicio=int(input("Dame un numero: "))
fin=int(input("Dame otro numero, que sea mas grande que el primero: "))
pares=[]
impares=[]

for n in range(inicio,fin+1):
    if n%2==0:
        pares.append(n)
    if n%2==1:
        impares.append(n)
print(f"Pares: {pares}")
print(f"Impares: {impares}")"""

#6.- Repetir hasta acertar
#Crea un programa que pida una contrasena hasta que el usuario escriba "python123". Usa bucle while.
"""contrasena_correcta="python123"
contrasena=input("Ingresa la contrasena correcta: ")
while contrasena_correcta!=contrasena:
    print("Contrasena incorrecta, intenta de nuevo")
    contrasena=input("Ingresa la contrasena correcta: ")
    if contrasena==contrasena_correcta:
        print("Bienvenido! :) ")
        break"""

#7.- Contador regresivo
#Pide un numero y muestra un conteo regresivo hasta 0 (usa while).
"""print("Yo hago una cuenta regresiva desde el numero que escojas.")
inicio=int(input("Dame un numero: "))
while inicio!=0:

    if inicio>0:
        print(inicio)
        inicio-=1
        
    else:
        print(inicio)
        inicio+=1"""
        
        

#8.- Promedio de notas
#Pide al usuario cuantas notas desea ingresar,, luego solicita cada nota y al final muestra el promedio.
"""print("Hola, dime cuantas notas quieres que calcule, las notas y yo te dare el promedio.")
cantidad_notas=int(input("Cuantas notas quieres calcular?: "))
lista_notas=[]

while len(lista_notas)<cantidad_notas:
    notas=int(input("Dame una nota: "))
    lista_notas.append(notas)

    if len(lista_notas)==cantidad_notas:
        print(f"Tu promedio es de: {sum(lista_notas)/cantidad_notas}")
        break"""

#9.- Deteccion de numero mayor
#Pide al usuario una cantidad n y luego ingresa n numeros. 
#El programa debe mostrar cual fue el mayor numero ingresado.
"""print("Hola, dime cuantos numeros quieres que guarde, damelos y luego te dire cual es el mayor de ellos.")
cantidad_numeros=int(input("Cuantos numeros quieres guardar?: "))
lista_numeros=[]

while len(lista_numeros)<cantidad_numeros:
    numeros=int(input("Dame un numero: "))
    lista_numeros.append(numeros)

    if len(lista_numeros)==cantidad_numeros:
        print(f"El numero mas grande que has ingresado es el {max(lista_numeros)}")
        break"""

#10.- Piramide de asteriscos
#Usa un blucle for para imprimir una piramide de altura n con el caracter *.
"""altura=int(input("Hola, ingresa una altura: "))

for n in range(1,altura+1):
    print("*"*n)"""