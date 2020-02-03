from django.shortcuts import render
from .models import AdminProfile


def home(request):
    context = {
        'admin': AdminProfile.objects.all()
    }
    return render(request, 'home.html', context)


def about(request):
    context = {
        'admin': AdminProfile.objects.all()
    }
    return render(request, 'about.html', context)
