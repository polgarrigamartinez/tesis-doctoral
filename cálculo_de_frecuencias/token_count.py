import spacy
import os

def cargar_textos_desde_carpeta(carpeta):
    textos = {}
    for archivo in sorted(os.listdir(carpeta)):
        if archivo.endswith(".txt"):
            with open(os.path.join(carpeta, archivo), "r", encoding="utf-8") as f:
                textos[archivo] = f.read()
    return textos

def contar_tokens(textos, max_chars=1_000_000):
    nlp = spacy.load("es_core_news_lg")
    nlp.max_length = max_chars  # Límite de caracteres por fragmento
    total_tokens = 0

    for archivo, texto in textos.items():
        # Dividir el texto en fragmentos grandes para evitar errores de memoria
        fragmentos = [texto[i:i+max_chars] for i in range(0, len(texto), max_chars)]
        for i, fragmento in enumerate(fragmentos):
            print(f"Procesando '{archivo}', fragmento {i+1} de {len(fragmentos)}...")
            doc = nlp(fragmento)
            # Solo contar tokens que no sean puntuación ni espacios
            total_tokens += sum(1 for token in doc if not token.is_punct and not token.is_space)

    return total_tokens

if __name__ == "__main__":
    carpeta = "/Users/martagcasado/Desktop/ES_general"  # Ruta de la carpeta con los archivos
    textos = cargar_textos_desde_carpeta(carpeta)

    print("Textos cargados y procesando con spaCy...")
    total_tokens = contar_tokens(textos)
    print(f"Total de tokens (sin puntuación ni espacios) en todos los TXT: {total_tokens}")
