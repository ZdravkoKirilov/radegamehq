from rest_framework import serializers


from ..entities.Condition import ConditionClause, Condition

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
            {'name': 'disable', 'model': Condition, 'm2m': True},
            {'name': 'enable', 'model': Condition, 'm2m': True},
        ]


