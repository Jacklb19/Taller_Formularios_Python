from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.solicitud_view, name='solicitud_form'),
    path('confirmacion/', views.solicitud_confirmacion, name='solicitud_confirmacion'),
]
