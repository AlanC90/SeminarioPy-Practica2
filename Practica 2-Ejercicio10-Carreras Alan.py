#Alumno: Alan Carreras 
#Legajo: 16497/4


#Ejercicio 10. 

#Variables globales.
nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


#Funciones.
def cargar_datos(dicc_alumnos_notas):
    """Funcion genera y retorna diccionario con nombres de alumnos y sus notas."""     
    #Dar formato a datos iniciales.
    
    #Obtener lista de nombres.
    global nombres
    nombres = nombres.split("/n")
    nombres = nombres[0].split("'")
    nombres = list(filter(lambda x: len(x) > 2, nombres))
    nombres.remove(" , ")
    
    #Formato nombre.
    nombres = list(map(lambda x: x.lower(), nombres))
    nombres = list(map(lambda x: (x[0].upper() + x[1:]), nombres))


    #Zipear notas por alumno.
    notas_alumnos = list(zip(notas_1, notas_2))


    #Almacenar datos en diccionario.
    indice = 0
    for elem in nombres:
        dicc_alumnos_notas[nombres[indice]] = notas_alumnos[indice]
        indice += 1


    #--------------------#


def promedio_por_alumno(dicc_alumnos_notas):
    """Calcula promedio de notas por cada estudiante y retorna esa informacion 
    en una lista."""

    lista_promedios = []
    for elem in dicc_alumnos_notas: 
        promedio = (dicc_alumnos_notas[elem][0] + dicc_alumnos_notas[elem][1]) / 2 
        lista_promedios.append(promedio)

    return(lista_promedios)


    #--------------------#

def imprimir_lista_promedios(lista_promedios):
    """Genera e imprime diccionario de alumnos y sus promedios."""
    
    dicc_aux = {}
    
    indice = 0
    for elem in lista_promedios:
        dicc_aux[nombres[indice]] = elem
        indice += 1

    print(dicc_aux)



def promedio_general_del_curso(lista_promedios, cant_alumnos):
    """Calcula y retorna promedio general del curso."""

    promedio_gral = sum(lista_promedios) / cant_alumnos

    return promedio_gral
    
    
    #--------------------#


def estudiante_mayor_promedio(lista_promedios):
    """Calcula maximo entre los promedios de alumnos y retorna el nombre
    del alumno y su promedio que resultaron maximos"""

    prom_Max = max(lista_promedios)
    pos = lista_promedios.index(prom_Max)
    
    return nombres[pos], prom_Max

    
    #--------------------#


def estudiante_menor_promedio(lista_promedios):
    """Calcula minimo entre los promedios de alumnos y retorna el nombre
    del alumno y su promedio que resultaron minimos"""

    prom_Min = min(lista_promedios)
    pos = lista_promedios.index(prom_Min)
    
    return nombres[pos], prom_Min

    
    #--------------------#

def estudiante_nota_mas_baja():
    """Calcula y retorna nombre de alumno (y su nota) que resulto tener 
    la calificacion mas baja"""

    notas_alumnos = list(zip(notas_1, notas_2))

    lista_notas_minimas = []
    for elem in notas_alumnos:
        lista_notas_minimas.append(min(elem))


    nota_minima = min(lista_notas_minimas)    
    pos = lista_notas_minimas.index(nota_minima)

    return nombres[pos], nota_minima
    
    #--------------------#



#--------------------#
#Main.
#Inicio del programa.
print('--------------------\n')
print("Bienvenido/a.\n")
print('Resolucion de Ejercicio 10 de la Practica 2.\n')
print()

#Generar diccionario.
dicc_alumnos_notas = {}
cargar_datos(dicc_alumnos_notas)
print("Diccionario de alumnos y sus notas: ")
print(dicc_alumnos_notas)

print()


#Calcular promedio por alumno.
lista_promedios = promedio_por_alumno(dicc_alumnos_notas)
print("Lista de promedios por alumno: ")
imprimir_lista_promedios(lista_promedios)
#print(lista_promedios)

print()

#Calcular promedio general.
promedio_gral = (promedio_general_del_curso(lista_promedios, len(dicc_alumnos_notas.keys())))
print("Promedio general: ", end=" ")
print("{:.2f}".format(promedio_gral))

print()

#Identificar estudiante nota promedio mas alta.
nombre_Max, promedio_Max = estudiante_mayor_promedio(lista_promedios)
print(f"Estudiante con mayor promedio: {nombre_Max} ({promedio_Max})")

print()

#Identificar estudiante nota (promedio) mas baja.
nombre_Min, promedio_Min = estudiante_menor_promedio(lista_promedios)
print(f"Estudiante con menor promedio: {nombre_Min} ({promedio_Min})")

print()

#Identificar estudiante nota mas baja.
nombre_nota_min, nota_min = estudiante_nota_mas_baja()
print(f"Estudiante con nota mas baja: {nombre_nota_min} ({nota_min}))")

print()

print()


#Fin del programa.
print()
print()
print("Fin del programa.\n")
print("--------------------\n")




