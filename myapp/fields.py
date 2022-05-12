from rest_framework import serializers
from .models import Tag

BASE_API_URL = 'https://8000-blairpresto-finalprojec-khbsmmpuzia.ws-us44.gitpod.io/'

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
        print('self', self)
        print('type', type(tag_id))
        if isinstance(tag_id, int):
            tag = Tag.objects.filter(id=tag_id).first()
            if tag:
                return tag
        elif isinstance(tag_id, str):
            print('tag', tag_id)
            print('type', type(tag_id))
            tag = Tag.objects.filter(label=tag_id).first()
            if tag:
                return tag.id
            else:
                id = int(tag_id)
                tag = Tag.objects.filter(label=id).first
                if tag:
                    return tag

        raise serializers.ValidationError(
            "No tag exists with id \"%s\"." % str(tag_id),
        )

class URLForImage(serializers.ImageField):
     def to_representation(self, value):
         if value:
            return BASE_API_URL + value.url