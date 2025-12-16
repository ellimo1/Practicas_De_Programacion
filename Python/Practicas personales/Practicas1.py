#Esta es una serie de 10 ejercicios básicos de Python centrados en strings y tipos de datos primitivos (números, booleanos, cadenas).

#1.- Invertir una cadena
#Crear un programa que pida al usuario una palabra y muestre esa palabra invertida, ejemplo: "python" -> "nohtyp"
"""print("Hola, soy un inversor de palabras.")
palabra=input("Escribe una palabra para que la invierta: ")
print(f"Su palabra invertida es: {palabra[::-1]}")"""


#2.- Contar vocales
#Pide al usuario una frase y cuenta cuantas vocales contiene (sin importar mayusculas o minusculas)
"""print("Hola, soy un contador de vocales.")
palabra=input("Escribe la frase: ").lower()
conteo_de_a=palabra.count("a")
conteo_de_e=palabra.count("e")
conteo_de_i=palabra.count("i")
conteo_de_o=palabra.count("o")
conteo_de_u=palabra.count("u")
print(f"Tu palabra tiene un total de {conteo_de_a+conteo_de_e+conteo_de_i+conteo_de_o+conteo_de_u} vocales.")"""

#3.- Primera y ultima letra
#Solicita una palabra y muestra su primera y ultima letra.
"""print("Hola, yo cuento la primera y ultima letra de tu palabra")
palabra=input("Escribe una palabra: ")
print(f"La primera letra de tu palabra es {palabra[0]} y la ultima es {palabra[-1]}")"""

#4.- Reemplazo de caracteres
#Pide al usuario una oracion y reemplaza todas las letras "a" por "@"
"""print("Yo cambio todas las\"a\" de tus oraciones por \"@\"")
palabra=input("Dame una oracion: ")
cambio=palabra.replace("a","@")
print(cambio)"""

#5.- Verificar el tipo de dato.
#Declara diferentes variables y muestra en pantalla su tipo de dato
#Este es facil#
"""print(type(1))
print(type(1.1))
print(type("Manzana"))
print(type(5>12))"""

#6.- Concatenar nombre y edad
#Solicita el nombre y la edad del usuario y muestra un mensaje
"""print("Hola, yo te digo tu nombre y edad.")
nombre=input("Dime tu nombre: ")
edad=input("Dime tu edad: ")
print(f"Te llamas {nombre}, y tienes {edad} anios de edad.")"""

#7.- Mayusculas y minusculas
#Pide una cadena (alguna palabra u oracion) y muestrala: En mayusculas, en minusculas, con la primera letra en mayuscula.
"""print("Hola, yo convierto tus cadeas en mayusculas, minusculas y con primera letra en mayuscula.")
palabra=input("Dime algo: ")
print(f"\"{palabra.upper()}\", \"{palabra.lower()}\", \"{palabra.capitalize()}\"")"""

#8.- Contar caracteres sin espacios.
#Solicita una frase y muestra cuantos caracteres tien sin contar los espacios.
"""print("Hola, yo cuento los caracteres de tu oracion o frase sin contar los espacios.")
frase=input("Dime algo por favor: ")
print(f"Tu frase tiene un total de {len(frase.replace(" ",""))} caracteres.")"""

#9.- Numero par o impar?
#Pide un numero y muestra si es par o impar usando el operador %
"""print("Hola, yo te digo si tu numero es par o impar.")
tu_numero=float(input("Dame un numero: "))
if tu_numero%2==0:
    print("Tu numero es par.")
else:
    print("Tu numero es impar.")"""

#10.- Convertir tipos de datos.
#Pide un numero decimal y: Conviertelo a entero, a string, muestra ambos resultados
"""print("Hola, yo convierto tu numero decimal a entero y a string.")
tu_decimal=float(input("Dame un numero decimal: "))
nuevo_entero=int(tu_decimal)
nuevo_string=str(tu_decimal)
print(f"Tu decimal: {tu_decimal} --> Entero: {nuevo_entero}, String: \"{nuevo_string}\"")"""
