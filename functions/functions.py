#%% ################################################# Importaciones #########################################################################################
# Importaciones del sistema
from collections import defaultdict

# Importaciones para procesamiento de texto y comparación difusa
from fuzzywuzzy import process, fuzz

# Importaciones para procesamiento de lenguaje natural (NLP)
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Descargar recursos de nltk necesarios
nltk.download('wordnet')
nltk.download('omw-1.4')
#%% ################################################# Funciones #########################################################################################
def normalize_descriptions(descriptions):
    ''' 
    Normaliza descripciones convirtiéndolas a minúsculas y lematizándolas.
    
    Args:
    descriptions (list): Lista de descripciones a normalizar.
    
    Returns:
    list: Lista de descripciones normalizadas y lematizadas.
    
    Esta función convierte cada descripción a minúsculas, divide las palabras,
    y luego aplica lematización utilizando el lematizador de WordNet para 
    convertir cada verbo a su forma base.
    '''
    lemmatizer = WordNetLemmatizer()
    normalized_descriptions = []
    for desc in descriptions:
        words = desc.lower().split()
        lemmatized_words = [lemmatizer.lemmatize(word, wordnet.VERB) for word in words]
        normalized_descriptions.append(' '.join(lemmatized_words))
    return normalized_descriptions

# Función para encontrar posibles errores de tipeo y agruparlas en clusters
def cluster_similar_descriptions(descriptions, threshold=90):
    ''' 
    Agrupa descripciones similares en clusters basados en la similitud de texto.

    Args:
    descriptions (list): Lista de descripciones a agrupar.
    threshold (int, optional): Umbral de similitud mínimo para considerar una coincidencia. 
                               Valor por defecto es 90.

    Returns:
    defaultdict: Diccionario con las descripciones originales como claves y listas 
                 de descripciones similares como valores.

    Esta función encuentra y agrupa descripciones similares en clusters utilizando 
    el algoritmo FuzzyWuzzy. Para cada descripción única, encuentra coincidencias 
    con otras descripciones en la lista basadas en el puntaje de similitud (ratio). 
    Las descripciones que superan el umbral especificado se agrupan bajo una misma clave.
    '''
    unique_descriptions = list(set(descriptions))
    clusters = defaultdict(list)
    visited = set()

    for desc in unique_descriptions:
        if desc in visited:
            continue
        matches = process.extract(desc, unique_descriptions, scorer=fuzz.ratio)
        cluster = [match[0] for match in matches if match[1] >= threshold]
        for item in cluster:
            visited.add(item)
        clusters[desc].extend(cluster)
    return clusters

# Determinar la versión canónica para cada cluster (la más frecuente)
def determine_canonical_form(clusters, descriptions):
    ''' 
    Determina la forma canónica para cada cluster de descripciones.

    Args:
    clusters (dict): Diccionario donde las claves son las descripciones originales y 
                     los valores son listas de descripciones similares agrupadas.
    descriptions (list): Lista completa de todas las descripciones.

    Returns:
    dict: Diccionario de reemplazo donde las claves son las descripciones similares 
          y los valores son sus formas canónicas correspondientes.

    Esta función recorre cada cluster de descripciones similares y determina la forma 
    canónica para cada uno. La forma canónica es la descripción más frecuente dentro 
    del cluster, calculada a partir de la lista completa de todas las descripciones.
    '''
    replacement_dict = {}
    for key, cluster in clusters.items():
        canonical_form = max(set(cluster), key=descriptions.count)
        for item in cluster:
            replacement_dict[item] = canonical_form
    return replacement_dict