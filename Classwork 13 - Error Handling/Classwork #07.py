class DigitoVerificadorError(Exception):
    pass


rol = input("Ingrese el rol: ")

partes = rol.split("-")

if len(partes) != 2:
    print("Rol inválido: No tiene el formato XXXXXXXXX-X")
else:
    rol_sin_digito, digito = partes

    if not rol_sin_digito.isnumeric():
        print("Los digitos del rol deben ser numéricos")
    elif not digito.isnumeric():
        print("El digito verificador debe ser numérico")
    else:
        invertido = rol_sin_digito[::-1]
        secuencia = [2, 3, 4, 5, 6, 7]
        suma = 0

        for index in range(len(invertido)):
            multiplicando = secuencia[index % 6]
            numero = int(invertido[index])
            suma += numero * multiplicando

        total = suma % 11
        verificador = 11 - total

        if verificador == 11:
            verificador = 0
        elif verificador == 10:
            verificador = "K"

        try:
            if str(verificador) != digito:
                raise DigitoVerificadorError(
                    f"Error: El dígito verificador no conicide, se esperaba {verificador}"
                )
        except DigitoVerificadorError as e:
            print(e)
        else:
            print(f"{rol_sin_digito}-{digito}")

#AI DECLARATION I USE IT TO HELP ME WITH MY CODE
