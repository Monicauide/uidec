
#Aprender a montar en bicicleta

"""equilibrio = False
intentos = 0

while equilibrio == False:
    intentos += 1
    print(f"Intento {intentos}: intentando mantener equilibrio...")

    if intentos == 5:   # Supongamos que lo logró al 5to intento
        equilibrio = True

print("¡Lo lograste! Ya puedes avanzar sin caerte 🚴✨")"""








#Imprimir los números del 1 al 50
i = 1
while i <= 50:
    print(i)
    i += 1

i = 1
print (i)
i = i +1
print (i)
i = i+1
print (i)
i = i+1
print (i)
i = i+1
print (i)

#pseudocódigo suma de 5 numeros
"""Inicio
    Definir contador, numero, suma como Entero
    suma ← 0
    contador ← 1

    Mientras contador ≤ 5 Hacer
        Escribir "Ingrese un número:"
        Leer numero
        suma ← suma + numero
        contador ← contador + 1
    FinMientras

    Escribir "La suma total es: ", suma
Fin"""

"""contador = 1
suma = 0
while contador <= 5:
    numero = int(input("ingrese un numero:"))
    suma += numero
    contador +=1
print ("la suma total es:", suma)  """

"""suma = 0
contador = 1

# Bucle while que se repite 5 veces
while contador <= 5:
    numero = int(input("Ingrese un número: "))
    suma += numero
    contador += 1

# Mostrar el resultado final
print("La suma total es:", suma)



# Usando for 
for i in range(1, 6):
  print(i)

for i in range(5):
    if i == 3:
        break  # Termina el bucle cuando i es 3
    print(i)
else:
    print("Bucle finalizado sin interrupción")""" # No se ejecuta porque hubo un break


#imprime 10 numeros
"""i = 0
while i<10:
    i +=1         
    print (i)"""
    

"""contador = 1
while contador <= 10:
    print(contador)
    contador += 1"""

"""a = 0
b = 0
while b <10:
    a +=1
print(a)

a = 0
b = 0
1
2
3
4
5
6
7
"""

"""numero_ganador = 10 
numero = int(input("Adivina el numero y Gana!!! Ingresa un numero entre 1 y 100"))
while numero != numero_ganador: 

        print("Lo siento,El número ingresado no es correcto Intenta nuevamente. ") 
        numero = int(input("Ingrese otro numero: ")) 

print("Ganaste!!!") """

"""contador = 0
while (contador < 5):
    contador += 1
    print (contador)"""
   


"""numero = 2

while numero <= 10:
    print(numero)
    numero += 2  # Suma de 2 en 2"""

  
"""for i in (1,2,3,4,5):
     print (i)"""


"""for i in range(10):
    print (i)"""

"""for num in range(2, 11, 2): # Empieza en 2, termina en 10, incrementa de 2 en 2
    print(num)"""

"""for i in range(1, 7):  # range(inicio, fin) → fin no se incluye
    print(i)

"""for i in (1,2,3,4,5,6):
    print(i)"""

#for i in range(6):
    print(i)"""

#ejercicios con error
# ERROR: Bucle infinito porque la variable 'i' nunca cambia

"""i = 1
while i <= 5:
    print(i)"""


"""i = 1
while i <= 5:
    print(i)
i += 1"""



# Validación con while
"""numero = int(input("Ingrese un número positivo: "))

while numero <= 0:
    print("Ese no es un número positivo.")
    numero = int(input("Ingrese un número positivo: "))

# Contador con for
for i in range(1, numero+1 ):
       print(i)



       for i in range(5):
    print("Estoy aprendiendo bucles 😎")"""


"""i= 1
while i< 10:
  print (i)
  i+= 1"""

"""a = 0
b = 10 
while b <=10:
    print (b) 
    break
    a+=1
print (a) 
 

A=0
B=0
 
while (B+A)<10:
    A+=1
    print(A)"""

"""a = 0
while a<10:
      a += 1
      print(a)"""

"""a=0
b=0
while b<10:
    a+=1
    print(a)
    if a>=100:
        break"""


"""A=0
B=0
if A==B:
 while(A)<10:
    A+=1
    print(A)"""

"""a = 0
b = 0
a = int (input("ingrese número a: "))
b = int (input("ingrese número b: "))
while (a or b)<=10:
    print ("variable a: ", a)
    print ("variable b: ", b)
    a+=1
    b+=1"""


"""for i in range(1, 7):
  print(i)"""

"""for i in (1,2,3,4,5): 
    print (i)"""
