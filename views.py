from django.shortcuts import render, get_object_or_404, redirect
from .models import Amenity
from .forms import AmenityForm, AmenityImageForm
import logging
import requests
import os
from django.conf import settings
from django.contrib import messages

logger = logging.getLogger(__name__)


def amenity_detail(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    
    if request.method == 'POST':
        if 'image' in request.FILES:
            form = AmenityImageForm(request.POST, request.FILES, instance=amenity)
            if form.is_valid():
                form.save()
                messages.success(request, 'Изображение загружено успешно.')
                return redirect('amenity_detail', pk=amenity.pk)
        elif 'delete_image' in request.POST:
            amenity.image.delete()
            messages.success(request, 'Изображение удалено успешно.')
            return redirect('amenity_detail', pk=amenity.pk)
        elif 'file' in request.FILES:
            amenity.file = request.FILES.get('file')
            amenity.save()
            messages.success(request, 'Файл загружен успешно.')
            return redirect('amenity_detail', pk=amenity.pk)
        elif 'delete_file' in request.POST:
            amenity.file.delete()
            messages.success(request, 'Файл удален успешно.')
            return redirect('amenity_detail', pk=amenity.pk)
    
    return render(request, 'amenity_detail.html', {'amenity': amenity})


def upload_image(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    if request.method == 'POST':
        form = AmenityImageForm(request.POST, request.FILES, instance=amenity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изображение загружено успешно.')
            return redirect('amenity_detail', pk=amenity.pk)
    else:
        form = AmenityImageForm(instance=amenity)
    return render(request, 'upload_image.html', {'form': form})

# Удаление изображения с отображением сообщения об успешном удалении
def delete_image(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    if request.method == 'POST':
        if amenity.image:
            amenity.image.delete()
            messages.success(request, 'Изображение удалено успешно.')
        else:
            messages.error(request, 'Изображение не найдено.')
        return redirect('amenity_detail', pk=amenity.pk)
    return render(request, 'amenity_detail.html', {'amenity': amenity})

# Удаление файла с отображением сообщения об успешном удалении
def delete_file(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    if request.method == 'POST':
        if amenity.file:
            amenity.file.delete()
            messages.success(request, 'Файл удален успешно.')
        else:
            messages.error(request, 'Файл не найден.')
        return redirect('amenity_detail', pk=amenity.pk)
    return render(request, 'amenity_detail.html', {'amenity': amenity})


def amenity_list(request):
    amenities = Amenity.objects.all()
    logger.info(f"Загружены {amenities.count()} удобств(о)")
    return render(request, 'amenity_list.html', {'amenities': amenities})


def add_amenity(request):
    if request.method == 'POST':
        form = AmenityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Удобство добавлено успешно.')
            return redirect('amenity_list')
    else:
        form = AmenityForm()
    return render(request, 'add_amenity.html', {'form': form})


def amenity_cards(request):
    amenities = Amenity.objects.all()
    return render(request, 'amenity_cards.html', {'amenities': amenities})


def amenity_ul_list(request):
    amenities = Amenity.objects.all()
    return render(request, 'amenity_ul_list.html', {'amenities': amenities})


def fetch_data(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, verify=False)
    data = response.json()
    return render(request, 'your_template.html', {'data': data})

# Низкоуровневое сохранение файла
def save_amenity_file(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    if request.method == 'POST' and 'file' in request.FILES:
        file = request.FILES['file']
        file_path = os.path.join(settings.MEDIA_ROOT, 'amenities/files', file.name)
        
        # Низкоуровневое сохранение файла
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        amenity.file = file_path
        amenity.save()
        messages.success(request, 'Файл сохранен успешно.')
        return redirect('amenity_detail', pk=amenity.pk)

    return render(request, 'upload_file.html', {'amenity': amenity})

