from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from recipes.models import Recipe, Author
from recipes.forms import RecipeAddForm, AuthorAddForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def recipeadd(request):
    html = 'recipeaddform.html'

    if request.method == "POST":
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('recipe-list'))

    form = RecipeAddForm()
    return render(request, html, {"form": form})


def authoradd(request):
    html = 'authoraddform.html'

    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"]
            )
            return HttpResponseRedirect(reverse('recipe-list'))

    form = AuthorAddForm()
    return render(request, html, {"form": form})


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes_list'


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['personal_recipe_list'] = Recipe.objects.all()
        return context
