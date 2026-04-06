import pandas as pd
import re

# Cargar el Excel
df = pd.read_excel("/Users/martagcasado/Desktop/pol/hysterisch_sustantivo_classificado_ano.xlsx")

# Función para asignar periodo con regex
def asignar_periodo(anio):
    anio_str = str(anio)
    match = re.match(r"^(18[5-9]\d|190\d|191\d|192\d|193\d|194\d|1950)$", anio_str)
    if match:
        if re.match(r"185\d", anio_str):
            return "1850-1859"
        elif re.match(r"186\d", anio_str):
            return "1860-1869"
        elif re.match(r"187\d", anio_str):
            return "1870-1879"
        elif re.match(r"188\d", anio_str):
            return "1880-1889"
        elif re.match(r"189\d", anio_str):
            return "1890-1899"
        elif re.match(r"190\d", anio_str):
            return "1900-1909"
        elif re.match(r"191\d", anio_str):
            return "1910-1919"
        elif re.match(r"192\d", anio_str):
            return "1920-1929"
        elif re.match(r"193\d", anio_str):
            return "1930-1939"
        elif re.match(r"194\d|1950", anio_str):
            return "1940-1950"
    return "Fuera de rango"

# Crear la columna con el periodo
df["Periodo"] = df["año"].apply(asignar_periodo)

# Crear la tabla de contingencia
tabla = pd.crosstab(df["Periodo"], df["clasificación"])

# Guardar el resultado
tabla.to_excel("/Users/martagcasado/Desktop/pol/tabla_contingencia_hysterisch_sustantivo.xlsx")

print("Done")
