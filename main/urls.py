from django.urls import path
from . import views

app_name = 'Main'
urlpatterns = [
    path('', views.main, name='index'),
    path('person', views.person, name='person'),
    path('about', views.about, name='about'),
]