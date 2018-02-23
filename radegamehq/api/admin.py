from django.contrib import admin

from .models import Game, BoardField, MapLocation, \
    MapPath, Resource, FieldIncome, FieldCost, Faction, FactionResource, Round, RoundActivity, RoundQuest, \
    RoundCondition, FieldQuest, FieldActivity, Activity, ActivityConfig, Quest, QuestCost, QuestCondition, QuestAward, \
    QuestPenalty, Trivia, TriviaAnswer, TriviaAnswerEffect, Stage

admin.site.register(Game)
admin.site.register(BoardField)
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
