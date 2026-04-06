import spacy
import os

# Definimos los periodos como rangos de años
PERIODOS = {
    "1850-1874": (1850, 1874),
    "1875-1899": (1875, 1899),
    "1900-1924": (1900, 1924),
    "1925-1950": (1925, 1950),
}

def cargar_textos_desde_carpeta(carpeta):
    textos = {}
    for archivo in sorted(os.listdir(carpeta)):
        if archivo.endswith(".txt"):
            with open(os.path.join(carpeta, archivo), "r", encoding="utf-8") as f:
                textos[archivo] = f.read()
    return textos

def asignar_periodo(nombre_archivo):
    try:
        año = int(nombre_archivo.split("_")[0])  
        for periodo, (inicio, fin) in PERIODOS.items():
            if inicio <= año <= fin:
                return periodo
    except ValueError:
        pass
    return None  

def contar_tokens_por_periodo(textos, max_chars=1_000_000):
    nlp = spacy.load("es_core_news_lg")
    nlp.max_length = max_chars

    conteo_periodos = {p: 0 for p in PERIODOS.keys()}

    for archivo, texto in textos.items():
        periodo = asignar_periodo(archivo)
        if periodo is None:
            continue

        fragmentos = [texto[i:i+max_chars] for i in range(0, len(texto), max_chars)]
        for i, fragmento in enumerate(fragmentos):
            print(f"Procesando '{archivo}' ({periodo}), fragmento {i+1} de {len(fragmentos)}...")
            doc = nlp(fragmento)
            conteo_periodos[periodo] += sum(1 for token in doc if not token.is_punct and not token.is_space)

    return conteo_periodos

if __name__ == "__main__":
    carpeta = "/Users/martagcasado/Desktop/textos" 
    textos = cargar_textos_desde_carpeta(carpeta)

    print("Textos cargados y procesando con spaCy...")
    frecuencias = contar_tokens_por_periodo(textos)

    print("\nFrecuencia de tokens por periodos")
    for periodo, freq in frecuencias.items():
        print(f"{periodo}: {freq}")
