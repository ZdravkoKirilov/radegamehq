from django.db import models

from api.entities.Game import Game
from api.entities.Resource import Resource


class BoardField(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='field_images', blank=True, null=True, max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    income = models.ManyToManyField(Resource, blank=True, through='FieldIncome', related_name='_income')
    cost = models.ManyToManyField(Resource, blank=True, through='FieldCost', related_name='_cost')

    def __str__(self):
        return "{}".format(self.name)


class FieldQuest(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='field_quest')
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.field.name, self.quest.name)


class FieldActivity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='field_activity')
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.field.name, self.activity.name)

    class Meta:
        verbose_name_plural = 'Field activities'


class FieldIncome(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='field_income')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.field.name, self.resource.name)


class FieldCost(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='field_cost')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.field.name, self.resource.name)