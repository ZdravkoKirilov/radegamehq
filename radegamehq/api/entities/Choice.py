from django.db import models

from ..mixins.EntityBase import EntityBase, WithKeywords, WithFrame, WithImage


class Choice(EntityBase, WithKeywords, WithImage):
    chances = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='choice_chances')
    time = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='choice_time')
    options_filter = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='choice_options_filter')
    scope = models.ForeignKey('Expression', on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='choice_scope')

    def __str__(self):
        return "{}".format(self.name)


class ChoiceFrame(WithFrame):
    owner = models.ForeignKey(Choice, blank=True, null=True, on_delete=models.CASCADE, related_name='frames')


class ChoiceTip(WithKeywords):
    owner = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='tips', null=True, blank=True)

    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey('ImageAsset', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "Tip{}_{}".format(self.id, self.owner.name)


class ChoiceOption(WithKeywords):
    owner = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='options', null=True, blank=True)

    name = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(blank=True, null=True)

    image = models.ForeignKey('ImageAsset', blank=True, null=True, on_delete=models.SET_NULL)

    effect = models.ForeignKey('Expression', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Option_{}_{}".format(self.id, self.owner.name)
