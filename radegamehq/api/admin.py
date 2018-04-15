from django.contrib import admin

from api.entities.Path import MapPath
from api.entities.Location import MapLocation
from api.entities.Stage import Stage
from api.entities.Trivia import Trivia, TriviaAnswer, TriviaAnswerEffect
from api.entities.Quest import Quest, QuestCost, QuestAward, QuestPenalty, QuestCondition
from api.entities.Field import Field, FieldQuest, FieldActivity, FieldIncome, FieldCost
from api.entities.Resource import Resource
from api.entities.Activity import Activity, ActivityConfig
from api.entities.Round import Round, RoundQuest, RoundCondition, RoundActivity
from api.entities.Faction import Faction, FactionResource
from .entities.Game import Game

admin.site.register(Game)
admin.site.register(Field)
admin.site.register(FieldQuest)
admin.site.register(FieldActivity)
admin.site.register(MapLocation)
admin.site.register(MapPath)
admin.site.register(Resource)
admin.site.register(FieldIncome)
admin.site.register(FieldCost)
admin.site.register(Faction)
admin.site.register(FactionResource)
admin.site.register(Activity)
admin.site.register(ActivityConfig)
admin.site.register(Quest)
admin.site.register(QuestCost)
admin.site.register(QuestAward)
admin.site.register(QuestCondition)
admin.site.register(QuestPenalty)
admin.site.register(Round)
admin.site.register(RoundActivity)
admin.site.register(RoundQuest)
admin.site.register(RoundCondition)
admin.site.register(Trivia)
admin.site.register(TriviaAnswer)
admin.site.register(TriviaAnswerEffect)
admin.site.register(Stage)
