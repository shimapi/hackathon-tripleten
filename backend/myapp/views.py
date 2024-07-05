from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import os

# Asegúrate de que la carpeta de cargas exista
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if not file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)
        if not file.name.endswith('.csv'):
            return JsonResponse({'error': 'File is not CSV format'}, status=400)
        
        filepath = os.path.join(UPLOAD_FOLDER, file.name)
        with open(filepath, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        # Leer el archivo CSV con pandas
        df = pd.read_csv(filepath)
        
        # Procesar el DataFrame (aquí puedes añadir tu lógica de procesamiento)
        # Por ejemplo, convertir el DataFrame a JSON y enviarlo de vuelta al cliente
        data = df.head().to_dict()
        
        return JsonResponse(data)
    return JsonResponse({'error': 'Invalid request'}, status=400)