# Preprocessing

## p00_preprocessing.py

**Descripción** 
Este script de Python realiza el proceso de limpieza de datos para un dataset de ventas en línea (Online_Retail.csv). A continuación, se detallan los pasos realizados y cómo usar el script.

Pasos Realizados
1. Importación de Librerías
Se importan las librerías necesarias para el procesamiento de datos, incluyendo funciones locales para el clustering y normalización de descripciones.

2. Lectura de Datos
Se detecta automáticamente el encoding del archivo CSV y se lee el dataset (Online_Retail.csv) usando Pandas.

3. Limpieza de Datos
- Tratamiento de Valores Ausentes
- Se eliminan las filas donde la columna description es NaN, representando solo el 0.2% de los datos.
- Se reemplazan los valores NaN en la columna customer_id con la palabra 'unknown'.
- Eliminación de Cadenas Vacías en Descripción
- Se eliminan caracteres especiales y se limpian espacios en blanco en la columna description.
- Se identifican y reemplazan las cadenas vacías en description con 'unknown'.
- Cambio del tipo de Dato de las columnas
- Se convierte la columna invoice_date a tipo datetime.
- Eliminación de Duplicados
- Se eliminan duplicados explícitos basados en todas las columnas del DataFrame.
- Limpieza del Texto de las Descripciones
    - Se normalizan las descripciones convirtiéndolas a minúsculas y lematizándolas.
    - Clustering de Descripciones Similares
    - Se agrupan las descripciones similares en clusters usando el algoritmo FuzzyWuzzy.
    - Determinación de Forma Canónica
    - Se determina la forma canónica (más frecuente) para cada cluster de descripciones similares.
4. Conversión a CSV
El DataFrame limpiado y procesado se guarda como df_online_retail_cleaned.csv sin incluir el índice. Contiene las columnas con la descripción original como la descripción limpia. Para que en analisis posteriores si es necesario comparar, se realice de forma mas simple.

**Uso del Script**
1) Asegúrate de tener instaladas las librerías necesarias mencionadas en requirements.txt.

2) Ejecuta el script clean_data.py. Asegúrate de ajustar las rutas de los archivos según sea necesario.

3) El script realizará automáticamente todos los pasos de limpieza y procesamiento de datos descritos anteriormente.