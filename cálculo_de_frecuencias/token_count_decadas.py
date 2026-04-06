import pandas as pd
import re

archivo = "/Users/martagcasado/Desktop/pol/anys_histerico_adj_gemini.csv"

# Leer CSV con una sola columna
df = pd.read_csv(archivo, header=None, names=["documento"])

# Extraer año con regex (4 dígitos al principio)
df["año"] = df["documento"].str.extract(r"^(\d{4})")

# Filtrar filas sin año
df = df[df["año"].notna()]

# Convertir a entero
df["año"] = df["año"].astype(int)

# Función para asignar década con regex
def asignar_decada(anio):
    s = str(anio)
    if re.match(r"185\d", s):
        return "1850-1859"
    elif re.match(r"186\d", s):
        return "1860-1869"
    elif re.match(r"187\d", s):
        return "1870-1879"
    elif re.match(r"188\d", s):
        return "1880-1889"
    elif re.match(r"189\d", s):
        return "1890-1899"
    elif re.match(r"190\d", s):
        return "1900-1909"
    elif re.match(r"191\d", s):
        return "1910-1919"
    elif re.match(r"192\d", s):
        return "1920-1929"
    elif re.match(r"193\d", s):
        return "1930-1939"
    elif re.match(r"194\d|1950", s):
        return "1940-1950"
    else:
        return "Fuera de rango"

# Aplicar función
df["decada"] = df["año"].apply(asignar_decada)

# Lista completa de décadas que quieres
todas_decadas = [
    "1850-1859","1860-1869","1870-1879","1880-1889",
    "1890-1899","1900-1909","1910-1919","1920-1929",
    "1930-1939","1940-1950"
]

# Contar por década
conteo = df["decada"].value_counts().reindex(todas_decadas, fill_value=0)

# Guardar resultado
with open("/Users/martagcasado/Desktop/pol/count_por_decadas_histerico_adj_gemini.txt", "w", encoding="utf-8") as f:
    for periodo, cantidad in conteo.items():
        f.write(f"{periodo}: {cantidad}\n")

print("Done")
