from rest_framework import serializers

from api.entities.Stack import EffectStack
from api.helpers.image_sanitize import sanitize_image


class StackSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(max_length=None, use_url=True)
    class Meta:
        model = EffectStack
        fields = ('id', 'game', 'name', 'description', 'image', 'keywords', 'action', 'condition', 'relation')

    def to_internal_value(self, data):
        data = sanitize_image(data)
        value = super(StackSerializer, self).to_internal_value(data)
        return value
