from rest_framework import serializers

from ..helpers.image_sanitize import sanitize_image

from ..entities.Condition import ConditionClause, Condition
from ..entities.Source import Source

from ..mixins.NestedSerializing import NestedSerializer


class ConditionClauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionClause
        fields = '__all__'


class ConditionSerializer(NestedSerializer, serializers.ModelSerializer):
    clauses = ConditionClauseSerializer(many=True)

    class Meta:
        model = Condition
        fields = '__all__'

    def nested_entities(self):
        return [
            {'name': 'clauses', 'model': ConditionClause, 'm2m': False, 'serializer': ConditionClauseSerializer},
            {'name': 'done', 'model': Source, 'm2m': True},
            {'name': 'undone', 'model': Source, 'm2m': True},
            {'name': 'disable', 'model': Condition, 'm2m': True},
            {'name': 'enable', 'model': Condition, 'm2m': True},
            {'name': 'reveal_cost', 'model': Source, 'm2m': True},
            {'name': 'cost', 'model': Source, 'm2m': True},
        ]


