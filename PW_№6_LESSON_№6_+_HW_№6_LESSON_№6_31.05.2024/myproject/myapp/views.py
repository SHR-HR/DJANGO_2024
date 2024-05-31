from django.shortcuts import render
from .models import Parent

def parent_view(request):
    parents = Parent.objects.all()
    return render(request, 'parents.html', {'parents': parents})
