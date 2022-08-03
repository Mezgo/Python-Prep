from ast import While
from operator import ne
import random
from secrets import choice
from turtle import done

txt = "Respuesta: "
line = "----------------------------------------------------------------"


def org(qstn, respuesta, var, var2):
    txt = "Respuesta: "
    line = "----------------------------------------------------------------"

    print(qstn)
    print(var)
    print(var2)
    print(txt, respuesta)
    print(line)


qstn = '1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero'
rdm = random.randint(-99, 99)

if rdm > 0:
    org(qstn, 'Es mayor a 0', rdm, ' ')

else:
    org(qstn, 'No es mayor a 0', rdm, ' ')
# ---------------------

qstn = '2) Crear dos variables y un condicional que informe si son del mismo tipo de dato'

var1 = 73
var2 = 34, 2

if type(var1) == type(var2):
    org(qstn, 'Son del mismo tipo', var1, var2)

else:
    org(qstn, 'No son del mismo tipo', var1, var2)
# ---------------------

qstn = '3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar'
num = 1

print(qstn)
print(txt)

while num <= 20:
    if num % 2 == 0:
        print(num, 'Es par')
        num += 1
    else:
        print(num, 'No es par')
        num += 1

print(line)
# ---------------------

qstn = '4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3'
print(qstn)
print(txt)

for i in range(0, 6):
    print(i**3)
print(line)
# ---------------------

qstn = '5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos'
num2 = 5

print(qstn)
print(txt)

for i in range(0, num2):
    print('Ciclo ', i+1)

print(line)
# ---------------------

qstn = '6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0'

fact = 5

factor = 1

print(qstn)
print('El factorial de ', fact, ' es: ')

if fact >= 0 and type(fact) == int:

    while fact != 0:
        print(fact)
        factor *= fact
        fact -= 1

print(txt, factor)
print(line)
# ---------------------

qstn = '7) Crear un ciclo for dentro de un ciclo while'
a = 0

print(qstn)
while a < 5:
    print('|')
    for i in range(0, 2):
        print('-')
        a += 1

print(line)

qstn = '8) Crear un ciclo while dentro de un ciclo for'
a = 0
print(qstn)
for i in range(0, 2):
    print('-')
    while a < 5:
        print('|')
        a += 1
print(line)
# ---------------------

qstn = '9) Imprimir los números primos existentes entre 0 y 30'
print(qstn)

num = 0
num2 = 30
primo = True
while num < num2:
    for i in range(2, num):
        if num % i == 0:
            # print(num, ' nunca primo')
            primo = False
    if primo:
        print(num, ' siempre primo')

    else:
        primo = True
    num += 1
print(line)
# ---------------------

qstn = '10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin'
print(qstn)

num = 0
num2 = 30
primo = True
while num < num2:
    for i in range(2, num):
        if num % i == 0:
            # print(num, ' nunca primo')
            primo = False
            break
    if primo:
        print(num, ' siempre primo')

    else:
        primo = True
    num += 1
print(line)
# ---------------------

qstn = '11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?'
print(qstn)
# codigo sin break
ciclos_sin_break = 0
num = 0
num2 = 30
primo = True
while num < num2:
    for i in range(2, num):
        ciclos_sin_break += 1
        if num % i == 0:
            # print(num, ' nunca primo')
            primo = False
    if primo:
        print(num, ' siempre primo')

    else:
        primo = True
    num += 1


# ciclo con break
ciclos_con_break = 0
num = 0
num2 = 30
primo = True
while num < num2:
    for i in range(2, num):
        ciclos_con_break += 1
        if num % i == 0:
            # print(num, ' nunca primo')
            primo = False
            break
    if primo:
        print(num, ' siempre primo')

    else:
        primo = True
    num += 1

print('Cantidad de ciclos: ', ciclos_sin_break,
      '\n', 'Ciclos con break: ', ciclos_con_break)
print(line)

# ---------------------

qstn = '12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?'
print(qstn)

print('si')
print(line)
# ---------------------

qstn = '13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300'
print(qstn)
# un numero es divisible entre 12 si es divisible entre 3 y 4.
# un numero es divisible entre 3 si es divisible entre si la suma de sus digito es multiplo de 3.
# un numero es divisible entre 4.
init = 100
end = 300

while init <= end:
    if init % 12 != 0:
        init += 1
        continue
    print(init)
    init += 1

print(line)
# ---------------------

qstn = '14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente'
print(qstn)

#next = True
primo = False

while next:

    optn = input('Ingrese un número para averiguar si este es primo suyo: \n')

    for num in range(2, 10):
        if int(optn) % num == 0:
            if int(optn) == num:
                continue
            else:
                primo = False

                break
        else:
            primo = True

    if primo:
        print('!Saluda al primo¡ :D \n', optn)
    else:
        print('No es primo >:v')

    x = input('Desea hallar a otro primo 🌝? (S/N): ')

    if x.upper() == 'N':
        print('Adios')
        next = False
print(line)
# ---------------------

qstn = '15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6'
print(qstn)

low = 100
up = 301

while low != up:
    if low % 3 == 0 and low % 6 == 0:
        print(low)
        break
    else: 
        low += 1