from rest_framework import serializers
from .models import Tag

BASE_API_URL = 'https://8000-blairpresto-finalprojec-khbsmmpuzia.ws-us45.gitpod.io/'

class CustomForeignKeyField(serializers.PrimaryKeyRelatedField):
    """
    To use (serializer mustn subclass MODELSERIALIZER)
        class ParentSerializer(ModelSerializer):
            child = CustomForeignKeyField(queryset=Child.objects.all(), serializer=ChildSerializer)
    """

    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)

class TagListingField(serializers.RelatedField):
 
    def to_representation(self, value):
        return value.label

    def to_internal_value(self, tag_id):
        print('self1', self)
        print('type2', type(tag_id))
        if isinstance(tag_id, int):
            tag = Tag.objects.filter(id=tag_id).first()
            if tag:
                return tag
        elif isinstance(tag_id, str):
            print('tag3', tag_id)
            print('type4', type(tag_id))
            tag = Tag.objects.filter(id=tag_id).first()
            if tag:
                return tag.id

        raise serializers.ValidationError(
            "No tag exists with id \"%s\"." % str(tag_id),
        )

class URLForImage(serializers.ImageField):
     def to_representation(self, value):
         if value:
            return BASE_API_URL + value.url