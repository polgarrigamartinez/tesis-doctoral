import pandas as pd
import re

archivo = "/Users/martagcasado/Desktop/pol/anys_histerico_adj_gemini.csv"

df = pd.read_csv(archivo, header=None, names=["documento"])

df["año"] = df["documento"].str.extract(r"^(\d{4})")

df = df[df["año"].notna()]

df["año"] = df["año"].astype(int)

def asignar_periodo(anio):
    s = str(anio)
    if re.match(r"18[5-6]\d|187[0-4]", s):
        return "1850-1874"
    elif re.match(r"187[5-9]|18[8-9]\d|1899", s):
        return "1875-1899"
    elif re.match(r"190\d|191\d|192[0-4]", s):
        return "1900-1924"
    elif re.match(r"192[5-9]|193\d|194\d|1950", s):
        return "1925-1950"
    else:
        return "Fora de rang"

# Apliquem la funció
df["cuarto"] = df["año"].apply(asignar_periodo)

# Comptem per períodes
conteo = df["cuarto"].value_counts().sort_index()

# Guardem el resultat
with open("/Users/martagcasado/Desktop/pol/count_por_cuartos_histerico_adj_gemini.txt", "w", encoding="utf-8") as f:
    for periodo, cantidad in conteo.items():
        f.write(f"{periodo}: {cantidad}\n")

print("Done")

