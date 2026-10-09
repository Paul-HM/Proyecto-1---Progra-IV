"""Módulo encargado de LIMPIAR los valores del Excel y convertirlos en números."""
import datetime


def convertir_numero(valor):
    if isinstance(valor, bool):
        return None
    if isinstance(valor, (int, float)):
        return float(valor)
    if isinstance(valor, str):
        try:
            return float(valor.strip().replace(",", "."))
        except ValueError:
            return None  # textos como '<3,87' o 'ND'
    return None


def convertir_ph(valor):
    if isinstance(valor, datetime.datetime):
        # Excel convirtió un pH (ej. 5.6) en fecha (5 de junio).
        # Con mes 11 o 12 solo puede ser d.11 o d.12; con meses 1-9 es ambiguo (5.6 o 5.06).
        if valor.month in (11, 12):
            return valor.day + valor.month / 100
        return None
    ph = convertir_numero(valor)
    if ph is None or not 3 <= ph <= 10:  # rango razonable de pH en suelos
        return None
    return ph

def _es_entero_danado(valor):
    return (isinstance(valor, (int, float)) and not isinstance(valor, bool)
            and valor == valor and float(valor).is_integer())


def convertir_fosforo(valor):
    """Fósforo (mg/kg). SUPUESTO: los enteros de 15-17 dígitos perdieron 15 decimales."""
    if not _es_entero_danado(valor):
        return convertir_numero(valor)
    cifras = len(str(int(valor)))
    if cifras >= 15:
        return valor / 10 ** 15
    if cifras <= 4:      # entero pequeño: se toma tal cual (ej. 12)
        return float(valor)
    return None          # longitud intermedia: no se puede reconstruir


def convertir_potasio(valor):
    """Potasio (cmol/kg). SUPUESTO: el valor real es menor que 1 (el entero son los decimales)."""
    if not _es_entero_danado(valor):
        return convertir_numero(valor)
    cifras = len(str(int(valor)))
    if cifras == 1:      # un solo dígito: se toma tal cual
        return float(valor)
    return valor / 10 ** cifras