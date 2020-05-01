from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from recipes.models import Recipe, Author
# Create your views here.


def index(request):
    return render(request, 'index.html')


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes_list'


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
