# Estudio del cambio léxico y semántico en el lenguaje de la salud mental entre 1850 y 1950 en castellano y alemán: elaboración y explotación de dos corpus especializados a través del concepto de _histeria_

Este repositorio contiene las herramientas de procesamiento de lenguaje natural (PLN) y los datos utilizados en mi investigación doctoral.

## Estructura del Repositorio

* **`clasificador/`**: Contiene los programas de etiquetado morfológico y clasificación semántica.
    * `spacy_pos_tagger.py`: Programa para el etiquetado morfológico (POS tagging) utilizando la librería spaCy.
    * `tabla_contingencia.py`: Programa para la elaboración de tablas de contingencia según la clasificación de usos de cada término.
* **`cálculo_de_frecuencias/`**: Herramientas para el análisis cuantitativo del corpus.
    * `extractor_años.py`: Programa diseñado para localizar y extraer el año de publicación de cada obra.
    * `token_count.py`: Programa diseñado para tokenizar y extraer el total de tokens de cada corpus.
    * `token_count_cuartos.py`: Programa diseñado para tokenizar y extraer el total de tokens de cada cuarto de siglo.
    * `token_count_decadas.py`: Programa diseñado para tokenizar y extraer el total de tokens de cada década.
* **`documentación_corpus/`**: Desglose de textos recopilados para la elaboración de los corpus.
    * `MentEs.xlsx`: Corpus especializado en español.
    * `DeMens.xlsx`: Corpus especializado en alemán.
    * `español_contraste.xlsx`: Corpus general en español.
    * `alemán_contraste.xlsx`: Corpus general en alemán.
* **`README.md`**: Guía general del proyecto (este archivo).

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.14.3
* **Librería de PLN:** spaCy (https://spacy.io/)
* **Gestión de Datos:** Microsoft Excel / Pandas / PyTorch

---
*Autor: Pol Garriga Martínez y Marta Garcia-Casado*
