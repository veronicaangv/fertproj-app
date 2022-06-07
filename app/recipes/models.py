from django.db import models


class Meal(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FertConcern(models.Model):
    concern = models.CharField(max_length=255)

    def __str__(self):
        return self.concern


class MensePhase(models.Model):
    phase = models.CharField(max_length=255)

    def __str__(self):
        return self.phase


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField(max_length=4100)
    description = models.TextField(max_length=4100, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    fert_concern = models.ForeignKey(
        FertConcern, on_delete=models.CASCADE, null=True)
    mense_phase = models.ForeignKey(
        MensePhase, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
