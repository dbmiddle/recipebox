from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='recipe-home'),
    path('details', views.details, name='recipe-details'),
    path('author', views.author, name='recipe-author')
]
