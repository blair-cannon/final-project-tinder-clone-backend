from .models import Location, Park, Breed, Gender, Socialization, Aggression, Tag, Size, User, Dog, Image, Connection, Conversation, Message, Comment
from rest_framework import serializers
from rest_framework.response import Response
from .fields import CustomForeignKeyField, TagListingField


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class SocializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socialization
        fields = '__all__'

class AggressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggression
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True
    # )
    # username = serializers.CharField()
    # password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'password', 'first_name', 'second_parent', 'phone_number', 'location') 
        """ 
        only pull in the PROVIDED DJANGO USER FIELDS that are going to be used in creating a user, 
        and then add your extended fields,
        '__all__' pulls in all fields and creates an error for the validation step below
        """
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class DogSerializer(serializers.ModelSerializer):
    user = CustomForeignKeyField(queryset=User.objects.all(), serializer=UserSerializer)
    breed = CustomForeignKeyField(queryset=Breed.objects.all(), serializer=BreedSerializer)
    size = CustomForeignKeyField(queryset=Size.objects.all(), serializer=SizeSerializer)
    gender = CustomForeignKeyField(queryset=Gender.objects.all(), serializer=GenderSerializer)
    socialization = CustomForeignKeyField(queryset=Socialization.objects.all(), serializer=SocializationSerializer)
    aggression = CustomForeignKeyField(queryset=Aggression.objects.all(), serializer=AggressionSerializer)
    favorite_park = CustomForeignKeyField(queryset=Park.objects.all(), serializer=ParkSerializer)
    tags = TagListingField(queryset=Tag.objects.all(), many=True)
   
    class Meta:
        model = Dog
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ConnectionSerializer(serializers.ModelSerializer):
    dog_target = DogSerializer(read_only=True)
    dog_initializer = DogSerializer(read_only=True)
    class Meta:
        model = Connection
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    # dog_creator = DogSerializer(queryset=User.objects.all())
    # dog_other = DogSerializer(queryset=User.objects.all())
    def get_created_at(self, obj):
        return obj.created_at.strftime("%m/%d")

    class Meta:
        model = Conversation
        fields = '__all__'
        

class MessageSerializer(serializers.ModelSerializer):
    sent_at = serializers.SerializerMethodField()
    dog_sent = DogSerializer(read_only=True)
    dog_received = DogSerializer(read_only=True)
    conversation = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="subject"
  )

    def get_sent_at(self, obj):
        return obj.sent_at.strftime("%H:%M %m-%d")    
    class Meta:
        model = Message
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'