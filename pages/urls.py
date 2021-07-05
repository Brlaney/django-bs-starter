# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    # path('<str:slug>/', views.navLink, name='navLink'),
]
