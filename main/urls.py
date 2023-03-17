from django.urls import path
from . import views

app_name = 'Main'
urlpatterns = [
    path('', views.main, name='index'),
    path('person-<int:pk>', views.person, name='person'),
    path('author', views.author, name='author'),
    path('about', views.about, name='about'),
]