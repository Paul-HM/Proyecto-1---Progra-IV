import unicodedata

from api.estadisticas import mediana, moda
from api.limpieza import convertir_ph, convertir_fosforo, convertir_potasio


def normalizar(texto):
    texto = str(texto).strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return " ".join(texto.split())


def filtrar_registros(registros, departamento, municipio, cultivo, limite):
    departamento = normalizar(departamento)
    municipio = normalizar(municipio)
    cultivo = normalizar(cultivo)

    encontrados = []
    for registro in registros:
        if (normalizar(registro["departamento"]) == departamento
                and normalizar(registro["municipio"]) == municipio
                and normalizar(registro["cultivo"]) == cultivo):
            encontrados.append(registro)
            if len(encontrados) == limite:
                break
    return encontrados


def consultar(registros, departamento, municipio, cultivo, limite):
    encontrados = filtrar_registros(registros, departamento, municipio, cultivo, limite)
    if not encontrados:
        return None

    primero = encontrados[0]
    return {
        "departamento": primero["departamento"],
        "municipio": primero["municipio"],
        "cultivo": primero["cultivo"],
        "topografia": moda([r["topografia"] for r in encontrados]),
        "registros": len(encontrados),
        "ph": mediana([convertir_ph(r["ph"]) for r in encontrados]),
        "fosforo": mediana([convertir_fosforo(r["fosforo"]) for r in encontrados]),
        "potasio": mediana([convertir_potasio(r["potasio"]) for r in encontrados]),
    }