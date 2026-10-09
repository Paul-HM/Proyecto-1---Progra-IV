def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  Este campo no puede estar vacío.")


def pedir_entero_positivo(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.isdigit() and int(texto) > 0:
            return int(texto)
        print("  Escribe un número entero mayor que cero.")


def pedir_consulta():
    print("\n--- Nueva consulta ---")
    departamento = pedir_texto("Departamento: ")
    municipio = pedir_texto("Municipio: ")
    cultivo = pedir_texto("Cultivo: ")
    limite = pedir_entero_positivo("Número de registros a consultar: ")
    return departamento, municipio, cultivo, limite


def _formato(valor):
    return "N/D" if valor is None else f"{valor:.2f}"


def mostrar_tabla(resumen):
    encabezados = ["Departamento", "Municipio", "Cultivo", "Topografía",
                   "Registros", "Mediana pH", "Mediana P (mg/kg)", "Mediana K (cmol/kg)"]
    fila = [resumen["departamento"], resumen["municipio"], resumen["cultivo"],
            resumen["topografia"], resumen["registros"], _formato(resumen["ph"]),
            _formato(resumen["fosforo"]), _formato(resumen["potasio"])]

    anchos = [max(len(e), len(str(v))) for e, v in zip(encabezados, fila)]
    linea = "+" + "+".join("-" * (a + 2) for a in anchos) + "+"

    def formatear(celdas):
        return "| " + " | ".join(str(c).ljust(a) for c, a in zip(celdas, anchos)) + " |"

    print()
    print(linea)
    print(formatear(encabezados))
    print(linea)
    print(formatear(fila))
    print(linea)


def mostrar_mensaje(mensaje):
    print(f"\n{mensaje}")


def preguntar_continuar():
    respuesta = input("\n¿Hacer otra consulta? (s/n): ").strip().lower()
    return respuesta in ("s", "si", "sí")