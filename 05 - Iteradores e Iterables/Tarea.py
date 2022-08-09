txt = "Respuesta: "
line = "----------------------------------------------------------------"


def org(qstn, respuesta, var, var2):

    txt = "Respuesta: "
    line = "----------------------------------------------------------------"

    print(qstn, '\n \n', txt, '\n \n',
          respuesta, '\n \n', var, '\n \n', var2)
    '''print(var)
    print(var2)
    print(txt, respuesta)'''
    print(line, '\n')


q = '1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1'

L1 = []
n = -15
while n != 0:
    L1.append(n)
    n += 1
org(q, L1, '', '')
# ---------------------

q = '2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?'
L2 = []
n = 0
while n != len(L1)-1:
    if L1[n] % 2 == 0:
        L2.append(L1[n])
    n += 1
org(q, L2, '', '')
# ---------------------

q = '3) Resolver el punto anterior sin utilizar un ciclo while'

L2_2 = [i for i in L1 if i % 2 == 0]

org(q, L2_2, '', '')
# ---------------------

q = '4) Utilizar el iterable para recorrer sólo los primeros 3 elementos'

print(q, '\n\n' + txt + '\n')
for e in L1[:3]:
    print(e)
print('\n' + line + '\n')
# --------------------

q = '5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento'
print(q, '\n\n' + txt + '\n')
print('Index  Elemento')
for index, el in enumerate(L1):
    print(index, '     ', el)
print('\n' + line + '\n')
# --------------------

q = '6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]'
lista = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]
n = 0

print(q, '\n\n' + txt + '\n\n', 'lista antes = ', lista, '\n\n')
while n < len(lista)-1:
    if lista[n] + 1 == lista[n + 1]:
        # print(lista)
        # print('Entró al if', lista)
        n += 1
        continue
    else:
        lista.insert(n+1, lista[n]+1)
        # print('Entró al else', lista)
        n += 1
print('lista despues = ', lista, '\n\n', line + '\n\n')
# --------------------

q = '7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: \n\n N0 = 0 \n\n N1 = 1 \n\n Ni = Ni-1 + Ni-2 \n\n Crear una lista con los primeros treinta números de la sucesión.'


n = 2
fibonacci = [0, 1]
while n < 30:
    fibonacci.append(fibonacci[n-1] + fibonacci[n-2])
    n += 1
org(q, fibonacci, '', '')
# ---------------------

q = '8) Realizar la suma de todos elementos de la lista del punto anterior'
org(q, sum(fibonacci), '', '')
# ---------------------

q = '9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos. Donde i es la cantidad total de elementos: \n\n Ni-1 / Ni \n\n Ni-2 / Ni-1 \n\n Ni-3 / Ni-2 \n\n Ni-4 / Ni-3 \n\n Ni-5 / N'
primeros = 15
n = primeros - 5
aurea = []
while(n < primeros):
    aurea.append(fibonacci[n-1]/fibonacci[n])
    n += 1
org(q, aurea, '', '')
# ---------------------

q = '10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n". cadena = "Hola Mundo. Esto es una practica del lenguaje de programación Python"'

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python\n'
print(q, '\n\n' + txt + '\n\n', cadena)
for i, e in enumerate(cadena):
    if e == 'n':
        print(i)
print('\n\n' + line + '\n\n')
# --------------------

q = '11) Crear un diccionario e imprimir sus claves utilizando un iterador'

f1 = {'Nombre': ['Max', 'Lewis', 'Charles',
                 'Carlos', 'George', 'Lando',
                 'Daniel', 'Sergio', 'Mick',
                 'Kevin', 'Sebastian', 'Lance'],
      'Apellido': ['Verstappen', 'Hamilton', 'Leclerc',
                   'Sainz', 'Russell', 'Norris',
                   'Ricciardo', 'Pérez', 'Shumacher',
                   'Magnussen', 'Vettel', 'Stroll'],
      'Escudería': ['RedBull', 'Mercedes', 'Ferrari',
                    'McLaren', 'Hass', 'AstonMartin']
      }
llaves = []
for i in f1:
    llaves.append(i)
org(q, llaves, '', '')
# ---------------------

q = '12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador'
print(q)
print(txt)
l = list(cadena)
iterador = iter(l)
for i in range(0, len(l)):
    print(next(iterador))
print(line)
# ---------------------

q = '13) Crear dos listas y unirlas en una tupla utilizando la función zip'

l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']
l3 = zip(l1,l2)
org(q,list(l3),'', '')
# ---------------------

q = '14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7: \nlis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]'


lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

lis2 = [i for i in lis if i % 7 == 0]
org(q, lis2, '', '')
# ---------------------

q = '15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista: lis = [[1,2,3,4],"rojo","verde",[True,False,False],["uno","dos","tres"]]'

lis = [[1,2,3,4],"rojo","verde",[True,False,False],["uno","dos","tres"]]
m = []
for e in lis:
    if type(e) == list:
        m.append(len(e))
    else: 
        m.append(1)
org(q, 'La cantidad total de elementos es: ', sum(m), '')
# ---------------------

q = '16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es'

for i, e in enumerate(lis):
    if type(e) != list:
        lis[i] = [e]
org(q, lis, '', '')        