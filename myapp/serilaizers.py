from .models import Location, Park, Breed, Gender, Socialization, Aggression, Tag, Size, User, Dog, Image, Connection, Conversation, Message, Comment
from rest_framework import serializers

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
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'second_parent', 'phone_number', 'location') 
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
    user = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="first_name"
  )
    breed = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="name"
  )
    size = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="label"
  )
    gender = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="label"
  )
    socialization = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="label"
  )
    aggression = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="label"
  )
    favorite_park = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="name"
  )
    tags = serializers.SlugRelatedField(
    many=True, 
    read_only=True,
    slug_field="label"
  )
    class Meta:
        model = Dog
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    dog_creator = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="name"
  )
    dog_other = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="name"
  )

    def get_created_at(self, obj):
        return obj.created_at.strftime("%H:%M %m-%d")

    class Meta:
        model = Conversation
        fields = '__all__'
        

class MessageSerializer(serializers.ModelSerializer):
    sent_at = serializers.SerializerMethodField()
    dog_sent = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="name"
  )
    dog_received = serializers.SlugRelatedField( 
    read_only=True,
    slug_field="name"
  )
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