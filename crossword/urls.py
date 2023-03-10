from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.crossword_creation_form),
    path('result/<str:data>', views.get_result_page),
]