from django.urls import path
from person import views



app_name = 'person'


urlpatterns = [
    path('', views.index, name='person'),
    path('license/', views.license, name='license'),
]
