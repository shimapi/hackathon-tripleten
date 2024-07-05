from django.shortcuts import render
from django.http import JsonResponse
import os
from .scripts.preprocessing import process_csv

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
        
        # Llama al script personalizado para procesar el CSV
        data = process_csv(filepath)
        
        return JsonResponse(data)
    return JsonResponse({'error': 'Invalid request'}, status=400)