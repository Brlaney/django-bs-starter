# pages/views.py
from django.shortcuts import render, redirect
# from .forms import ContactForm
from .models import Page
# from django.views import generic

# Homepage//landing-page//index
def home(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'pages/index.html', context)

# Dynamic routing for navbar links
# def navLink(request, slug):
#     pages = Page.objects.all()
#     page = Page.objects.get(slug=slug)
#     context = {'pages': pages, 'page': page}
#     return render(request, 'pages/navLink.html', context)
