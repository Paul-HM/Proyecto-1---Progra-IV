from api.lector_excel import cargar_registros
from api.consultas import consultar
from ui import consola

RUTA_EXCEL = "datos/resultado_laboratorio_suelo.xlsx"


def main():
    consola.mostrar_mensaje("Cargando datos del Excel, un momento...")
    registros = cargar_registros(RUTA_EXCEL)

    continuar = True
    while continuar:
        departamento, municipio, cultivo, limite = consola.pedir_consulta()
        resumen = consultar(registros, departamento, municipio, cultivo, limite)

        if resumen is None:
            consola.mostrar_mensaje("No se encontraron registros con esos datos.")
        else:
            consola.mostrar_tabla(resumen)

        continuar = consola.preguntar_continuar()

    consola.mostrar_mensaje("¡Hasta pronto!")


if __name__ == "__main__":
    main()