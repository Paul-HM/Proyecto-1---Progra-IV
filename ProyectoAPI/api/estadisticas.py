from collections import Counter
from statistics import median


def mediana(valores):
    validos = [v for v in valores if v is not None]
    if not validos:
        return None
    return median(validos)


def moda(valores):
    validos = [v for v in valores if v is not None]
    if not validos:
        return None
    return Counter(validos).most_common(1)[0][0]