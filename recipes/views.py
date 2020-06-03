from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.detail import View
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect


from recipes.models import Recipe, Author
from recipes.forms import EditRecipeForm
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

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['personal_recipe_list'] = Recipe.objects.all()
        return context


class EditRecipe(View):

    def post(self, request, *args, **kwargs):
        data = Recipe.objects.get(id=kwargs.get('id'))
        form = EditRecipeForm(request.POST, instance=data)
        form.save()
        return HttpResponseRedirect(reverse('recipe-detail', args=(data.id,)))

    def get(self, request, *args, **kwargs):
        data = Recipe.objects.get(id=kwargs.get('id'))
        form = EditRecipeForm(instance=data)
        return render(request, 'recipes/edit_recipe_form.html', {'form': form, 'data': data})
