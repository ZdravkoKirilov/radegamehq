from django.db.models import Model, base, Manager, QuerySet
from typing import DefaultDict, List, Union
import copy


class NestedSerializer:

    @property
    def nested_entities(self):
        raise NotImplementedError

    def update_all_items(self, data: DefaultDict, owner: base, instance: Model = None):

        data_copy = copy.deepcopy(data)

        for item in self.nested_entities():
            data_copy.pop(item['name'])

        if instance is None:
            instance = owner(**data_copy)
        else:
            instance.__dict__.update(**data_copy)

        instance.save()

        for item in self.nested_entities():
            items = data[item['name']]
            entity_model = item['model']
            m2m = getattr(instance, item['name']) if item['m2m'] is True else None

            self.update_items(items, entity_model, instance, m2m)

        instance.save()
        return instance

    def update_items(self, items: List[Union[DefaultDict, int]], entity_model: base, parent: Model = None,
                     m2m: Manager = None):

        try:
            existing = entity_model.objects.filter(owner=parent)
        except:
            existing = None

        self.remove_items(items, existing, entity_model, m2m)

        for item in items:
            self.upsert_item(item, parent, entity_model, m2m)

    @classmethod
    def remove_items(cls, items: List[DefaultDict], existing: QuerySet, entity_model: Model, m2m: Manager):

        item_ids = [item['id'] for item in items if 'id' in item]
        redundant = existing.exclude(pk__in=item_ids) if existing is not None else list()

        try:
            if m2m is not None:
                for item in redundant:
                    m2m.remove(item)
            else:
                redundant.delete()
        except (entity_model.DoesNotExist, AttributeError):
            pass

    @classmethod
    def upsert_item(cls, item: DefaultDict, parent: Model, entity_model: Model, m2m: Manager):
        if m2m is not None:
            entity = entity_model.objects.get(pk=item['id'])
            m2m.add(entity)
        else:
            item_id = item['id'] if 'id' in item else None
            entity, created = entity_model.objects.update_or_create(pk=item_id,
                                                                    defaults=dict(**item, **{'owner': parent}))
        entity.save()
