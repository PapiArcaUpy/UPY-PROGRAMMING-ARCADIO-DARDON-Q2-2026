class ConfigError(Exception):
    pass


# INPUT: read config.txt
config = {}

try:
    archivo_config = open("config.txt", "r")
except FileNotFoundError:
    print("Error: config.txt file was not found.")
else:
    try:
        for linea in archivo_config:
            linea = linea.strip()
            if linea == "":
                continue
            clave, valor = linea.split("=")
            config[clave] = float(valor)
    except ValueError:
        print("Error: config.txt has an invalid line (expected 'key=value').")
        config = {}
    finally:
        archivo_config.close()

    try:
        if not config:
            raise ConfigError("Error: config.txt is empty or could not be read.")

        ancho = int(config["ancho"])
        alto = int(config["alto"])
        real_min = config["real_min"]
        real_max = config["real_max"]
        imag_min = config["imag_min"]
        imag_max = config["imag_max"]
        max_iter = int(config["max_iter"])

        if ancho <= 0 or alto <= 0:
            raise ConfigError("Error: 'ancho' and 'alto' must be greater than 0.")

    except KeyError as e:
        print(f"Error: Missing key {e} in config.txt")
    except ConfigError as e:
        print(e)
    else:
        # OUTPUT: create the CSV file
        try:
            salida = open("mandelbrot.csv", "w")
        except OSError:
            print("Error: Could not create mandelbrot.csv")
        else:
            try:
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
            except Exception as e:
                print(f"Error while generating the Mandelbrot data: {e}")
            else:
                print("Done")
            finally:
                salida.close()

# AI DECLARATION
# I use Claude to fix my code, help me with the changes, and add error handling.
