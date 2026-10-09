# Consulta de propiedades edáficas - Risaralda

Proyecto de Programación 4 (Universidad Tecnológica de Pereira).
Docente: Alejandro Rodas Vásquez.

Aplicación de consola, hecha en Python y organizada en módulos, que consulta el archivo
"Resultados de Análisis de Laboratorio Suelos en Colombia" y muestra una tabla con la
mediana de pH, fósforo (P) y potasio (K) del cultivo consultado.

## Funcionamiento

El programa pide:

1. Departamento
2. Municipio
3. Cultivo
4. Número de registros a consultar (máximo de filas usadas para el cálculo)

Y muestra una tabla con departamento, municipio, cultivo, topografía más frecuente,
número de registros usados y la mediana de pH, P (mg/kg) y K (cmol/kg).

Los textos se pueden escribir en mayúsculas o minúsculas y con o sin tildes.
Los nombres deben coincidir con los del Excel (por ejemplo, el cultivo
"Caña panelera/azucar").

## Estructura del proyecto

```
ProyectoAPI/
├── api/
│   ├── __init__.py
│   ├── lector_excel.py    # Lee el archivo de Excel
│   ├── limpieza.py        # Convierte los valores del Excel en números
│   ├── estadisticas.py    # Mediana y moda
│   └── consultas.py       # Filtra los registros y arma el resumen
├── ui/
│   ├── __init__.py
│   └── consola.py         # Entrada de datos y tabla en consola
├── datos/
│   └── resultado_laboratorio_suelo.xlsx
├── main.py                # Punto de entrada
└── requirements.txt
```

## Requisitos

- Python 3.12 (o similar)
- openpyxl

## Instalación y ejecución

En la terminal, dentro de la carpeta del proyecto:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

(En Mac o Linux, el entorno virtual se activa con `source venv/bin/activate`.)

El archivo de Excel debe estar en `datos/resultado_laboratorio_suelo.xlsx`.
La carga inicial tarda unos 10 segundos.

## Ejemplo

Entradas: `risaralda`, `pereira`, `platano`, `5`

| Departamento | Municipio | Cultivo | Topografía | Registros | Mediana pH | Mediana P (mg/kg) | Mediana K (cmol/kg) |
|---|---|---|---|---|---|---|---|
| RISARALDA | PEREIRA | Plátano | Pendiente | 4 | 5.37 | 7.94 | 0.35 |

## Limitaciones de los datos

El archivo de Excel proporcionado tiene problemas de calidad: se perdió el separador
decimal en las columnas de fósforo y potasio, y algunos valores de pH se convirtieron en
fechas. Para poder calcular las medianas se aplicaron reglas de reconstrucción basadas
en rangos plausibles, y se descartaron los valores que no se pueden recuperar de forma
confiable (como "<3,87" o fechas ambiguas). Por eso, los resultados son aproximados.
Todas estas reglas están en `api/limpieza.py`.

## Autor

Paula Andrea Hernández Marin - Programación 4, UTP
