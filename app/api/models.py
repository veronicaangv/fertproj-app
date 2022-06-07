from django.db import models
from tastypie.resources import ModelResource
from recipes.models import Recipe



class RecipeResource(ModelResource):
    class Meta:
        queryset = Recipe.objects.all()
        resource_name = 'recipes'
