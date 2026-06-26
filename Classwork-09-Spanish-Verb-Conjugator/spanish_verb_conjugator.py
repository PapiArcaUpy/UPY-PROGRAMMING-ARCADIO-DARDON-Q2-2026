# INPUT
accion = input("Ingrese un verbo: ")

# PROCESS

# Lista de pronombres
personas = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

# Diccionario de terminaciones
conjugaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# Obtener la raíz y la terminación del verbo
raiz = accion[:-2]
tipo = accion[-2:]

# Buscar las terminaciones correspondientes
lista_final = conjugaciones[tipo]

# OUTPUT
for posicion, persona in enumerate(personas):
    sufijo = lista_final[posicion]
    print(f"{persona} {raiz}{sufijo}")
    #AI DECLARATION
    #I only use it to help me with the code
