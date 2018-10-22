from rest_framework import serializers
from django.db import transaction

from api.entities.Pool import Pool, PoolItem
from api.helpers.image_sanitize import sanitize_image


class PoolItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolItem
        fields = ('id', 'action', 'condition', 'cost', 'quota', 'restriction')


class PoolSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(max_length=None, use_url=True)
    items = PoolItemSerializer(many=True)

    class Meta:
        model = Pool
        fields = (
            'id', 'game', 'name', 'description', 'image', 'keywords', 'mode', 'pick', 'quota', 'min_cap', 'max_cap',
            'random_cap',
            'allow_same_pick', 'items')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(PoolSerializer, self).to_internal_value(data)
        return value

    @transaction.atomic
    def create(self, validated_data):
        items = validated_data.pop('items')

        group = Pool(**validated_data)
        self.upsert_items(items, group)

        return group

    @transaction.atomic
    def update(self, instance: Pool, validated_data):
        items = validated_data.pop('items')

        instance.__dict__.update(**validated_data)
        self.upsert_items(items, instance)
        instance.save()

        return instance

    @classmethod
    def upsert_items(cls, items, group: Pool):

        for item in items:
            cls.upsert_item(item, group)

    @classmethod
    def upsert_item(cls, item, group: Pool):
        try:
            existing = PoolItem.objects.get(pk=item['id'])
            existing.__dict__.update(**item, owner=group)
            existing.save()
            return existing
        except (PoolItem.DoesNotExist, KeyError):
            return PoolItem(**item, owner=group)
