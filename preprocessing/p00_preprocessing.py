#%% ################################################# Importar librerias ################################################################################
import chardet
import pandas as pd
from functions.functions import cluster_similar_descriptions, determine_canonical_form, fill_missing_descriptions, normalize_descriptions # Funciones locales
#%% ################################################# Lectura de datos ##################################################################################

# Abre el archivo en modo binario para detectar su encoding
with open('../datasets/input/Online_Retail.csv', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

# Lectura del dataset 
df_online_retail = pd.read_csv('../datasets/input/Online_Retail.csv', encoding=encoding)
#%% ################################################# Limpieza de datos ###########################################################################################

# Pasar el nombre de las columnas a mínusculas y dejarlo en snake_case
df_online_retail.columns = df_online_retail.columns.str.lower()

################################################# Tratamiento de valores ausentes ##################################################################################
df_online_retail_cleaned = df_online_retail.copy()
# Se recuperaran algunos valores ausentes de description usando el stock_code
# Crear el diccionario de mapeo de stock_code a description
mapping_dict = df_online_retail.dropna(subset=['description']).drop_duplicates(subset=['stock_code']).set_index('stock_code')['description'].to_dict()

# Aplicar la función para rellenar las descripciones faltantes
df_online_retail['description'] = df_online_retail.apply(fill_missing_descriptions, axis=1, args=(mapping_dict,))

df_online_retail_cleaned = df_online_retail_cleaned.dropna(subset=['description'])   # Para la columna descripcion se elimininaran al ser solo el 0.2% de los datos. 
df_online_retail_cleaned = df_online_retail_cleaned.fillna('unknown')                # Para la columna customer_id se reemplazaran por la palabra unknown

################################################# Eliminar cadenas vacías en description ###########################################################################

# Eliminar caracteres especiales usando una expresión regular
df_online_retail_cleaned['description'] = df_online_retail_cleaned['description'].str.replace(r'[^A-Za-z0-9\s]', '', regex=True)

# Limpiar la columna 'description' eliminando espacios en blanco y convirtiendo None a cadenas vacías
df_online_retail_cleaned['description'] = df_online_retail_cleaned['description'].str.strip()

# Encontrar cadenas vacías
empty_strings = df_online_retail_cleaned[df_online_retail_cleaned['description'] == '']

# Remplazar cadenas vacias por unknown
df_online_retail_cleaned = df_online_retail_cleaned.replace('','unknown')

################################################# Cambiar el tipo de dato #########################################################################################
# Pasar la columna invoice_date a tipo datetime
df_online_retail_cleaned['invoice_date'] = pd.to_datetime(df_online_retail_cleaned['invoice_date'])

################################################# Eliminar duplicados #############################################################################################
# Eliminar duplicados explicitos
df_online_retail_cleaned.drop_duplicates(inplace=True)

################################################# Limpieza del texto de las descripciones ##########################################################################

# Normalizar descripciones
df_online_retail_cleaned['normalized_description'] = normalize_descriptions(df_online_retail_cleaned['description'])

# Crear clusters de frases similares
clusters = cluster_similar_descriptions(df_online_retail_cleaned['normalized_description'])

# Crear diccionario de reemplazo automáticamente
replacement_dict = determine_canonical_form(clusters, df_online_retail_cleaned['normalized_description'].tolist())

# Reemplazar las frases en el DataFrame
df_online_retail_cleaned['normalized_description'] = df_online_retail_cleaned['normalized_description'].replace(replacement_dict)
#%% Convertir el dataframe a CSV
df_online_retail_cleaned.to_csv('./datasets/intermediate/df_online_retail_cleaned.csv', index=False)