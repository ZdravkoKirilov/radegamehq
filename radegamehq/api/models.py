from django.db import models


class Game(models.Model):
    TYPE_TERRITORY_MAP = 'MAP'
    TYPE_BASIC_GRID = 'BASIC_GRID'

    TYPE_CHOICES = (
        (TYPE_TERRITORY_MAP, 'MAP'),
        (TYPE_BASIC_GRID, 'BASIC_GRID'),
    )

    title = models.CharField(max_length=255, blank=False)
    boardType = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class Resource(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='resource_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)


class Round(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='round_images', blank=True, null=True, max_length=200)
    replay = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class RoundQuest(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='round_quest')
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.round.name, self.quest.name)


class RoundCondition(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='round_condition')
    quest = models.ForeignKey('Quest', on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.round.name, self.quest.name)


class RoundActivity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='round_activity')
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.round.name, self.activity.name)

    class Meta:
        verbose_name_plural = 'Round activities'


class BoardField(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='field_images', blank=True, null=True, max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
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


class MapLocation(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    width = models.FloatField()
    height = models.FloatField()
    left = models.FloatField()
    top = models.FloatField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    field = models.OneToOneField(
        BoardField,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{}".format(self.field.name)


class Map(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='maps', blank=True, null=True, max_length=200)
    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{}".format('Map_') + self.game.title


class MapPath(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    fromLoc = models.ForeignKey(
        MapLocation,
        related_name='from_loc+',
        on_delete=models.CASCADE,
    )
    toLoc = models.ForeignKey(
        MapLocation,
        related_name='to_loc+',
        on_delete=models.CASCADE,
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return "{}".format('From: ' + self.fromLoc.field.name + ' To: ' + self.toLoc.field.name)


class Faction(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='faction_images', blank=True, null=True, max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    resources = models.ManyToManyField(Resource, blank=True, through='FactionResource')
    income = models.ManyToManyField(Resource, blank=True, through='FactionIncome', related_name='faction_income')

    def __str__(self):
        return self.name


class FactionResource(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='faction_resource')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.faction.name, self.resource.name)


class FactionIncome(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='faction_income')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}_{}".format(self.faction.name, self.resource.name)


class Activity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='activity_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = 'Activities'


class ActivityConfig(models.Model):
    ATTACK_FIELD = 'ATTACK_FIELD'
    DEFEND_FIELD = 'DEFEND_FIELD'
    MINE_RESOURCES = 'MINE_RESOURCES'
    CANCEL_ATTACK_FIELD = 'CANCEL_ATTACK_FIELD'
    CANCEL_DEFEND_FIELD = 'CANCEL_DEFEND_FIELD'
    CANCEL_MINE_RESOURCE = 'CANCEL_MINE_RESOURCE'
    ALTER_RESOURCE = 'ALTER_RESOURCE'
    STEAL_QUEST = 'STEAL_QUEST'
    DISCARD_QUEST = 'DISCARD_QUEST'
    DRAW_QUEST = 'DRAW_QUEST'
    STEAL_ACTIVITY = 'STEAL_ACTIVITY'
    DISCARD_ACTIVITY = 'DISCARD_ACTIVITY'
    CANCEL_ACTIVITY = 'CANCEL_ACTIVITY'
    PEEK_QUESTS = 'PEEK_QUESTS'
    PEEK_ACTIVITIES = 'PEEK_ACTIVITIES'

    TYPE_CHOICES = (
        (ATTACK_FIELD, 'ATTACK_FIELD'),
        (DEFEND_FIELD, 'DEFEND_FIELD'),
        (MINE_RESOURCES, 'MINE_RESOURCES'),
        (CANCEL_ATTACK_FIELD, 'CANCEL_ATTACK_FIELD'),
        (CANCEL_DEFEND_FIELD, 'CANCEL_DEFEND_FIELD'),
        (CANCEL_MINE_RESOURCE, 'CANCEL_MINE_RESOURCE'),
        (ALTER_RESOURCE, 'ALTER_RESOURCE'),
        (STEAL_QUEST, 'STEAL_QUEST'),
        (DISCARD_QUEST, 'DISCARD_QUEST'),
        (DRAW_QUEST, 'DRAW_QUEST'),
        (STEAL_ACTIVITY, 'STEAL_ACTIVITY'),
        (DISCARD_ACTIVITY, 'DISCARD_ACTIVITY'),
        (CANCEL_ACTIVITY, 'CANCEL_ACTIVITY'),
        (PEEK_QUESTS, 'PEEK_QUESTS'),
        (PEEK_ACTIVITIES, 'PEEK_ACTIVITIES'),
    )

    TRIGGER = 'TRIGGER'
    PASSIVE = 'PASSIVE'
    HIDDEN = 'HIDDEN'

    MODE_CHOICES = (
        (TRIGGER, 'TRIGGER'),
        (PASSIVE, 'PASSIVE'),
        (HIDDEN, 'HIDDEN'),
    )

    FIELD = 'FIELD'
    PLAYER = 'PLAYER'
    OTHER_PLAYER = 'OTHER_PLAYER'
    SELF = 'SELF'
    ACTIVE_FIELD = 'ACTIVE_FIELD'
    ACTIVE_PLAYER = 'ACTIVE_PLAYER'

    TARGET_CHOICES = (
        (FIELD, 'FIELD'),
        (PLAYER, 'PLAYER'),
        (OTHER_PLAYER, 'OTHER_PLAYER'),
        (SELF, 'SELF'),
        (ACTIVE_FIELD, 'ACTIVE_FIELD'),
        (ACTIVE_PLAYER, 'ACTIVE_PLAYER')
    )

    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    mode = models.CharField(max_length=255, blank=False, choices=MODE_CHOICES)
    target = models.CharField(max_length=255, blank=False, choices=TARGET_CHOICES)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='config')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='config_resource', blank=True,
                                 null=True)
    amount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}".format(self.activity.name, self.type)


class Quest(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='quest_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)


class QuestCost(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_cost')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quest_cost_activity')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Cost_{}_{}".format(self.quest.name, self.activity.name)


class QuestAward(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_award')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quest_award_activity')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Award_{}_{}".format(self.quest.name, self.activity.name)


class QuestPenalty(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_penalty')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quest_pen_activity')

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Penalty_{}_{}".format(self.quest.name, self.activity.name)

    class Meta:
        verbose_name_plural = 'Quest penalties'


class QuestCondition(models.Model):
    CLAIM_FIELD = 'CLAIM_FIELD'
    CLAIM_ANY_FIELDS = 'CLAIM_ANY_FIELDS'
    DEFEND_FIELD = 'DEFEND_FIELD'
    DEFEND_ANY_FIELDS = 'DEFEND_ANY_FIELDS'
    CLAIM_RESOURCE = 'CLAIM_RESOURCE'
    CLAIM_ANY_RESOURCE = 'CLAIM_ANY_RESOURCE'
    STEAL_ACTIVITY = 'STEAL_ACTIVITY'
    STEAL_ANY_ACTIVITY = 'STEAL_ANY_ACTIVITY'
    DISCARD_ACTIVITY = 'DISCARD_ACTIVITY'
    DISCARD_ANY_ACTIVITY = 'DISCARD_ANY_ACTIVITY'
    PLAY_ACTIVITY = 'PLAY_ACTIVITY'
    PLAY_ANY_ACTIVITY = 'PLAY_ANY_ACTIVITY'

    TYPE_CHOICES = (
        (CLAIM_FIELD, 'CLAIM_FIELD'),
        (CLAIM_ANY_FIELDS, 'CLAIM_ANY_FIELDS'),
        (DEFEND_FIELD, 'DEFEND_FIELD'),
        (DEFEND_ANY_FIELDS, 'DEFEND_ANY_FIELDS'),
        (CLAIM_RESOURCE, 'CLAIM_RESOURCE'),
        (CLAIM_ANY_RESOURCE, 'CLAIM_ANY_RESOURCE'),
        (STEAL_ACTIVITY, 'STEAL_ACTIVITY'),
        (STEAL_ANY_ACTIVITY, 'STEAL_ANY_ACTIVITY'),
        (DISCARD_ACTIVITY, 'DISCARD_ACTIVITY'),
        (DISCARD_ANY_ACTIVITY, 'DISCARD_ANY_ACTIVITY'),
        (PLAY_ACTIVITY, 'PLAY_ACTIVITY'),
        (PLAY_ANY_ACTIVITY, 'PLAY_ANY_ACTIVITY'),
    )

    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)
    owner = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_condition')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_condition_quest', blank=True,
                              null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='quest_condition_activity',
                                 blank=True,
                                 null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='quest_cond_resource', blank=True,
                                 null=True)
    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='quest_cond_field', blank=True,
                              null=True)
    byRound = models.ForeignKey(Round, blank=True, null=True, related_name='quest_cond_byRound',
                                on_delete=models.SET_NULL)
    atRound = models.ForeignKey(Round, blank=True, null=True, related_name='quest_cond_atRound',
                                on_delete=models.SET_NULL)
    amount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Condition_{}_{}".format(self.owner.name, self.type)


class Trivia(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='trivia_images', blank=True, null=True, max_length=200)
    mode = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class TriviaAnswer(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name='trivia_answer')
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='trivia_answer_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)


class TriviaAnswerEffect(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    answer = models.ForeignKey(TriviaAnswer, on_delete=models.CASCADE, related_name='trivia_answer_effect')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}_{}".format(self.answer.name, self.activity.name, self.id)
