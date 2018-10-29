from django.db.models import Model, base, Manager, QuerySet
from django.db import transaction
from typing import DefaultDict, List, Union
import copy
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError


class NestedSerializer:

    @property
    def nested_entities(self):
        raise NotImplementedError

    def update_all_items(self, data: DefaultDict, owner: base, instance: Model = None):
        nested_data = dict()

        for item in self.nested_entities():
            coll = data.pop(item['name'])
            nested_data[item['name']] = coll

        if instance is None:
            instance = owner(**data)
        else:
            instance.__dict__.update(**data)

        instance.save()

        for item in self.nested_entities():
            items = nested_data[item['name']]
            entity_model = item['model']
            serializer = item['serializer'] if 'serializer' in item else None
            m2m = getattr(instance, item['name']) if item['m2m'] is True else None

            self.update_items(items, entity_model, serializer, instance, m2m)

        instance.save()
        return instance

    def update_items(self, items: List[Union[DefaultDict, int]], entity_model: base, serializer: ModelSerializer,
                     parent: Model = None,
                     m2m: Manager = None):

        try:
            existing = entity_model.objects.filter(owner=parent)
        except:
            existing = None

        self.remove_items(items, existing, entity_model, m2m)

        for item in items:
            self.upsert_item(item, parent, serializer, m2m)

    @classmethod
    def remove_items(cls, items: List[DefaultDict], existing: QuerySet, entity_model: Model, m2m: Manager):

        item_ids = [item.id for item in items] if m2m is not None else [item['id'] for item in items if 'id' in item]
        redundant = existing.exclude(pk__in=item_ids) if existing is not None else None

        try:
            if m2m is not None:
                m2m.clear()
            else:
                redundant.delete()
        except (entity_model.DoesNotExist, AttributeError):
            pass

    @classmethod
    def upsert_item(cls, item: Union[DefaultDict, Model], parent: Model,
                    serializer: ModelSerializer, m2m: Manager):
        if m2m is not None:
            m2m.add(item)
        else:
            data = cls.clean_data(item)
            validated = serializer(data=data)
            if validated.is_valid():
                instance = validated.save()
                instance.owner = parent
                instance.save()
            else:
                raise ValidationError(validated.errors)

    @transaction.atomic
    def create(self, validated_data):
        action = self.update_all_items(validated_data, self.Meta.model)
        return action

    @transaction.atomic
    def update(self, instance, validated_data):
        instance = self.update_all_items(validated_data, self.Meta.model, instance)
        return instance

    @classmethod
    def clean_data(cls, _data: DefaultDict):
        data = copy.deepcopy(_data)
        for prop in data:
            try:
                data[prop] = data[prop].pk
            except AttributeError:
                pass

        return data