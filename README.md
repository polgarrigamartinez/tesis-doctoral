# Estudio del cambio léxico y semántico en el lenguaje de la salud mental entre 1850 y 1950 en castellano y alemán: elaboración y explotación de dos corpus especializados a través del concepto de _histeria_

Este repositorio contiene las herramientas de procesamiento de lenguaje natural (PLN) y los datos utilizados en mi investigación doctoral.

## Estructura del Repositorio

* **`clasificador/`**: Contiene los programas de etiquetado morfológico y clasificación semántica.
    * `spacy_pos_tagger.py`: Programa para el etiquetado morfológico (POS tagging) utilizando la librería spaCy.
    * 'tabla_contingencia.py': Programa para la elaboración de tablas de contingencia según la clasificación de usos de cada término.
* **`cálculo_de_frecuencias/`**: Herramientas para el análisis cuantitativo del corpus.
    * `extractor_años.py`: Script diseñado para localizar y extraer menciones temporales/años en el texto.
* **`documentación_corpus/`**: Desglose de textos recopilados para la elaboración de los corpus.
    * `MentEs.xlsx`: Dataset principal (Corpus de Salud Mental en español).
* **`README.md`**: Guía general del proyecto (este archivo).

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.14.3
* **Librerías de PLN:** spaCy (https://spacy.io/)
* **Gestión de Datos:** Microsoft Excel / Pandas

---
*Autor: Pol Garriga Martínez*
