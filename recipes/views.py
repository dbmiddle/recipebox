from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from recipes.models import Recipe, Author
from recipes.forms import RecipeAddForm, AuthorAddForm, LoginForm
# Create your views here.


def loginview(request):
    html = 'genericform.html'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('recipe-list'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})


def logoutview(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(reverse('recipe-list'))


def index(request):
    return render(request, 'index.html')


@login_required
def recipeadd(request):
    html = 'genericform.html'

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


@staff_member_required
@login_required
def authoradd(request):
    html = 'genericform.html'
    form = AuthorAddForm()
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
            Author.objects.create(
                user=user,
                name=data["name"],
                bio=data["bio"]
            )
            messages.info(request, "Author created successfully!")
            return HttpResponseRedirect(reverse('recipe-list'))

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
