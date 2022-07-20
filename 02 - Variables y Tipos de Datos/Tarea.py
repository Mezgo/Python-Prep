txt = "Respuesta: "
line = "----------------------------------------------------------------"


def org(qstn, res):
    txt = "Respuesta: "
    line = "----------------------------------------------------------------"

    print(qstn)
    print(txt, res)
    print(line)


qstn1 = "1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla"
x = 27
org(qstn1, x)

# -------------------------

qstn2 = "2) Imprimir el tipo de dato de la constante 8.5"
org(qstn2, 8.5)
# ---------------------

qstn3 = "3) Imprimir el tipo de dato de la variable creada en el punto 1"
res3 = type(x)
org(qstn3, res3)
# ---------------------

print("4) Crear una variable que contenga tu nombre")
nombre = "Sebastian"
print(txt, nombre)
print(line)
# ---------------------

print("5) Crear una variable que contenga un número complejo")
complejo = 5 + 3j
print(line)
# ---------------------

print("6) Mostrar el tipo de dato de la variable crada en el punto 5")
print(txt, complejo)
print(line)
# ---------------------

print(
    "7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales"
)
pi = 3.1416
print(line)
# ---------------------

print(
    "8) Crear una variable que contenga el valor ",
    '"True"',
    " y otra que contenga el valor True. ¿Se trata de lo mismo?",
)
tru_str = "True"
tru_bul = True
print(txt, tru_bul == tru_str)
print(line)
# ---------------------

print(
    "9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9"
)
print(txt, type(tru_str), type(tru_bul))
print(line)
# ---------------------

print("10) Asignar a una variable, la suma de un número entero y otro decimal")
suma = 23 + 23.32
print(line)
# ---------------------

print("11) Realizar una operación de suma de números complejos")
complejo2 = 3 + 1j
sum_complex = complejo + complejo2
print(txt, "La suma entre ", complejo, " y ", complejo2, " es: ", sum_complex)
print(line)
# ---------------------

print("12) Realizar una operación de suma de un número real y otro complejo")
suma = suma + complejo
print(txt, suma)
print(line)
# ---------------------

print("13) Realizar una operación de multiplicación")
print(txt, 23 * 11)
print(line)
# --------------------

qstn14 = "14) Mostrar el resultado de elevar 2 a la octava potencia"
org(qstn14, 2**8)
# --------------------

qstn15 = "15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla"
res15 = 27 / 4
org(qstn15, res15)
# ---------------------

qstn16 = "16) De la división anterior solamente mostrar la parte entera"
res16 = 27 // 4
org(qstn16, res16)
# ---------------------

qstn17 = "17) De la división de 27 entre 4 mostrar solamente el resto"
res17 = 27 % 4
org(qstn17, res17)
# ---------------------

qstn18 = "18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado"
res18 = (4 * res16) + res17
org(qstn18, res18)
# ---------------------

qstn19 = '19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas'
org(qstn19, "con" + "ca" + "te" + "nar")
# ---------------------

qstn20 = '20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?'
res20 = "no son del mismo tipo"
print(2, ' == "2": ', 2 == "2")
org(qstn20, res20)
# ---------------------

qstn21 = "21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera"
res21 = str(2) == "2"
org(qstn21, res21)
# ---------------------

qstn22 = (
    '22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float("3,8")'
)
res22 = "La coma denota la entrada de dos datos diferentes, no la separación entre un entero y su parte decimal"
org(qstn22, res22)
# ---------------------

qstn23 = '23) Crear una variable con el valor 3, y utilizar el operador "-=" para modificar su contenido'
res23 = 3
res23 -= 1
org(qstn23, res23)
# ---------------------

qstn24 = "24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?"
res24 = 1 << 2
org(qstn24, res24)
# ---------------------

qstn25 = '25) Realizar la operación 2 + "2" ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?'
res25 = 'No se pueden concatenar un str con otro tipo de dato a traves de "+".'
org(qstn25, res25)
# ---------------------

qstn26 = "26) Realizar una operación válida entre valores de tipo entero y string"
m = 2 == "2"
res26 = '2== "2"', m
print(type(res26))
org(qstn26, res26)
