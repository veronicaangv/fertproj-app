from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})


def detail(request, recipe_id):

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})
