from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.detail import View
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



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
        # current_user = Author.objects.get(id=request.user.id)
        context = super(DetailView, self).get_context_data(**kwargs)
        context['personal_recipe_list'] = Recipe.objects.all()
        return context

    # def get(self, request, *args, **kwargs):
    #     author_ = Author.objects.get(id=request.user.id)
    #     favorites = author_.favorite.all()
    #     return render(request, 'recipes/author_detail.html', {'favorites': favorites})


class EditRecipe(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        data = Recipe.objects.get(id=kwargs.get('id'))
        form = EditRecipeForm(request.POST, instance=data)
        form.save()
        return HttpResponseRedirect(reverse('recipe-detail', args=(data.id,)))

    def get(self, request, *args, **kwargs):
        data = Recipe.objects.get(id=kwargs.get('id'))
        form = EditRecipeForm(instance=data)
        return render(request, 'recipes/edit_recipe_form.html', {'form': form, 'data': data})


@login_required
def favorite(request, id):
    recipe_to_favorite = Recipe.objects.get(id=id)
    author = Author.objects.get(id=request.user.id)
    author.favorite.add(recipe_to_favorite)
    author.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# def author(request, author_id):
#     author = Author.objects.get(id=author_id)
#     favorites = author.favorite.all()
#     return render(request, 'recipes/author_detail.html', {'favorites': favorites})
