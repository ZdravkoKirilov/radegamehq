from rest_framework import serializers

from ..helpers.image_sanitize import sanitize_image
from .custom_serializers import Base64ImageField

from ..entities.Condition import ConditionClause, Condition
from ..entities.Source import Source

from api.mixins.NestedSerializing import NestedSerializer


class ConditionClauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionClause
        fields = (
            'id', 'type', 'target_entity', 'condition', 'action', 'resource', 'field', 'faction', 'token', 'choice',
            'keywords',
            'amount', 'round', 'phase', 'stage', 'relation')


class ConditionSerializer(NestedSerializer, serializers.ModelSerializer):
    clauses = ConditionClauseSerializer(many=True)
    image = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = Condition
        fields = (
            'id', 'game', 'name', 'description', 'keywords', 'image', 'stage', 'restricted', 'allowed', 'award',
            'penalty', 'mode', 'clauses')

    def nested_entities(self):
        return [
            {'name': 'clauses', 'model': ConditionClause, 'm2m': False, 'serializer': ConditionClauseSerializer},
            {'name': 'done', 'model': Source, 'm2m': True},
            {'name': 'undone', 'model': Source, 'm2m': True},
            {'name': 'restricted', 'model': Condition, 'm2m': True},
            {'name': 'allowed', 'model': Condition, 'm2m': True},
        ]

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(ConditionSerializer, self).to_internal_value(data)
        return value
