from django.db import models

from api.mixins.EntityBase import EntityBase

TYPE_CHOICES = (
    ('CLAIM', 'CLAIM'),
    ('REACH', 'REACH'),
    ('MEET', 'MEET'),
    ('AVOID', 'AVOID'),
    ('COMPLETE', 'COMPLETE'),
    ('PLAY', 'PLAY'),
    ('PLAY_MAX', 'PLAY_MAX'),
    ('HAVE', 'HAVE'),
    ('HAVE_MAX', 'HAVE_MAX'),
    ('HAVE_MORE', 'HAVE_MORE'),
    ('HAVE_LESS', 'HAVE_LESS'),
    ('IS', 'IS'),
    ('IS_BEFORE', 'IS_BEFORE'),
    ('IS_AFTER', 'IS_AFTER'),
)

RELATIONS = (
    ('AND', 'AND'),
    ('OR', 'OR'),
    ('NOT', 'NOT')
)

CONDITION_MODES = (
    ('TRAP', 'TRAP'),
    ('TRIGGER', 'TRIGGER'),
    ('HYBRID', 'HYBRID'),  # both trap and trigger
    ('PASSIVE', 'PASSIVE'),
    ('AUTO', 'AUTO')  # for internal, 'hidden' logic
)

ENTITY_TYPES = (
    ('FACTION', 'FACTION'),
    ('TOKEN', 'TOKEN'),
    ('CONDITION', 'CONDITION'),
    ('ACTION', 'ACTION'),
    ('ROUND', 'ROUND'),
    ('PHASE', 'PHASE'),
    ('CHOICE', 'CHOICE'),
    ('FIELD', 'FIELD'),
    ('STAGE', 'STAGE'),
    ('TEAM', 'TEAM'),
    ('RESOURCE', 'RESOURCE'),
    ('LOCATION', 'LOCATION'),
)


class Condition(EntityBase):
    image = models.ImageField(upload_to='condition_images', blank=True, null=True, max_length=255)

    mode = models.CharField(max_length=255, choices=CONDITION_MODES, default=CONDITION_MODES[1][1])

    stage = models.ForeignKey('Stage', on_delete=models.CASCADE, blank=True, null=True)

    done = models.ManyToManyField('Source', related_name='condition_award', blank=True)
    undone = models.ManyToManyField('Source', related_name='condition_penalty', blank=True)

    restricted = models.ManyToManyField('Condition', related_name='condition_restricted', blank=True)
    allowed = models.ManyToManyField('Condition', related_name='condition_allowed',
                                     blank=True)

    def __str__(self) -> str:
        return "{}".format(self.name)


class ConditionClause(models.Model):
    owner = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='clauses', blank=True, null=True)

    type = models.CharField(max_length=255, blank=False, choices=TYPE_CHOICES)

    target_entity: models.CharField(max_length=255, blank=True, null=True, choices=ENTITY_TYPES)

    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='clause_condition',
                                  blank=True, null=True)
    action = models.ForeignKey('Action', on_delete=models.CASCADE,
                               blank=True, null=True)
    token = models.ForeignKey('Token', on_delete=models.CASCADE, blank=True, null=True)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE, blank=True, null=True)
    faction = models.ForeignKey('Faction', on_delete=models.CASCADE, blank=True,
                                null=True)
    field = models.ForeignKey('Field', on_delete=models.CASCADE, blank=True,
                              null=True)
    phase = models.ForeignKey('Phase', on_delete=models.CASCADE, blank=True, null=True)
    round = models.ForeignKey('Round', on_delete=models.CASCADE, blank=True, null=True)
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE, blank=True, null=True)

    keywords = models.CharField(null=True, blank=True, max_length=255)

    amount = models.IntegerField(blank=True, null=True)

    relation = models.TextField(choices=RELATIONS, default=RELATIONS[0][0])

    def __str__(self):
        return "Condition_{}_{}".format(self.owner.name, self.type)

# Do something at X round => can be done by composing 2 clauses: 1) the doing and 2) the circumstance
