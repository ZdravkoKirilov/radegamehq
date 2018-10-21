from rest_framework import serializers
from django.db import transaction

from api.entities.EffectGroup import EffectGroup, EffectGroupItem
from api.helpers.image_sanitize import sanitize_image


class EffectGroupItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EffectGroupItem
        fields = ('id', 'action', 'condition', 'cost', 'quota', 'restriction')


class EffectGroupSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(max_length=None, use_url=True)
    items = EffectGroupItemSerializer(many=True)

    class Meta:
        model = EffectGroup
        fields = (
            'id', 'game', 'name', 'description', 'image', 'keywords', 'mode', 'pick', 'quota', 'min_cap', 'max_cap',
            'random_cap',
            'allow_same_pick', 'items')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(EffectGroupSerializer, self).to_internal_value(data)
        return value

    @transaction.atomic
    def create(self, validated_data):
        items = validated_data.pop('items')

        group = EffectGroup(**validated_data)
        self.upsert_items(items, group)

        return group

    @transaction.atomic
    def update(self, instance: EffectGroup, validated_data):
        items = validated_data.pop('items')

        instance.__dict__.update(**validated_data)
        self.upsert_items(items, instance)
        instance.save()

        return instance

    @classmethod
    def upsert_items(cls, items, group: EffectGroup):

        for item in items:
            cls.upsert_item(item, group)

    @classmethod
    def upsert_item(cls, item, group: EffectGroup):
        try:
            existing = EffectGroupItem.objects.get(pk=item['id'])
            existing.__dict__.update(**item, owner=group)
            existing.save()
            return existing
        except (EffectGroupItem.DoesNotExist, KeyError):
            return EffectGroupItem(**item, owner=group)
