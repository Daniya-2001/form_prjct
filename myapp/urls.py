from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('form/', views.FormVali, name="formvali"),
    path('Sform', views.SecondForm, name='secondform')
]