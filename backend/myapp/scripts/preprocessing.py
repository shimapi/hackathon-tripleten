import pandas as pd

def process_csv(filepath):
    # Lee el archivo CSV
    df = pd.read_csv(filepath)
    
    # Realiza algún procesamiento (aquí puedes añadir tu lógica personalizada)
    processed_data = df.head().to_dict()
    
    return processed_data