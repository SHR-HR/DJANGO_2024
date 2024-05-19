from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.show_list, name='list'),
    path('card/', views.show_card, name='card'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
]
