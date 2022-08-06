

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


q = '1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla'

cities = ['Bogotá', 'Buenos Aires', 'Santiago', 'Atenas',
          'El Cairo', 'Oslo', 'Londres', 'Madrid', 'París']

org(q, cities, '', '')
# ---------------------

q = '2) Imprimir por pantalla el segundo elemento de la lista'

org(q, cities[1], '', '')
# ---------------------

q = '3) Imprimir por pantalla del segundo al cuarto elemento'

org(q, cities[1:4], '', '')
# ---------------------

q = '4) Visualizar el tipo de dato de la lista'

org(q, type(cities), '', '')
# ---------------------

q = '5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento'

org(q, cities[2:], '', '')
# ---------------------

q = '6) Visualizar los primeros 4 elementos de la lista'

org(q, cities[:4], '', '')
# ---------------------

q = '7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?'

cities.append('Santiago')
cities.append('Jerusalen')
org(q, cities, 'No se evidencia ningún tipo de error', '')
# ---------------------

q = '8) Agregar otra ciudad, pero en la cuarta posición'

cities.insert(3, ' Beijing')

org(q, cities, '', '')
# ---------------------

q = '9) Concatenar otra lista a la ya creada'

colors = ['Amarillo', 'Azul', 'Rojo', 'Verde', 'Magenta', 'Blanco', 'Negro']
cities.extend(colors)

org(q, cities, '', '')
# ---------------------

q = '10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?'

cities.remove('Amarillo')
cities.remove('Azul')
cities.remove('Rojo')
cities.remove('Verde')
cities.remove('Magenta')
cities.remove('Blanco')
cities.remove('Negro')

org(q, cities.index('Santiago'),
    'Muestra el indice del primero que encuentra solamente', '')
# ---------------------

q = '11) ¿Qué pasa si se busca un elemento que no existe?'

org(q, 'cities.index(Viena)',
    'Arroja un error que especifica que <Austria> no está en la lista', '')
# ---------------------

q = '12) Eliminar un elemento de la lista'

cities.remove('Santiago')
org(q, 'cities.remove("Chile")', cities,
    'NOTA: si se da el nombre de un elemento que esta repetido, borra el primero que encuentre')
# ---------------------

q = '13) ¿Qué pasa si el elemento a eliminar no existe?'

org(q, 'cities.remove("Madagascar")', cities,
    'Arroja un error que anuncia que el elemento no está en la lista')
# ---------------------

q = '14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo'

x = cities.pop(len(cities)-1)

org(q, cities, 'x = cities.pop(len(cities)-1)', x)
# ---------------------

q = '15) Mostrar la lista multiplicada por 4'

org(q, cities*4, 'NOTA: imprime todo como si fuera una sola lista', '')
# ---------------------

q = '16) Crear una tupla que contenga los números enteros del 1 al 20'

x = range(1, 21)
nums = []
for n in x:
    nums.append(n)
nums = tuple(nums)
# print(type(nums), type(nums))
org(q, nums, type(nums), '')
# ---------------------

q = '17) Imprimir desde el índice 10 al 15 de la tupla'

org(q, nums[10:16], '', '')
# ---------------------

q = '18) Evaluar si los números 20 y 30 están dentro de la tupla'


if 20 in nums and 30 in nums:
    org(q, 'Ambos elementos estan presentes', '', '')
elif 20 in nums and not 30 in nums:
    org(q, 'Solo el 20 esta presente', '', '')
elif not 20 in nums and 30 in nums:
    org(q, 'Solo el 30 esta presente', '', '')
else:
    org(q, 'Ninguno de los elementos está presente', '', '')
# ---------------------

q = '19) Con la lista creada en el punto 1, validar la existencia del elemento "París" y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.'

y = 'París'
x = y in cities

if x:
    org(q, 'La ciudad: ' + y, 'Está en la lista', cities)
else:
    cities.append(y)
    org(q, 'La ciudad: ' + y, 'No está en la lista. Se procedera a agregarla', cities)
# ---------------------

q = '20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista'

el = '9'

x = el in cities
y = int(el) in nums

if x:
    org(q, el, 'Está ' + str(cities.count(el)) + ' veces en cities', cities)
elif y:
    org(q, el, 'Está ' + str(nums.count(el)) + ' veces en nums', nums)
else:
    org(q, el, 'No está en cities ni en nums', cities.append(nums))
# ---------------------

q = '21) Convertir la tupla en una lista'
Lnums = list(nums)
org(q, Lnums, type(Lnums), '')
# ---------------------

q = '22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables'

x, y, z = nums[0:3]

org(q, x, y, z)
# ---------------------

q = '23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".'


Mundo = {
    'Capitales': cities,
    'Paises': ['Colombia', 'Argentina', 'China', 'Grecia', 'Egipto', 'Noruega', 'Inglaterra', 'España',
               'Francia', 'Chile'],
    'Continentes': ['America', 'Europa', 'Asia', 'Africa', 'Oceanía']
}

org(q, Mundo, '', '')
# ---------------------

q = '24) Imprimir las claves del diccionario'

org(q,'Las claves del diccionario son: ', Mundo.keys(), '')
# ---------------------

q = '25) Imprimir las ciudades a través de su clave'

org(q, 'Las ciudades son: ', Mundo['Capitales'], '')