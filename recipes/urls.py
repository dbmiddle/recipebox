from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name='recipe-home'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes-list'),
    path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
]
