import spacy
from collections import defaultdict
import os

def cargar_textos_desde_carpeta(carpeta):
    """
    Carga todos los textos .txt de una carpeta y los almacena en un diccionario con el nombre del archivo como clave.
    """
    textos = {}
    for archivo in sorted(os.listdir(carpeta)):  # Ordenar archivos alfabéticamente
        if archivo.endswith(".txt"):
            with open(os.path.join(carpeta, archivo), "r", encoding="utf-8") as f:
                textos[archivo] = f.read()
    return textos

def procesar_textos(textos, max_chars=1_000_000):
    """
    Procesa cada archivo individualmente con spaCy y almacena las oraciones junto con el nombre del documento.
    """
    nlp = spacy.load("de_core_news_lg")
    nlp.max_length = max_chars  # Límite de procesamiento por fragmento

    palabras_por_categoria = defaultdict(list)

    for archivo, texto in textos.items():
        # Dividir el texto en fragmentos para evitar errores de memoria
        fragmentos = [texto[i:i+max_chars] for i in range(0, len(texto), max_chars)]
        
        for i, fragmento in enumerate(fragmentos):
            print(f"Procesando '{archivo}', fragmento {i+1} de {len(fragmentos)}...")
            doc = nlp(fragmento)
            
            for sent in doc.sents:
                for token in sent:
                    palabras_por_categoria[(token.lemma_.lower(), token.pos_)].append((archivo, sent.text))
    
    return palabras_por_categoria

def buscar_oraciones(lema, categorias, palabras_por_categoria):
    """
    Dado un lema y una o varias categorías gramaticales,
    devuelve las oraciones en las que aparece junto con el nombre del documento.
    """
    oraciones = []
    for categoria in categorias:
        oraciones.extend(palabras_por_categoria.get((lema.lower(), categoria), []))
    return sorted(oraciones)  # Ordenar por nombre del archivo

if __name__ == "__main__":
    carpeta = "/Users/martagcasado/Desktop/corpus_alemany"  # Ruta de la carpeta con los archivos de entrada
    textos = cargar_textos_desde_carpeta(carpeta)

    print("Textos cargados y procesando con spaCy...")
    palabras_por_categoria = procesar_textos(textos)
    print("Procesamiento completado.")

    # Lema y categoría que queremos buscar
    lema = "hysterisch"
    categorias = ["ADJ"]

    oraciones = buscar_oraciones(lema, categorias, palabras_por_categoria)

    # Guardar resultados en archivo
    ruta_salida = "resultados_hysterisch_adj.txt"
    with open(ruta_salida, "w", encoding="utf-8") as f:
        if oraciones:
            f.write(f"Se encontraron {len(oraciones)} oraciones con '{lema}' como {categorias}:\n\n")
            for archivo, oracion in oraciones:
                f.write(f"{archivo}: {oracion.strip()}\n\n")
        else:
            f.write(f"No se encontraron oraciones con '{lema}' como {categorias}.\n")

    print(f"Resultados guardados en '{ruta_salida}'.")


