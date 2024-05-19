from django.shortcuts import render
import requests
import random

def random_features():
    features = [
        "Функция автоматического сохранения",
        "Интеграция с внешними API",
        "Расширенные аналитические возможности",
        "Поддержка многопользовательского доступа",
        "Облачные решения для хранения данных"
    ]
    return random.choice(features)

def features(request):
    feature_description = random_features()
    return render(request, 'myapp/features.html', {'feature': feature_description})

def home(request):
    return render(request, 'myapp/home.html')

def show_list(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json() if response.status_code == 200 else []
    print(posts)  # Это временно, для отладки. Убедитесь, что данные приходят корректно.
    return render(request, 'myapp/list.html', {'items': posts})

def show_card(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json() if response.status_code == 200 else []
    print(users)  # Это временно, для отладки. Убедитесь, что данные приходят корректно.
    return render(request, 'myapp/card.html', {'items': users})

def random_pricing():
    plans = [
        {"name": "Базовый", "price": "100$", "description": "Основные функции без ограничений по времени."},
        {"name": "Профессиональный", "price": "200$", "description": "Расширенные функции и аналитика."},
        {"name": "Премиум", "price": "300$", "description": "Все возможные функции и премиум поддержка."}
    ]
    return random.choice(plans)

def pricing(request):
    pricing_plan = random_pricing()
    return render(request, 'myapp/pricing.html', {'plan': pricing_plan})
