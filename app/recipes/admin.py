from django.contrib import admin
from .models import Meal, FertConcern, MensePhase, Recipe


class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class FertConcernAdmin(admin.ModelAdmin):
    list_display = ('id', 'concern')


class MensePhaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'phase')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fert_concern', 'mense_phase')


admin.site.register(Meal, MealAdmin)
admin.site.register(FertConcern, FertConcernAdmin)
admin.site.register(MensePhase, MensePhaseAdmin)
admin.site.register(Recipe, RecipeAdmin)