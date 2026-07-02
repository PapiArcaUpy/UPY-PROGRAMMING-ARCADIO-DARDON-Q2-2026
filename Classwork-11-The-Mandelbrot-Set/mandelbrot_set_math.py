# INPUT: read config.txt
config = {}
archivo_config = open("config.txt", "r")
for linea in archivo_config:
    clave, valor = linea.strip().split("=")
    config[clave] = float(valor)
archivo_config.close()

ancho = int(config["ancho"])
alto = int(config["alto"])
real_min = config["real_min"]
real_max = config["real_max"]
imag_min = config["imag_min"]
imag_max = config["imag_max"]
max_iter = int(config["max_iter"])

# OUTPUT: create the CSV file
salida = open("mandelbrot.csv", "w")
salida.write("fila,columna,iteraciones\n")

# PROCESS: iterate every point of the grid
for fila in range(alto):
    for columna in range(ancho):

        real = real_min + (columna / ancho) * (real_max - real_min)
        imag = imag_min + (fila / alto) * (imag_max - imag_min)
        c = complex(real, imag)

        z = 0 + 0j
        iteraciones = 0

        while abs(z) <= 2 and iteraciones < max_iter:
            z = z * z + c
            iteraciones += 1

        salida.write(f"{fila},{columna},{iteraciones}\n")

salida.close()
print("Done")
#AI DECLARATION I USE CLAUDE TO FIX MY CODE AND HELP ME WITH THE CHANGES
