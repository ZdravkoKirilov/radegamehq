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


class Action(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    image = models.FileField(upload_to='action_images', blank=True, null=True, max_length=200)

    def __str__(self):
        return "{}".format(self.name)


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
    type = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_cost')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_cost_quest', blank=True, null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='quest_cost_action', blank=True,
                               null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='quest_cost_resource', blank=True,
                                 null=True)
    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='quest_cost_field', blank=True,
                              null=True)
    amount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}".format(self.action.name, self.type)


class QuestCondition(models.Model):
    type = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_condition')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_condition_quest', blank=True,
                              null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='quest_condition_action', blank=True,
                               null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='quest_cond_resource', blank=True,
                                 null=True)
    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='quest_cond_field', blank=True,
                              null=True)
    amount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}".format(self.action.name, self.type)


class QuestAward(models.Model):
    type = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_award')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_award_quest', blank=True, null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='quest_award_action', blank=True,
                               null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='quest_award_resource', blank=True,
                                 null=True)
    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='quest_award_field', blank=True,
                              null=True)
    minAmount = models.IntegerField(blank=True, null=True)
    maxAmount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}".format(self.action.name, self.type)


class QuestPenalty(models.Model):
    type = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_penalty')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quest_pen_quest', blank=True,
                              null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='quest_pen_action', blank=True, null=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='quest_pen_resource', blank=True,
                                 null=True)
    field = models.ForeignKey(BoardField, on_delete=models.CASCADE, related_name='quest_pen_field', blank=True,
                              null=True)
    minAmount = models.IntegerField(blank=True, null=True)
    maxAmount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}".format(self.action.name, self.type)


class ActionConfig(models.Model):
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
    action = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='config')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='config_resource', blank=True,
                                 null=True)
    amount = models.IntegerField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}".format(self.action.name, self.type)


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
